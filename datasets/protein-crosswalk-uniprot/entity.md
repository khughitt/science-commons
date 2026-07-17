---
schema_profile: science-entity-base/1.0+dataset/2.0+bio.protein_crosswalk/1.0
id: dataset:protein-crosswalk-uniprot
kind: dataset
title: "UniProt protein crosswalk — protein_key-keyed reference collection (human, reviewed)"
version: "1.0.0"
created: "2026-05-27"
updated: "2026-05-27"
tags: []
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
  source_url: https://www.uniprot.org/help/downloads
datapackage: datapackage.yaml
origin: external
status: active
tier: use-now
update_cadence: quarterly
member_key_column: protein_key
protein_count: 0
---

# UniProt protein crosswalk

A reference collection (foundation primitive, fourth instance) whose member rows
are addressed by an opaque composite `protein_key` `"<taxon>|uniprot|<accession>"`
(e.g. `9606|uniprot|P04217`). Built from pinned, dated UniProt release files
(reviewed Swiss-Prot human idmapping + secondary accessions); see `recipe/`. The
UniProtKB accession is the canonical human protein anchor (C-D1); Ensembl protein
/ RefSeq protein / entry name are accepted inputs resolved *to* it. Each row
carries the C2 canonical `gene_key` (protein→gene join). Isoform accessions
(`P12345-2`) are a valid lower-level identity surfaced against the canonical, not
collapsed. Secondary (merged) accessions are retained with a `replacement_protein_keys`
forward pointer. Individual proteins are promoted to their own `dataset`
(`derivation.kind: member_of`, `member_key` = the `protein_key`) only on demand.
