# Assembly registry build (no FASTA)

This recipe builds `dataset:assembly-registry`, the seqcol-keyed registry used
by variant, liftover, sequence-store, and dbSNP workflows.

Run through the commons-born lifecycle:

```bash
science commons dataset build assembly-registry
science commons dataset validate assembly-registry
```

The workflow writes:

- `$SCIENCE_COMMONS_DATA_ROOT/assembly-registry/assemblies.csv`
- `$SCIENCE_COMMONS_DATA_ROOT/assembly-registry/contigs.csv`
- `$SCIENCE_COMMONS_DATA_ROOT/assembly-registry/contig_aliases.csv`

`sources.yaml` pins the seqcol collection digests and NCBI assembly report URLs
for RefSeq GRCh38 (`GCF_000001405.40`) and GRCh37 (`GCF_000001405.25`).
No FASTA is downloaded. Per-contig `SQ.` digests come from the pinned seqcol
level-2 records. Contig aliases come from pinned NCBI assembly reports.

The current seqcol records use RefSeq accession names such as `NC_000001.11`.
The assembly report parser joins those rows through report aliases, then emits
all available aliases for each matched contig.
