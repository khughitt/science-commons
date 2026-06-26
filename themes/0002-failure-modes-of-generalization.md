---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0002-failure-modes-of-generalization
type: theme
title: Failure Modes Of Generalization
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs:
- report:0004-phase-7-deep-read-synthesis
- report:0005-phase-8-evidence-operationalization
- report:0007-child-evidence-export-checklist
- report:0008-meta-methods-literature-synthesis
related:
- question:0001-recurring-evolutionary-features
- question:0002-tissue-origin-vs-selection
- question:0003-indolent-vs-progressive-clones
- question:0004-driver-cause-vs-marker
- question:0005-cross-cancer-resistance-mechanisms
source_refs:
- paper:BalsaCanto2025
- paper:Fletcher2022
- paper:Neal2025
- paper:Sanchez2022
- paper:Wahl2024
- report:0016-reproducibility-robustness-and-evidence-quality-synthesis
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Failure modes of generalization name the ways cross-cancer synthesis can become
wrong while still sounding plausible. The main risks are source-method artifacts,
survivorship and selection bias, treatment-history confounding, tumor purity,
lineage vocabulary mismatch, endpoint mismatch, and aggregation across
incompatible layers or scales.

## Why It Matters

The meta project exists to synthesize across children, so its main failure mode
is over-generalization. Naming these risks as a theme makes them reusable across
questions, reports, evidence exports, and future child-routing decisions.

## Boundaries

This theme is a guardrail set for synthesis quality. It is not a generic list of
limitations for every paper, and it should not replace specific uncertainty,
confounding, or validation notes in child projects. Use it when the failure mode
affects whether meta can compare or generalize claims across projects.

## Guardrails

- Always ask what artifact would produce the same cross-cancer pattern.
- Keep measurement layer, biological scale, population, and endpoint visible in
  the claim sentence or export table.
- Treat vocabulary mismatch as a substantive synthesis risk, not a naming issue.
- Preserve negative and non-portable cases because they define the boundary of a
  meta claim.
- Do not use generic robustness, replication, or weight-of-evidence labels without the target, modifier, metric, scoring rule, and interpretation threshold.

## Open Questions

- Which failure modes recur often enough to become standard fields in child
  evidence exports?
- How should meta rank claims that are recurrent but vulnerable to different
  failure modes in different children?
- When is a failure mode a reason to block synthesis, and when is it a named
  limitation that can travel with the claim?

## Update Triggers

Review this theme when a synthesis report generalizes across cancer types, when
child exports disagree, when a new data source changes ascertainment, or when a
claim depends on treatment history, endpoint definition, tumor purity, or
cross-lineage vocabulary alignment.
