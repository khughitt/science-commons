---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0005-transportability-across-cancer-types
kind: theme
title: Transportability Across Cancer Types
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs:
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
- paper:Carver2026
- paper:Lechner2025
- paper:Sanchez2022
- paper:Tang2025
- paper:Wahl2024
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Transportability asks when a claim from one child project, cancer type, cohort,
assay, or treatment context can be carried into another without changing its
meaning. It treats tissue, lineage, treatment history, measurement layer,
aggregation scale, cohort selection, and endpoint definition as explicit
constraints rather than background details.

## Why It Matters

The meta project asks what recurs across cancer, but recurrence is not the same
as portability. A child claim becomes useful for federation-level synthesis only
when the conditions that made it true locally are visible enough to compare,
limit, or deliberately transfer.

This theme should keep cross-cancer synthesis from turning a local signal into a
general cancer principle before the transport conditions are named.

## Boundaries

This theme organizes portability rules across multiple claims. It is not a
single biological mechanism, not an atomic concept, and not a task to run one
validation. Local biological evidence stays in the relevant child project; meta
uses this theme to decide whether that evidence can be compared, contrasted, or
exported across children.

## Guardrails

- Do not treat shared vocabulary as evidence of shared mechanism.
- Do not transport a claim across cancer types without naming the measurement
  layer, scale, population, and treatment context.
- Do not merge pediatric, adult, precursor, treatment-naive, and relapsed cohorts
  unless the synthesis states why the grouping is appropriate.
- Do not use pathway recurrence alone as portability evidence for intervention
  or resistance claims.

## Open Questions

- Which transport constraints are mandatory for all meta synthesis, and which
  depend on the claim type?
- When should a claim be called non-portable rather than merely under-specified?
- How should meta represent a claim that transports only after re-indexing by
  lineage, treatment exposure, or measurement layer?

## Update Triggers

Review this theme when a child project exports a claim intended for cross-cancer
use, when a new child joins the federation, or when a synthesis report promotes a
local finding into a meta-level recurrence, resistance, progression, or
intervention claim.
