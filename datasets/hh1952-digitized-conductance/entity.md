---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:hh1952-digitized-conductance
kind: dataset
title: Hodgkin-Huxley 1952 digitized conductance traces
version: "1.0.0"
created: "2026-05-30"
updated: "2026-05-30"
tags: []
access:
  level: public
  availability: available
  available_after: ''
  verified: true
  verification_method: retrieved
  last_reviewed: '2026-05-30'
  verified_by: codex
  source_url: https://raw.githubusercontent.com/Chaste/project_HodgkinHuxleyABC/master/src/HodgkinHuxley.py
  credentials_required: ''
  exception:
    mode: ''
    decision_date: ''
    followup_task: ''
    superseded_by_dataset: ''
    rationale: ''
accessions: []
consumed_by:
- task:t251
- task:t377
datapackage: datapackage.yaml
ontology_terms: []
origin: external
siblings: []
source_class: reference
status: active
tier: use-now
update_cadence: static
---
# Hodgkin-Huxley 1952 Digitized Conductance Traces

## Summary

This dataset entity records the clean-base conductance substrate produced by `workflows/hh-voltage-clamp`.
The workflow retrieves the public Chaste Hodgkin-Huxley accessor, extracts the digitized Figure 3 potassium and Figure 6 sodium conductance traces, and writes `data/processed/hh-voltage-clamp/hh1952-digitized-conductance.json`.
The paired datapackage records the retrieved accessor, staged marker, extracted conductance JSON, file sizes, and SHA-256 hashes.

## Access Verification Log

- 2026-05-30 (codex): Verified the public Chaste accessor URL by rerunning `uv run --frozen snakemake -s workflows/hh-voltage-clamp/Snakefile --cores 1`; the default target produced `data/processed/hh-voltage-clamp/qa/conductance-qa.json` with `status: pass` and `datapackage: pass`.

## Granularity At This Access Level

This entity covers the extracted conductance traces and their source accessor, not a full independent transcription of the Hodgkin-Huxley 1952 paper.
It is suitable as the reusable base substrate for conductance-generalization and source-audit workflows.
It is not sufficient by itself to unblock rate-recovery parameter-fidelity scoring against Chaste-reported rates, which remain diagnostic and non-independent.

## Connections To Project

- Questions/hypotheses it can inform: `hypothesis:h07-empirical-fidelity-alignment`.
- Variables likely available: trace figure, channel, plot index, time in milliseconds, conductance in millimho per square centimeter, and Chaste-reported diagnostic rate metadata.
- Planned usage: upstream clean base for `workflows/hh-source-audit` and `workflows/hh-fit`.

## Related

- Task: `task:t251`
- Task: `task:t377`
