---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:variant-labels-dbsnp-human
kind: dataset
title: Human dbSNP rsID to small-allele variant-label map
version: "1.0.0"
created: "2026-05-31"
updated: "2026-05-31"
status: exploratory
origin: external
source_class: reference
tier: track
access:
  level: public
  availability: available
  verified: false
  verification_method: ''
datapackage: datapackage.yaml
---

Pinned dbSNP build 157 human rsID label map for C4c variant input translation.

This dataset record is a recipe placeholder until an operator fetches the pinned dbSNP archives, builds
`rsid_mappings.sqlite`, and commits non-zero datapackage hashes. Do not treat it as a usable registry
until that full artifact pin is complete.

This dataset is not a canonical variant identity system. It resolves external rsID labels to exact
assembly-anchored alleles so the Science C4a resolver can mint canonical GA4GH VRS identifiers from the
pinned local sequence store.

Only precise literal small alleles are retained. Symbolic alleles, breakends, imprecise structural
variants, and rows that cannot be represented as `contig:pos0:ref:alt` SPDI inputs are skipped and counted
in `build-summary.yaml`.
