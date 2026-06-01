from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from science_tool.commons.config import resolve_commons_data_root

# science:code
# status: exploratory
# science:end

OBO_REPLACED_BY = "http://purl.obolibrary.org/obo/IAO_0100001"
OBO_NAMESPACE = "http://www.geneontology.org/formats/oboInOwl#hasOBONamespace"
_GO_NAMESPACES = frozenset({"biological_process", "molecular_function", "cellular_component"})
_OBO_PURL = re.compile(r"^http://purl\.obolibrary\.org/obo/([A-Za-z][A-Za-z0-9]*)_(.+)$")


@dataclass(frozen=True, slots=True)
class GoTables:
    nodes: list[dict[str, str]]
    edges: list[dict[str, str]]
    summary: dict[str, Any]


def curie_or_iri(value: object) -> str:
    text = str(value or "").strip()
    match = _OBO_PURL.fullmatch(text)
    if match is None:
        return text
    return f"{match.group(1)}:{match.group(2)}"


def load_obograph(path: Path) -> dict[str, Any]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    graphs = raw.get("graphs") if isinstance(raw, dict) else None
    if not isinstance(graphs, list) or len(graphs) != 1 or not isinstance(graphs[0], dict):
        raise ValueError(f"{path}: expected OBO Graph JSON with exactly one graph")
    graph = graphs[0]
    if not isinstance(graph.get("nodes"), list) or not isinstance(graph.get("edges"), list):
        raise ValueError(f"{path}: expected graph.nodes and graph.edges lists")
    return graph


def _is_go_curie(value: str) -> bool:
    return value.startswith("GO:")


def _namespace(meta: dict[str, Any]) -> str:
    for entry in meta.get("basicPropertyValues", []) or []:
        if isinstance(entry, dict) and entry.get("pred") == OBO_NAMESPACE:
            val = str(entry.get("val") or "").strip()
            if val in _GO_NAMESPACES:
                return val
    return ""


def _replacement_values(meta: dict[str, Any]) -> tuple[str, ...]:
    raw = meta.get("basicPropertyValues", [])
    if not isinstance(raw, list):
        return ()
    out: list[str] = []
    for entry in raw:
        if not isinstance(entry, dict) or entry.get("pred") != OBO_REPLACED_BY:
            continue
        replacement = curie_or_iri(entry.get("val"))
        if replacement:
            out.append(replacement)
    return tuple(dict.fromkeys(out))


def _xref_values(meta: dict[str, Any]) -> tuple[str, ...]:
    raw = meta.get("xrefs", [])
    if not isinstance(raw, list):
        return ()
    out: list[str] = []
    for entry in raw:
        if not isinstance(entry, dict):
            continue
        val = str(entry.get("val") or "").strip()
        if val:
            out.append(val)
    return tuple(dict.fromkeys(out))


