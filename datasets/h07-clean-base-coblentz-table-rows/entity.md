---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:h07-clean-base-coblentz-table-rows
type: dataset
title: H07 Coblentz table-row clean base
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
# H07 Coblentz Table-Row Clean Base

## Summary

This dataset entity records the source-level Coblentz 1916 blackbody table rows produced by `workflows/h07-fidelity`.
The workflow stages the transcribed Coblentz table, normalizes temperature and radiation fields before H07 Stefan-Boltzmann fitting, and writes a QA-gated datapackage under `data/processed/h07/clean-bases/coblentz-table-rows`.
The paired datapackage records the table-row CSV, structural QA report, file sizes, row counts, schema, and SHA-256 hashes.

## Access Verification Log

- 2026-05-30 (codex): Ran `uv run --frozen snakemake --snakefile workflows/h07-fidelity/Snakefile --cores 1 data/processed/h07/clean-bases/coblentz-table-rows/datapackage.json`.
  `data/processed/h07/clean-bases/coblentz-table-rows/qa/coblentz-table-rows-qa.json` reports `status: passed`, `row_count: 59`, `unique_id_count: 59`, and `error_count: 0`.

## Granularity At This Access Level

This entity covers cleaned Coblentz table rows and source-marker provenance.
It does not cover H07 Stefan-Boltzmann fitting, sensitivity analysis, parameter-fidelity scores, or matrix-level H07 interpretation.
Those remain downstream analysis artifacts.

## Connections To Project

- Questions/hypotheses it can inform: `hypothesis:h07-empirical-fidelity-alignment` and `question:q62-model-fidelity-validation-tiers`.
- Variables likely available: series/table identifiers, temperature fields, radiation measurements, normalized SI sigma fields, units, and source marker metadata.
- Planned usage: reusable clean base for blackbody-radiation data checks before H07-specific fitting.

## Related

- Task: `task:t632`
- Task: `task:t631`
- Task: `task:t436`
