---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:ctrpv2
kind: dataset
title: CTRPv2 — Cancer Therapeutics Response Portal (v2)
version: "1.0.0"
created: "2026-05-29"
updated: "2026-06-28"
tags: []
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
  last_reviewed: '2026-05-29'
  verified_by: claude
  source_url: https://ctd2-data.nci.nih.gov/Public/Broad/CTRPv2.0_2015_ctd2_ExpandedDataset/
  credentials_required: ''
datapackage: datapackage.yaml
ontology_terms: []
origin: external
status: active
tier: use-now
benchmark:
  domains: ["biology", "cancer"]
  modalities: ["drug-response", "cell-line"]
  signal_types: ["perturbation", "drug-response"]
  benchmark_kinds: ["perturbation-response", "cross-context-generalization"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark for small-molecule perturbation-response prediction across cancer cell lines."
    - "Complements expression and proteomics seeds by testing whether molecular context predicts drug sensitivity."
  limitations:
    - "Cell-line drug response is an in vitro perturbation signal and should not be treated as direct clinical efficacy."
    - "Compound coverage and curve-fit quality vary."
  tasks:
    - id: drug-sensitivity-prediction
      task_type: "response-prediction"
      prediction_target: "compound sensitivity area-under-curve"
      held_out_unit: "cell-line-compound pair"
      metric: "spearman-correlation"
      baseline: "compound median sensitivity"
      ground_truth:
        type: "measured-outcome"
        description: "CTRPv2 fitted small-molecule sensitivity measurements"
      interpretation_limits:
        - "Useful for perturbation-response validation; clinical translation needs independent evidence."
      intervention: "small-molecule compound exposure"
      contexts: ["cell line", "compound", "histology"]
---
# CTRPv2 — Cancer Therapeutics Response Portal (v2)

Broad Institute Cancer Therapeutics Response Portal v2: quantitative small-molecule
sensitivity (area-under-curve) for ~480 compounds across ~860 CCLE cancer cell lines,
linkable to CCLE molecular features. Used in MM30's integration stage (wired via
`config/workflow.yml` `external_raw`) for exploratory drug-sensitivity vs expression
cross-references in multiple-myeloma cell lines.

## Curated data package

Workflow-owned recipe: `workflows/external/ctrp_v2.smk` (`bin/snakemake ctrp_v2_all`).
The build joins the post-QC curve fits to the cell-line and compound dimension tables
and emits the **full pan-cancer** release (no MM subset) so the promoted commons
dataset is reusable across projects:

- `ctrpv2-sensitivity-long.parquet` — 395,263 rows (cell line × compound): AUC,
  apparent EC50 (µmol), predicted high-conc viability.
- `ctrpv2-cell-lines.parquet` — 1,107 cell lines (CCLE site / histology / subtype).
- `ctrpv2-compounds.parquet` — 545 compounds (target gene, activity class, SMILES).

Manifest: `data/external/ctrp_v2/2015/datapackage.json` (tracked); the Parquet
payloads are regenerable build artifacts and gitignored. This package is the
promote source for `science commons promote dataset --slug ctrpv2 --from multiple-myeloma`.
