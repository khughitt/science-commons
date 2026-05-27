# Assembly registry build (no-FASTA)

1. Fill `sources.yaml` with each assembly's seqcol collection digest. Discover
   digests from `https://seqcolapi.databio.org/list/collection` (or the refget
   seqcol standard paper). The build verifies each by recomputing it from the
   server's level-2 record (`names` + `sequences`), so a wrong digest fails fast.
2. Build: `uv run --with refget --with httpx --with pyyaml python recipe/build.py`
   (writes `../assemblies.csv`).
3. Pin the artifact hash + size into `datapackage.yaml` (sha256 of assemblies.csv).
4. Update `entity.md` `assembly_count` to the row count.

No FASTA is downloaded; per-contig `SQ.` digests come from the seqcol server.
