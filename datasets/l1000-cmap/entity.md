---
schema_profile: "science-entity-base/1.0+dataset/1.0"
id: "dataset:l1000-cmap"
type: "dataset"
title: "LINCS L1000 Connectivity Map"
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
  source_url: "https://clue.io/"
ontology_terms: []
tags: []
benchmark:
  domains: ["biology"]
  modalities: ["bulk-expression", "landmark-transcriptomics"]
  signal_types: ["perturbation", "cross-context-generalization"]
  benchmark_kinds: ["perturbation-response", "mechanism-discrimination"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark for perturbational expression signatures and mechanism ranking."
  limitations:
    - "L1000 measures landmark genes and inferred expression rather than full transcriptomes."
  tasks:
    - id: perturbation-signature-retrieval
      task_type: "signature-retrieval"
      prediction_target: "matched perturbation class for a query signature"
      held_out_unit: "perturbagen"
      metric: "connectivity score"
      baseline: "nearest landmark expression signature"
      ground_truth:
        type: "labeled-class"
        description: "known perturbagen class for each signature"
      interpretation_limits:
        - "Query should retrieve the matched perturbation class above baseline."
      intervention: "compound, knockdown, or overexpression"
      contexts: ["cell line", "perturbagen", "dose", "time"]
---
# LINCS L1000 Connectivity Map
