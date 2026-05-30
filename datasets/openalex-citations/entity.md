---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:openalex-citations
type: dataset
title: OpenAlex citation substrate
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
  source_url: https://api.openalex.org
accessions: []
datapackage: datapackage.yaml
license: unknown
origin: external
source_class: observational
status: active
tier: use-now
---
# OpenAlex Citation Substrate

## Summary

This dataset entity records the processed OpenAlex citation and attention substrate produced by `workflows/openalex-analysis`.
The workflow builds model-level OpenAlex search terms from generated guide data, fetches OpenAlex work and domain responses, reduces those responses to per-model citation and topic summaries, and writes a QA-gated datapackage under `data/processed/openalex-citations`.

The paired datapackage records raw OpenAlex responses, raw-response QA, processed citation CSV/JSON resources, processed-citation QA, file sizes, row counts, schema, and SHA-256 hashes.

## Access Verification Log

- 2026-05-30 (codex): Ran `uv run --frozen snakemake -s workflows/openalex-analysis/Snakefile data/processed/openalex-citations/datapackage.json --cores 1`.
  The fetch step produced 249 model responses with 0 fetch errors.
  The processed citation table has 249 rows and 249 unique model IDs.
  `data/processed/openalex-citations/qa/raw-responses-qa.json` reports `status: passed`, `query_count: 249`, `work_count: 1233`, `null_publication_year_count: 1`, and `error_count: 0`.
  `data/processed/openalex-citations/qa/citations-qa.json` reports `status: passed`, `row_count: 249`, `model_count: 249`, and `error_count: 0`.

## Granularity At This Access Level

This entity covers model-keyed OpenAlex citation and topic summaries for the current guide catalog.
It does not cover OpenAlex discovery candidate tables, sibling-topic reports, grammar-validation outputs, MathModDB cross-reference outputs, or downstream causal/fidelity interpretations.
Those outputs remain project-specific analysis products unless later split into separate reusable substrates.

## Connections To Project

- Questions/hypotheses it can inform: `question:q67-beta-vs-research-attention`, `question:q62-model-fidelity-validation-tiers`, and `question:q38-meta-model-selection-bias`.
- Variables likely available: model ID, chapter ID, structure class, paper count, top and median citation counts, earliest/latest publication year, OpenAlex domain counts, primary domain, primary topic, and match-quality class.
- Planned usage: stable attention/citation substrate for formulation-breadth, fidelity, catalog-bias, and attention-residual analyses.

## Related

- Task: `task:t634`
- Task: `task:t133`
- Task: `task:t120`
