---
schema_profile: science-entity-base/1.0+dataset/2.0+bio.reference_graph/1.0
id: dataset:go
kind: dataset
title: Gene Ontology term reference graph
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
graph_format: obograph_json
member_key_space:
  kind: curie
  prefixes: [GO]
  resolution_status: resolved
node_index_resource: nodes
edge_resource: edges
member_count: 51967
edge_count: 103808
license: CC-BY-4.0
origin: external
source_class: reference
status: active
tier: use-now
---
# Gene Ontology term reference graph

Pinned GO release `2026-05-19`, represented as a `bio.reference_graph` commons
dataset. The canonical graph artifact is the upstream OBO Graph JSON release
asset (`go.json`); `nodes.csv` and `edges.csv` are build-derived projections
used for fast validation and virtual member payload resolution.

The member surface is the set of addressable `GO:` terms. Each member is typed
by its sub-ontology in `member_kind` — `biological_process`,
`molecular_function`, or `cellular_component` — with a `term` fallback for
terms whose sub-ontology is not declared. Deprecated GO terms remain
addressable members and count toward `member_count`; when GO declares a
replacement with `IAO:0100001`, the replacement is recorded in
`nodes.csv.replaced_by` and is not auto-applied.

The edge projection includes direct graph edges where either endpoint is a GO
term, with predicates as GO emits them: `is_a` bare, `part_of` as
`BFO:0000050`, and the regulates family as `RO:0002211`/`RO:0002212`/
`RO:0002213`, among others. GO node xrefs are included as `predicate=xref`.
Xrefs and related external terms are retained as relations, not identity
rewrites.
