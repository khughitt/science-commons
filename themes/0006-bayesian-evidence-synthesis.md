---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0006-bayesian-evidence-synthesis
kind: theme
title: Bayesian Evidence Synthesis
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs: []
related:
- question:0006-evidence-synthesis-method-choice
- theme:0002-failure-modes-of-generalization
- theme:0003-intervention-readiness
- theme:0005-transportability-across-cancer-types
source_refs:
- report:0010-bayesian-evidence-synthesis-and-calibration-synthesis
- report:0011-bayesian-meta-analysis-core-methods-synthesis
- report:0018-federation-evidence-synthesis-method-guide
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Bayesian evidence synthesis organizes methods for combining evidence across studies, models, assumptions, and data sources while preserving uncertainty.
It covers Bayesian meta-analysis, Bayes factors, Bayesian evidence synthesis for heterogeneous replications, model averaging, prior sensitivity, and Bayesian calibration with external evidence.

## Why It Matters

The meta project needs to combine evidence across child projects without treating every study as exchangeable.
Bayesian synthesis methods are relevant because they can make prior information, study heterogeneity, model uncertainty, and evidence accumulation explicit.

This theme is especially important when conventional meta-analysis is too narrow for the federation's evidence structure.
Cross-cancer synthesis often compares studies that differ in population, measurement layer, estimand, and endpoint rather than repeating the same design.

## Boundaries

This theme is methodological.
It does not make a biological claim by itself and should not become a generic statistics bucket.
Use it when the project needs to decide how evidence should be accumulated, how priors should be represented, or how study heterogeneity changes the interpretation of a combined claim.

## Guardrails

- Do not treat a pooled estimate as meaningful unless the estimand, population, measurement layer, and heterogeneity assumptions are explicit.
- Do not use Bayes factors or posterior probabilities without documenting prior sensitivity when the conclusion would affect project direction.
- Do not collapse conceptual replication, direct replication, meta-analysis, and Bayesian updating into one synthesis problem.
- Do not use external evidence as a prior without naming its provenance and checking whether it is transportable to the target claim.
