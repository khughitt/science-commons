---
schema_profile: science-entity-base/1.0+dataset/2.0+bio.reference_graph/1.0
id: dataset:mondo
kind: dataset
title: MONDO disease ontology reference graph
version: "1.0.0"
created: "2026-05-31"
updated: "2026-05-31"
tags: []
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
datapackage: datapackage.yaml
graph_resource: graph
graph_format: obograph_json
member_key_space:
  kind: curie
  prefixes: [MONDO]
  resolution_status: resolved
node_index_resource: nodes
edge_resource: edges
member_count: 31958
edge_count: 199449
license: CC-BY-4.0
origin: external
source_class: reference
status: active
tier: use-now
---
# MONDO disease ontology reference graph

Pinned MONDO release `v2026-05-05`, represented as a `bio.reference_graph`
commons dataset. The canonical graph artifact is the upstream OBO Graph JSON
release asset; `nodes.csv` and `edges.csv` are build-derived projections used
for fast validation and virtual member payload resolution.

The member surface is restricted to addressable `MONDO:` terms. Deprecated
MONDO terms remain addressable members and count toward `member_count`; when
MONDO declares a replacement with `IAO:0100001`, the replacement is recorded in
`nodes.csv.replaced_by` and is not auto-applied.

The edge projection includes direct graph edges where either endpoint is a
MONDO term plus MONDO node xrefs as `predicate=xref`. Xrefs and related external
terms are retained as relations, not identity rewrites.
