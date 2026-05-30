---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:arxiv-source-equations
type: dataset
title: arXiv source equation records
version: "1.0.0"
created: "2026-05-30"
updated: "2026-05-30"
tags: []
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
  last_reviewed: '2026-05-30'
  verified_by: codex
  source_url: https://arxiv.org/e-print/
accessions: []
datapackage: datapackage.yaml
license: unknown
origin: external
source_class: observational
status: active
tier: use-now
---
# arXiv Source Equation Records

## Summary

This dataset entity records the equation-token records produced by `workflows/arxiv-sources`.
The workflow fetches source bundles for the configured selected arXiv IDs, records inaccessible-source failures separately, extracts equation records from cached TeX files, and writes `data/processed/arxiv/sources/equations.jsonl`.
The paired datapackage records selected IDs, equation records, equation-record QA, failed-source IDs, failure audit rows, file sizes, row counts, and SHA-256 hashes.

## Access Verification Log

- 2026-05-30 (codex): Regenerated `data/processed/arxiv/sources/datapackage.json` with `uv run --frozen snakemake -s workflows/arxiv-sources/Snakefile data/processed/arxiv/sources/datapackage.json --cores 1 --rerun-triggers mtime --forcerun write_datapackage`.
  The existing `data/processed/arxiv/sources/qa/equation-records-qa.json` report has `status: pass`, `selected_id_count: 2`, `failed_id_count: 0`, `equation_record_count: 781`, and `source_id_without_equations_count: 0`.
  The regenerated datapackage lists `equation-records-qa` as a resource.

## Granularity At This Access Level

This entity covers the configured selected-ID source-equation extraction output and its source-access failure audit.
It is not a full arXiv source corpus and should not be interpreted as representative of all arXiv source availability.
The selected-ID file is part of the datapackage because it defines the extraction boundary.

## Connections To Project

- Questions/hypotheses it can inform: `question:q67-beta-vs-research-attention` and `hypothesis:h07-empirical-fidelity-alignment`.
- Variables likely available: arXiv ID, equation record fields, token-map structure, failed-source status, and selected-ID membership.
- Planned usage: upstream clean base for formulation-breadth and source-equation coverage analyses.

## Related

- Task: `task:t629`
- Task: `task:t631`
