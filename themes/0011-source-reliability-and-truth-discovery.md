---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0011-source-reliability-and-truth-discovery
type: theme
title: Source Reliability And Truth Discovery
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs: []
related:
- question:0007-source-reliability-agent-curation
- theme:0002-failure-modes-of-generalization
- theme:0004-observation-and-measurement-bias
- theme:0010-scientific-knowledge-systems-and-agents
source_refs:
- report:0017-source-reliability-truth-discovery-and-knowledge-systems-synthesis
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Source reliability and truth discovery covers methods for reconciling conflicting claims across sources, estimating source quality, cleaning data, and preserving uncertainty during integration.
It includes truth discovery, Bayesian data cleaning, weight-of-evidence methods, and systems that surface candidate correlations or claims from large heterogeneous repositories.

## Why It Matters

Meta synthesis depends on child projects, databases, papers, and derived model outputs that can disagree.
This theme keeps disagreement and source quality visible before the federation treats an integrated statement as a stable claim.

## Boundaries

This theme is about source reliability and conflict resolution.
It is not a generic data-cleaning backlog and should not absorb child-local quality-control work.
Use it when source reliability affects cross-project synthesis, graph curation, or the interpretation of conflicting evidence.

## Guardrails

- Do not treat majority agreement as truth without checking source dependence and reliability.
- Do not clean or reconcile data silently when the correction changes the claim.
- Do not collapse source reliability, measurement bias, and biological uncertainty into one caveat.
- Do not use correlation discovery as causal evidence without a separate causal analysis.
