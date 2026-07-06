---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Grechkin2016
kind: paper
title: Identifying Network Perturbation in Cancer
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Grechkin2016
tags: []
ontology_terms:
- cancer driver genes
- conditional dependence
- differential network
- epigenomic validation
- gene regulatory network
- lasso regression
- network perturbation
- sparse linear model
- transcriptional rewiring
dataset_usage:
- ref: dataset:encode
  role: analyzed
  overlap: unknown
- ref: dataset:gse12417
  role: analyzed
  overlap: unknown
- ref: dataset:gse13159
  role: analyzed
  overlap: unknown
- ref: dataset:metabric
  role: analyzed
  overlap: unknown
- ref: dataset:tcga
  role: analyzed
  overlap: unknown
---
## Key Findings

### Synthetic benchmarks

- DISCERN AUC = 0.81 on 100 synthetic dataset pairs (100 variables, ground-truth perturbed gene labels).
- Best competing method (pD⁰, permutation-augmented) AUC = 0.72; PLSNet AUC = 0.68; LNS AUC = 0.55; D-score AUC = 0.53.
- DISCERN does not require per-gene permutation tests (which would require ~4×10⁹ permutations at p = 20,000 genes), making it the only genome-scalable method among top performers.

### Cancer-specific perturbed gene counts (FDR < 0.05)

- AML: 1,351 significantly perturbed genes
- BRC: 2,137 significantly perturbed genes
- LUAD: 3,836 significantly perturbed genes (consistent with LUAD having more non-synonymous mutations than BRC, which has more than AML)

### AML top hits

- Highest-ranked gene: HOXB3 (expressed in multipotent hematopoietic progenitors). 13 of 39 known HOX family genes are in the significantly perturbed set (p = 5.99×10⁻⁶).
- Top MSigDB hit: VERHAAK_AML_WITH_NPM1_MUTATED_DN (p = 2×10⁻⁸⁶); NPM1, FLT3, and CEBPA (three standard AML clinical markers) are all significantly perturbed.
- GO enrichment: hemostasis, blood coagulation, GTPase activity/binding, SH3/SH2 adaptor activity.
- Genes implicated in leukemic stem cells (BAALC, GUCY1A3, RBPMS, MSI2) among top scorers.

### LUAD top hits

- Top gene: MCM7 (DNA replication helicase; implicated in carcinogenesis via PRMT6 binding, therapeutic target candidate).
- Ranked genes include ICOS, YWHAZ, GIMAP5, CARD6, NFKBIB, CTNNBIP1 — spanning immune costimulation, EMT via beta-catenin, and apoptosis.
- Top MSigDB hit: NGF-TrkA signaling (also top hit in BRC; p = 3.16×10⁻¹⁰⁴ in BRC), upstream of PI3K-AKT and RAS-MAPK.

### BRC top hits

- 2,137 significantly perturbed genes; top gene CLN5A (chloride channel; novel, no prior cancer link noted).
- Enrichment for BRCA1-correlated gene cluster, luminal A/B/HER2/basal subtype-specific genes, MYC targets, EZH2 targets.
- Third-ranked gene: BRF2 (RNA Pol III TF; oncogene in BRC and lung squamous).

### Prognostic prediction

- Cox regression models trained on DISCERN-identified genes (AML: 1,351 genes; BRC: 2,137 genes) and tested on fully held-out datasets:
  - AML: c-index = 0.669 (se 0.031), comparable to the Leukemic Stem Cell (LSC) score (22-gene established marker, p = 3e-08 vs. DISCERN p = 8e-10 by log-rank).
  - BRC: c-index = 0.668 (se 0.027), comparable to MammaPrint (67 of 70 genes present; p = 1e-08 vs. DISCERN p = 9e-12).
  - DISCERN-based models outperform clinical covariates alone in both cancers.

### Epigenomic validation (AML)

- DISCERN scores for genes differentially bound by known AML-associated TFs (e.g., STAT3, JUNB, PAX5) are significantly higher than scores for non-differentially-bound genes (Kolmogorov-Smirnov test, one-sided; Pearson correlation between DISCERN score and proportion of differentially binding TFs: strongest among all four methods compared).
- Specific example: STAT3 differentially regulates BATF in AML (NB4) but not normal (CD34+); DISCERN correctly identifies STAT3 as the strongest condition-specific regulator of BATF in AML, while LNS and D-score detect STAT3 as a regulator in both conditions.
- Intersecting DISCERN hits with DNase-seq-defined differentially bound genes improves Reactome pathway fold enrichment (Wilcoxon p < 7×10⁻⁵): platelet activation/aggregation (f = 2.9 with DISCERN filter vs. f = 1.03 without), Gq signaling (f = 2.16 vs. 0.92), G12/13 signaling (f = 3.4 vs. 1.5).

## Limitations

- Expression-only input: the DISCERN score is inferred from mRNA and cannot directly detect post-translational regulatory changes (e.g., kinase rewiring without transcriptional readout). Epigenomic integration is downstream post-hoc validation, not part of the score.
- Single cross-sectional comparison (bulk tumor vs. normal): does not resolve intratumoral heterogeneity, subclone-specific rewiring, or temporal ordering of perturbation events. Each patient's tumor is treated as a single network state.
- Candidate regulator list is fixed at 3,545 genes; perturbations involving non-canonical regulators or lncRNAs are missed by design.
- Normal reference tissues for AML (non-leukemic bone marrow) and BRC/LUAD (adjacent normal) are not perfectly matched and may carry field cancerization effects; ENCODE cell lines used for epigenomic validation are only proxies for primary tumor/normal tissue.
- Lasso arbitrarily selects among collinear regulators; the DISCERN score mitigates (but does not fully eliminate) this ambiguity for genes whose top candidate regulators are highly correlated.
- No single-cancer-type replication study; all validation is cross-dataset within the same cohort design.
