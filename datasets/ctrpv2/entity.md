---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:ctrpv2
type: dataset
title: CTRPv2 — Cancer Therapeutics Response Portal (v2)
version: "1.0.0"
created: "2026-05-29"
updated: "2026-05-29"
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
