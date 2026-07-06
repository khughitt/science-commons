---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Galassi2025
kind: paper
title: Epigenetic regulation of cancer stemness
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Galassi2025
tags: []
ontology_terms:
- DNA methylation
- cancer stem cells
- drug tolerance
- epigenetics
- epithelial-mesenchymal transition
- histone modification
- plasticity
---
## Key Findings

### Load-bearing epigenetic mechanisms for stemness

**DNA methylation**
- DNMT1 is uniquely required for CSC (not bulk cancer cell) survival; DNMT1 sustains bivalent chromatin domains and pluripotency-related gene expression (SOX2, NANOG, FOXO3) across AML, breast cancer, GBM, and CRC.
- TET2 loss in AML drives hypermethylation at regulatory enhancers, repressing differentiation genes (GATA2, HOX family) and reinforcing LSC self-renewal; TET2 reconstitution blocks leukemogenesis.
- IDH1/2 mutations produce D-2-hydroxyglutarate, which inhibits TET enzymes, causing widespread hypermethylation that locks cells in an undifferentiated, stemness-permissive state — a direct mechanistic bridge between a somatic mutation and epigenetic state stabilization.
- DNMT3A mutations (frequent in AML) increase LSC self-renewal via blocked differentiation; contribute to anthracycline resistance through impaired nucleosome eviction.

**Histone methylation (H3K4, H3K9, H3K27, H3K36, H3K79)**
- H3K4 methyltransferases KMT2A and SMYD3 transactivate pluripotency TFs (SOX2, NANOG, POU5F1) and stemness pathways (WNT/β-catenin, NOTCH) in AML, pancreatic, CRC, and breast CSCs.
- KDM1A (LSD1; H3K4 demethylase) promotes GSC oncogenesis by repressing BMP2/CDKN1A and enhancing WNT/β-catenin; KDM1A inhibition reduces stemness and sensitizes GSCs to temozolomide.
- H3K9 methylation by SUV39H1 suppresses stemness in melanoma and AML; EHMT2 (G9a) promotes CSC-driven EMT and AML development, while pharmacological EHMT2 inhibitors eradicate LSCs in CML models.
- EZH2 (H3K27 methyltransferase, PRC2 catalytic subunit) consistently supports CSC maintenance and therapy resistance across GBM, CRC, breast cancer, CML, and AML: silences differentiation-associated genes (IHH, CCND1) and tumor suppressors (PTEN); gain-of-function mutations frequent in germinal-center B-cell lymphomas.
- DOT1L (H3K79 methyltransferase) is critical for LSC survival (not normal HSCs), supporting MLL-AF9 chimera-driven leukemogenesis; DOT1L loss reduces LSC tumorigenicity in vivo.
- Bivalent chromatin domains (H3K4me3 + H3K27me3) maintain stemness-associated and plasticity genes in a "poised" transcriptional state, allowing rapid activation or repression on environmental cue — a key heritability mechanism.

**Histone acetylation (HATs and HDACs)**
- CREBBP/EP300 drive GSC emergence and expansion via FOXM1, STAB2, and other stemness genes; EP300 also transactivates SNAI1, ZEB1, ZEB2, supporting EMT and CSC acquisition.
- Multiple HDACs (HDAC1–4, HDAC6, KAT2A, KAT7) exhibit complex, context-dependent effects on stemness; HDAC1 reinforces GSC tumorigenicity via p53 repression; HDAC6 sustains colorectal CSCs via IL-6/STAT3.
- KAT2A (GCN5) is essential for LSC maintenance and eradication (specific to LSCs, spares HSCs); KAT7 supports LSC clonogenic potential.

**Histone ubiquitination (PRC1/BMI1)**
- BMI1 (PRC1 core component; H2A monoubiquitination) is the single most broadly cited CSC self-renewal regulator in the review, operating across AML, CRC, breast cancer, GBM, and prostate cancer; BMI1 inhibition induces cellular senescence in GSCs and sensitizes multiple tumor types to chemotherapy.
- CBX8 supports stemness via NOTCH (H3K4 trimethylation at NOTCH-related promoters); RING1/RNF2 maintain LSC tumorigenicity by repressing GLIS2 and CDKN2A.

