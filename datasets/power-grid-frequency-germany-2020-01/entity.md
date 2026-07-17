---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:power-grid-frequency-germany-2020-01
kind: dataset
title: Power-Grid Frequency Germany January 2020
version: "1.0.0"
created: "2026-05-31"
updated: "2026-05-31"
tags: []
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
  last_reviewed: '2026-05-31'
  verified_by: codex
  source_url: https://osf.io/download/5eef6d1d76ebd8015fce13df/
datapackage: datapackage.yaml
license: unknown
origin: external
source_class: observational
status: active
tier: use-now
update_cadence: static
---
# Power-Grid Frequency Germany January 2020

## Summary

This dataset entity records one month of Germany-area power-grid frequency measurements from the Power-grid Frequency Database, prepared by `workflows/h08-empirical-grounding`.
The workflow downloads the OSF-hosted zipped CSV, normalizes the two-column time series into row-level frequency-deviation records, runs contract QA, and writes a datapackage under `data/processed/h08-empirical-grounding/power-grid-frequency-germany-2020-01`.

The paired datapackage records the normalized CSV, raw staging manifest, QA report, row counts, file sizes, and SHA-256 hashes.

## Access Verification Log

- 2026-05-31 (codex): Ran `uv run --frozen snakemake -s workflows/h08-empirical-grounding/Snakefile --cores 1 data/processed/h08-empirical-grounding/power-grid-frequency-germany-2020-01/datapackage.json`.
  The staging step downloaded `https://osf.io/download/5eef6d1d76ebd8015fce13df/`, the Germany January 2020 CSV zip linked from the Power-grid Frequency Database.
  The normalized table has 2,418,495 rows and 2,418,495 unique row IDs.
  `data/processed/h08-empirical-grounding/power-grid-frequency-germany-2020-01/qa/power-grid-frequency-germany-2020-01-qa.json` reports `status: passed`, `column_count: 12`, and no errors.

## Granularity At This Access Level

This entity covers Germany-area frequency-deviation observations for January 2020 at the access level exposed by the database file.
It does not cover other synchronous areas, other months, or any downstream synchronization/Kuramoto reduction.
Those should be separate workflow targets or derived analysis products.

## Connections To Project

- Questions/hypotheses it can inform: `question:q106-bottom-up-generator-basis`, `hypothesis:h08-bottom-up-generator-basis`, `hypothesis:h07-empirical-fidelity-alignment`, and `question:q62-model-fidelity-validation-tiers`.
- Variables available: observation timestamp, frequency deviation in mHz, location, country, synchronous area, evidence tier, promotability flag, and independence group.
- Independence handling: this substrate is tagged `independence_group: power-grid-frequency`, so additional power-grid months or regions should not be counted as independent evidence rows by default.
- Planned usage: empirical grounding for synchronization and frequency-stability generator families, with downstream reductions kept separate from the reusable clean-base dataset.

## Related

- Task: `task:t646`
- Task: `task:t644`
