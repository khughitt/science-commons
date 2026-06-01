from __future__ import annotations

import argparse
import csv
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import pyarrow.parquet as pq
import yaml

from science_tool.commons.config import resolve_commons_data_root

# science:code
# status: exploratory
# science:end

PREDICATE = "associated_with"
_ENSG_RE = re.compile(r"^ENSG[0-9]+$")
KNOWN_DISEASE_PREFIXES = frozenset(
    {
        "EFO", "MONDO", "HP", "Orphanet", "OBA", "GO", "GSSO",
        "OTAR", "DOID", "OBI", "NCIT", "MP", "PATO", "OGMS", "UBERON",
    }
)
NODE_FIELDS = ["member_key", "member_kind", "label", "status", "replaced_by", "dataset_usage", "symbol", "biotype"]


@dataclass(frozen=True, slots=True)
class OpenTargetsTables:
    nodes: list[dict[str, str]]
    edges: list[tuple[str, str, float]]  # (subject_curie, object_curie, score); predicate is constant PREDICATE
    summary: dict[str, Any]


def load_target_index(target_dir: Path) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for path in sorted(target_dir.glob("*.parquet")):
        table = pq.read_table(path, columns=["id", "approvedSymbol", "approvedName", "biotype"])
        for row in table.to_pylist():
            out[row["id"]] = {
                "approvedSymbol": row.get("approvedSymbol"),
                "approvedName": row.get("approvedName"),
                "biotype": row.get("biotype"),
            }
    return out


def load_disease_index(disease_path: Path) -> dict[str, dict[str, Any]]:
    path = disease_path if disease_path.is_file() else disease_path / "disease.parquet"
    table = pq.read_table(path, columns=["id", "name"])
    return {row["id"]: {"name": row.get("name")} for row in table.to_pylist()}


def iter_associations(assoc_dir: Path) -> Iterable[dict[str, Any]]:
    for path in sorted(assoc_dir.glob("*.parquet")):
        table = pq.read_table(path, columns=["targetId", "diseaseId", "score"])
        for row in table.to_pylist():
            yield {"targetId": row["targetId"], "diseaseId": row["diseaseId"], "score": row["score"]}


def _normalize_target(raw: str) -> str:
    if not _ENSG_RE.fullmatch(raw):
        raise ValueError(f"target id {raw!r} does not match ^ENSG[0-9]+$")
    return f"ENSEMBL:{raw}"


def _normalize_disease(raw: str) -> str:
    prefix, sep, local = raw.partition("_")
    if not sep or not local or prefix not in KNOWN_DISEASE_PREFIXES:
        raise ValueError(f"disease id {raw!r} has an unknown or malformed prefix")
    return f"{prefix}:{local}"


def _check_score(score: object, t_raw: str, d_raw: str) -> float:
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise ValueError(f"score {score!r} for ({t_raw},{d_raw}) is not numeric")
    value = float(score)
    if not math.isfinite(value) or not (0.0 <= value <= 1.0):
        raise ValueError(f"score {score!r} for ({t_raw},{d_raw}) is not a finite value in [0, 1]")
    return value


def build_opentargets_tables(
    associations: Iterable[dict[str, Any]],
    target_index: dict[str, dict[str, Any]],
    disease_index: dict[str, dict[str, Any]],
) -> OpenTargetsTables:
    target_curies: dict[str, str] = {}
    disease_curies: dict[str, str] = {}
    edges: list[tuple[str, str, float]] = []

    for assoc in associations:
        t_raw = str(assoc["targetId"]).strip()
        subject = target_curies.get(t_raw)
        if subject is None:
            subject = _normalize_target(t_raw)
            target_curies[t_raw] = subject
        d_raw = str(assoc["diseaseId"]).strip()
        object_ = disease_curies.get(d_raw)
        if object_ is None:
            object_ = _normalize_disease(d_raw)
            disease_curies[d_raw] = object_
        score = _check_score(assoc["score"], t_raw, d_raw)
        edges.append((subject, object_, score))

    edges.sort(key=lambda edge: (edge[0], edge[1]))
    for i in range(1, len(edges)):
        if edges[i][0] == edges[i - 1][0] and edges[i][1] == edges[i - 1][1]:
            raise ValueError(f"duplicate association edge ({edges[i][0]}, {edges[i][1]})")

    nodes: list[dict[str, str]] = []
    label_fallback_count = 0
    join_miss_target_count = 0
    join_miss_disease_count = 0

    for raw, curie in target_curies.items():
        meta = target_index.get(raw)
        if meta is None:
            join_miss_target_count += 1
            label_fallback_count += 1
            label, symbol, biotype = curie, "", ""
        else:
            symbol = str(meta.get("approvedSymbol") or "").strip()
            name = str(meta.get("approvedName") or "").strip()
            biotype = str(meta.get("biotype") or "").strip()
            label = symbol or name or curie
            if not (symbol or name):
                label_fallback_count += 1
        nodes.append(
            {
                "member_key": curie,
                "member_kind": "target",
                "label": label,
                "status": "active",
                "replaced_by": "",
                "dataset_usage": "[]",
                "symbol": symbol,
                "biotype": biotype,
            }
        )

    for raw, curie in disease_curies.items():
        meta = disease_index.get(raw)
        if meta is None:
            join_miss_disease_count += 1
            label_fallback_count += 1
            label = curie
        else:
            name = str(meta.get("name") or "").strip()
            label = name or curie
            if not name:
                label_fallback_count += 1
        nodes.append(
            {
                "member_key": curie,
                "member_kind": "disease",
                "label": label,
                "status": "active",
                "replaced_by": "",
                "dataset_usage": "[]",
                "symbol": "",
                "biotype": "",
            }
        )

    nodes.sort(key=lambda row: row["member_key"])

    disease_prefix_counts: dict[str, int] = {}
    for curie in disease_curies.values():
        prefix = curie.split(":", 1)[0]
        disease_prefix_counts[prefix] = disease_prefix_counts.get(prefix, 0) + 1

    summary = {
        "member_count": len(nodes),
        "edge_count": len(edges),
        "kind_counts": {"target": len(target_curies), "disease": len(disease_curies)},
        "participating_target_count": len(target_curies),
        "participating_disease_count": len(disease_curies),
        "disease_prefix_counts": dict(sorted(disease_prefix_counts.items())),
        "label_fallback_count": label_fallback_count,
        "join_miss_target_count": join_miss_target_count,
        "join_miss_disease_count": join_miss_disease_count,
    }

    _self_verify(nodes, edges, summary)
    return OpenTargetsTables(nodes=nodes, edges=edges, summary=summary)


def _self_verify(
    nodes: list[dict[str, str]],
    edges: list[tuple[str, str, float]],
    summary: dict[str, Any],
) -> None:
    node_keys = {row["member_key"] for row in nodes}
    if len(node_keys) != len(nodes):
        raise ValueError("duplicate member_key in node index")
    endpoints: set[str] = set()
    for subject, object_, _score in edges:
        endpoints.add(subject)
        endpoints.add(object_)
    missing = endpoints - node_keys
    if missing:
        raise ValueError(f"{len(missing)} edge endpoints absent from nodes, e.g. {sorted(missing)[:3]}")
    orphans = node_keys - endpoints
    if orphans:
        raise ValueError(f"{len(orphans)} nodes participate in no edge, e.g. {sorted(orphans)[:3]}")
    expected = summary["participating_target_count"] + summary["participating_disease_count"]
    if summary["member_count"] != expected or summary["member_count"] != len(nodes):
        raise ValueError("member_count does not equal participating target + disease counts")
