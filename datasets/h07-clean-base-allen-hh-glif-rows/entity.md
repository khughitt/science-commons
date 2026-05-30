---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:h07-clean-base-allen-hh-glif-rows
type: dataset
title: H07 Allen HH/GLIF row clean base
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
# H07 Allen HH/GLIF Row Clean Base

## Summary

This dataset entity records the source-level Allen Cell Types electrophysiology rows produced by `workflows/h07-fidelity`.
The workflow stages Allen specimen-detail data, extracts shared HH/GLIF feature rows before H07 parameter-primary reductions, and writes a QA-gated datapackage under `data/processed/h07/clean-bases/allen-hh-glif-rows`.
The paired datapackage records the HH/GLIF row CSV, structural QA report, file sizes, row counts, schema, and SHA-256 hashes.

## Access Verification Log

- 2026-05-30 (codex): Ran `uv run --frozen snakemake --snakefile workflows/h07-fidelity/Snakefile --cores 1 data/processed/h07/clean-bases/allen-hh-glif-rows/datapackage.json`.
  `data/processed/h07/clean-bases/allen-hh-glif-rows/qa/allen-hh-glif-rows-qa.json` reports `status: passed`, `row_count: 2333`, `unique_id_count: 2333`, and `error_count: 0`.

## Granularity At This Access Level

This entity covers cleaned Allen specimen rows and source-marker provenance for the shared HH/GLIF substrate.
It does not cover H07 HH/GLIF parameter-primary reductions, fit estimates, parameter-fidelity scores, or matrix-level H07 interpretation.
Those remain downstream analysis artifacts.

## Connections To Project

- Questions/hypotheses it can inform: `hypothesis:h07-empirical-fidelity-alignment` and `question:q62-model-fidelity-validation-tiers`.
- Variables likely available: specimen and cell identifiers, model-family eligibility flags, electrophysiology feature columns, derived GLIF threshold fields, and source marker metadata.
- Planned usage: reusable clean base for Allen electrophysiology checks before H07-specific fitting.

## Related

- Task: `task:t632`
- Task: `task:t631`
- Task: `task:t440`
