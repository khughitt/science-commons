"""Operator-run build of the HGNC gene crosswalk's crosswalk.csv.

Run from the dataset directory:  uv run --with httpx --with pyyaml python recipe/build.py
Network fetches the pinned dated HGNC release files; output is a few-MB CSV.
"""

from __future__ import annotations

import csv
from pathlib import Path

import yaml

from science_tool.commons.gene_crosswalk_build import build_rows, fetch_text

_HERE = Path(__file__).resolve().parent
_OUT = _HERE.parent / "crosswalk.csv"
_FIELDS = [
    "gene_key",
    "symbol",
    "entrez_id",
    "ensembl_gene_id",
    "alias_symbol",
    "prev_symbol",
    "status",
    "replacement_gene_keys",
]


def main() -> None:
    src = yaml.safe_load((_HERE / "sources.yaml").read_text(encoding="utf-8"))
    complete = fetch_text(src["complete_set_url"])
    withdrawn = fetch_text(src["withdrawn_url"])
    rows = build_rows(complete_set_text=complete, withdrawn_text=withdrawn)
    with _OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {_OUT}")


if __name__ == "__main__":
    main()
