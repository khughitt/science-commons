"""Operator-run build of the UniProt protein crosswalk's crosswalk.csv.

Run from the dataset directory:  uv run --with httpx --with pyyaml python recipe/build.py
Network fetches the pinned dated UniProt release files; output is a few-MB CSV.
The idmapping source is expected pre-filtered to reviewed Swiss-Prot human (v1
scope); the parser is source-agnostic (it emits a row per accession it sees).
"""

from __future__ import annotations

import csv
from pathlib import Path

import yaml

from science_tool.commons.protein_crosswalk_build import build_rows, fetch_text

_HERE = Path(__file__).resolve().parent
_OUT = _HERE.parent / "crosswalk.csv"
_FIELDS = [
    "protein_key",
    "entry_name",
    "ensembl_protein",
    "refseq_protein",
    "gene_key",
    "status",
    "replacement_protein_keys",
]


def main() -> None:
    src = yaml.safe_load((_HERE / "sources.yaml").read_text(encoding="utf-8"))
    idmapping = fetch_text(src["idmapping_url"])  # transparently gunzips a .gz handle
    secondary = fetch_text(src["secondary_url"])
    rows = build_rows(idmapping_text=idmapping, secondary_text=secondary)
    with _OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {_OUT}")


if __name__ == "__main__":
    main()
