---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:sequence-store-grch38-grch37
type: dataset
title: "Reference sequence store - GRCh38 + GRCh37 per-contig refget bytes"
version: "1.0.0"
created: "2026-05-28"
updated: "2026-05-28"
tags: []
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
datapackage: datapackage.yaml
origin: external
status: active
tier: use-now
update_cadence: static
source_class: reference
---

# Reference sequence store

Per-contig reference sequence bytes for GRCh38 + GRCh37, content-addressed by
refget digest. Built locally via `recipe/build.py`; only `manifest.csv` is
committed. See `~/d/science/docs/plans/2026-05-28-c4-variant-identity-design.md`
(C4a-D3).
