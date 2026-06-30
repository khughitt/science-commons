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

Each dbSNP archive is a separate Snakemake target. Interrupted downloads keep
their partial `<archive>.tmp` file under
`$SCIENCE_COMMONS_DATA_ROOT/variant-labels-dbsnp-human/_src/`; rerunning the
workflow resumes those partial files with HTTP Range requests when the server
supports them. The `recipe/lockfile.yaml` target is written only after both
archives and `.md5` sidecars exist and validate.

## Lifecycle commands

Run the package through the commons-born lifecycle:

```bash
SCIENCE_COMMONS_ROOT=~/d/science-commons science commons dataset status variant-labels-dbsnp-human
SCIENCE_COMMONS_ROOT=~/d/science-commons science commons dataset build variant-labels-dbsnp-human --cores 1
SCIENCE_COMMONS_ROOT=~/d/science-commons science commons dataset validate variant-labels-dbsnp-human
```

The workflow requires the standard `dataset_output_dir` config passed by
`science commons dataset build`; recipe code should write outputs there directly
rather than reconstructing `output_root/variant-labels-dbsnp-human`.

The full build also requires a pinned `assembly-registry/assemblies.csv` resource
for GRCh38 `GCF_000001405.40` and GRCh37 `GCF_000001405.25`. If that resource is
not available under `$SCIENCE_COMMONS_DATA_ROOT/assembly-registry/`, pass an
equivalent pinned file with Snakemake config `assembly_registry=...` for fixture
or operator smoke runs.
