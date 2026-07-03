---
schema_profile: "science-entity-base/1.0+dataset/1.0"
id: "dataset:mmrf-commpass"
type: "dataset"
title: "MMRF CoMMpass"
version: "1.0.0"
status: "active"
created: "2026-06-28"
updated: "2026-07-03"
scope: "shared"
origin: "external"
source_class: "observational"
dataset_class: "pointer"
tier: "track"
license: "restricted"
access:
  level: "public"
  availability: "available"
  verified: true
  verification_method: "landing-confirmed"
  source_url: "https://registry.opendata.aws/mmrf-commpass/"
ontology_terms: []
tags: []
benchmark:
  domains: ["biology", "cancer", "multiple-myeloma"]
  modalities: ["bulk-rna-seq", "genomics", "clinical", "multimodal"]
  signal_types: ["longitudinal", "time-series", "clinical-outcome", "multi-omic"]
  benchmark_kinds: ["static-association", "cross-context-generalization", "time-series-forecasting"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark for longitudinal multiple myeloma progression and treatment-response questions."
    - "CoMMpass includes molecular and clinical data with longitudinal disease-course context."
  limitations:
    - "Access, consent, and redistribution terms must be checked before staging analysis-ready resources."
    - "Longitudinal sampling density varies by patient and assay."
  tasks:
    - id: progression-risk
      task_type: "outcome-prediction"
      prediction_target: "progression or relapse risk from baseline molecular and clinical features"
      held_out_unit: "patient"
      metric: "concordance-index"
      baseline: "clinical covariates"
      ground_truth:
        type: "measured-outcome"
        description: "observed clinical progression or relapse outcome"
      interpretation_limits:
        - "Associational clinical benchmark; causal treatment conclusions require stronger design."
      timepoints: ["baseline and follow-up disease-course observations where available"]
      contexts: ["patient", "treatment line", "disease stage"]
      support:
        state: blocked
        reason: open-metadata-missing-progression-endpoint
        checked_at: "2026-07-03"
        evidence:
          - recipe/manifest.schema.yaml#validation_report.task_support
          - recipe/README.md#dry-run
        notes:
          - Live GDC dry run on 2026-07-03 reported endpoint_status=survival-only, progression_fields=[], survival_fields=[vital_status, days_to_death], and promotable=false.
          - The same dry run reported cohort_mode=unresolved-cohort, so overall-survival remains a recipe-level candidate rather than an authored benchmark task.
---
# MMRF CoMMpass