def build_go_tables(graph: dict[str, Any]) -> GoTables:
    nodes: list[dict[str, str]] = []
    edges: list[dict[str, str]] = []
    status_counts = {"active": 0, "deprecated": 0, "withdrawn": 0}
    namespace_counts = {
        "biological_process": 0,
        "molecular_function": 0,
        "cellular_component": 0,
    }
    go_keys: set[str] = set()
    label_fallback_count = 0
    namespace_fallback_count = 0
    skipped_non_class_go_count = 0

    for node in graph["nodes"]:
        if not isinstance(node, dict):
            raise ValueError("node entry is not an object")
        member_key = curie_or_iri(node.get("id"))
        if not _is_go_curie(member_key):
            continue
        if node.get("type") != "CLASS":
            skipped_non_class_go_count += 1
            continue
        if member_key in go_keys:
            raise ValueError(f"duplicate GO node {member_key}")
        raw_meta = node.get("meta")
        meta: dict[str, Any] = raw_meta if isinstance(raw_meta, dict) else {}
        status = "deprecated" if meta.get("deprecated") is True else "active"
        label = str(node.get("lbl") or "").strip()
        if not label:
            if status != "deprecated":
                raise ValueError(f"{member_key}: blank label")
            label = member_key
            label_fallback_count += 1
        member_kind = _namespace(meta)
        if not member_kind:
            member_kind = "term"
            namespace_fallback_count += 1
        else:
            namespace_counts[member_kind] += 1
        replaced_by = _replacement_values(meta)
        nodes.append(
            {
                "member_key": member_key,
                "member_kind": member_kind,
                "label": label,
                "status": status,
                "replaced_by": ";".join(replaced_by),
                "dataset_usage": "[]",
            }
        )
        status_counts[status] += 1
        go_keys.add(member_key)
        for xref in _xref_values(meta):
            edges.append(
                {
                    "subject": member_key,
                    "predicate": "xref",
                    "object": xref,
                    "evidence": "",
                    "dataset_usage": "[]",
                }
            )

    for edge in graph["edges"]:
        if not isinstance(edge, dict):
            raise ValueError("edge entry is not an object")
        subject = curie_or_iri(edge.get("sub") or edge.get("subj"))
        predicate = curie_or_iri(edge.get("pred"))
        object_ = curie_or_iri(edge.get("obj"))
        if not subject or not predicate or not object_:
            raise ValueError("edge has blank subject, predicate, or object")
        if subject not in go_keys and object_ not in go_keys:
            continue
        edges.append(
            {
                "subject": subject,
                "predicate": predicate,
                "object": object_,
                "evidence": "",
                "dataset_usage": "[]",
            }
        )

    nodes.sort(key=lambda row: row["member_key"])
    edges.sort(key=lambda row: (row["subject"], row["predicate"], row["object"]))
    summary = {
        "member_count": len(nodes),
        "edge_count": len(edges),
        "status_counts": status_counts,
        "namespace_counts": namespace_counts,
        "namespace_fallback_count": namespace_fallback_count,
        "label_fallback_count": label_fallback_count,
        "skipped_non_class_go_count": skipped_non_class_go_count,
    }
    return GoTables(nodes=nodes, edges=edges, summary=summary)


def write_tables(tables: GoTables, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        output_dir / "nodes.csv",
        ["member_key", "member_kind", "label", "status", "replaced_by", "dataset_usage"],
        tables.nodes,
    )
    _write_csv(
        output_dir / "edges.csv",
        ["subject", "predicate", "object", "evidence", "dataset_usage"],
        tables.edges,
    )
    (output_dir / "build-summary.yaml").write_text(
        yaml.safe_dump(tables.summary, sort_keys=False),
        encoding="utf-8",
    )


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def verify_entity(entity_path: Path, summary_path: Path) -> None:
    text = entity_path.read_text(encoding="utf-8")
    frontmatter = text.split("---", 2)[1]
    entity = yaml.safe_load(frontmatter)
    summary = yaml.safe_load(summary_path.read_text(encoding="utf-8"))
    for key in ("member_count", "edge_count"):
        if entity.get(key) != summary.get(key):
            raise ValueError(f"{entity_path}: {key}={entity.get(key)!r} does not match build summary {summary.get(key)!r}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build GO RG2 projections from OBO Graph JSON.")
    parser.add_argument("--source-json", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--verify-entity", type=Path)
    args = parser.parse_args()

    output_dir = args.output_dir or resolve_commons_data_root() / "go"
    source_json = args.source_json or output_dir / "_src" / "go.json"
    tables = build_go_tables(load_obograph(source_json))
    write_tables(tables, output_dir)
    if args.verify_entity is not None:
        verify_entity(args.verify_entity, output_dir / "build-summary.yaml")
    print(f"wrote {tables.summary['member_count']} GO nodes and {tables.summary['edge_count']} edges to {output_dir}")


if __name__ == "__main__":
    main()
