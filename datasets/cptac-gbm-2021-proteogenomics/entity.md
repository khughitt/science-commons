---
schema_profile: "science-entity-base/1.0+dataset/1.0"
id: "dataset:cptac-gbm-2021-proteogenomics"
kind: "dataset"
title: "CPTAC GBM proteogenomics (cBioPortal, Cell 2021)"
version: "1.0.0"
status: "active"
created: "2026-07-03"
updated: "2026-07-03"
scope: "shared"
origin: "external"
source_class: "derived"
derived_kind: "transform"
dataset_class: "deposit"
tier: "evaluate-next"
license: "ODbL-1.0"
access:
  level: "public"
  availability: "available"
  verified: true
  verification_method: "metadata-confirmed"
  source_url: "https://github.com/cBioPortal/datahub/tree/master/public/gbm_cptac_2021"
ontology_terms: []
tags: []
datapackage: datapackage.yaml
benchmark:
  domains: ["biology", "cancer", "glioblastoma"]
  modalities: ["proteomics", "bulk-rna-seq", "genomics", "multimodal"]
  signal_types: ["cross-sectional", "multi-omic"]
  benchmark_kinds: ["cross-modal-prediction", "mechanism-discrimination"]
  source_datasets: ["dataset:cptac-proteogenomics"]
  related_beliefs: []
  notes:
    - "Study-specific CPTAC GBM package derived from cBioPortal DataHub gbm_cptac_2021."
    - "Fetchability spike on 2026-07-03 verified direct GitHub LFS object downloads for mRNA and protein matrices."
    - "cBioPortal DataHub publishes its study data under the Open Data Commons Open Database License."
  limitations:
    - "cBioPortal-derived package; DataHub uses ODbL terms, so attribution and share-alike terms apply."
    - "Cross-modal prediction is observational and cross-sectional, not causal perturbation evidence."
  tasks:
    - id: protein-rna-cross-modal
      task_type: "cross-modal-prediction"
      prediction_target: "mass-spectrometry protein abundance from mRNA expression"
      held_out_unit: "gene-by-sample protein measurements"
      metric: "held-out Pearson correlation"
      baseline: "per-protein training-set mean"
      ground_truth:
        type: "measured-proteomics"
        description: "protein abundance ratio measured by mass spectrometry in the matched CPTAC GBM sample"
      interpretation_limits:
        - "Cross-sectional association benchmark; do not interpret mRNA-to-protein prediction as causal regulation."
        - "Feature and target matrices are cBioPortal-transformed derivatives of CPTAC GBM source data."
      contexts: ["glioblastoma", "matched tumor sample", "mRNA expression", "protein abundance"]
      support:
        state: supported
        checked_at: "2026-07-03"
        evidence:
          - datapackage.yaml
          - datapackage.yaml#resources
          - "~/d/science/docs/audits/benchmark-cptac-gbm-fetchability-spike-2026-07-03.md"
          - "https://github.com/cBioPortal/datahub/blob/master/LICENSE"
        notes:
          - "Direct GitHub LFS batch downloads verified mRNA SHA-256 235cef753fc34d0168e97c145616bcfb3fe1c2f726038bef891639dfbec05722 and protein SHA-256 b5512312c26b68b1f137fa493448ecce0e9a8b44a5bd35b8cc9dfb67f68a6a0e."
          - "Runnable deposit benchmark for cross-modal mRNA-to-protein prediction in matched CPTAC GBM samples."
---
# CPTAC GBM proteogenomics
