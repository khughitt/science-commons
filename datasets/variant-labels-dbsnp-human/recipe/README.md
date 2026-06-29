# Human dbSNP rsID Variant Labels

This recipe builds `dataset:variant-labels-dbsnp-human`, the C4c rsID input resolver artifact.

Use archived NCBI dbSNP URLs only:

- `https://ftp.ncbi.nih.gov/snp/archive/b157/VCF/GCF_000001405.40.gz`
- `https://ftp.ncbi.nih.gov/snp/archive/b157/VCF/GCF_000001405.25.gz`

Do not use `https://ftp.ncbi.nih.gov/snp/latest_release/VCF/`; that path is mutable.

The built SQLite file is large and belongs under `$SCIENCE_COMMONS_DATA_ROOT/variant-labels-dbsnp-human/`.
The commons repository stores the recipe, entity, and datapackage hash placeholders, not the bulk SQLite
or VCF bytes.

Run the fetch/build through Snakemake so the source downloads, lockfile, SQLite build, and datapackage
hash refresh are reproducible workflow targets:

```bash
rtk uv run --frozen --project ~/d/science/meta snakemake \
  -s ~/d/science-commons/datasets/variant-labels-dbsnp-human/recipe/Snakefile \
  --cores 1
```

The workflow defaults to `$SCIENCE_COMMONS_DATA_ROOT` when set and `/data/science-commons` otherwise. It
expects the assembly registry at `$SCIENCE_COMMONS_DATA_ROOT/assembly-registry/assemblies.csv`; override it
with `--config assembly_registry=/path/to/assemblies.csv` only when using an equivalent pinned registry.
No full-source lockfile is committed yet; the first successful workflow run should be reviewed before
committing `recipe/lockfile.yaml` and the refreshed `datapackage.yaml`.
