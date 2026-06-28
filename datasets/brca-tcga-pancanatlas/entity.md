---
schema_profile: science-entity-base/1.0+dataset/1.0+bio.matrix/1.0+bio.rnaseq/1.0
id: dataset:brca-tcga-pancanatlas
type: dataset
title: TCGA-BRCA (PanCancer Atlas) — mRNA expression + clinical
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
  source_url: https://www.cbioportal.org/study/summary?id=brca_tcga_pan_can_atlas_2018
  credentials_required: ''
  exception:
    mode: ''
    decision_date: ''
    followup_task: ''
    superseded_by_dataset: ''
    rationale: ''
accessions:
- 'cBioPortal: brca_tcga_pan_can_atlas_2018'
assay: polya-rnaseq
col_kind: sample
consumed_by: []
datapackage: datapackage.yaml
feature_axis: rows
license: custom
n_cols: 1082
n_rows: 20511
ontology_terms: []
origin: external
row_kind: gene
siblings: []
source_class: observational
species:
- Homo sapiens
status: active
tier: use-now
update_cadence: static
value_dtype: float32
benchmark:
  domains: ["biology", "cancer"]
  modalities: ["bulk-rna-seq", "clinical", "multimodal"]
  signal_types: ["clinical-outcome", "cross-sectional"]
  benchmark_kinds: ["static-association", "cross-context-generalization"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark for transcriptomic clinical-outcome prediction in a large primary breast-cancer cohort."
    - "Useful as an RNA-seq counterpart to METABRIC for platform-transfer and clinical-outcome checks."
  limitations:
    - "Observational cohort; prognostic associations do not establish treatment causality."
    - "Survival labels depend on curated clinical follow-up completeness."
  tasks:
    - id: survival-risk-prediction
      task_type: "outcome-prediction"
      prediction_target: "overall or disease-specific survival risk from expression and clinical features"
      held_out_unit: "patient"
      metric: "concordance-index"
      baseline: "clinical covariates"
      ground_truth:
        type: "measured-outcome"
        description: "curated TCGA clinical survival outcomes"
      interpretation_limits:
        - "Performance supports prognostic validation, not causal treatment inference."
      contexts: ["patient", "tumor subtype", "clinical stage", "RNA-seq platform"]
---
# TCGA-BRCA (PanCancer Atlas) — mRNA expression + clinical

## Summary

The cBioPortal study `brca_tcga_pan_can_atlas_2018`: TCGA breast invasive carcinoma,
PanCancer Atlas freeze. This entity covers the **mRNA expression + clinical** modality
surfaced by the `export_study_expression` rule (the mutation modality is covered by the
generic pipeline). Tidy products: **20,511 genes × 1,082 samples** (RNA-seq RSEM,
`data_mrna_seq_v2_rsem.txt`; 0 missing cells) and a merged sample-level clinical table
(1,084 rows, 57 fields incl. `OS_MONTHS`/`OS_STATUS`, `DSS_*`, `AGE`,
`AJCC_PATHOLOGIC_TUMOR_STAGE`, PAM50 `SUBTYPE`). PAM50 luminal A n = 499. The paired
`datapackage.json` records both parquet resources with byte sizes, SHA-256 hashes, and
shapes.

## Access verification log

- 2026-05-30 (claude, t046): exported from the cached cBioPortal tarball already staged
  under `/data/raw/cbioportal/brca_tcga_pan_can_atlas_2018`; products + datapackage
  written by `all_expression`. `verified: true` — files materialized and hashed.

## Granularity at this access level

mRNA expression matrix (genes × samples) + merged sample-level clinical/survival. TCGA
open-access tier (de-identified). Survival fields follow the Liu 2018 TCGA-CDR curation.

## Connections to Project

- Questions/hypotheses it can inform: the health-cycles tumor-CMag prognostic validation
  (`task:t046`, `question:77-tumor-cmag-prognostic-validation-breast-cancer`).
- Variables likely available: mRNA RSEM expression; OS/DSS survival; age; AJCC stage;
  PAM50 subtype.
- Planned usage: luminal-A reproduction cohort — CYCLOPS ordering → CMag → 5-yr-death
  logistic model.

## Related

- Source: `cite:Koboldt2012` (TCGA-BRCA), `cite:Liu2018TCGACDR` (survival curation).
