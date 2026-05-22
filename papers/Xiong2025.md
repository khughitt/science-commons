---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Xiong2025
type: paper
title: 'PCMR: a comprehensive precancerous molecular resource'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Xiong2025
tags: []
datasets:
- dataset:pcmr
ontology_terms:
- cancer evolution
- database
- epigenomics
- multi-omics
- precancerous lesions
- transcriptomics
---
## Key Findings

1. **Scale:** PCMR is the first resource systematically covering precancerous molecular profiles; 25,828 profiles and 62,566 precancer-gene associations spanning 35 cancer types represent a qualitative increase in coverage versus any prior single-cancer or single-modality effort.

2. **Multi-modal pairing:** Profiles are explicitly paired with matched normal and/or malignant counterparts, enabling three-way differential analysis (normal → precancer → cancer) rather than only tumor vs. normal comparisons available in TCGA-class resources.

3. **Cross-cancer scope:** Liver and ovarian precancer have the largest differential gene sets; esophageal, intestinal, and lung precancer also well-represented. Liquid biopsy precancer profiles are included (important for early detection contexts).

4. **Precancer-specific expression dynamics:** Technical validation in esophageal adenocarcinoma revealed that some genes show differential expression specifically at the precancerous transition (RETSAT, NAT8) while others show stable disease-association patterns (BMP4, SMO, PTCH1, HES1) or cancer-only changes (TP53). This suggests the precancerous stage has a distinct, partially non-overlapping gene expression signature from invasive cancer.

5. **Prognostic signal in precancer resource:** NAT8 (N-acetyltransferase activity, shares function with NAT2) shows a consistent differential pattern at premalignancy and independently predicts survival in esophageal carcinoma — illustrating that PCMR can surface precancer-relevant prognostic markers not discoverable from cancer-only datasets.

6. **Pathway enrichment in precancer:** Dorsal/ventral neural tube patterning (Wnt, Notch, BMP) and smooth muscle development pathways are enriched among differentially expressed genes in esophageal precancerous lesions — linking early neoplastic transformation to developmental signaling reactivation.

## Limitations

1. **Predominantly transcriptomic / epigenomic; no genomic instability measures.** No CNV, SV, or mutation burden data. The resource cannot address q010 directly. Genomic instability at the precancer stage (which is central to evolution questions) remains outside PCMR's scope.

2. **Single-cell resolution absent.** All profiles are bulk or micro-dissected samples. Intra-lesion heterogeneity — critical for evolutionary analysis — cannot be assessed. PCMR captures population-level molecular state, not clonal architecture.

3. **GEO-derived data with heterogeneous platforms.** Despite normalization, cross-study comparability is limited by batch effects, platform diversity (microarray vs. RNA-seq), and variable clinical annotation quality. Cross-cancer comparisons must account for these confounders.

4. **ChatGPT association tier has unvalidated false positive rate.** 41,862 of 62,566 associations come from LLM text-mining with unknown precision in the precancerous context. Only the differential analysis tier and manually curated tier are experimentally grounded.

5. **Precancer lesion definitions vary across cancer types.** PCMR uses keywords (dysplasia, preinvasive, etc.) without enforcing canonical lesion ontology. Lesion-type heterogeneity within a cancer type (e.g., Barrett's esophagus vs. esophageal dysplasia) is partially collapsed.

6. **Protein and circRNA coverage sparse.** Only 60 protein and 78 circRNA profiles — insufficient for cross-cancer proteomics or circRNA comparisons. The resource is effectively a transcriptomics + methylation resource with limited proteomics.

7. **Functional and clinical annotation depth varies.** Clinical stage information and patient outcome data are not systematically included; survival analysis in the validation section relied on an external resource (GEPIA/TCGA), not PCMR itself.
