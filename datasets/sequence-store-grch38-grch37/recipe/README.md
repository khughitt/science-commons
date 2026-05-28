# GRCh38 + GRCh37 sequence store build

This dataset is pinned and verifiable, not archival. `manifest.csv` records the
committed authority for each contig: assembly seqcol digest, seqcol name, refget
digest, length, and sha256 of the exact sequence bytes. The sequence byte files
are materialized locally as one file per refget digest and are not committed.

1. Build `datasets/assembly-registry/contigs.csv` first.
2. Pin dated FASTA URLs in `sources.yaml`; do not use mutable `latest` handles.
3. The selected FASTA for each assembly must match the seqcol contig set and
   naming exactly. Do not use analysis-set FASTAs with extra alts/decoys/HLA
   unless those contigs are present in the pinned seqcol. The first FASTA header
   token must equal the corresponding `contigs.csv` `name`.
4. Build from this dataset directory:
   `uv run --with httpx --with pyyaml python recipe/build.py`
5. Commit only `manifest.csv`; keep the per-refget sequence byte files local.
6. Update the `manifest` resource hash and byte count in `datapackage.yaml`:

   ```bash
   python - <<'PY'
   import hashlib
   import os

   p = "manifest.csv"
   print("sha256:" + hashlib.sha256(open(p, "rb").read()).hexdigest(), os.path.getsize(p))
   PY
   ```

A future rebuild can fail if an upstream FASTA disappears, but any produced store
is digest-checked against `assembly-registry/contigs.csv` and the manifest.
