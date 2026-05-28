"""Operator-run build of the GRCh38+GRCh37 sequence store.

Run from this dataset directory:
  uv run --with httpx --with pyyaml python recipe/build.py

Network fetches the pinned FASTAs. Output is ~6 GB of per-contig files plus
manifest.csv. Commit only manifest.csv after building; do not commit sequence
byte files.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import yaml

from science_tool.commons.sequence_store_build import fetch_fasta, slice_fasta_to_store

_HERE = Path(__file__).resolve().parent
_DATASET = _HERE.parent
_COMMONS = _DATASET.parents[1]
_ASSEMBLY_CONTIGS = _COMMONS / "datasets" / "assembly-registry" / "contigs.csv"
_FIELDS = ["assembly_seqcol_digest", "name", "refget_digest", "length", "sha256"]


def _expected_by_assembly(path: Path) -> dict[str, dict[str, dict[str, str]]]:
    if not path.is_file():
        raise FileNotFoundError(f"build assembly-registry/contigs.csv first: {path}")

    expected: dict[str, dict[str, dict[str, str]]] = {}
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        required = {"seqcol_digest", "name", "refget_digest", "length"}
        if reader.fieldnames is None or set(reader.fieldnames) != {
            "seqcol_digest",
            "sequence_index",
            "name",
            "refget_digest",
            "length",
        }:
            raise ValueError(f"unexpected assembly-registry contigs.csv columns: {reader.fieldnames!r}")
        for row in reader:
            seqcol_digest = row["seqcol_digest"]
            name = row["name"]
            if not seqcol_digest or not name or any(not row[field] for field in required):
                raise ValueError(f"invalid contigs.csv row: {row!r}")
            assembly = expected.setdefault(seqcol_digest, {})
            if name in assembly:
                raise ValueError(f"duplicate contig {name!r} in registry for {seqcol_digest!r}")
            assembly[name] = row
    return expected


def _checked_manifest_rows(
    *,
    assembly: dict[str, Any],
    manifest: list[dict[str, Any]],
    expected: dict[str, dict[str, dict[str, str]]],
) -> list[dict[str, Any]]:
    seqcol_digest = str(assembly["seqcol_digest"])
    expected_rows = expected.get(seqcol_digest)
    if expected_rows is None:
        raise RuntimeError(f"assembly {assembly['label']!r} seqcol {seqcol_digest!r} is absent from contigs.csv")

    rows: list[dict[str, Any]] = []
    seen_names: set[str] = set()
    for row in manifest:
        name = str(row["name"])
        if name in seen_names:
            raise RuntimeError(f"duplicate FASTA contig {name!r} for {assembly['label']!r}")
        seen_names.add(name)
        expected_row = expected_rows.get(name)
        if expected_row is None:
            raise RuntimeError(
                f"FASTA contig {name!r} for {assembly['label']!r} is absent from contigs.csv; "
                "the FASTA must match the seqcol contig set and naming exactly"
            )
        if row["refget_digest"] != expected_row["refget_digest"]:
            raise RuntimeError(
                f"refget digest mismatch for {assembly['label']!r} {name!r}: "
                f"registry={expected_row['refget_digest']!r} fasta={row['refget_digest']!r}"
            )
        if int(row["length"]) != int(expected_row["length"]):
            raise RuntimeError(
                f"length mismatch for {assembly['label']!r} {name!r}: "
                f"registry={expected_row['length']!r} fasta={row['length']!r}"
            )
        rows.append({"assembly_seqcol_digest": seqcol_digest, **row})

    missing = sorted(set(expected_rows) - seen_names)
    if missing:
        raise RuntimeError(
            f"FASTA for {assembly['label']!r} is missing contig {missing[0]!r}; "
            "the FASTA must match the seqcol contig set and naming exactly"
        )
    return rows


def main() -> None:
    sources = yaml.safe_load((_HERE / "sources.yaml").read_text(encoding="utf-8"))
    expected = _expected_by_assembly(_ASSEMBLY_CONTIGS)
    rows: list[dict[str, Any]] = []
    for assembly in sources["assemblies"]:
        fasta = fetch_fasta(assembly["fasta_url"], _HERE / f"{assembly['label']}.fa")
        try:
            manifest = slice_fasta_to_store(fasta, _DATASET)
            rows.extend(_checked_manifest_rows(assembly=assembly, manifest=manifest, expected=expected))
        finally:
            fasta.unlink(missing_ok=True)

    manifest_path = _DATASET / "manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} contigs to {manifest_path}")
    print("commit manifest.csv only; keep per-refget sequence byte files local")


if __name__ == "__main__":
    main()
