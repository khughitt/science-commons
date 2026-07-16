---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Lionetti2025
kind: paper
title: Clonal hematopoiesis is clonally unrelated to multiple myeloma and is associated
  with specific microenvironmental changes
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Lionetti2025
tags: []
ontology_terms:
- T-cell exhaustion
- clonal hematopoiesis
- clonal independence
- multiple myeloma
- scRNA-seq
- tumor microenvironment
dataset_usage:
- ref: dataset:egac00000000232
  role: analyzed
  overlap: unknown
---
## Key Findings

**CHIP prevalence and spectrum**
- CHIP detected in 22.6% of patients (24/106; after excluding MM-origin variants in KRAS, TP53, RB1: 21.7%, 23/106), carrying 40 variants at median VAF 7.9%.
- Most frequently mutated genes: TET2 (8.5%), DNMT3A (5.6%), ASXL1 (3.7%), SF3B1 (2.8%), PPM1D (1.8%).
- CHIP-positive patients were significantly older (median 72 vs. 67 years, P = .024) and trended toward lower hemoglobin (P = .056); CHIP associated with more advanced R-ISS stage III (28.6% vs. 8.3%, P = .049).
- In 27 patients with longitudinal sampling, CHIP was mostly stable; branching clonal evolution was observed in MM16 (SF3B1 hotspot plus a TET2 subclone at diagnosis and post-DRd), and linear evolution in MM4 (TP53 p.K132R absent at diagnosis, detected at relapse). Two patients showed de novo TP53 variants post-first-line therapy consistent with lenalidomide-driven selection of TP53-mutated HSC clones.

**Clonal independence (the key result)**
- In all 8 CHIP-positive patients where BM HSC and PC DNA could be compared: CHIP mutations (present in BM CD34+) were absent from BM CD138+ PCs.
- In 5/8 patients, BM CD138+ PCs carried a distinct set of variants (n = 10 total) found in neither PB WBC nor BM CD34+ cells — these were MM-specific driver variants (KRAS, TP53, TENT5C, NRAS, CCND1, SF3B1, TET2).
- Conclusion: MM and CHIP represent two independent clonal conditions coexisting in the same BM niche; no common ancestor HSC was identified.

**TME remodeling in CHIP-positive MM**
- scRNA-seq identified a significantly lower proportion of CD8 naive T cells in CHIP-positive BM (P = .029); other T, NK, B, myeloid, and DC proportions were not significantly different.
- Differential expression across all T-cell and monocyte types in CHIP-positive patients revealed consistent upregulation of hallmark inflammatory response, IFN-α, IFN-γ, TNF/NF-κB, IL-6/JAK/STAT3, IL-2/STAT5, and TGF-β signaling.
- Myeloid DCs in CHIP-positive TME showed significantly lower peptide antigen binding scores (impaired antigen presentation); CD14 and CD16 monocytes showed higher M1 polarization scores.
- Cell-cell communication analysis (MultiNicheNet): 64/100 top differential interactions were specific to the clonal (CHIP-positive) TME. Key predicted interactions: T-cell-to-monocyte proinflammatory signaling (TNF-TNFRSF1B; IFN-γ/IFNGR1; T cells as sender, CD16 monocytes as receiver); immune checkpoint upregulation on effector T cells (HLA-DRB5/DRA-LAG3; CD48-CD244); clonal PCs signaling to naive T cells via TNFSF10-TNFRSF10D/C (TRAIL axis, potentially protecting MM PCs from apoptosis) and to NK cells via B2M-KLRC1 (inhibitory); TME-to-PC survival signals (TNFSF13B-TNFRSF17; CCL5-SDC1; IFNG-IFNGR1).

