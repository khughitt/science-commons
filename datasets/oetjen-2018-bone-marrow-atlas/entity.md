---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:oetjen-2018-bone-marrow-atlas
kind: dataset
title: Oetjen 2018 — Human bone marrow single-cell reference atlas
version: "1.0.0"
created: "2026-06-01"
updated: "2026-06-28"
tags: []
access:
  level: public
  availability: available
  available_after: ''
  verified: true
  verification_method: retrieved
  last_reviewed: '2026-05-29'
  verified_by: claude
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE120221
  credentials_required: ''
  exception:
    mode: ''
    decision_date: ''
    followup_task: ''
    superseded_by_dataset: ''
    rationale: ''
accessions:
- GSE120221
datapackage: datapackage.yaml
license: CC-BY-4.0
ontology_terms:
- CL:0000988
- UBERON:0002371
origin: external
status: active
tier: use-now
update_cadence: static
benchmark:
  domains: ["biology", "hematology"]
  modalities: ["single-cell-rna-seq", "cytometry", "multimodal"]
  signal_types: ["reference-atlas"]
  benchmark_kinds: ["static-association", "cross-context-generalization"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark for healthy bone-marrow cell-state annotation and cross-modality reference transfer."
    - "Useful for projects that need a normal hematopoietic reference before interpreting disease-state signals."
  limitations:
    - "Healthy donor atlas; disease-state extrapolation needs separate validation."
    - "Plasma cells are sparse, so plasma-cell-specific tasks may need aggregation across donors."
  tasks:
    - id: marrow-cell-state-transfer
      task_type: "cell-state-classification"
      prediction_target: "bone-marrow cell type or maturation state"
      held_out_unit: "donor"
      metric: "balanced-accuracy"
      baseline: "majority cell type within donor"
      ground_truth:
        type: "curated-label"
        description: "single-cell annotations supported by cytometry-calibrated reference labels"
      interpretation_limits:
        - "Performance supports reference-transfer checks, not tumor-state causality."
      contexts: ["donor", "cell type", "single-cell chemistry", "cytometry panel"]
---
# Oetjen 2018 — Human bone marrow single-cell reference atlas

## Summary

Healthy-donor human bone marrow scRNA-seq reference (20 donors / 25 GSM samples,
~90k cells) with
paired mass cytometry and flow cytometry calibration.
Provides the normal-baseline PC and hematopoietic reference needed to
contrast tumor-specific PC states identified in MM30.

## Access and Scope

- Accessions: GSE120221
- Source URL: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE120221
- Organism/population: Homo sapiens; 20 healthy BM donors represented by 25 scRNA GSM samples
- Modality: 10x scRNA-seq + CyTOF + FACS
- Sample size: ~90,000 cells (90,653 retained in the MM30 ingest cache; unsorted BM mononuclear)
- License: Open (GEO policy)
- Format: CellRanger outputs + FCS files for CyTOF

## Thoughts

- **Manifest nuance:** GEO publishes 25 sample-level CellRanger triplets, not 20
  one-to-one donor files. Donors `C` and `S` are sampled multiple times, so MM30
  should treat GSM as `sample_ID` and collapse to donor slug for `donor_id`.

- **Strength**: True healthy reference with cross-modality calibration;
  essential for distinguishing lineage biology from disease biology.
- **Strength**: Unsorted BM mononuclear cells — contains naive B, memory B,
  plasmablast, and plasma cell continuum needed for maturation-axis calibration.
- **Limitation**: Low PC numbers per donor (PCs are <1% of BMMC); requires
  integration across donors to build a robust PC-maturation reference.
- **Limitation**: 10x v2 chemistry — older than current best practice,
  sensitivity lower than v3.

## Connections to Project

### Questions/hypotheses it can inform

- Open question: identity of the dominant bulk composition channel — Oetjen
  provides healthy PC-maturation reference to anchor the tumor ↔ normal contrast
  observed in t174 Q1 (β_pc_mature = −0.306 tumor vs +0.510 NBM).
- `question:ribosome-axis-pc-continuum-vs-nucleolar-stress` — healthy PC
  reference for deriving a PC-maturity signature that can be projected onto
  bulk MM30 without tumor-specific contamination.
- Validation of t172 NBM cohort results on a larger healthy BM dataset.

### Variables likely available

- Per-cell transcriptome (healthy)
- Cell type labels via CyTOF integration
- Donor-level metadata

### Planned usage

- Build healthy-donor PC-maturation reference (supplementary to Boiarsky NBM
  cohort used in t172).
- Derive healthy-PC signature panel for bulk projection as an alternative
  to the tumor-derived signature that was uninformative in t202.

## Related

- Method notes: t172 NBM integration strategy
- Article notes: Oetjen et al., JCI Insight 2018
