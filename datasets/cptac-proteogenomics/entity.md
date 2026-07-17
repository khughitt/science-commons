---
schema_profile: "science-entity-base/1.0+dataset/2.0"
id: "dataset:cptac-proteogenomics"
kind: "dataset"
title: "CPTAC proteogenomics"
version: "1.0.0"
status: "active"
created: "2026-06-27"
updated: "2026-06-27"
scope: "shared"
origin: "external"
source_class: "reference"
dataset_class: "reference"
tier: "track"
license: "unknown"
access:
  level: "public"
  availability: "available"
  verified: true
  verification_method: "landing-confirmed"
  source_url: "https://proteomic.datacommons.cancer.gov/pdc/"
ontology_terms: []
tags: []
benchmark:
  domains: ["biology", "cancer"]
  modalities: ["proteomics", "bulk-rna-seq", "genomics", "multimodal"]
  signal_types: ["cross-sectional", "multi-omic"]
  benchmark_kinds: ["static-association", "cross-context-generalization"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark for testing multi-omic model transfer beyond RNA-only datasets."
  limitations:
    - "Cancer cohort context; access and license terms must be checked per study before staging."
  tasks:
    - id: protein-rna-cross-modal
      task_type: "cross-modal-prediction"
      prediction_target: "protein abundance from transcriptomic and genomic features"
      held_out_unit: "tumor sample"
      metric: "spearman-correlation"
      baseline: "gene-wise RNA abundance"
      ground_truth:
        type: "measured-outcome"
        description: "mass-spectrometry protein abundance"
      interpretation_limits:
        - "Protein prediction should exceed the RNA-only baseline."
      contexts: ["tumor type", "assay batch"]
      support:
        state: candidate
        reason: requires-study-specific-staging
        checked_at: "2026-07-03"
        evidence:
          - entity.md#benchmark.limitations
          - https://proteomic.datacommons.cancer.gov/pdc/
        notes:
          - Benchmark-relevant portal record; a concrete study/package must be selected and staged before use.
          - Keep visible as a candidate for proteogenomic cross-modal validation, not as a runnable fallback.
---
# CPTAC proteogenomics
