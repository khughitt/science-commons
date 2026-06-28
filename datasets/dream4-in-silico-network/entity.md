---
schema_profile: "science-entity-base/1.0+dataset/1.0"
id: "dataset:dream4-in-silico-network"
type: "dataset"
title: "DREAM4 in silico network challenge"
version: "1.0.0"
status: "active"
created: "2026-06-28"
updated: "2026-06-28"
scope: "shared"
origin: "external"
source_class: "derived"
derived_kind: "model_output"
dataset_class: "pointer"
tier: "track"
license: "unknown"
access:
  level: "public"
  availability: "available"
  verified: true
  verification_method: "landing-confirmed"
  source_url: "https://www.synapse.org/Synapse:syn3049712"
ontology_terms: []
tags: []
benchmark:
  domains: ["biology", "systems-biology"]
  modalities: ["simulated-gene-expression"]
  signal_types: ["time-series", "perturbation"]
  benchmark_kinds: ["mechanism-discrimination", "time-series-forecasting"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark for temporal and perturbational gene regulatory network inference."
    - "The DREAM4 in silico challenge includes steady-state, perturbation, and time-series expression data with known simulated network structure."
  limitations:
    - "Synthetic benchmark; biological conclusions should be limited to method validation and model-behavior checks."
    - "Verify current download terms and exact challenge package layout before staging runnable resources."
  tasks:
    - id: network-reconstruction
      task_type: "mechanism-inference"
      prediction_target: "directed regulatory network edges"
      held_out_unit: "network"
      metric: "auroc-aupr"
      baseline: "correlation network"
      ground_truth:
        type: "known-simulation"
        description: "simulated network topology used to generate expression trajectories"
      interpretation_limits:
        - "Useful for testing temporal/mechanistic inference behavior, not for organism-specific biological claims."
      timepoints: ["challenge-provided simulated time-series measurements"]
      intervention: "simulated perturbation experiments"
      contexts: ["synthetic network", "time series", "perturbation"]
---
# DREAM4 in silico network challenge
