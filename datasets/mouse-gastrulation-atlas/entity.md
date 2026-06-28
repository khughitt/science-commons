---
schema_profile: "science-entity-base/1.0+dataset/1.0"
id: "dataset:mouse-gastrulation-atlas"
type: "dataset"
title: "Mouse gastrulation single-cell atlas"
version: "1.0.0"
status: "active"
created: "2026-06-28"
updated: "2026-06-28"
scope: "shared"
origin: "external"
source_class: "reference"
dataset_class: "pointer"
tier: "track"
license: "unknown"
access:
  level: "public"
  availability: "available"
  verified: true
  verification_method: "landing-confirmed"
  source_url: "https://explore.data.humancellatlas.org/projects/1defdada-a365-44ad-9b29-443b06bd11d6"
ontology_terms: []
tags: []
benchmark:
  domains: ["biology", "developmental-biology"]
  modalities: ["single-cell-rna-seq"]
  signal_types: ["time-series", "reference-atlas"]
  benchmark_kinds: ["static-association", "cross-context-generalization", "time-series-forecasting"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark for temporal single-cell developmental trajectories outside cancer."
    - "Useful as a broad biology example for testing whether models preserve ordered developmental-state structure."
  limitations:
    - "Atlas/pointer seed; concrete analysis-ready subsets should be modeled separately before runnable benchmarking."
    - "Developmental time is an ordered sampling axis, not an intervention."
  tasks:
    - id: developmental-time-prediction
      task_type: "timepoint-prediction"
      prediction_target: "developmental stage or collection time from single-cell expression"
      held_out_unit: "embryo or batch"
      metric: "balanced-accuracy"
      baseline: "cell-type-majority stage"
      ground_truth:
        type: "measured-outcome"
        description: "annotated embryonic collection time and developmental stage"
      interpretation_limits:
        - "Temporal ordering supports dynamic-model checks but does not establish perturbational causality."
      timepoints: ["mouse gastrulation collection timepoints"]
      contexts: ["embryo", "cell type", "developmental stage"]
---
# Mouse gastrulation single-cell atlas
