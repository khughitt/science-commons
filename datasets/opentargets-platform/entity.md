---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:opentargets-platform
kind: dataset
title: Open Targets Platform — target-disease evidence graph
version: "1.0.0"
created: "2026-05-28"
updated: "2026-05-28"
tags: []
access:
  level: public
  availability: available
  available_after: ''
  verified: false
  verification_method: ''
  last_reviewed: '2026-05-28'
  verified_by: ''
  source_url: https://platform.opentargets.org/downloads
  credentials_required: ''
  exception:
    mode: ''
    decision_date: ''
    followup_task: ''
    superseded_by_dataset: ''
    rationale: ''
datapackage: datapackage.yaml
ontology_terms: []
origin: external
status: active
tier: use-now
update_cadence: quarterly
---
# Open Targets Platform — target-disease evidence graph

## Summary

Pre-computed target-disease evidence graph aggregating genetic association,
somatic mutation, literature, drug, animal model, pathway, and expression
evidence from >20 upstream sources into per-target-disease association scores.
The highest-leverage low-friction annotation layer for MM30 top-ranked genes:
provides systematic druggability, genetic support, and tractability priors at
near-zero ingestion cost.

## Access and Scope

- Accessions: Open Targets Platform 24.06 (or latest; released quarterly)
- Source URL: https://platform.opentargets.org/downloads
- Organism/population: Human targets × all indications
- Modality: Target-disease evidence graph (Parquet / JSON-lines bulk downloads)
- Sample size: ~63k targets × ~28k diseases; ~16M evidence records
- License: CC0 1.0
- Format: Apache Parquet (preferred), JSON-lines, Neo4j dump
- Bulk download: FTP / Google Cloud Storage; ~100 GB full snapshot

## Thoughts

- **Strength**: Aggregates sources that MM30 would otherwise need to integrate
  independently: ChEMBL drugs, Europe PMC literature, GWAS/OT Genetics,
  IntOGen somatic, Reactome pathways, UniProt functions, Expression Atlas,
  PhenoDigm mouse phenotypes.
- **Strength**: Quarterly release cadence with semantic versioning;
  re-joinable onto MM30 tables at pipeline scale.
- **Strength**: CC0 license — no integration friction.
- **Limitation**: Association scores are heuristic; high OT score is a prior,
  not an effect estimate.
- **Limitation**: MM (EFO_0001378 / MONDO_0009693) has fewer curated records
  than e.g. breast cancer — useful but not saturating.
- **Limitation**: Updates quarterly; specific evidence entries can disappear
  between versions.

## Connections to Project

### Questions/hypotheses it can inform

- the 35-gene mutation × cytogenetic overlap set — druggability and
  tractability scoring for the 35 overlap genes (already 10 DepMap-essential, 2 druggable;
  OT adds animal model, genetic, literature priors).
- `question:nucleoporin-signal` — druggability of NUP133 / NUP155 and their
  known drug interactions (selinexor is already catalogued; OT gives systematic
  view of nuclear-export-related chemistry).
- `question:stratum-specific-biology` — prioritize the 132 gain(1q)-unique
  genes and HD+/HD- unique genes by OT tractability + MM-specific evidence.
- All hypotheses with gene-level claims — attach a per-gene "OT score × MM"
  annotation to MM30 ranking tables.

### Variables likely available

- Per-gene MM association score (overall + per-evidence-class)
- Druggability (ChEMBL-derived)
- Tractability (small molecule, antibody, PROTAC classes)
- Genetic association evidence (GWAS, rare-disease)
- Literature evidence (Europe PMC co-mentions)
- Animal model phenotype evidence

### Planned usage

- One-time bulk download of latest Platform snapshot to `data/raw/opentargets/`.
- Build a per-gene-per-disease-association Parquet join table restricted to
  MM, MGUS, and related hematological indications.
- Add a post-meta-analysis annotation rule in the reports stage:
  attach OT MM evidence to every MM30 top-ranked gene.

## Related

- Prose support note: `doc/notes/topic-support/convergence-genes.md`
- Article notes: Ochoa et al., NAR 2024 (Open Targets Platform 24.06)
