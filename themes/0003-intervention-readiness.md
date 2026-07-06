---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0003-intervention-readiness
kind: theme
title: Intervention Readiness
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs:
- report:0005-phase-8-evidence-operationalization
- report:0007-child-evidence-export-checklist
- report:0008-meta-methods-literature-synthesis
- report:0021-q004-causal-claim-checklist
related:
- question:0003-indolent-vs-progressive-clones
- question:0004-driver-cause-vs-marker
- question:0005-cross-cancer-resistance-mechanisms
source_refs:
- cancer-meta:paper:Mao2025
- paper:Lechner2025
- paper:Miladinovic2025
- paper:Rohbeck2024
- paper:Sanchez2022
theme_kind: methodological
theme_scope: cross-project
---
## Definition

Intervention readiness separates evidence that a mechanism exists from evidence
that the mechanism can guide treatment, prevention, monitoring, or adaptive
control. It asks whether the claim has an intervention, comparator, target
population, timing, endpoint, uncertainty estimate, and decision rule.

## Why It Matters

Meta needs a disciplined bridge from biological explanation to clinical action.
Driver, resistance, progression, and perturbation claims can be biologically
important without being ready to guide treatment. This theme keeps those levels
separate while showing what evidence would move a claim closer to actionability.

## Boundaries

This theme is not a treatment guideline and does not decide clinical standard of
care. It organizes evidence readiness for research synthesis. Local therapeutic
claims, disease-specific evidence, and trial details stay in the relevant child
project unless meta is comparing readiness across children.

## Guardrails

- Do not equate mechanism existence with treatment utility.
- Do not equate perturbation response in a model system with a patient-level
  treatment effect unless the population, intervention, comparator, and endpoint
  are named.
- Do not mix prognostic, predictive, causal, and decision-rule claims.
- Do not treat adaptive-therapy logic as ready for use without observability and
  control constraints.

## Open Questions

- What is the minimum evidence package for a meta claim to be called
  intervention-relevant?
- How should the federation represent mechanisms that are causally plausible but
  not currently observable or controllable?
- When should intervention readiness be evaluated at the subgroup, patient, or
  treatment-sequence level?

## Update Triggers

Review this theme when a child project proposes a treatment-relevant export,
when perturbation evidence is added to a mechanism claim, or when adaptive
therapy, prevention, or monitoring tasks are created.
