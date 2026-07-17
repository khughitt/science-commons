---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:hmcl-drug-screen
kind: dataset
title: HMCL NCATS MIPE 4.0 drug screen — 1,912 compounds x 11 doses x 47 human myeloma cell lines (Hughitt et al., Zenodo 13910207)
version: "1.0.0"
created: "2026-07-09"
updated: "2026-07-09"
tags: []
access:
  level: public
  availability: available
  verified: true
  source_url: https://zenodo.org/records/13910207
  verification_method: landing-confirmed
  last_reviewed: '2026-07-09'
  verified_by: Keith Hughitt
consumed_by:
- task:t869
- task:t870
datapackage: datapackage.yaml
dataset_class: deposit
license: CC-BY-4.0
ontology_terms:
- DOID:9538
origin: external
source_class: observational
status: active
tier: use-now
provided_capabilities:
- {assay: drug-sensitivity, modality: cell-line-viability}
identity_context: {taxon: 9606}
---
# HMCL NCATS MIPE 4.0 drug screen

Large-scale pharmacological screen of **1,912 small-molecule compounds tested at
11 doses across 47 human myeloma cell lines (HMCL)**, generated at the NCATS
(NIH) with the MIPE 4.0 mechanism-interrogation library. Published CC-BY on
Zenodo (record 13910207); processing pipeline at
`github.com/khughitt/hmcl-drug-screen-pipeline`. This is the best-powered,
response-contrast-rich MM cell-line drug-screen substrate available locally —
larger and more informative for myeloma than the pan-cancer CTRPv2/GDSC slices
(which cover only 15–17 MM lines and fail to recover the t(11;14)→venetoclax
positive control).

## Curated data package

Workflow-owned recipe: `workflows/external/hmcl_drug_screen.smk`
(`bin/snakemake hmcl_drug_screen_all`). The build curates three tables from the
already-local published release (wired via
`config/workflow.yml::external_raw.hmcl_drug_screen`) and normalizes the
dimension join keys so the package is self-consistent:

- `hmcl-drug-curves.parquet` — 82,216 rows, one per (cell line × compound ×
  plate): curve-fit parameters (slope, ac50, lac50, ac50_pval) and the 11-point
  `dose_0..dose_10` percent-viability + `conc_0..conc_10` concentration grid.
  Foreign keys `cell_line`, `drug_id`.
- `hmcl-cell-lines.parquet` — 47 cell lines (join key `cell_line`): curated
  cytogenetics (`transloc_11_14` 12+/35−, `transloc_4_14`,
  `canonical_translocations`), driver-gene status (KRAS/NRAS/TP53/TRAF3), and
  screen-level summaries.
- `hmcl-drugs.parquet` — 1,912 compounds (join key `drug_id`): mechanistic
  class, cellular mechanisms, target genes, development phase, indication.
  Venetoclax = ABT-199 = `NCGC00345789-01`.

Manifest: `data/external/hmcl_drug_screen/2025/datapackage.json` (tracked); the
Parquet payloads are regenerable build artifacts and gitignored. This package is
the promote source for
`science commons promote dataset --slug hmcl-drug-screen --from multiple-myeloma`.

The build asserts referential integrity (every curve `cell_line`/`drug_id`
resolves to a dimension row; dimension keys unique) and fails fast on violation.

## Companion expression

Matched HMCL RNA-seq (GRCh38 featureCounts, symbol-keyed; 45 lines) is **not**
part of this drug-screen package. It is wired separately as
`config/workflow.yml::external_raw.hmcl_expression_grch38`. The two join by
normalized cell-line name (shared `_SOURCE` suffix, e.g. `KMS12BM_JCR…`).

## Use in MM30

Consumed by **t869** (H0025 P3 cell-line bridge): a continuous BCL2-dependency
priming score predicts venetoclax (ABT-199) sensitivity **beyond** curated
t(11;14) — verdict `P3_supported` at n=43, with the panel recovering the
t(11;14)→sensitivity positive control (Mann-Whitney p=0.0093). See
`interpretation:0192` and `pre-registration:0059`.
