---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Jurgens2024
kind: paper
title: Rare coding variant analysis for human diseases across biobanks and ancestries
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Jurgens2024
tags: []
authors:
- Jurgens et al.
doi: 10.1038/s41588-024-01894-5
ontology_terms:
- gene-based-burden-test
- loss-of-function-variant
- pan-ancestry-analysis
- phecode
- rare-coding-variant
pmcid: PMC11576993
pmid: ''
venue: Nature Genetics
year: 2024
dataset_usage:
- ref: dataset:all-of-us
  role: analyzed
  overlap: unknown
- ref: dataset:mgb-biobank
  role: analyzed
  overlap: unknown
- ref: dataset:uk-biobank
  role: analyzed
  overlap: unknown
---
## One-Sentence Summary

Pan-ancestry gene-based rare variant burden testing across 748,879 individuals from three large biobanks identifies 363 significant gene-disease associations for 601 disease phenotypes, demonstrating largely consistent rare coding variant effect sizes across ancestries and implicating both known Mendelian disease genes and novel candidates including UBR3 for cardiometabolic disease and YLPM1 for psychiatric disorders.

## Key Findings

1. **Scale and scope.** Meta-analysis of exome/WGS data from UKB (n=454,162), AoU (n=242,902), and MGB (n=51,815) — a combined 748,879 individuals — tested 11,060,516 unique gene-phecode pairs across 601 disease phenotypes. Of 155,236 individuals with ancestry dissimilar to European, 119,660 were from defined non-European continental groups and 35,576 were "admixed."

2. **363 significant associations at FDR Q<0.01.** These span 165 unique phecodes and 123 unique genes. 301 of 363 (82.9%) were in OMIM or directly related to OMIM entries. A naïve uncorrected meta-analysis would have yielded 464 signals; omitting MGB would have yielded 319 — showing the overlap-correction and multi-biobank design each matter.

3. **Core disease phenome genes are pleiotropic.** PKD1 associated with 29 phenotype codes (most of any gene), notably genitourinary congenital anomalies (OR_LOF 78.71, P=1.1x10⁻¹⁵³) and chronic renal failure (OR_LOF 17.36, P=1.8x10⁻⁷³). FBN1 (Marfan syndrome) associated with 13 codes; APC with colorectal cancer (OR_LOF 12.7, P=2.8x10⁻¹⁸) and 22 other codes. Effect size distributions: circulatory system median OR_LOF = 4.5 (Q1-Q3 2.7-16.6, N=53 pairs); neoplasms median OR_LOF = 8.3 (Q1-Q3 5.1-19.5, N=54); congenital anomalies median OR_LOF = 24.3 (Q1-Q3 15.0-119.8, N=15).

4. **Novel associations surviving sensitivity analyses.** YLPM1 LOF/missense variants associated with bipolar disorder (OR_LOF 3.9, P_Cauchy=8.1x10⁻⁹) and personality disorders (OR_LOF 7.8, P_Cauchy=2.0x10⁻⁷). UBR3 variants associated with hypertension (OR_LOF 2.8, P_Cauchy=6.7x10⁻⁹), type 2 diabetes (OR_LOF 3.6, P_Cauchy=3.8x10⁻⁸), and suggestive obesity signal (OR_LOF 2.6, P_Cauchy=1.8x10⁻⁶). MIB1 (Notch signaling) associated with type 2 diabetes (OR_LOF 1.3, P_Cauchy=5.3x10⁻⁸). SYTL1 associated with hypothyroidism (OR_LOF 1.7, P_Cauchy=6.5x10⁻⁸).

5. **42.4% of associations novel relative to prior PheWAS.** 154 of 363 associations (42.4%) were not identified in two previous biobank-scale PheWAS; 32 (8.8%) were not in OMIM, representing potential genuinely novel gene-disease links.

6. **Pan-ancestry approach yields 18.2% more associations than European-ancestry-only.** The all-ancestry analysis identified 363 associations vs. 297 in a European-ancestry-restricted analysis. The gain reflects larger total sample size rather than a clear diversity-driven discovery boost; when AoU was down-sampled to European-ancestry-equivalent size, ancestrally diverse subsets showed comparable or slightly fewer significant signals than the European subset.

7. **Rare LOF effect sizes are consistent across ancestries (β_deming ≈ 0.7-1.0).** Deming regression of European vs. non-European ancestry effect sizes for LOF variants gave slopes of 0.9 for European vs. African ancestry (P=3.9x10⁻²³, 95%CI [0.72; 1.08]) and 0.9 for European vs. Admixed-American (P=6.4x10⁻⁴⁷, 95%CI [0.78; 1.02]). The abstract-reported β_deming = 0.7-1 encompasses both the LOF and ultra-rare missense masks (which tend to be somewhat attenuated). Cross-ancestry consistency supports trans-ancestry meta-analysis as a valid strategy for rare variant discovery.

8. **Somatic variation (CHIP) confounds hematological trait associations.** Known CHIP genes — DNMT3A, TET2, SRSF2, SF3B1, ASXL1 — and somatic leukemia genes — TP53, NOTCH1, IDH2, KLHL6, RUNX1, CHD2, DDX41 — showed the strongest age-associations and hematological/leukemic outcome associations among the inflated signals. The paper recommends careful interpretation of blood-derived DNA associations for hematological phenotypes.

9. **Human Disease Knowledge Portal (public data release).** All gene-burden results browsable at https://hugeamp.org:8000/research.html?pageid=600_traits_app_home, including per-cohort and meta-analysis results stratified by ancestry and mask.

## Limitations

- **Protein-coding regions only.** Rare non-coding variants (regulatory, intronic, UTR) are not tested; the causal landscape for complex or polygenic diseases is incomplete.
- **Phenotype misclassification.** ICD-code-derived phecodes imperfectly capture disease status; binary case/control endpoint ignores disease severity, stage, and subtype.
- **AoU+MGB sample overlap.** Partial recruitment from shared sites; overlap correction applied but imperfect — residual inflation possible for high allele-count masks.
- **Pan-ancestry power plateau.** The 18.2% more associations from pan-ancestry vs. European-only analysis reflect larger N rather than diversity-driven discovery. At current sample sizes, ancestrally diverse subsets of AoU do not outperform the European subset of equal size for burden testing of binary disease endpoints. True ancestry-specific rare variants and ancestry-enriched phenotypes are likely underpowered.
- **Somatic contamination in hematological traits.** Blood-derived DNA cannot cleanly separate germline from somatic CHIP variation; the paper advises caution but cannot fully resolve this for hematological endpoints.
- **Liberal FDR threshold (Q<0.01 overall).** Novel associations require external replication; ~17.6% of the 363 associations could be false discoveries at this threshold if signal is uniform.
- **Association, not mechanism.** Gene-based rare variant associations identify candidate causal genes but do not establish mechanism, cell type of action, or therapeutic relevance.
