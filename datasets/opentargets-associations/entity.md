---
schema_profile: science-entity-base/1.0+dataset/2.0+bio.reference_graph/1.0
id: dataset:opentargets-associations
kind: dataset
title: Open Targets target–disease association reference graph
version: "1.0.0"
created: "2026-06-01"
updated: "2026-06-01"
tags: []
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
datapackage: datapackage.yaml
graph_resource: graph
graph_format: jsonl_edges
member_key_space:
  kind: curie
  prefixes: [ENSEMBL, DOID, EFO, GO, GSSO, HP, MONDO, MP, NCIT, OBA, OTAR, Orphanet, PATO, UBERON]
  resolution_status: resolved
node_index_resource: nodes
member_count: 57543
edge_count: 4492971
license: CC0-1.0
origin: external
source_class: reference
status: active
tier: use-now
update_cadence: quarterly
---
# Open Targets target–disease association reference graph

Pinned **Open Targets Platform 25.12** (`25.12.0`, CC0 1.0), represented as a
`bio.reference_graph` commons dataset — the first *association graph* in the
family (after `dataset:mondo` and `dataset:go`).

Members are the targets (`ENSEMBL:ENSG…`, `member_kind: target`) and diseases
(`EFO:…`/`MONDO:…`/…, `member_kind: disease`) that participate in at least one
`association_overall_direct` association; every member has ≥1 incident edge.
Edges are `subject=target, predicate=associated_with, object=disease`, carrying
the 0–1 overall score in the canonical `graph.jsonl` (`graph_format:
jsonl_edges`).

## edge_resource omitted

25.12 has 4,492,971 overall-direct associations, well above the ~2 M threshold
at which a CSV `edge_resource` would make every `commons validate` load the full
edge set. Per the design (§8), `edge_resource` is omitted: the full edge set is
hash-pinned only in `graph.jsonl` (which `commons validate` existence-checks).
RG2 returns node-only payloads for this dataset; incident-association resolution
and a first-class edge score are later increments. `build.py` self-verifies
`edge_count == graph.jsonl` line count, full endpoint coverage in `nodes.csv`,
and no orphan members.

## Distinct from `dataset:opentargets-platform`

`dataset:opentargets-platform` is a separate MM-family-filtered annotation slice
(`mm-associations` / `mm-drugs` / `mm-tractability`). This dataset is the
general, unfiltered target–disease association graph and does not supersede it.
