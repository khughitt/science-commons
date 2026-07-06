---
schema_profile: "science-entity-base/1.0+dataset/1.0"
id: "dataset:human-cell-atlas"
kind: "dataset"
title: "Human Cell Atlas"
version: "1.0.0"
status: "active"
created: "2026-06-27"
updated: "2026-06-29"
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
  source_url: "https://www.humancellatlas.org/"
ontology_terms: []
tags: []
benchmark:
  domains: ["biology"]
  modalities: ["single-cell-rna-seq", "spatial", "multimodal"]
  signal_types: ["reference-atlas"]
  benchmark_kinds: ["cross-context-generalization", "static-association"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Reference atlas seed for cross-context cell state and tissue generalization examples."
  limitations:
    - "Atlas/portal record only; concrete analysis-ready subsets should be separate deposit records."
  tasks:
    - id: atlas-label-transfer
      task_type: "cross-context-label-transfer"
      prediction_target: "cell type or cell state label in a held-out tissue, donor, or contributing study"
      held_out_unit: "tissue, donor, or contributing study"
      metric: "macro-F1"
      baseline: "nearest-neighbor or marker-gene label transfer from the reference atlas"
      ground_truth:
        type: "curated-label"
        description: "curated cell type or cell state annotations supplied by the contributing atlas dataset"
      interpretation_limits:
        - "Reference-portal task metadata only; runtime tests should use a specific staged HCA subset or derived deposit record."
      contexts: ["tissue", "donor", "study", "assay"]
---
# Human Cell Atlas
