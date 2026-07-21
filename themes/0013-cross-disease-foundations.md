---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0013-cross-disease-foundations
kind: theme
title: Cross-disease foundations
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs: []
related: []
source_refs: []
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Cancer-federation anchor for the cross-disease foundations program. This theme marks
cancer/meta entities that participate in a coordinated effort to test whether mechanistic
axes discovered in disease-specific child projects recur at the pan-cancer or pan-disease
level. The program hub lives in health/meta:
`health/meta:doc/plans/2026-05-24-cross-disease-foundations-program.md`
(`~/d/health/meta`, `plan:cross-disease-foundations-program`).

## Why It Matters

Entities organized under this theme make the cross-disease foundations initiative
discoverable from the cancer side of the federation. Without an explicit anchor,
cancer/meta questions and topics that belong to this program scatter across unrelated
themes and are not recognized as a coordinated signal-testing effort.

## Boundaries

Cancer-scoped routing only. This theme marks questions, topics, and tasks in cancer/meta
that are direct participants in the cross-disease program. The foundational mechanistic
hypotheses and program-level plans live in health/meta, not here. Do not import
health/meta entities into cancer/meta frontmatter — cross-project references remain
prose-only.

## Guardrails

- Do not add entities to this theme unless they are part of a deliberate cross-disease
  signal test — not merely thematically adjacent to multi-cancer biology.
- Do not promote a child-project observation to a cross-disease recurrence claim without
  first running the pan-cancer test; observational support from one lineage is a
  hypothesis, not a finding.
- Cross-project references (health/meta, MM30) must stay in prose. Never put external
  project entity IDs in frontmatter `related`.

## Open Questions

- Which additional cancer/meta axes are candidates for cross-disease testing in
  iteration 2 of the program?
- What statistical standard (effect size, lineage coverage, confounder adjustment)
  is sufficient to call a pan-cancer recurrence established vs suggestive?

## Update Triggers

Review this theme when a new child-project axis is nominated for cross-disease testing,
when a pan-cancer test result is returned, or when the health/meta program hub is
revised to add or retire program-level hypotheses.
