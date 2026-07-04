# CPTAC GBM Proteogenomics Recipe

This recipe stages a study-specific cBioPortal/DataHub-derived CPTAC GBM
package for `dataset:cptac-gbm-2021-proteogenomics`.

Do not commit generated data. Keep generated files under
`~/d/science-commons-data/cptac-gbm-2021-proteogenomics` or another explicit
output directory outside git-tracked commons metadata.

## Dry Run

```bash
PYTHONPATH=~/d/science/science/src rtk uv run --frozen --project ~/d/science/science \
  python fetch_manifest.py --dry-run \
  --output-dir ~/d/science-commons-data/cptac-gbm-2021-proteogenomics
```

The dry run writes:

```text
manifest/study.json
manifest/molecular_profiles.json
manifest/sample_lists.json
reports/validation.json
```

## Download

```bash
PYTHONPATH=~/d/science/science/src rtk uv run --frozen --project ~/d/science/science \
  python fetch_manifest.py --download \
  --output-dir ~/d/science-commons-data/cptac-gbm-2021-proteogenomics
```

The download step parses DataHub LFS pointers, requests signed direct URLs from
the GitHub LFS batch API, downloads the mRNA and protein payloads, and verifies
byte counts plus SHA-256 hashes.

## Build

```bash
PYTHONPATH=~/d/science/science/src rtk uv run --frozen --project ~/d/science/science \
  python build.py \
  --output-dir ~/d/science-commons-data/cptac-gbm-2021-proteogenomics
```

The build writes:

```text
expression/mrna_fpkm_uq.parquet
proteomics/protein_abundance_log2.parquet
metadata/samples.parquet
reports/build-summary.json
```

## Datapackage

```bash
PYTHONPATH=~/d/science/science/src rtk uv run --frozen --project ~/d/science/science \
  python build_datapackage.py \
  --data-dir ~/d/science-commons-data/cptac-gbm-2021-proteogenomics \
  --import-date "2026-01-07 13:14:46" \
  --output ../datapackage.yaml
```

## Validation

```bash
PYTHONPATH=~/d/science/science/src rtk uv run --frozen --project ~/d/science/science \
  pytest test_cptac_gbm_recipe.py -q
```
