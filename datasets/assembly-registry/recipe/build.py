"""Operator-run, no-FASTA build of the assembly registry resources.

Run from the dataset directory:
  uv run --with refget --with httpx --with pyyaml python recipe/build.py
Network is used only to fetch pinned seqcol level-2 records and pinned NCBI
assembly reports; output is small CSV resources.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import yaml

from science_tool.commons.assembly_registry_build import (
    build_contig_rows,
    build_registry_row,
    fetch_seqcol_level2,
)
from science_tool.commons.assembly_report_build import build_contig_alias_rows, fetch_text, parse_assembly_report

_HERE = Path(__file__).resolve().parent
_OUT = _HERE.parent
_ASSEMBLY_FIELDS = ["seqcol_digest", "label", "accession", "n_sequences", "source_url"]
_CONTIG_FIELDS = ["seqcol_digest", "sequence_index", "name", "refget_digest", "length"]
_ALIAS_FIELDS = ["seqcol_digest", "refget_digest", "alias", "alias_kind", "sequence_accession"]


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    sources = yaml.safe_load((_HERE / "sources.yaml").read_text(encoding="utf-8"))
    assembly_rows: list[dict[str, Any]] = []
    contig_rows: list[dict[str, Any]] = []
    alias_rows: list[dict[str, Any]] = []

    for src in sources["assemblies"]:
        level2 = fetch_seqcol_level2(src["seqcol_digest"])
        assembly_rows.append(
            build_registry_row(
                level2=level2,
                label=src["label"],
                accession=src["accession"],
                server_digest=src["seqcol_digest"],
                source_url=f"https://seqcolapi.databio.org/collection/{src['seqcol_digest']}",
            )
        )
        assembly_contigs = build_contig_rows(level2=level2, seqcol_digest=src["seqcol_digest"])
        contig_rows.extend(assembly_contigs)
        report_rows = parse_assembly_report(fetch_text(src["assembly_report_url"]))
        alias_rows.extend(build_contig_alias_rows(contig_rows=assembly_contigs, report_rows=report_rows))

    _write_csv(_OUT / "assemblies.csv", _ASSEMBLY_FIELDS, assembly_rows)
    _write_csv(_OUT / "contigs.csv", _CONTIG_FIELDS, contig_rows)
    _write_csv(_OUT / "contig_aliases.csv", _ALIAS_FIELDS, alias_rows)
    print(f"wrote {len(assembly_rows)} assemblies, {len(contig_rows)} contigs, {len(alias_rows)} aliases to {_OUT}")


if __name__ == "__main__":
    main()
