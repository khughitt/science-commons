---
schema_profile: science-entity-base/1.0+dataset/1.0+bio.geneset/1.0
id: dataset:reactome
type: dataset
title: Reactome human pathway gene-set collection
version: "1.0.0"
created: "2026-05-30"
updated: "2026-05-30"
tags: []
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
datapackage: datapackage.yaml
identifier_space:
  tier: gene
  namespace: entrez
  registry: dataset:gene-crosswalk-hgnc
  resolution_status: resolved
license: CC-BY-4.0
member_key_column: set_key
members_resource: sets
n_sets: 2819
origin: external
set_size_summary:
  min: 1
  median: 15.0
  max: 2606
source_class: reference
status: active
tier: use-now
---
# Reactome human pathway gene-set collection

Curated Reactome human pathways from release v96, represented as a faithful
reference gene-set collection. The D1 member surface is Entrez-keyed because
Reactome publishes the NCBI mapping files in that namespace; canonical C2
resolution to opaque `gene_key` values and display symbols is recorded in the
auxiliary `gene_set_panel.csv` resource.

The canonical `sets.csv` resource excludes pathways with zero approved C2 member
resolutions among pathways that have at least one NCBI membership row, and records
those exclusions in `resolution_report.csv`. Human catalog pathways with no
published NCBI gene membership are omitted from both `sets.csv` and the resolution
report because they cannot form a gene set. No enrichment-style size filter is
applied; consumers should apply analysis-specific windows downstream.
