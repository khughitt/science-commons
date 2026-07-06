---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:owid-reported-measles
kind: dataset
title: OWID Reported Measles Cases
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
  source_url: https://ourworldindata.org/grapher/reported-cases-of-measles.csv?v=1&csvType=full&useColumnShortNames=false
datapackage: datapackage.yaml
license: unknown
origin: external
source_class: observational
status: active
tier: use-now
update_cadence: rolling
---
# OWID Reported Measles Cases

## Summary

This dataset entity records reported measles case counts from the Our World in Data Grapher CSV, prepared by `workflows/h08-empirical-grounding`.
The workflow downloads the current Grapher CSV, normalizes it into entity-year reported-case rows, runs contract QA, and writes a datapackage under `data/processed/h08-empirical-grounding/owid-reported-measles`.

The paired datapackage records the normalized CSV, raw staging manifest, QA report, row counts, file sizes, and SHA-256 hashes.

## Access Verification Log

- 2026-05-31 (codex): Ran `uv run --frozen snakemake -s workflows/h08-empirical-grounding/Snakefile --cores 1 data/processed/h08-empirical-grounding/owid-reported-measles/datapackage.json`.
  The staging step downloaded `https://ourworldindata.org/grapher/reported-cases-of-measles.csv?v=1&csvType=full&useColumnShortNames=false`.
  The normalized table has 9,316 rows and 9,316 unique row IDs.
  `data/processed/h08-empirical-grounding/owid-reported-measles/qa/owid-reported-measles-qa.json` reports `status: passed`, `column_count: 11`, and no errors.

## Granularity At This Access Level

This entity covers reported measles counts at OWID's entity-year granularity.
It does not cover Project Tycho lineages, outbreak reconstructions, contact networks, compartmental model fits, or branching-process reductions.
Those remain downstream analysis products or separate source datasets.

## Connections To Project

- Questions/hypotheses it can inform: `question:q106-bottom-up-generator-basis`, `hypothesis:h08-bottom-up-generator-basis`, `hypothesis:h07-empirical-fidelity-alignment`, and `question:q62-model-fidelity-validation-tiers`.
- Variables available: entity, country/code identifier when present, year, reported cases, evidence tier, promotability flag, and independence group.
- Independence handling: this substrate is tagged `independence_group: infectious-disease-measles` and overlaps existing H07 infectious-disease reductions, so same-family rows should not be treated as independent evidence by default.
- Planned usage: empirical grounding for epidemic/contact-process and branching-process generator families, with reductions and scoreable correspondence assertions kept separate from the reusable clean-base dataset.

## Related

- Task: `task:t646`
- Task: `task:t644`
