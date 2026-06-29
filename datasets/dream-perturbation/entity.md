---
schema_profile: "science-entity-base/1.0+dataset/1.0"
id: "dataset:dream-perturbation"
type: "dataset"
title: "DREAM perturbation challenge registry"
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
  source_url: "https://dreamchallenges.org/"
ontology_terms: []
tags: []
benchmark:
  domains: ["biology"]
  modalities: ["varies"]
  signal_types: ["perturbation"]
  benchmark_kinds: ["mechanism-discrimination"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Reference-class registry for challenge-style perturbation benchmarks."
  limitations:
    - "Registry record only; individual challenge datasets require separate dataset records before runtime use."
  tasks:
    - id: perturbation-mechanism-recovery
      task_type: "mechanism-discrimination"
      prediction_target: "causal regulator, pathway, or mechanism implied by perturbation-response measurements"
      held_out_unit: "challenge dataset, perturbation condition, or held-out label set"
      metric: "challenge-specific ranking metric"
      baseline: "challenge-provided baseline or leaderboard reference model"
      ground_truth:
        type: "challenge-held-out-label"
        description: "challenge-specific held-out labels or reference answers"
      interpretation_limits:
        - "Registry-level task metadata only; use an individual DREAM challenge dataset record for runtime benchmarking."
      intervention: "challenge-specific perturbation"
      contexts: ["challenge", "perturbation", "assay"]
---
# DREAM perturbation challenge registry
