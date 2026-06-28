---
schema_profile: science-entity-base/1.0+dataset/1.0+bio.matrix/1.0
id: dataset:brca-metabric
type: dataset
title: METABRIC — mRNA expression + clinical
version: "1.0.0"
created: "2026-05-30"
updated: "2026-06-28"
tags: []
access:
  level: public
  availability: available
  available_after: ''
  verified: true
  verification_method: retrieved
  last_reviewed: '2026-05-30'
  verified_by: claude
  source_url: https://www.cbioportal.org/study/summary?id=brca_metabric
  credentials_required: primary data EGA-gated; cBioPortal redistributes the processed study
  exception:
    mode: ''
    decision_date: ''
    followup_task: ''
    superseded_by_dataset: ''
    rationale: ''
accessions:
- 'cBioPortal: brca_metabric'
col_kind: sample
consumed_by: []
datapackage: datapackage.yaml
feature_axis: rows
license: custom
n_cols: 1980
n_rows: 20385
ontology_terms: []
origin: external
row_kind: gene
siblings: []
source_class: observational
status: active
tier: use-now
update_cadence: static
value_dtype: float32
benchmark:
  domains: ["biology", "cancer"]
  modalities: ["bulk-expression", "clinical", "multimodal"]
  signal_types: ["clinical-outcome", "cross-sectional"]
  benchmark_kinds: ["static-association", "cross-context-generalization"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark for platform-distinct breast-cancer prognostic validation using microarray expression plus long clinical follow-up."
    - "Useful as an independent validation counterpart to TCGA-BRCA."
  limitations:
    - "Processed cBioPortal redistribution is public, but primary data have controlled-access terms."
    - "Observational outcome benchmark; prognostic associations do not imply treatment causality."
  tasks:
    - id: platform-transfer-survival
      task_type: "outcome-prediction"
      prediction_target: "overall or relapse-free survival risk from expression and clinical features"
      held_out_unit: "patient"
      metric: "concordance-index"
      baseline: "clinical covariates"
      ground_truth:
        type: "measured-outcome"
        description: "METABRIC clinical survival and relapse outcomes"
      interpretation_limits:
        - "Useful for platform-transfer validation; causal interpretation requires separate study design."
      contexts: ["patient", "tumor subtype", "microarray platform", "clinical follow-up"]
---
# METABRIC — mRNA expression + clinical

## Summary

The cBioPortal study `brca_metabric`: Molecular Taxonomy of Breast Cancer International
Consortium. This entity covers the **mRNA expression + clinical** modality surfaced by
the `export_study_expression` rule. Tidy products: **20,385 genes × 1,980 samples**
(Illumina HT-12 v3 microarray, `data_mrna_illumina_microarray.txt`; **16 missing cells
across 11 genes** — genuine source NAs, flagged for WP2 to resolve before Julia) and a
merged sample-level clinical table (2,509 rows — 1,980 with matched expression, 529
clinical-only — 37 fields incl. `OS_MONTHS`/`OS_STATUS`, `RFS_*`, `AGE_AT_DIAGNOSIS`,
`CLAUDIN_SUBTYPE`, `ER_STATUS`). PAM50/claudin luminal A n = 700; long follow-up
supports independent survival validation. The paired `datapackage.json` records both
parquet resources with byte sizes, SHA-256 hashes, shapes, and the missing-cell count.

## Access verification log

- 2026-05-30 (claude, t046): exported from the cached cBioPortal tarball already staged
  under `/data/raw/cbioportal/brca_metabric`; products + datapackage written by
  `all_expression`. `verified: true` — files materialized and hashed. Note the 11 genes
  with ≥1 missing expression value (genuine NAs in the source microarray matrix).

## Granularity at this access level

mRNA expression matrix (genes × samples) + merged sample-level clinical/survival.
Processed study publicly redistributed via cBioPortal; primary METABRIC data is
EGA-controlled.

## Connections to Project

- Questions/hypotheses it can inform: the health-cycles tumor-CMag prognostic validation
  (`task:t046`, `question:77-tumor-cmag-prognostic-validation-breast-cancer`).
- Variables likely available: Illumina microarray expression; OS/RFS survival; age;
  claudin/PAM50 subtype; ER status.
- Planned usage: **independent (platform-distinct) validation cohort** for CMag.

## Related

- Source: `cite:Curtis2012` (METABRIC discovery), `cite:Pereira2016` (expanded landscape).
