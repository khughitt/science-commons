---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:h07-clean-base-dart-event-window
kind: dataset
title: H07 DART event-window clean base
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
# H07 DART Event-Window Clean Base

## Summary

This dataset entity records the source-level DART 21418 event-window rows produced by `workflows/h07-fidelity`.
The workflow stages the NOAA DART source file, extracts event-window observations before H07 shallow-water scoring, and writes a QA-gated datapackage under `data/processed/h07/clean-bases/dart-event-window`.
The paired datapackage records the event-window CSV, structural QA report, file sizes, row counts, schema, and SHA-256 hashes.

## Access Verification Log

- 2026-05-30 (codex): Ran `uv run --frozen snakemake --snakefile workflows/h07-fidelity/Snakefile --cores 1 data/processed/h07/clean-bases/dart-event-window/datapackage.json`.
  `data/processed/h07/clean-bases/dart-event-window/qa/dart-event-window-qa.json` reports `status: passed`, `row_count: 834`, `unique_id_count: 834`, and `error_count: 0`.

## Granularity At This Access Level

This entity covers cleaned DART station event-window rows and source-marker provenance.
It does not cover the H07 shallow-water reference reduction, fit estimate, parameter-fidelity score, or matrix-level H07 interpretation.
Those remain downstream analysis artifacts.

## Connections To Project

- Questions/hypotheses it can inform: `hypothesis:h07-empirical-fidelity-alignment` and `question:q62-model-fidelity-validation-tiers`.
- Variables likely available: station ID, timestamp, observed height, residual, event-relative time, and source marker metadata.
- Planned usage: reusable clean base for tsunami shallow-water data checks before H07-specific scoring.

## Related

- Task: `task:t632`
- Task: `task:t631`
