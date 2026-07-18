---
schema_profile: science-entity-base/1.0+dataset/2.0
id: dataset:twitter-pathology-images
kind: dataset
title: Twitter/social-media pathology image corpus (@pathobot, Schaumberg2020)
version: "1.0.0"
created: "2026-07-18"
updated: "2026-07-18"
tags: []
access:
  level: public
  availability: embargoed
  available_after: ''
  verified: false
  verification_method: ''
  last_reviewed: '2026-07-18'
  verified_by: claude
  source_url: https://pathobotology.org/
  credentials_required: Compiled from pathology images shared publicly on Twitter/social media; pathologist majority-vote curated. The consolidated corpus was announced (pathobotology.org) but was not fully public at time of publication
  exception:
    mode: ''
    decision_date: ''
    followup_task: ''
    superseded_by_dataset: ''
    rationale: ''
accessions:
- 'pathobotology.org (author-hosted resource)'
dataset_class: reference
ontology_terms: []
origin: external
source_class: observational
tier: track
---
# Twitter/social-media pathology image corpus (@pathobot, Schaumberg2020)

A corpus of histopathology images shared publicly by pathologists on Twitter/social
media, curated by pathologist majority vote, assembled by Schaumberg et al. (2020) to
train and prospectively test the @pathobot case-similarity system. The corpus is biased
toward unusual/challenging cases (the kind pathologists share), with hashtag/keyword
label noise acknowledged by the authors.

Reference-level entity for the social-media-sourced corpus; not a stageable data
package.

Referenced by `paper:Schaumberg2020` (multimodal pathology search on social media).

**Provenance note (AI-drafted, unverified):** access status is uncertain — the underlying
images are public on social media, but the consolidated dataset was announced rather than
released at publication. `access.verified: false`; confirm the current availability at
pathobotology.org before relying on this entity.
