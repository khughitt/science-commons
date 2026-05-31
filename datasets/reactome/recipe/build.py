from __future__ import annotations

import argparse
import csv
import statistics
from collections import Counter, defaultdict
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import yaml
from science_tool.commons.config import resolve_commons_data_root
from science_tool.commons.gene_crosswalk import CrosswalkRow, load_gene_crosswalk

# science:code
# status: exploratory
# science:end

ResolutionStatus = Literal["approved", "unresolved", "ambiguous", "deprecated"]

NCBI_FIELDNAMES = ["entrez_id", "pathway_id", "pathway_url", "pathway_name", "evidence_code", "species"]
PATHWAY_FIELDNAMES = ["set_key", "name", "species", "is_top_level"]
RELATION_FIELDNAMES = ["parent_pathway_id", "child_pathway_id"]
SET_FIELDNAMES = ["set_key", "name", "member_ids", "source_pmids", "dataset_usage"]
PANEL_FIELDNAMES = ["set_key", "name", "entrez_id", "gene_key", "symbol", "match_type"]
REPORT_FIELDNAMES = ["set_key", "approved", "unresolved", "ambiguous", "deprecated", "retained", "dropped_empty"]


@dataclass(frozen=True, slots=True)
class GeneResolution:
    status: ResolutionStatus
    gene_key: str = ""
    symbol: str = ""
    match_type: str = ""


@dataclass(frozen=True, slots=True)
class ReactomeTables:
    sets: list[dict[str, str]]
    ncbi_gene_pathway: list[dict[str, str]]
    pathways: list[dict[str, str]]
    pathway_relations: list[dict[str, str]]
    gene_set_panel: list[dict[str, str]]
    resolution_report: list[dict[str, str]]
    summary: dict[str, object]


def normalize_ncbi_rows(rows: list[list[str]]) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    for row in rows:
        cells = _clean_cells(row)
        if len(cells) < 6 or cells[5] != "Homo sapiens":
            continue
        normalized.append(
            {
                "entrez_id": cells[0],
                "pathway_id": cells[1],
                "pathway_url": cells[2],
                "pathway_name": cells[3],
                "evidence_code": cells[4],
                "species": cells[5],
            }
        )
    return normalized


def normalize_pathways(rows: list[list[str]], relations: list[list[str]]) -> list[dict[str, str]]:
    child_ids = {cells[1] for row in relations if len(cells := _clean_cells(row)) >= 2}
    normalized: list[dict[str, str]] = []
    for row in rows:
        pathway_id, name, species = _parse_pathway_row(_clean_cells(row))
        if not pathway_id or species != "Homo sapiens":
            continue
        normalized.append(
            {
                "set_key": pathway_id,
                "name": name,
                "species": species,
                "is_top_level": "false" if pathway_id in child_ids else "true",
            }
        )
    return normalized


def normalize_relations(rows: list[list[str]], pathway_ids: set[str]) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for row in rows:
        cells = _clean_cells(row)
        if len(cells) < 2:
            continue
        parent_id, child_id = cells[0], cells[1]
        if parent_id not in pathway_ids or child_id not in pathway_ids:
            continue
        key = (parent_id, child_id)
        if key in seen:
            continue
        seen.add(key)
        normalized.append({"parent_pathway_id": parent_id, "child_pathway_id": child_id})
    return normalized


def build_gene_index(crosswalk_rows: list[CrosswalkRow]) -> dict[str, GeneResolution]:
    grouped: dict[str, list[CrosswalkRow]] = defaultdict(list)
    for row in crosswalk_rows:
        if row.entrez_id:
            grouped[row.entrez_id].append(row)

    index: dict[str, GeneResolution] = {}
    for entrez_id, rows in grouped.items():
        if len(rows) > 1:
            index[entrez_id] = GeneResolution(status="ambiguous")
            continue
        row = rows[0]
        if row.status == "split":
            index[entrez_id] = GeneResolution(status="ambiguous")
        elif row.status == "approved":
            index[entrez_id] = GeneResolution(
                status="approved",
                gene_key=row.gene_key,
                symbol=row.symbol,
                match_type="exact",
            )
        else:
            index[entrez_id] = GeneResolution(status="deprecated")
    return index


