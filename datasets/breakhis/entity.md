---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:breakhis
kind: dataset
title: BreakHis — Breast Cancer Histopathological Image Database
version: "1.0.0"
created: "2026-07-18"
updated: "2026-07-18"
tags: []
access:
  level: public
  availability: available
  available_after: ''
  verified: true
  verification_method: landing-confirmed
  last_reviewed: '2026-07-18'
  verified_by: reviewer
  source_url: https://web.inf.ufpr.br/vri/databases/breast-cancer-histopathological-database-breakhis/
  credentials_required: Freely available for research; direct download from the P&D Laboratory / Universidade Federal do Paraná (UFPR) Vision Robotics and Imaging (VRI) database page (a request form is offered after download, not required for access)
  exception:
    mode: ''
    decision_date: ''
    followup_task: ''
    superseded_by_dataset: ''
    rationale: ''
accessions:
- 'BreakHis (UFPR VRI): https://web.inf.ufpr.br/vri/databases/breast-cancer-histopathological-database-breakhis/'
dataset_class: reference
license: CC-BY-4.0
ontology_terms: []
origin: external
source_class: observational
tier: track
---
# BreakHis — Breast Cancer Histopathological Image Database

BreakHis is a breast-cancer histopathology image dataset assembled by the P&D
Laboratory (Pathological Anatomy and Cytopathology, Paraná, Brazil) and the UFPR
Vision Robotics and Imaging group (Spanhol et al., 2016). It contains ~7,909
H&E-stained microscopy images of breast tumor tissue from 82 patients, captured at
four magnification factors (40×, 100×, 200×, 400×) and labeled benign vs. malignant
with tumor-subtype annotations. It is a standard benchmark for breast-cancer
histopathology image classification.

Reference-level entity for the resource; this is not a stageable data package.

Referenced by `paper:Islam2024` (global + multiscale context fusion for breast-cancer
classification), which trains and evaluates on BreakHis across all four magnification
levels.

**Provenance note:** initial metadata was drafted from the citing paper and prior
knowledge; the UFPR VRI landing page was subsequently confirmed live (2026-07-18,
`landing-confirmed`), verifying the 7,909-image total, CC BY 4.0 license, and direct
download. (The landing page's introductory sentence inconsistently states 9,109; the
detailed per-magnification table sums to 7,909.)
