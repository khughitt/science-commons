---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0001-cross-scale-state-transitions
type: theme
title: Cross-Scale State Transitions
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs:
- report:0004-phase-7-deep-read-synthesis
- report:0005-phase-8-evidence-operationalization
- report:0008-meta-methods-literature-synthesis
related:
- question:0001-recurring-evolutionary-features
- question:0002-tissue-origin-vs-selection
- question:0003-indolent-vs-progressive-clones
- question:0004-driver-cause-vs-marker
- question:0005-cross-cancer-resistance-mechanisms
source_refs:
- cancer-meta:paper:Mao2025
- paper:Fletcher2022
- paper:Heiner2013
- paper:Neal2025
- paper:Rohbeck2025
- paper:Seyfried2014
- paper:Wurthner2022
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Cross-scale state transitions organize claims that connect clone, cell state,
tissue ecology, immune context, treatment exposure, and clinical phenotype. The
theme keeps progression, plasticity, resistance, relapse, and pre-cancer
transition language tied to the scale where the transition is observed or
modeled.

## Why It Matters

The federation spans pre-cancer, cancer evolution, multiple myeloma, and
data-source work. Those projects all use transition language, but they often
mean different things: clonal expansion, transcriptional plasticity, tissue
reorganization, treatment response, or clinical progression. This theme prevents
those meanings from collapsing into one vague state-change concept.

## Boundaries

This theme organizes multi-claim synthesis across scales. It is not a single
biological transition, pathway, or mechanism. A biological theme would organize
multiple concepts and mechanisms, but this meta theme is methodological because
it governs how state-transition claims are compared across child projects.

## Guardrails

- Do not use progression, plasticity, resistance, and relapse as interchangeable
  labels.
- Do not infer temporal order from cross-sectional state differences without
  naming the temporal evidence or model assumption.
- Do not treat cell-state transitions as clonal transitions unless the evidence
  links state, lineage, and time.
- Do not mix biological scale with measurement layer; a single-cell assay can be
  used to infer different biological scales depending on the model.

## Open Questions

- Which transition types recur across child projects after layer and scale are
  controlled?
- How should meta represent a transition that is observed at one scale but
  hypothesized to be caused at another?
- When does a transition claim become a mechanism claim rather than a theme-level
  organizing problem?

## Update Triggers

Review this theme when child projects export progression, plasticity,
resistance, relapse, or adaptive-therapy claims, or when a synthesis report links
pre-cancer, evolution, and disease-specific evidence through shared transition
language.
