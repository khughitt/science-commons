"""Operator-run, no-FASTA build of the assembly registry's assemblies.csv.

Run from the dataset directory:  uv run --with refget --with httpx \
    --with pyyaml python recipe/build.py
Network is used only to fetch pinned seqcol level-2 records; output is KBs.
"""

from __future__ import annotations

import csv
from pathlib import Path

import yaml

from science_tool.commons.assembly_registry_build import build_registry_row, fetch_seqcol_level2

_HERE = Path(__file__).resolve().parent
_OUT = _HERE.parent / "assemblies.csv"
_FIELDS = ["seqcol_digest", "label", "accession", "n_sequences", "source_url"]


def main() -> None:
    sources = yaml.safe_load((_HERE / "sources.yaml").read_text(encoding="utf-8"))
    rows = []
    for src in sources["assemblies"]:
        level2 = fetch_seqcol_level2(src["seqcol_digest"])
        rows.append(
            build_registry_row(
                level2=level2,
                label=src["label"],
                accession=src["accession"],
                server_digest=src["seqcol_digest"],
                source_url=f"https://seqcolapi.databio.org/collection/{src['seqcol_digest']}",
            )
        )
    with _OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {_OUT}")


if __name__ == "__main__":
    main()
