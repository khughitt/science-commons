# MMRF CoMMpass Staging Recipe

This recipe stages a conservative, open-access MMRF CoMMpass package for the
`progression-risk` task. The commons entity remains a pointer until a future
promotion review verifies a runnable package and updates `entity.md`.

The recipe uses GDC metadata as the source of truth for file selection,
case/sample linkage, endpoint discovery, data release provenance, and download
URLs. It does not emit AWS S3 URIs because the bucket/key convention has not
been separately verified.

## Requirements

- Run commands from `~/d/science-commons/datasets/mmrf-commpass/recipe`.
- Use the Science source tree on `PYTHONPATH`.
- Pass `--output-dir` explicitly unless `SCIENCE_COMMONS_DATA_ROOT` is set.
- Keep generated data outside git, for example under
  `~/d/science-commons-data/mmrf-commpass`.

## Dry Run

The dry run queries GDC, writes metadata, and then refuses non-promotable
outcomes. It writes the manifest and validation report before raising for these
known blocker states:

- manifest-linked cases missing from the GDC cases response;
- open metadata exposing only overall-survival fields;
- open metadata missing usable progression fields.

```bash
PYTHONPATH=~/d/science/science/src rtk uv run --frozen --project ~/d/science/science \
  python fetch_manifest.py \
  --output-dir ~/d/science-commons-data/mmrf-commpass
```

With an environment-rooted output directory:

```bash
SCIENCE_COMMONS_DATA_ROOT=~/d/science-commons-data \
PYTHONPATH=~/d/science/science/src rtk uv run --frozen --project ~/d/science/science \
  python fetch_manifest.py
```

Dry-run outputs:

```text
manifest/files.parquet
manifest/cases.json
manifest/query.json
reports/validation.json
```

`manifest/files.parquet` follows `manifest.schema.yaml`. The required columns
are `file_id`, `file_name`, `data_category`, `data_type`, `data_format`,
`experimental_strategy`, `access`, `file_size`, `md5sum`, `case_id`,
`case_submitter_id`, `sample_submitter_id`, `sample_type`, and
`gdc_download_url`.

## Package Build

`build.py` expects a completed dry-run directory plus expression TSVs staged by
GDC file id under `_src/expression/`:

```text
~/d/science-commons-data/mmrf-commpass/
  manifest/files.parquet
  manifest/cases.json
  _src/expression/<file_id>.tsv
```

Build the analysis-ready package:

```bash
PYTHONPATH=~/d/science/science/src rtk uv run --frozen --project ~/d/science/science \
  python build.py \
  --output-dir ~/d/science-commons-data/mmrf-commpass
```

The default expression measure is `tpm_unstranded`. Override it only with a
column present in every staged GDC augmented STAR gene-count TSV:

```bash
PYTHONPATH=~/d/science/science/src rtk uv run --frozen --project ~/d/science/science \
  python build.py \
  --output-dir ~/d/science-commons-data/mmrf-commpass \
  --measure tpm_unstranded
```

Build outputs:

```text
data/expression.parquet
data/samples.parquet
data/outcomes.parquet
splits/heldout_patient_v1.parquet
reports/build-summary.json
```

The split is deterministic by patient. Patients are ranked by
`sha256(case_submitter_id || split_salt)` and assigned to nonempty
train/validation/test splits when at least three patients are available. The
default split salt is `mmrf-commpass-heldout-patient-v1`.

## Datapackage Metadata

Render `datapackage.yaml` only after the dry run and build reports agree on the
GDC data release and split salt:

```bash
PYTHONPATH=~/d/science/science/src rtk uv run --frozen --project ~/d/science/science \
  python build_datapackage.py \
  --data-dir ~/d/science-commons-data/mmrf-commpass \
  --split-salt mmrf-commpass-heldout-patient-v1 \
  --gdc-data-release "Data Release 45.0 - December 04, 2025"
```

The rendered datapackage records local resource hashes using the
`{SCIENCE_COMMONS_DATA_ROOT}` token. Do not add it to `entity.md` until a future
promotion task verifies the full package and explicitly changes the dataset
class.

## Validation

Run the recipe tests from this directory:

```bash
PYTHONPATH=~/d/science/science/src rtk uv run --frozen --project ~/d/science/science \
  pytest test_mmrf_recipe.py -q
```

The tests cover the open RNA-seq GDC filter, manifest normalization, endpoint
validation, dry-run artifact writes, package table creation, deterministic
patient splits, datapackage rendering, and the invariant that `entity.md`
remains `dataset_class: pointer`.
