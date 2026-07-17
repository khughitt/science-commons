---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:h07-clean-base-gebco-path-samples
kind: dataset
title: H07 GEBCO path-sample clean base
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
# H07 GEBCO Path-Sample Clean Base

## Summary

This dataset entity records the source-level GEBCO bathymetry path samples produced by `workflows/h07-fidelity`.
The workflow stages the GEBCO subset for the Tohoku-to-DART path, extracts path-depth samples before H07 wave-speed scoring, and writes a QA-gated datapackage under `data/processed/h07/clean-bases/gebco-path-samples`.
The paired datapackage records the path-sample CSV, structural QA report, file sizes, row counts, schema, and SHA-256 hashes.

## Access Verification Log

- 2026-05-30 (codex): Ran `uv run --frozen snakemake --snakefile workflows/h07-fidelity/Snakefile --cores 1 data/processed/h07/clean-bases/gebco-path-samples/datapackage.json`.
  The pinned GEBCO basket endpoint returned `HTTP 500` during the first build attempt, so this run reused the existing local staged ASCII grid and marker before extracting the clean base.
  `data/processed/h07/clean-bases/gebco-path-samples/qa/gebco-path-samples-qa.json` reports `status: passed`, `row_count: 256`, `unique_id_count: 256`, and `error_count: 0`.

## Granularity At This Access Level

This entity covers cleaned bathymetry samples along the configured path and source-marker provenance.
It does not cover the H07 shallow-water reference reduction, fit estimate, parameter-fidelity score, or matrix-level H07 interpretation.
Those remain downstream analysis artifacts.

## Connections To Project

- Questions/hypotheses it can inform: `hypothesis:h07-empirical-fidelity-alignment` and `question:q62-model-fidelity-validation-tiers`.
- Variables likely available: sample index, path fraction, latitude, longitude, elevation or depth, and source marker metadata.
- Planned usage: reusable clean base for bathymetry-derived path checks before H07-specific scoring.

## Related

- Task: `task:t632`
- Task: `task:t631`
