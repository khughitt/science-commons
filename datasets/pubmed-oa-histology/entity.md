---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:pubmed-oa-histology
kind: dataset
title: PubMed Open-Access histopathology figure corpus (Schaumberg2020)
version: "1.0.0"
created: "2026-07-18"
updated: "2026-07-18"
tags: []
access:
  level: public
  availability: embargoed
  available_after: ''
  verified: false
  verification_method: ''
  last_reviewed: '2026-07-18'
  verified_by: claude
  source_url: https://pmc.ncbi.nlm.nih.gov/tools/openftlist/
  credentials_required: Derived from the open-access subset of PubMed Central; the underlying articles are open, but the curated histopathology-figure corpus itself was only announced for release via the authors' site (pathobotology.org) — no confirmed downloadable release, hence availability=embargoed
  exception:
    mode: ''
    decision_date: ''
    followup_task: ''
    superseded_by_dataset: ''
    rationale: ''
accessions:
- 'PubMed Central Open Access Subset: https://pmc.ncbi.nlm.nih.gov/tools/openftlist/'
- 'pathobotology.org (author-hosted resource)'
dataset_class: reference
ontology_terms: []
origin: external
source_class: reference
tier: track
---
# PubMed Open-Access histopathology figure corpus (Schaumberg2020)

A corpus of histopathology (H&E) figures mined from the PubMed Central open-access
literature, built by Schaumberg et al. (2020). An H&E-vs-other-stain classifier was
used to identify ~113,161 H&E figures from ~1,074,484 PubMed OA articles, expanding
the searchable pathology-image set by roughly an order of magnitude. It underpins the
PubMed side of the @pathobot pan-tissue pathology case-similarity search.

Reference-level entity for the derived corpus; not a stageable data package. The
underlying source is the PubMed Central Open Access Subset.

Referenced by `paper:Schaumberg2020` (multimodal pathology search on social media).

**Provenance note (AI-drafted, unverified):** counts and access details derive from the
citing paper; `access.verified: false` because neither the PMC OA landing page nor the
author-hosted corpus (pathobotology.org, announced but not fully public at publication)
was confirmed at authoring time. Upgrade after a manual check.
