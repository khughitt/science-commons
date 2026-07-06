---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Kim2024-ecdna-progression
kind: paper
title: Mapping extrachromosomal DNA amplifications during cancer progression
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Kim2024-ecdna-progression
tags: []
ontology_terms:
- AmpliconArchitect
- AmpliconClassifier
- AmpliconSuite
- cancer progression
- chemotherapy-induced amplification
- ecDNA
- extrachromosomal DNA
- kataegis
- localized hypermutation
- longitudinal cohort
- pan-cancer
dataset_usage:
- ref: dataset:glass
  role: analyzed
  overlap: unknown
- ref: dataset:hartwig
  role: analyzed
  overlap: unknown
- ref: dataset:pcawg
  role: analyzed
  overlap: unknown
- ref: dataset:tcga
  role: analyzed
  overlap: unknown
---
## Key Findings

### Data-derived findings (D)

- **(D)** Pan-cancer ecDNA prevalence increases with progression: **23.2% (346/1,490)** in newly diagnosed primary tumours → **31.8% (777/2,440)** in advanced (untreated metastatic + pretreated) tumours.
- **(D)** Multivariate Cox proportional-hazards model: ecDNA-positive vs no-focal-amplification comparator is associated with significantly worse overall survival (`P < 0.001`), after adjusting for tumour location, sex, age, whole-genome doubling, microsatellite instability, homologous-recombination status, and stage. *Headline hazard-ratio magnitude not extracted from PMC page* — to be filled when paper text is fully read. The comparator is "no focal amplification", *not* "linear focal amplification with matched copy number" (the latter is what `task:t007`'s Fit A is designed to provide).
- **(D)** Longitudinal retention asymmetry: **54.5% (30/55)** of T1 ecDNAs were also detected at T2; only **16% (46/288)** of T1 chromosomal amplifications were retained at T2.
- **(D)** ecDNA amplicons in the advanced cohort show enriched kataegis-style clustered mutations vs ecDNA in primary tumours (`P < 0.001`).
- **(D)** Tubulin-inhibitor chemotherapy showed the strongest association with elevated ecDNA frequencies among the chemotherapy mechanism classes (see Supplementary Table 2).

### Author interpretations (L)

- **(L)** ecDNA presence "provides tumours with competitive advantages" during metastasis and treatment.
- **(L)** Tubulin-inhibitor association is interpreted as evidence that tubulin inhibition "may drive amplicon formation" — mechanistic link is suggestive, not causally tested.
- **(L)** Uneven (non-Mendelian) ecDNA segregation "likely contributes to their competitive advantage" — same regime-view framing inherited from Kim2020 / Bafna2022.
