---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0007-causal-data-integration
type: theme
title: Causal Data Integration
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs: []
related:
- question:0004-driver-cause-vs-marker
- question:0006-evidence-synthesis-method-choice
- theme:0003-intervention-readiness
- theme:0005-transportability-across-cancer-types
- theme:0009-data-integration-and-multi-omics
source_refs:
- paper:Carver2026
- paper:Long2023
- report:0012-causal-data-integration-and-estimands-synthesis
- report:0018-federation-evidence-synthesis-method-guide
- report:0021-q004-causal-claim-checklist
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Causal data integration organizes methods that combine heterogeneous data sources while preserving causal estimands, assumptions, and target populations.
It covers causal fusion, transportability, causal meta-analysis, Mendelian randomization graphs, causal mediation across molecular layers, and the integration of causal modeling with statistical estimation.

## Why It Matters

Meta-level synthesis often asks whether an observed association should be interpreted as a cause, marker, mechanism, or intervention target.
Causal data integration methods are relevant because they force the project to state the target estimand before combining evidence across studies or children.

## Boundaries

This theme is distinct from general multi-omics integration.
A model belongs here when the integration problem changes, identifies, transports, or estimates a causal claim.
Purely predictive or exploratory integration belongs primarily under `theme:0009-data-integration-and-multi-omics`.

## Guardrails

- Do not combine causal effects unless the target population and estimand are compatible.
- Do not treat adjustment, mediation, Mendelian randomization, and causal discovery as interchangeable routes to causality.
- Do not move from causal plausibility to intervention readiness without naming the intervention, comparator, timing, and endpoint.
- Do not use causal vocabulary for integrated associations unless the assumptions are explicit.
