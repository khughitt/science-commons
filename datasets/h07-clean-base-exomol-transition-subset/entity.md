---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:h07-clean-base-exomol-transition-subset
type: dataset
title: H07 ExoMol transition-subset clean base
version: "1.0.0"
created: "2026-05-30"
updated: "2026-05-30"
tags: []
datapackage: datapackage.yaml
derivation:
  kind: workflow
  workflow_recipe: workflow:h07-fidelity
  inputs: []
  recipe_lockfile: workflows/h07-fidelity/config.yaml
license: unknown
origin: derived
source_class: observational
status: active
tier: use-now
---
# H07 ExoMol Transition-Subset Clean Base

## Summary

This dataset entity records the source-level ExoMol CO transition subset produced by `workflows/h07-fidelity`.
The workflow stages the ExoMol Li2015 state and transition files, joins selected transitions to parsed state rows before H07 omega-e estimation, and writes a QA-gated datapackage under `data/processed/h07/clean-bases/exomol-transition-subset`.
The paired datapackage records the transition-subset CSV, structural QA report, file sizes, row counts, schema, and SHA-256 hashes.

## Access Verification Log

- 2026-05-30 (codex): Ran `uv run --frozen snakemake --snakefile workflows/h07-fidelity/Snakefile --cores 1 data/processed/h07/clean-bases/exomol-transition-subset/datapackage.json`.
  `data/processed/h07/clean-bases/exomol-transition-subset/qa/exomol-transition-subset-qa.json` reports `status: passed`, `row_count: 120`, `unique_id_count: 120`, and `error_count: 0`.

## Granularity At This Access Level

This entity covers parsed state/transition rows and source-marker provenance for the selected CO band subset.
It does not cover H07 omega-e fitting, fit uncertainty, parameter-fidelity scores, or matrix-level H07 interpretation.
Those remain downstream analysis artifacts.

## Connections To Project

- Questions/hypotheses it can inform: `hypothesis:h07-empirical-fidelity-alignment` and `question:q62-model-fidelity-validation-tiers`.
- Variables likely available: transition ID, upper/lower state IDs, line intensity or transition metadata, vibrational and rotational quantum numbers, and source marker metadata.
- Planned usage: reusable clean base for CO spectral-line checks before H07-specific fitting.

## Related

- Task: `task:t632`
- Task: `task:t631`
- Task: `task:t434`
