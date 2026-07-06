---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0014-convergent-escape-nodes
kind: theme
title: Convergent Escape Nodes
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs: []
related:
- question:0005-cross-cancer-resistance-mechanisms
source_refs: []
theme_kind: conceptual
theme_scope: cross-project
---
## Definition

A convergent escape node is a single molecular state — a protein, complex, or
pathway output — that multiple distinct upstream lesions funnel into to evade an
otherwise-effective therapy. Resistance is then better predicted by the state of
the node than by any one of its upstream causes. This theme organizes the
recurring observation that diverse genetic and transcriptional routes to
resistance collapse onto a small number of shared nodes, and that those nodes are
candidate cross-cancer (not merely cross-patient) resistance hubs.

## Why It Matters

`question:0005-cross-cancer-resistance-mechanisms` asks which resistance
mechanisms are shared across therapies and which are constrained by lineage or
treatment context. Convergent escape nodes are the constructive form of the
"shared" answer: they specify *where* to look for transportable resistance
biology and *what* to measure (the node state) rather than enumerating
upstream causes that differ by patient and disease. Framing resistance around
nodes also reframes combination design — co-targeting the node, or a drug whose
mechanism is orthogonal to it, is a more durable strategy than chasing each
upstream lesion.

## Boundaries

This theme catalogs and tests *candidate* convergent nodes; it does not assert
that any node is universal. A node earns the label only with evidence that
(a) multiple independent upstream routes engage it and (b) its state predicts
resistance better than those routes individually. Disease-specific mechanistic
detail, drug-specific pharmacology, and the primary expression/dependency
analyses stay in the relevant child project. Meta owns only the cross-cancer
comparison: does a node identified in one lineage recur, and does it transport?

## Guardrails

- Do not equate "many papers mention gene X in resistance" with convergence;
  convergence requires multiple *independent upstream routes* engaging the same
  node, demonstrated, not assumed.
- Do not promote a node from one lineage to "cross-cancer" without an explicit
  transportability test in a second lineage.
- Do not conflate the node being *prognostic* (its state correlates with poor
  outcome) with the node being *causal/targetable* (perturbing it restores
  response).
- Watch for measurement substitution: an upstream cause (e.g. a cytogenetic
  lesion) is often easier to measure than the node state, but the node state is
  the claim.

## Open Questions

- What is the minimum evidence to call a node "convergent" rather than "recurrent"?
- Which candidate nodes transport across lineages, and which are
  context-constrained (the core question:0005-cross-cancer-resistance-mechanisms split)?
- Are convergent escape nodes preferentially the most therapeutically attractive
  co-targets, or does convergence also concentrate toxicity?

## Update Triggers

Review this theme when a child reports a resistance mechanism with multiple
distinct upstream routes, when a candidate node is tested in a second lineage,
or when question:0005-cross-cancer-resistance-mechanisms synthesis adds or removes a shared-mechanism claim.