**CD8 T-cell exhaustion**
- ProjecTILs-based analysis of scRNA-seq identified 7 CD8 functional subtypes. CHIP-positive precursor exhausted T cells (TPEX) showed significant upregulation of inhibitory checkpoint receptors LAG3, TIGIT, CD160, CD244 and exhaustion-associated TFs EOMES, BATF, TCF7, FOXP1 versus CHIP-negative counterparts.
- T-cell dysfunction scores were significantly elevated in CHIP-positive CD8 central memory, naïve-like memory, and terminally differentiated effector memory subsets; only effector memory cells trended opposite.
- Interpretation: a relatively widespread CD8 T-cell dysfunction is present in the clonal CHIP-positive TME at MM diagnosis.

**Clinical impact**
- CHIP had no statistically significant effect on treatment response, ASCT engraftment, or cytopenia rates during treatment in this cohort. One therapy-related MN was observed (CHIP-negative patient). Overall clinical impact assessed as mild in this cohort.

## Methods

Single-center prospective cohort study at Fondazione IRCCS Ca' Granda Ospedale Maggiore Policlinico (Milan) enrolling 106 patients with newly diagnosed multiple myeloma (NDMM) between April 2016 and September 2024 (median follow-up 27 months; 85% alive at last follow-up). CHIP was detected by targeted next-generation sequencing of a 74-gene myeloid-malignancy panel on peripheral-blood white-blood-cell DNA at mean 1099× depth (range 381–2193×); a VAF threshold near 2% was used to call variants [UNVERIFIED exact cutoff — the defining sentence is not in the extracted main text, likely in supplemental Methods]. Pathogenic CHIP variants were found in 24/106 patients (22.6%); after excluding KRAS/TP53/RB1 variants confirmed via CD138+ bone-marrow plasma-cell (PC) DNA sequencing to be MM-derived, prevalence was 21.7% (23/106).

Clonal relatedness of CHIP to MM was tested in 8 CHIP-positive patients by fluorescence-activated cell sorting of BM CD34+ (HSC) and CD138+ (PC) fractions, each independently sequenced with a second targeted panel covering CHIP, myeloid-malignancy, and MM driver genes; shared variants between fractions would indicate a common clonal origin.

Tumor-microenvironment profiling used single-cell RNA sequencing (10x Genomics Chromium Single-cell 5' Gene Expression + V(D)J enrichment) on BM samples from 16 patients (8 CHIP+/8 CHIP−), processed with Cell Ranger and Seurat (132,752 integrated cells, 27 clusters); ProjecTILs for CD8 T-cell subtyping (7 functional clusters); MultiNicheNet for cell-cell communication inference; and a Cytokine Signaling Analyzer for cytokine-activity prediction. Statistics used Student t and Wilcoxon rank-sum tests for clinical/laboratory comparisons and GSEA hallmark gene-set enrichment for differential-expression comparisons, all performed in R.

## Limitations

- **Sample size for scRNA-seq:** Only 16 patients (8 CHIP-positive, 8 CHIP-negative) were subjected to scRNA-seq; the mutational heterogeneity among the 8 CHIP-positive cases is acknowledged. Statistical power for mutation-specific TME effects is limited.
- **Clonality test breadth:** The HSC/PC sorting and orthogonal sequencing was done in only 8 CHIP-positive patients. The remaining 15 CHIP-positive patients lack direct clonality confirmation (though PB data argue strongly against overlap).
- **Causal directionality unresolved:** The authors explicitly note they cannot determine whether the inflamed TME in CHIP-positive MM is caused by CHIP, is a pre-existing feature of MM that favors CHIP, or is a combined effect. The study design is cross-sectional at diagnosis.
- **No matched CHIP-positive healthy BM controls:** Without BM scRNA-seq from CHIP-positive individuals without MM, it is impossible to separate CHIP-specific TME effects from MM-specific or combination-specific effects.
- **Short follow-up / mild clinical impact in this cohort:** Median follow-up 27 months; 85% alive at end of follow-up. The cohort may be underpowered to detect survival differences or late treatment-related MN.
- **Panel-based NGS:** The 74-gene targeted panel does not capture structural variants, copy number alterations, or CHIP mutations in genes outside the panel.
