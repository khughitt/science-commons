---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:uk-biobank
kind: dataset
title: UK Biobank — prospective population cohort resource (phenotypes, imaging, genomics)
version: "1.0.0"
created: "2026-07-17"
updated: "2026-07-17"
tags: []
access:
  level: registration
  availability: available
  available_after: ''
  verified: true
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: claude
  source_url: https://biobank.ndph.ox.ac.uk/showcase/
  credentials_required: UK Biobank approved-researcher application via the Access Management System (AMS); individual-level data access is application-gated
  exception:
    mode: ''
    decision_date: ''
    followup_task: ''
    superseded_by_dataset: ''
    rationale: ''
accessions:
- 'UK Biobank Showcase: https://biobank.ndph.ox.ac.uk/showcase/'
- 'UK Biobank Access Management System (AMS): https://ams.ukbiobank.ac.uk/ams/'
dataset_class: reference
ontology_terms: []
origin: external
source_class: observational
tier: track
---
# UK Biobank

Umbrella entity for the UK Biobank resource: a prospective population cohort of
~500,000 UK participants (recruited 2006–2010) with deep phenotyping, linked
health records, multi-organ imaging (brain, cardiac, abdominal MRI), and genome-wide
genotyping plus whole-exome and whole-genome sequencing. This entity is the
resource-level anchor, not a stageable data package — individual-level data are
obtained only through an approved-researcher application via the UK Biobank Access
Management System (AMS). The public Showcase catalogs the available data-fields
without exposing participant-level records.

This is deliberately an **umbrella**. UK Biobank's sub-resources have divergent
access and provenance and are represented as their own dataset entities that
declare `parent_dataset: dataset:uk-biobank` (sub-cohort lineage) as projects
actually need them — for example a proteomics release (UKB-PPP) or an imaging
sub-cohort. Do not attach data packages or benchmark metadata to this umbrella;
attach them to the specific child dataset.

Note on derived public products: imaging-derived-phenotype (IDP) GWAS **summary
statistics** computed from UK Biobank (e.g. the abdominal/cardiac/brain sumstats
catalogued in `dataset:wang2025-mri-gwas`) are public, reusable, derived aggregates
rather than sub-cohorts of the individual-level resource, and are represented as
independent `reference` datasets rather than via `parent_dataset` lineage.
