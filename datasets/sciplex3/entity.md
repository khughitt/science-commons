---
schema_profile: "science-entity-base/1.0+dataset/1.0"
id: "dataset:sciplex3"
type: "dataset"
title: "Sci-Plex 3"
version: "1.0.0"
status: "active"
created: "2026-06-27"
updated: "2026-06-27"
scope: "shared"
origin: "external"
source_class: "observational"
dataset_class: "pointer"
tier: "track"
license: "unknown"
access:
  level: "public"
  availability: "available"
  verified: true
  verification_method: "landing-confirmed"
  source_url: "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE139944"
ontology_terms: []
tags: []
benchmark:
  domains: ["biology"]
  modalities: ["single-cell-rna-seq"]
  signal_types: ["perturbation"]
  benchmark_kinds: ["perturbation-response", "cross-context-generalization"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark-capable dataset for single-cell perturbation response examples."
  limitations:
    - "Verify exact downloadable package location before marking as runnable deposit."
  tasks:
    - id: compound-response
      task_type: "response-prediction"
      prediction_target: "post-treatment single-cell expression signature"
      held_out_unit: "compound"
      metric: "rank correlation"
      baseline: "untreated expression profile"
      ground_truth:
        type: "measured-outcome"
        description: "measured post-perturbation expression state"
      interpretation_limits:
        - "Positive rank correlation against held-out perturbation response is the intended signal."
      intervention: "small-molecule compound and dose"
      contexts: ["cell line", "compound", "dose"]
---
# Sci-Plex 3
