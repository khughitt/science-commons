---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0004-observation-and-measurement-bias
type: theme
title: Observation And Measurement Bias
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
- paper:BalsaCanto2025
- paper:Comitani2023
- paper:Stock2025
- paper:Tang2025
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Observation and measurement bias tracks what each evidence modality can see,
what it systematically misses, and how those limits shape cross-cancer claims.
It covers bulk DNA, single-cell RNA, spatial assays, ctDNA, imaging, clinical
outcomes, perturbation screens, curated databases, and derived model outputs.

## Why It Matters

Many meta-level disagreements are really source-method disagreements. A signal
seen in bulk sequencing, a state inferred from single-cell RNA, and a response
endpoint measured in clinical records do not support the same claim type even
when they use similar biological language.

This theme makes observation limits explicit before meta compares recurrence,
selection, progression, resistance, or intervention evidence.

## Boundaries

This theme organizes measurement limitations and source-method artifacts. It is
not a catalog of assay technologies and should not become a generic method topic.
Assay-specific methods belong in child projects or paper notes; this theme keeps
the cross-project consequences visible.

## Guardrails

- Do not interpret absence of detection as absence of biology without naming the
  modality's detection limits.
- Do not combine evidence across bulk, single-cell, spatial, circulating, and
  clinical layers without stating what layer each supports.
- Do not let database availability, study inclusion, tumor purity, or sample
  processing become hidden biological evidence.
- Do not promote source-method artifacts into recurring cancer mechanisms.

## Open Questions

- Which modality limitations should be mandatory in every child export?
- How should meta compare evidence when two modalities observe different layers
  of a coupled process?
- When does a source-method limitation require a new child task rather than a
  caveat in the synthesis?

## Update Triggers

Review this theme when a new evidence modality enters the federation, when a
child export relies on a derived or indirect measurement, or when a cross-cancer
synthesis depends on mixing measurement layers.
