---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Gavish2023
kind: paper
title: Hallmarks of transcriptional intratumour heterogeneity across a thousand tumours
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Gavish2023
tags: []
ontology_terms:
- 3CA
- NMF
- cancer cell states
- cell of origin
- convergent evolution
- intratumour heterogeneity
- meta-programs
- pan-cancer
- single-cell RNA-sequencing
- transcriptional heterogeneity
dataset_usage:
- ref: dataset:3ca
  role: analyzed
  overlap: unknown
---
## Key Findings

### Data-derived findings (D)

- **41 consensus meta-programs recovered from 5,547 robust NMF programs across 1,163 tumors and 24 cancer types.** The 41 MPs cover 66% of all robust NMF programs; the remaining 34% fall outside any consensus cluster (idiosyncratic or study-specific patterns).
- **83% of the 41 meta-programs were derived from multiple cancer types**, providing a direct empirical estimate of the pan-cancer recurrence rate of transcriptional ITH programs at this resolution.
- **Most carcinoma meta-programs have direct counterparts in non-malignant epithelial cells.** The same NMF/Jaccard pipeline applied to normal epithelium identifies analogous programs, indicating that the dominant axes of variation in malignant cells largely pre-exist in normal tissue heterogeneity, not just arising de novo during oncogenesis.
- **67 → 41 program attrition via QC:** 26 of 67 initial clusters were removed as likely technical artifacts (ribosomal/mitochondrial enrichment, single-study origin, doublet profiles), establishing that ~39% of raw NMF clusters are artifactual at this scale without careful filtering. [UNVERIFIED: exact breakdown of which QC criterion removed how many programs not confirmed from accessible sources]
- **Jaccard-based cross-tumor similarity threshold ≥ 20% is the operational convergence criterion.** Programs meeting this threshold are classified as "recurrent"; those below are classified as "idiosyncratic." This provides a concrete, gene-set-overlap-based definition of transcriptional convergence at the program scale.

### Author interpretations (L)

- **The 11 hallmarks framework is a proposed functional taxonomy**, not an independently derived statistical clustering. The grouping of 41 MPs into 11 hallmarks reflects the authors' annotation judgment about which programs represent related biology. The hallmarks include: cell cycle, stress response, interferon response, hypoxia, epithelial-mesenchymal plasticity (EMP/EMT), MYC targets, protein regulation, senescence, cilia/differentiation markers, lineage-specific programs, and TME-interaction programs. [UNVERIFIED: exact canonical names for all 11 hallmarks not fully confirmed from accessible sources; names listed here are reconstructed from secondary sources]
- **The "cell of origin" interpretation** — that malignant ITH programs are largely pre-specified by normal tissue heterogeneity — is the authors' central explanatory framework. This is supported by the program-overlap finding but the causal inference (pre-specification vs. convergent re-discovery of the same gene modules) cannot be resolved from this observational data alone.
- **Interferon response variability is described as most pronounced in breast cancer despite moderate average activity**, while hypoxia variability is described as more pronounced in sarcoma and glioma than in common carcinomas. These differential patterns are presented as biologically meaningful, but whether they reflect tumor-intrinsic differences vs. scRNA-seq cohort composition is not controlled for in accessible summaries.
- **The framing as "hallmarks" deliberately parallels the Hanahan-Weinberg oncology framework**, positioning transcriptional ITH programs as analogous to hallmarks of cancer. This is a rhetorical/conceptual positioning; the statistical connection between these transcriptional programs and the classical hallmarks is not formally established in the paper.
- **Pan-cancer scope claim:** The authors characterize the 24 cancer type coverage as "across a thousand tumours," implying comprehensive generalizability. However, coverage across the 24 types is uneven (heavily weighted toward common solid tumors with available scRNA-seq data); hematologic malignancies are underrepresented relative to carcinomas.

## Limitations

- **Primary-tumor bias:** The 1,163 tumors are predominantly primary resections; metastatic representation is limited, making direct test of the convergence-progression question (q037) impossible from this dataset alone.
- **Cancer-type imbalance:** Carcinomas (especially head and neck, brain glioma, lung, colorectal) dominate the 24-type coverage; hematologic malignancies are underrepresented.
- **Threshold sensitivity not fully characterized:** The ≥20% Jaccard threshold for cross-tumor recurrence is stated but the sensitivity of the final 41-MP result to this parameter is not comprehensively explored in accessible sources. [UNVERIFIED from accessible sources]
- **Static snapshot:** Per-tumor NMF captures the state space at one timepoint; the method cannot directly measure transitions between states over time.
- **Causal ambiguity for cell-of-origin claim:** Observational overlap between malignant and normal-epithelial programs is consistent with multiple mechanisms (pre-specification, convergent re-use, partial epigenomic retention). The paper cannot distinguish these from observational data alone.
- **TME analysis scope:** The extension to six non-malignant cell types is mentioned in the abstract but methodological details for that component are less well characterized in accessible sources.
