---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Fehlmann2020
type: paper
title: Common diseases alter the physiological age-related blood microRNA profile
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Fehlmann2020
tags: []
authors:
- Fehlmann et al.
datasets:
- dataset:fehlmann2020-mirna-cohort
- dataset:interval-longevity-proteomics
doi: 10.1038/s41467-020-19665-1
ontology_terms:
- blood-transcriptome
- disease-biomarker
- healthy-aging
- microRNA
pmid: '33247091'
venue: Nature Communications
year: 2020
---
## One-Sentence Summary

Comprehensive profiling of 2549 miRNAs in 4393 whole blood samples across the lifespan shows that disease globally disrupts the healthy miRNA aging trajectory, that age is a stronger determinant of blood miRNA profiles than sex, and that miRNA biomarker sets for all four disease categories differ substantially between young and old patients — motivating age-stratified rather than age-agnostic biomarker design.

## Key Findings

1. **Age dominates over sex.** Of 2549 miRNAs measured, 1568 significantly correlate with age (BH-adjusted Wilcoxon p < 0.05), versus only 362 correlating with sex. The overlap of 231 miRNAs shared between age- and sex-correlated sets is non-significant (Fisher's exact p = 0.35), indicating largely non-overlapping groups. The Spearman correlation of age-correlation coefficients between males and females is 0.884 (p < 10^-16), confirming that the age trajectory is concordant across sexes even though sex has a weaker marginal effect.

2. **Nonlinear miRNA-aging trajectories are widespread and tissue-enriched.** Linear correlation analysis is supplemented by distance correlation to identify nonlinear dynamics: 116 miRNAs show significant nonlinear age associations (90 decreasing, 26 increasing with age). miEAA enrichment on nonlinearly-aging miRNAs shows significant enrichment across essentially all human tissues (lung p = 1.3×10^-10, myocardium p = 1.3×10^-10, brain p = 2.7×10^-7; 28 tissues total, all BH-adjusted p < 10^-4). This widespread signal implies that whole blood miRNAs capture multi-organ aging dynamics.

3. **Five aging clusters with functional asymmetry.** miRNAs sorted by Spearman correlation with age fall into five clusters: strongly decreasing (cluster 1: 174 miRNAs, SC < -0.2), moderately decreasing (cluster 2: 382 miRNAs), unaltered (cluster 3: 1451 miRNAs), moderately increasing (cluster 4: 368 miRNAs), strongly increasing (cluster 5: 174 miRNAs, SC > 0.2). miEAA on these ranked sets reveals 620 enriched pathways for decreasing-with-age miRNAs versus 0 for increasing-with-age miRNAs. Top enrichments for decreasing miRNAs include "Negative Correlated with Age" (p = 4×10^-10) and "Downregulated in Alzheimer's Disease" (p = 10^-5). Increasing-with-age miRNAs are enriched in "Regulation of synaptic transmission" (p = 0.028) and "APP catabolic processes" (p = 0.032).

4. **miRNA arm-shift (3' to 5') is a feature of healthy aging.** In 27 miRNAs (67.5% of the 40 showing arm-shift events), 5' mature expression increases while 3' expression decreases with age. In 13 cases (32.5%), the 3' form increases and 5' decreases. The largest absolute 5' arm shift is for miR-6786. This arm-ratio change in aging suggests altered RISC loading preferences — a level of regulatory complexity not captured by standard mature-miRNA abundance profiles.

5. **Disease globally disrupts healthy miRNA aging — and disrupts it differentially.** Pooling all four disease cohorts, diseased samples show far fewer miRNAs with significant age correlations than healthy controls (healthy controls have the largest absolute Spearman correlations, with differences to pooled diseased samples significant at p < 2.2×10^-16 by ANOVA and Wilcoxon). Importantly, the disruption is not uniform: the number of differentially expressed miRNAs in each disease peaks in young adults (ages 30-39), decreases sharply into midlife, then plateaus around age 60 for lung cancer (~50 miRNAs) and around age 50 for non-tumor lung diseases. Parkinson's disease is the exception, reaching its minimum around age 47 and then increasing through the 6th-7th decade. The most commonly disrupted miRNAs are also the ones with the largest effect sizes: miR-191-5p (pan-disease, targets cellular senescence pathways) and disease-specific examples like miR-16-5p (PI3K-Akt, lung cancer).

6. **Disease biomarker sets differ between young and old patients.** Self-organizing maps (SOM; 10×10 hexagonal grid, 10,000 iterations, learning rate 0.05-0.01) cluster miRNA expression by disease vs. healthy controls for young (30-59 years) and old (60-80 years) patients separately. Disease biomarker sets cluster by disease entity rather than by age group, confirming disease-specificity. However, the old biomarker set is generally closer to the all-ages biomarker set while the young biomarker set has larger distances — meaning disease-associated miRNA changes are most pronounced in younger patients and attenuate with age. Hierarchically, NTLD and lung cancer biomarkers are nearest neighbors; heart disease biomarkers are second-closest; Parkinson's disease biomarkers are most distant from all others.

7. **White blood cells are the dominant source of circulating miRNAs.** Computational deconvolution assigns 196 of the 1568 age-correlated miRNAs to a single cell type: 139 miRNAs arise from a combination of WBCs, RBCs, exosomes, and serum; 127 from neutrophils (CD15+); 119 from monocytes (CD14+). miRNAs increasing with age originate largely from B cells, monocytes, NK cells, cytotoxic T cells, and serum. miRNAs decreasing with age are enriched in neutrophils, T helper cells, and RBCs. This is consistent with known age-related immune cell composition shifts (lymphocytes decrease, neutrophils increase with age), but the authors argue that cell-intrinsic gene expression changes contribute substantially beyond composition shifts alone.

8. **A core miRNA-protein aging network of 36 miRNAs and 26 proteins.** Correlating age-related miRNAs with age-related plasma proteins (SomaScan, 4264 subjects), then applying five stringent filtering criteria (experimental evidence required, top 5% decreasing miRNAs, top 5% increasing proteins, absolute Spearman ≥ 0.6, at least one miRNA-gene pair from miRTarBase), a core network is identified: 36 miRNAs targeting 26 proteins in two major hubs. The denser hub centers on axon guidance molecule semaphorin 3E (SEMA3E), targeted by 8 miRNAs including miR-6812-3p (Spearman correlation with SEMA3E = -0.89 across lifespan). SEMA3E suppresses endothelial cell proliferation and angiogenic capacity; it is expressed in older individuals and low in younger individuals. The second hub centers on serine-arginine splicing factor 7 (SRSF7), an NXF1 adaptor for alternative RNA processing, broadly expressed across neutrophils, monocytes, and B cells (UMAP data). SRSF7 has no established role in aging or neurodegeneration, making the miR-6812-3p → SEMA3E edge the more interpretable biological link.

## Limitations

- **Cross-sectional design:** Cannot establish whether individuals who later developed disease showed miRNA deviations before diagnosis, or whether miRNA profile shifts are purely downstream of established disease. Longitudinal data are required to address temporal ordering.
- **miRNA microarray platform:** The authors chose microarray over RNA-seq because microarrays have higher dynamic range for blood (90-95% of reads match 2-5 miRNAs in whole blood RNA-seq). However, microarrays cannot detect novel miRNAs, and batch effects require careful normalization. The choice limits detection of rare miRNAs and isomiRs.
- **Whole blood as specimen:** Whole blood miRNA profiles reflect cell-type composition shifts (e.g., lymphocyte decline, neutrophil increase with age) in addition to cell-intrinsic expression changes. The deconvolution analysis suggests cell-intrinsic changes are important, but this is a computational inference, not directly validated with cell-sorted miRNA profiles.
- **Disease heterogeneity:** The four disease categories (PD, HD, NTLD, LCa) are broad. Heart diseases span coronary artery disease, dilated cardiomyopathy, and acute coronary syndrome. Non-tumor lung diseases include COPD, sepsis, liver cirrhosis, breast cancer, endometriosis, and melanoma (aggregated to organ level). Heterogeneity within categories will dilute disease-specific signals.
- **No longitudinal/intervention design:** The core finding that disease disrupts healthy aging trajectories is correlational. Whether restoring miRNA levels to age-expected values would confer health benefit is entirely untested.
- **Core network is a small, filtered subset:** The 36-miRNA/26-protein core network is produced by five stringent filters and may miss weaker but biologically real miRNA-protein interactions. The SEMA3E finding (8 miRNAs, miR-6812-3p Spearman = -0.89) is striking but lacks experimental validation in the paper itself.
- **Data access restriction:** Raw data available only for non-commercial use upon request (not deposited in a public repository like GEO). This limits reproducibility.
