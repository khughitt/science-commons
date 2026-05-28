# Assembly registry build (no-FASTA)

1. Fill `sources.yaml` with each assembly's seqcol collection digest and pinned
   NCBI assembly report URL. Discover digests from
   `https://seqcolapi.databio.org/list/collection` (or the refget seqcol
   standard paper). The build verifies each digest by recomputing it from the
   server's level-2 record (`names` + `sequences`), so a wrong digest fails fast.
2. Build: `uv run --with refget --with httpx --with pyyaml python recipe/build.py`
   (writes `../assemblies.csv`, `../contigs.csv`, and `../contig_aliases.csv`).
3. Pin each resource hash + size into `datapackage.yaml`:

   ```bash
   python - <<'PY'
   import hashlib
   import os

   for p in ("assemblies.csv", "contigs.csv", "contig_aliases.csv"):
       print(p, "sha256:" + hashlib.sha256(open(p, "rb").read()).hexdigest(), os.path.getsize(p))
   PY
   ```

4. Update `entity.md` `assembly_count` to the assembly row count.

No FASTA is downloaded; per-contig `SQ.` digests come from the seqcol server.
Contig aliases come from the pinned assembly reports and are joined through the
strict `build_contig_alias_rows` helper, which fails if seqcol names and report
names do not match exactly.
