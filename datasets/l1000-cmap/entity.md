---
schema_profile: "science-entity-base/1.0+dataset/2.0"
id: "dataset:l1000-cmap"
kind: "dataset"
title: "LINCS L1000 Connectivity Map"
version: "1.0.0"
status: "active"
created: "2026-06-27"
updated: "2026-06-29"
scope: "shared"
origin: "external"
source_class: "observational"
dataset_class: "deposit"
tier: "evaluate-next"
license: "unknown"
access:
  level: "public"
  availability: "available"
  verified: true
  verification_method: "metadata-confirmed"
  source_url: "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE92nnn/GSE92742/suppl/"
ontology_terms: []
tags: []
datapackage: datapackage.yaml
benchmark:
  domains: ["biology"]
  modalities: ["bulk-expression", "landmark-transcriptomics"]
  signal_types: ["perturbation"]
  benchmark_kinds: ["perturbation-response", "mechanism-discrimination"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark for perturbational expression signatures and mechanism ranking."
  limitations:
    - "L1000 measures landmark genes and inferred expression rather than full transcriptomes."
    - "The primary Level 5 matrices are large remote GEO artifacts; stage a task-specific slice before repeated local benchmarking."
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
