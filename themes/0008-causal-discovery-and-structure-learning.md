---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0008-causal-discovery-and-structure-learning
type: theme
title: Causal Discovery And Structure Learning
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs: []
related:
- question:0004-driver-cause-vs-marker
- theme:0002-failure-modes-of-generalization
- theme:0003-intervention-readiness
- theme:0007-causal-data-integration
source_refs:
- paper:Long2023
- report:0013-causal-discovery-and-structure-learning-synthesis
- report:0021-q004-causal-claim-checklist
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Causal discovery and structure learning covers methods that infer graphical structure from observational, interventional, prior-knowledge, or mixed evidence.
It includes causal discovery toolkits, Bayesian structure learning, latent-variable discovery, causal graph validation, weak-prior structure learning, and graph-learning methods that quantify uncertainty over structure.

## Why It Matters

The federation uses graphs to organize claims, but graph structure should not be confused with established causal truth.
This theme tracks when a graph is an organizing hypothesis, a statistical discovery output, a causal model, or an intervention-ready structure.

## Boundaries

This theme is about structure inference and validation.
It is not the same as `theme:0007-causal-data-integration`, which governs combining sources for causal estimands.
It is also not a replacement for child-owned biological mechanism work.

## Guardrails

- Do not promote a discovered edge without naming the assumptions used to identify it.
- Do not treat acyclic graph output as adequate for cyclic gene regulatory networks, feedback, or treatment-response systems unless the method supports those structures.
- Do not evaluate causal discovery only on simulated ground truth when real-data compatibility checks are available.
- Do not hide prior knowledge inside an algorithm without recording its provenance.
