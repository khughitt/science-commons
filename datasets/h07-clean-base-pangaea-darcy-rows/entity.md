---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:h07-clean-base-pangaea-darcy-rows
kind: dataset
title: H07 PANGAEA Darcy row clean base
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
# H07 PANGAEA Darcy Row Clean Base

## Summary

This dataset entity records the source-level PANGAEA permeameter rows produced by `workflows/h07-fidelity`.
The workflow stages the PANGAEA table, extracts cleaned Darcy-row measurements before H07 parameter fitting, and writes a QA-gated datapackage under `data/processed/h07/clean-bases/pangaea-darcy-rows`.
The paired datapackage records the Darcy-row CSV, structural QA report, file sizes, row counts, schema, and SHA-256 hashes.

## Access Verification Log

- 2026-05-30 (codex): Ran `uv run --frozen snakemake --snakefile workflows/h07-fidelity/Snakefile --cores 1 data/processed/h07/clean-bases/pangaea-darcy-rows/datapackage.json`.
  `data/processed/h07/clean-bases/pangaea-darcy-rows/qa/pangaea-darcy-rows-qa.json` reports `status: passed`, `row_count: 39`, `unique_id_count: 39`, and `error_count: 0`.

## Granularity At This Access Level

This entity covers cleaned permeameter rows and source-marker provenance.
It does not cover H07 Darcy parameter aggregation, fit estimates, parameter-fidelity scores, or matrix-level H07 interpretation.
Those remain downstream analysis artifacts.

## Connections To Project

- Questions/hypotheses it can inform: `hypothesis:h07-empirical-fidelity-alignment` and `question:q62-model-fidelity-validation-tiers`.
- Variables likely available: sample ID, permeability or hydraulic-conductivity fields, units, recomputed row-level conductivity, and source marker metadata.
- Planned usage: reusable clean base for Darcy-law data checks before H07-specific fitting.

## Related

- Task: `task:t632`
- Task: `task:t631`