def build_reactome_tables(
    *,
    ncbi_rows: list[list[str]],
    pathway_rows: list[list[str]],
    relation_rows: list[list[str]],
    gene_index: Mapping[str, GeneResolution],
) -> ReactomeTables:
    ncbi_gene_pathway = normalize_ncbi_rows(ncbi_rows)
    pathways = normalize_pathways(pathway_rows, relation_rows)
    pathway_ids = {row["set_key"] for row in pathways}
    pathway_relations = normalize_relations(relation_rows, pathway_ids)

    pathway_names = {row["set_key"]: row["name"] for row in pathways}
    pathway_names.update({row["pathway_id"]: row["pathway_name"] for row in ncbi_gene_pathway})
    pathway_to_entrez = _group_entrez_by_pathway(ncbi_gene_pathway)

    sets: list[dict[str, str]] = []
    gene_set_panel: list[dict[str, str]] = []
    resolution_report: list[dict[str, str]] = []
    total_counts: Counter[str] = Counter()

    for pathway_id in sorted(pathway_to_entrez):
        entrez_ids = pathway_to_entrez[pathway_id]
        counts: Counter[str] = Counter()
        retained: list[str] = []
        name = pathway_names.get(pathway_id, "")

        for entrez_id in entrez_ids:
            resolution = gene_index.get(entrez_id, GeneResolution(status="unresolved"))
            counts[resolution.status] += 1
            if resolution.status != "approved":
                continue
            retained.append(entrez_id)
            gene_set_panel.append(
                {
                    "set_key": pathway_id,
                    "name": name,
                    "entrez_id": entrez_id,
                    "gene_key": resolution.gene_key,
                    "symbol": resolution.symbol,
                    "match_type": resolution.match_type,
                }
            )

        dropped_empty = 0 if retained else 1
        for status in ("approved", "unresolved", "ambiguous", "deprecated"):
            total_counts[status] += counts[status]
        total_counts["dropped_empty"] += dropped_empty

        resolution_report.append(
            {
                "set_key": pathway_id,
                "approved": str(counts["approved"]),
                "unresolved": str(counts["unresolved"]),
                "ambiguous": str(counts["ambiguous"]),
                "deprecated": str(counts["deprecated"]),
                "retained": str(len(retained)),
                "dropped_empty": str(dropped_empty),
            }
        )

        if not retained:
            continue
        sets.append(
            {
                "set_key": pathway_id,
                "name": name,
                "member_ids": ";".join(retained),
                "source_pmids": "",
                "dataset_usage": "",
            }
        )

    sizes = [len(row["member_ids"].split(";")) for row in sets]
    summary = {
        "n_sets": len(sets),
        "set_size_summary": _set_size_summary(sizes),
        "resolution_counts": {
            "approved": total_counts["approved"],
            "unresolved": total_counts["unresolved"],
            "ambiguous": total_counts["ambiguous"],
            "deprecated": total_counts["deprecated"],
            "dropped_empty": total_counts["dropped_empty"],
        },
    }
    return ReactomeTables(
        sets=sets,
        ncbi_gene_pathway=ncbi_gene_pathway,
        pathways=pathways,
        pathway_relations=pathway_relations,
        gene_set_panel=gene_set_panel,
        resolution_report=resolution_report,
        summary=summary,
    )


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def verify_entity_summary(entity_path: Path, summary: dict[str, object]) -> None:
    text = entity_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{entity_path}: missing YAML frontmatter")
    try:
        _prefix, raw_frontmatter, _body = text.split("---\n", 2)
    except ValueError as exc:
        raise ValueError(f"{entity_path}: malformed YAML frontmatter fence") from exc
    frontmatter = yaml.safe_load(raw_frontmatter)
    if not isinstance(frontmatter, dict):
        raise ValueError(f"{entity_path}: expected frontmatter mapping")
    expected = {
        "n_sets": summary.get("n_sets"),
        "set_size_summary": summary.get("set_size_summary"),
    }
    actual = {
        "n_sets": frontmatter.get("n_sets"),
        "set_size_summary": frontmatter.get("set_size_summary"),
    }
    if actual != expected:
        raise ValueError(f"{entity_path}: summary mismatch: expected {expected}, got {actual}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build normalized Reactome commons CSV resources.")
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--verify-entity", type=Path, help="Assert entity n_sets and set_size_summary match the build.")
    args = parser.parse_args()

    output_dir = args.output_dir or resolve_commons_data_root() / "reactome"
    source_dir = args.source_dir or output_dir / "_src"
    tables = build_reactome_tables(
        ncbi_rows=_read_tsv(source_dir / "NCBI2Reactome_All_Levels.txt"),
        pathway_rows=_read_tsv(source_dir / "ReactomePathways.txt"),
        relation_rows=_read_tsv(source_dir / "ReactomePathwaysRelation.txt"),
        gene_index=build_gene_index(load_gene_crosswalk()),
    )

    write_csv(output_dir / "sets.csv", tables.sets, SET_FIELDNAMES)
    write_csv(output_dir / "ncbi_gene_pathway.csv", tables.ncbi_gene_pathway, NCBI_FIELDNAMES)
    write_csv(output_dir / "pathways.csv", tables.pathways, PATHWAY_FIELDNAMES)
    write_csv(output_dir / "pathway_relations.csv", tables.pathway_relations, RELATION_FIELDNAMES)
    write_csv(output_dir / "gene_set_panel.csv", tables.gene_set_panel, PANEL_FIELDNAMES)
    write_csv(output_dir / "resolution_report.csv", tables.resolution_report, REPORT_FIELDNAMES)
    (output_dir / "build-summary.yaml").write_text(yaml.safe_dump(tables.summary, sort_keys=False), encoding="utf-8")
    if args.verify_entity is not None:
        verify_entity_summary(args.verify_entity, tables.summary)
    print(f"wrote Reactome resources to {output_dir}")


def _clean_cells(row: list[str]) -> list[str]:
    return [cell.strip() for cell in row]


def _parse_pathway_row(cells: list[str]) -> tuple[str, str, str]:
    if len(cells) >= 4 and cells[1].startswith(("http://", "https://")):
        return cells[0], cells[2], cells[3]
    if len(cells) >= 3:
        return cells[0], cells[1], cells[2]
    return "", "", ""


def _group_entrez_by_pathway(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    for row in rows:
        pathway_id = row["pathway_id"]
        entrez_id = row["entrez_id"]
        key = (pathway_id, entrez_id)
        if key in seen:
            continue
        seen.add(key)
        grouped[pathway_id].append(entrez_id)
    for entrez_ids in grouped.values():
        entrez_ids.sort(key=_entrez_sort_key)
    return dict(grouped)


def _entrez_sort_key(entrez_id: str) -> tuple[int, int | str]:
    return (0, int(entrez_id)) if entrez_id.isdigit() else (1, entrez_id)


def _set_size_summary(sizes: list[int]) -> dict[str, int | float]:
    if not sizes:
        return {"min": 0, "median": 0.0, "max": 0}
    return {"min": min(sizes), "median": float(statistics.median(sizes)), "max": max(sizes)}


def _read_tsv(path: Path) -> list[list[str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return [row for row in csv.reader(fh, delimiter="\t") if row]


if __name__ == "__main__":
    main()
