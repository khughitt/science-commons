---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:h07-clean-base-gause-monoculture-rows
kind: dataset
title: H07 Gause monoculture row clean base
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
# H07 Gause Monoculture Row Clean Base

## Summary

This dataset entity records the source-level Gause Paramecium monoculture rows produced by `workflows/h07-fidelity`.
The workflow stages the Gause monoculture trajectories, extracts species/day/count rows before H07 logistic-growth reductions, and writes a QA-gated datapackage under `data/processed/h07/clean-bases/gause-monoculture-rows`.
The paired datapackage records the monoculture-row CSV, structural QA report, file sizes, row counts, schema, and SHA-256 hashes.

## Access Verification Log

- 2026-05-30 (codex): Ran `uv run --frozen snakemake --snakefile workflows/h07-fidelity/Snakefile --cores 1 data/processed/h07/clean-bases/gause-monoculture-rows/datapackage.json`.
  `data/processed/h07/clean-bases/gause-monoculture-rows/qa/gause-monoculture-rows-qa.json` reports `status: passed`, `row_count: 48`, `unique_id_count: 48`, and `error_count: 0`.

## Granularity At This Access Level

This entity covers cleaned Gause monoculture trajectory rows and source-marker provenance.
It does not cover H07 logistic-growth reductions, fit estimates, parameter-fidelity scores, or matrix-level H07 interpretation.
Those remain downstream analysis artifacts.

## Connections To Project

- Questions/hypotheses it can inform: `hypothesis:h07-empirical-fidelity-alignment` and `question:q62-model-fidelity-validation-tiers`.
- Variables likely available: species, day or time, abundance/count, source row identifiers, replicate/source labels, and source marker metadata.
- Planned usage: reusable clean base for population-growth data checks before H07-specific fitting.

## Related

- Task: `task:t632`
- Task: `task:t631`
- Task: `task:t440`
