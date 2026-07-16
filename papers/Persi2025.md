---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Persi2025
kind: paper
title: Genome-level selection in tumors as a universal marker of resistance to therapy
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Persi2025
tags: []
ontology_terms:
- dN/dS
- evolutionary monitoring
- neutral evolution
- prognosis
- selection regime
- therapy resistance
dataset_usage:
- ref: dataset:persi2025-myeloma
  role: analyzed
  overlap: unknown
---
## Key Findings

- In untreated primary settings, patient-specific `dN/dS` values are broadly stable despite natural progression and regional heterogeneity.
- Progression to metastasis can show cancer-specific shifts, including positive or relaxed selection in some cohorts.
- In treated cancers that developed resistance, post-treatment samples showed a near-universal tendency toward neutral evolution.
- Post-treatment tumors near neutrality or moving toward neutrality had worse prognosis in glioblastoma and multiple myeloma analyses.
- The authors propose a translational rule: if treatment moves a tumor from neutrality toward a selective regime, continue; if treatment moves a tumor toward neutrality or leaves it stably neutral despite therapy, consider changing treatment.

## Methods

The authors compiled whole-exome sequencing (WES) cohorts in which each patient had ≥2 samples (pre/post-treatment, primary/metastasis, or multiple primary regions) with both nonsynonymous (N) and synonymous (S) mutation counts available. Untreated cohorts: colorectal cancer (Hu et al.; 23 patients, 21 quantifiable), esophageal cancer (Yan et al.; 39 patients), small-cell lung cancer (Zhou et al.; 40 patients, 36 quantifiable). Treated (relapsed/resistant) cohorts: pediatric B-ALL (Ma et al.; 16/20 quantifiable), CLL post-venetoclax (Herling et al.; 7/8 quantifiable), ER-positive breast cancer (Nayar et al.; 7/8 quantifiable), urothelial/bladder carcinoma (Faltas et al.; 16 quantifiable), and glioblastoma post-radiotherapy/temozolomide (Wang et al.; 89/114 quantifiable). Validation used (i) a combined breast-cancer collection of 5 published studies (untreated primary-to-LN and primary-to-distant-metastasis series, plus ER- and HER2-targeted-therapy resistant series) and (ii) an original cohort of 624 multiple myeloma patients / 780 bone-marrow aspirates (Moffitt Cancer Center ORIEN/AVATAR, protocol MCC#14690), spanning MGUS/smoldering through diagnosis and relapse.

The core metric is genome-level, sample-level dN/dS = (N/nN)/(S/nS) (normalized nonsynonymous-to-synonymous mutation rate across the exome), assuming synonymous sites are neutral and unsaturated; samples with <10 mutations were excluded (threshold derived by matching TCGA data to a neutral model). Phylogenies used MesKit (R, v1.1.2; Neighbor-Joining) with COSMIC v2 signatures; cohort-level signatures used MafTools (v2.20.0); copy-number via sequenza/sequenza-utils (v3.0.0) and cntools (v1.30.0); MSI via MSISensor2 (v0.1); clonal composition via sciClone (v1.1.1) and fishPlot (v0.5.2). Statistics: one-way ANOVA F-tests comparing linear-regression slopes against reference models, Kaplan-Meier survival with log-rank tests, and Cox proportional-hazards regression (R `survival` v3.7-0) modeling drug exposure against distance from neutrality.

## Limitations

The treated datasets are enriched for resistant or failed-treatment cases, so the proposed clinical rule still needs prospective validation in cohorts with successful and failed responses.
The method depends on sufficient mutation counts (samples with <10 mutations are excluded) and on assumptions about synonymous neutrality and saturation; the authors flag possible bias in dN/dS from non-neutral or saturated synonymous sites as an open question.
It is also sample-level and exome-based. The paper explicitly tested dN/dS for copy-number sensitivity and found the distribution in CNA-affected regions statistically indistinguishable from diploid regions (i.e. it argues the metric is robust to CNA, not blind to it). Beyond the genetic signal, the authors note only a small and stable number of genetic clones in the myeloma cohort and suggest that non-genetic (epigenetic) diversification, which dN/dS does not capture, may also contribute to tumor fitness. (Claims that the method misses ecDNA-, spatial-, or plasticity-driven resistance do not appear in the paper's own discussion and have been removed.)
