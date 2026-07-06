---
schema_profile: science-entity-base/1.0+dataset/1.0+bio.assembly_registry/1.0
id: dataset:assembly-registry
kind: dataset
title: "Assembly registry — seqcol-keyed reference collection of genome assemblies"
version: "1.0.1"
created: "2026-05-26"
updated: "2026-07-03"
tags: []
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
  source_url: https://seqcolapi.databio.org
datapackage: datapackage.yaml
origin: external
status: active
tier: use-now
update_cadence: static
member_key_column: seqcol_digest
assembly_count: 2
---

# Assembly registry

A reference collection (foundation primitive, second instance) whose member rows
are addressed by their GA4GH refget Sequence Collection (seqcol) digest. Built
no-FASTA from pinned seqcol-server level-2 records; see `recipe/`. Individual
assemblies are promoted to their own `dataset` (derivation `kind: member_of`,
`member_key` = the `seqcol_digest`) only on demand.
