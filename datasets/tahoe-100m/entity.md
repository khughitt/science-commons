---
schema_profile: "science-entity-base/1.0+dataset/2.0"
id: "dataset:tahoe-100m"
kind: "dataset"
title: "Tahoe-100M perturbation atlas"
version: "1.0.0"
status: "candidate"
created: "2026-06-27"
updated: "2026-06-29"
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
  verification_method: "metadata-confirmed"
  source_url: "https://www.openproblems.bio/"
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
    - "Pointer seed for a large perturbation atlas candidate; useful to test how sparse benchmark metadata behaves before staging."
  limitations:
    - "Tracked candidate only; verify canonical landing page, license, and access package before converting to deposit."
  tasks:
    - id: compound-response-generalization
      task_type: "response-prediction"
      prediction_target: "post-perturbation single-cell transcriptomic response"
      held_out_unit: "perturbation or perturbation-context pair"
      metric: "rank correlation"
      baseline: "matched control expression state"
      ground_truth:
        type: "measured-outcome"
        description: "measured post-perturbation single-cell expression state"
      interpretation_limits:
        - "Pointer-level task metadata only; runtime use requires verifying and staging an analysis-ready Tahoe-100M package."
      intervention: "perturbation identity and dose where available"
      contexts: ["cell context", "perturbation", "dose"]
---
# Tahoe-100M perturbation atlas
