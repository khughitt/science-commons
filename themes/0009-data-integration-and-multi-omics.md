---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0009-data-integration-and-multi-omics
type: theme
title: Data Integration And Multi-Omics
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs: []
related:
- report:0007-child-evidence-export-checklist
- theme:0001-cross-scale-state-transitions
- theme:0004-observation-and-measurement-bias
- theme:0005-transportability-across-cancer-types
source_refs:
- report:0014-statistical-data-integration-and-multi-omics-synthesis
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Data integration and multi-omics covers methods for jointly analyzing heterogeneous molecular, clinical, and derived data layers.
It includes multiview learning, integrative clustering, graphical models, network inference, prior-knowledge integration, and Bayesian or regularized models that borrow strength across cancer types, assays, or subpopulations.

## Why It Matters

The federation depends on evidence that arrives from different assays and child projects.
Data integration methods can either make these differences explicit or hide them inside a joint model.
This theme keeps the integration assumptions visible before meta promotes a cross-cancer claim.

## Boundaries

This theme is not an assay catalog.
Local preprocessing, quality control, and disease-specific analysis belong in child projects.
Meta uses this theme to reason about when integrated evidence is comparable across children and when a joint model has changed the claim being made.

## Guardrails

- Do not treat higher dimensional integration as stronger evidence unless the model's borrowing structure is defensible.
- Do not let shared latent factors erase differences between assay layer, biological scale, and population.
- Do not interpret an integrated network edge as causal unless the method and evidence support a causal claim.
- Do not borrow across cancer types without checking whether the prior, penalty, or shared component encodes a transportability assumption.
