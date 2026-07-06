---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:arxiv-corpus
kind: dataset
title: arXiv metadata corpus
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
  source_url: https://www.kaggle.com/datasets/Cornell-University/arxiv
accessions: []
datapackage: datapackage.yaml
license: unknown
origin: external
source_class: observational
status: active
tier: use-now
---
# arXiv Metadata Corpus

## Summary

This dataset entity records the prepared arXiv metadata corpus produced by `workflows/arxiv-corpus`.
The workflow reads the Kaggle arXiv metadata snapshot, filters records without title or abstract text, normalizes core metadata fields, deduplicates repeated arXiv IDs by latest version timestamp, and writes `data/processed/arxiv/corpus/raw.feather`.
The paired datapackage records the raw snapshot, prepared corpus, structural QA report, file sizes, row count, schema, and SHA-256 hashes.

## Access Verification Log

- 2026-05-30 (codex): Regenerated `data/processed/arxiv/corpus/raw.feather`, `data/processed/arxiv/corpus/qa/raw-corpus-qa.json`, and `data/processed/arxiv/datapackage.json` with `uv run --frozen snakemake -s workflows/arxiv-corpus/Snakefile data/processed/arxiv/datapackage.json --cores 1`.
  The first QA pass found duplicate arXiv IDs in the upstream snapshot; the parser now emits one clean-base row per ID, keeping the row with the latest version timestamp.
  The regenerated QA report has `status: passed`, `row_count: 3021737`, `unique_id_count: 3021737`, and `error_count: 0`.

## Granularity At This Access Level

This entity covers the prepared metadata table used as a reusable local discovery corpus.
It does not cover arXiv source bundles, equation extraction records, citation counts, or downstream formulation-breadth estimates.
Those substrates have separate workflow outputs and should remain separately packaged when promoted.

## Connections To Project

- Questions/hypotheses it can inform: `question:q67-beta-vs-research-attention`.
- Variables likely available: arXiv ID, DOI, title, abstract, latest version timestamp, update date, category list, and primary category.
- Planned usage: upstream clean base for arXiv source selection, formulation-breadth analyses, and attention/corpus-substrate checks.

## Related

- Task: `task:t629`
- Task: `task:t631`
