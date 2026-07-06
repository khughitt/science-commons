---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Zgeib2026
kind: paper
title: Dedifferentiation-Driven Oncogenic Stemness Promotes Tumor-Sustaining Adaptability
  in the Intestinal Epithelium
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Zgeib2026
tags: []
ontology_terms:
- cancer stem cells
- colorectal cancer
- dedifferentiation
- intestinal tumorigenesis
- oncogenic stemness
- plasticity
- top-down tumorigenesis
---
## Key Findings

**Dedifferentiation triggers documented:**
- Simultaneous Smad4 LOF and beta-catenin GOF in villus (post-mitotic, differentiated) epithelium induces rapid dedifferentiation: Keratin-20 loss within 30 days, CD44 and EphB2 upregulation within 7 days (ectopic crypt formation precedes these).
- Bulk RNA-seq at day 7 showed downregulation of tumor suppressor *Clca4* and upregulation of stem cell marker *Prom1*, with enrichment of Hallmark Myc, E2F, cell fate plasticity, and embryonic stemness gene signatures.
- Aberrant Notch activation (NICD immunoreactivity) detected in villus epithelium within 7 days of mutation induction — **before** ectopic crypt formation and in the absence of Paneth cells in villi — indicating ligand-independent or non-canonical Notch activation at the onset of dedifferentiation.
- Metabolic reprogramming in dedifferentiating villi: elevated hypoxia (pimonidazole), increased Glutaminase (GLS) and TOM20 (mitochondrial function), and upregulation of cytoprotective antioxidants Prdx3, Prdx6, and mitochondrial quality-control protein PINK1.

**Dedifferentiation-derived stem cells outcompete crypt stem cells:**
- When Smad4^LOF^:beta-catenin^GOF^ was induced specifically in Lgr5+ crypt stem cells (Lgr5-CreERT2), mutant cells were progressively displaced from the crypt niche by wild-type stem cells by 22 days. This was attributed to Smad4/BMP signaling loss increasing proliferation and thus displacing mutant cells from the niche.
- In contrast, CD44+/Lgr5+ cells accumulated in Smad4-negative hyperplastic regions near the lumen — consistent with dedifferentiation-derived oncogenic stemness in the villus compartment.
- Mutant-derived organoids grew without EGF/Noggin/R-spondin (growth factor independence), demonstrating niche-independent proliferative capacity absent in wild-type.

**scRNA-seq heterogeneity of dedifferentiation-derived stem cells:**
- Mutant villi contained five stem clusters (c3, c6, c9, c10, c14) vs. two in wild-type (c5, c7), demonstrating greater stem cell heterogeneity.
- Cluster c3 (unique to double-mutant epithelium, no transcriptional overlap with wild-type): enriched for cancer-associated mESC-like gene signatures, Hallmark E2F/MYC/MTORC1, and ROS pathways; heterogeneous loss of intestinal lineage factor Cdx2; active tumor-driving potential.
- Clusters c9, c10, c14: enriched for Hedgehog signaling without proliferative signatures — quiescent/survival state.
- Cluster c14 showed co-expression of tuft cell markers and stem/proliferative markers — suggesting tuft cell contribution to dedifferentiation.
- Cluster c3 in mutant villi (vs. crypts) was specifically enriched for ROS and mTORC1 pathways, distinguishing villus-specific metabolic adaptations.

**Tumor formation:** Palpable tumors appeared within 1–2 months of mosaic induction (single 0.01 g/kg tamoxifen dose), histologically consistent with top-down / luminal origin.

## Limitations

- Mouse model uses simultaneous induction of two mutations (Smad4 LOF + beta-catenin GOF); the paper does not address whether dedifferentiation-driven tumorigenesis occurs with single mutations or in a stepwise sequence more typical of human CRC progression.
- Primary tissue is duodenum (small intestine); extrapolation to colorectal context requires caution, though human colon adenoma histology motivated the model.
- No chromatin accessibility profiling (scATAC-seq) was performed; it is unknown whether the villus chromatin landscape predisposes to the mESC-like trajectory or whether the mutations remodel chromatin de novo.
- No longitudinal single-cell profiling — the 7-day snapshot captures a single point; dynamics of dedifferentiation trajectory and cluster emergence over time are not resolved.
- Notch activation mechanism in villi is unresolved: ligand source and whether it is ligand-independent or reflects a non-canonical activation pathway requires further investigation.
- The paper does not assess whether genetic changes accumulate preferentially in dedifferentiation-derived lineages over time — the full genetic accommodation sequence (plastic first, genetic fixation second) is argued but not tracked.
- Tuft cell contribution to dedifferentiation is suggested by cluster c14 expression pattern but not functionally validated.
- Study does not include human patient-derived samples; the link to sporadic human colorectal adenoma is inferential based on histological features cited from the literature.
