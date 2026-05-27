---
schema_profile: science-entity-base/1.0+dataset/1.0+bio.gene_crosswalk/1.0
id: dataset:gene-crosswalk-hgnc
type: dataset
title: "HGNC gene crosswalk — gene_key-keyed reference collection (human)"
version: "1.0.0"
created: "2026-05-27"
updated: "2026-05-27"
tags: []
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
  source_url: https://www.genenames.org/download/archive/
datapackage: datapackage.yaml
origin: external
status: active
tier: use-now
update_cadence: quarterly
member_key_column: gene_key
gene_count: 0
---

# HGNC gene crosswalk

A reference collection (foundation primitive, third instance) whose member rows
are addressed by an opaque composite `gene_key` `"<taxon>|hgnc|<hgnc_id>"`
(e.g. `9606|hgnc|HGNC:5`). Built from pinned, dated HGNC complete-set + withdrawn
release files; see `recipe/`. The HGNC id is the canonical human gene anchor
(C-D1); symbol / Entrez / Ensembl are accepted inputs resolved *to* it. Deprecated
/ merged / split entries are retained with forward pointers (`replacement_gene_keys`).
Individual genes are promoted to their own `dataset` (`derivation.kind: member_of`,
`member_key` = the `gene_key`) only on demand.