### Heritability of epigenetic states across cell divisions

The review explicitly argues that epigenetic marks are "reversible but can be transmitted across generations, thereby preserving the memory of gene activity" (Introduction, citing Waddington/Allis). Specific heritable mechanisms highlighted:
1. **Bivalent chromatin domains** — maintained through cell division by PRC2/PRC1 propagation, keeping plasticity genes in a poised state accessible to environmental cues.
2. **DNMT1-mediated maintenance methylation** — copies DNA methylation patterns to daughter strands after replication; DNMT1 loss collapses CSC compartments, confirming that inheritance of methylation state is load-bearing for stemness.
3. **KDM5A-mediated slow-cycling DTP subpopulation** — drug-tolerant persisters (DTPs) are defined by a repressed bivalent chromatin state maintained by KDM6A/B erasing H3K27me3 during chemotherapy; this state seeds relapse and is reacquired rapidly on re-exposure, consistent with epigenetic memory.
4. **IDH1/2-driven hypermethylation** — oncometabolite D-2-HG irreversibly (or quasi-irreversibly) locks cells in a hypermethylated state; IDH1 mutations establish irreversible epigenetic changes contributing to stemness in AML and GBM.

The review does not resolve whether spontaneous heritable epigenetic variation (Darwinian substrate) is mechanistically distinguishable from regulated plastic responses to environmental signals.

### Epigenetic plasticity programs

Four CSC plasticity programs are identified (Fig. 5):
1. **Dedifferentiation** — differentiated cancer cells revert to stem-like states in response to therapy or microenvironmental cues; driven by EZH2, DNMT3A, and TET2.
2. **Drug-tolerant persistence (DTP)** — slow-cycling, stem-like subpopulation survives therapy via epigenetic reprogramming; bivalent chromatin state maintained by KDM6A/B; seeds relapse reservoir.
3. **Epithelial–mesenchymal plasticity (EMP)** — reversible transitions across hybrid EMT/MET states; dynamic DNA hypomethylation supports hybrid EMT in lung cancer; EZH2 and KDMs modulate bivalent chromatin domains; KMT2C loss enhances IFN-γ sensitivity and reduces EMP.
4. **CSC heterogeneity** — dynamic interconversion between CSC states driven by intrinsic cues and therapy; single-cell profiling in HCC, GBM, CRC, and breast cancer reveals transcriptionally distinct CSC subpopulations with lineage plasticity and dedifferentiation trajectories.

### Therapeutic targeting

Clinically approved epigenetic drugs include azacitidine/decitabine (DNMT inhibitors), EZH2 inhibitors, and HDAC inhibitors. Challenges: low target specificity, toxicity to normal stem cells (especially DNMT1, BMI1), acquired resistance via compensatory epigenetic reactivation, and incomplete CSC eradication due to plasticity. Combination strategies (e.g., HDAC + BRD4 inhibitors, EZH2 + TKI) appear necessary in multiple contexts.

## Limitations

- Narrative review; no systematic evidence grading or meta-analysis. Individual mechanistic claims are drawn from single-model systems and may not generalize.
- ncRNA mechanisms (lncRNAs, miRNAs, m6A) are explicitly excluded despite acknowledged importance; epitranscriptomic crosstalk is noted only briefly in the conclusion.
- Chromatin accessibility (ATAC-seq landscape) is not systematically treated as a mechanistic layer separate from histone modifications — this matters for q009 (accessibility vs. TF availability as the operative constraint).
- No longitudinal or single-cell evolutionary dynamics data; all claims about state transitions are inferred from static comparisons or pharmacological perturbations.
- Therapeutic claims are largely preclinical; clinical translation of most discussed targets remains unproven.
- Immunoevasive properties of CSCs explicitly out of scope (covered in companion review, Galassi et al. 2024, *Trends Cancer*).
