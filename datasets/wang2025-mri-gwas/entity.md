---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:wang2025-mri-gwas
kind: dataset
title: UK Biobank MRI imaging-derived-phenotype GWAS summary statistics (abdominal/cardiac/brain)
version: "1.0.0"
created: "2026-07-17"
updated: "2026-07-17"
tags: []
access:
  level: public
  availability: available
  available_after: ''
  verified: true
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: claude
  source_url: https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90016001-GCST90017000/
  credentials_required: ''
  exception:
    mode: ''
    decision_date: ''
    followup_task: ''
    superseded_by_dataset: ''
    rationale: ''
accessions:
- 'GWAS Catalog: GCST90016001-GCST90017000 (abdominal IDPs)'
- 'Oxford BIG40: https://open.oxcin.ox.ac.uk/ukbiobank/big40/ (brain IDPs)'
- 'heartkp.org (cardiac IDPs)'
dataset_class: reference
ontology_terms: []
origin: external
source_class: observational
tier: track
---
# UK Biobank MRI imaging-derived-phenotype GWAS summary statistics

Publicly downloadable imaging-derived-phenotype (IDP) GWAS summary statistics from
UK Biobank, reused by Wang et al. 2026 (paper:Wang2025) for the cross-trait
genetic-correlation, LAVA/GPA overlap, CPASSOC meta-analysis, and TWAS components of
their multi-organ cardiometabolic-depression multimorbidity study. Three linked
public resources:

- **Abdominal IDPs** — GWAS Catalog studies GCST90016001–GCST90017000
  (https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90016001-GCST90017000/).
- **Cardiac IDPs** — Cardiac GWAS knowledge portal, http://heartkp.org/.
- **Brain IDPs** — Oxford BIG40 (~4,000 multimodal brain IDPs, ~17.1M SNPs),
  https://open.oxcin.ox.ac.uk/ukbiobank/big40/.

These are the derived summary statistics only; the underlying individual-level UK
Biobank phenotype, neuroimaging, and genotype data are under restricted access via
the UK Biobank Access Management System (this study used Application #101169).
Analysis code is archived at Zenodo DOI 10.5281/zenodo.17669873.
