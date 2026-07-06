---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Patel2024
kind: paper
title: A developmental constraint model of cancer cell states and tumor heterogeneity
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Patel2024
tags: []
ontology_terms:
- cancer cell states
- cell of origin
- developmental constraint
- plasticity
- single-cell transcriptomics
- tumor heterogeneity
---
## Key Findings

**Cell-of-origin determines the accessible state repertoire (the core empirical claim):**
In every cancer type examined, the observed malignant cell states correspond to cell types that are developmentally proximate to the presumed cell of origin — both upstream (toward progenitor/stem states) and downstream (toward differentiated daughter states) along the same developmental branch. Cells do not acquire states from developmentally distant lineages except where the developmental map provides an accessible path (e.g., the embryonic-liver-like state in lung adenocarcinoma is reachable via a foregut progenitor intermediate).

**Seven cancer types surveyed:**

- *Lung adenocarcinoma* (cell of origin: alveolar type II): 7 states — alveolar type I-like, alveolar type II-like, mixed alveolar, club-like, gut-like, embryonic-liver-like, mesenchymal/EMT. All map onto the foregut developmental branch. Mouse Kras activation in AT2 cells recapitulates these states; SOX2 activation in AT2 or basal cells drives squamous histology.
- *Lung squamous cell carcinoma* (cell of origin: basal/proximal progenitor): states include basal-like, ciliated-like, club-like — proximal lung lineage, not the distal alveolar branch.
- *Glioblastoma* (putative cell of origin: oligodendrocyte progenitor cell): four dominant states — astrocyte-progenitor-like (APC), neural-progenitor-like (NPC), oligodendrocyte-progenitor-like (OPC), mesenchymal-like — all map to glial/neural progenitor development. Individual cell states have tumor-initiating capacity and generate heterogeneous tumors on transplantation.
- *Melanoma*: pigmented/MITF-high, neural-crest-like, invasive/AXL-high/mesenchymal — mapping to melanoblast and neural crest developmental lineage (ectoderm → neural crest → melanoblast).
- *AML* (hematopoietic stem cell of origin): states recapitulate hematopoietic stem, common myeloid progenitor, GMP-like, monocyte-like, cDC-like — consistent with the myeloid development hierarchy.
- *Rhabdomyosarcoma* (striated muscle cell of origin): muscle progenitor-like, differentiated muscle, mesenchymal — all mesodermal/muscle developmental branch.
- *Pancreatic ductal adenocarcinoma*: acinar-like, classical (pancreatic progenitor), basal-like, neuroendocrine-progenitor-like, mesenchymal — all within the pancreatic/foregut endoderm branch.

**The developmental constraint is bidirectional:** Cells traverse the map both forward (toward differentiation) and in reverse (toward progenitor states), but only within the accessible developmental branch. Trans-differentiation events that cross to distant branches (e.g., lung adenocarcinoma to squamous carcinoma histological transformation under EGFR-targeted therapy) are explained as traversal via a shared upstream progenitor state (the proximal lung multi-lineage state), not a direct jump.

**Chromatin remodeling as the molecular mechanism:** The constraint is proposed to operate via chromatin accessibility. During tumorigenesis, the transformed cell of origin establishes a chromatin landscape reminiscent of a plasticity-permissive developmental cell type. Chromatin remodelers (histone-lysine demethylases; EZH2 gain-of-function mutations; PHF8 histone demethylase) are frequently mutated in cancer and can promote bidirectional cell state transitions within the developmental map. Bivalent promoters and chromatin loop remodeling encode the developmental map and are exploited by cancer cells.

**Contrast with cancer stem cell (CSC) model:** The CSC model requires a privileged stem-cell population with high propagating potential producing non-CSC progeny with limited propagating potential. The developmental constraint model instead posits that all states in a tumor share plasticity to traverse the developmental map — no single state holds privileged propagating capacity — and heterogeneity is a population-level property of traversal dynamics, not a hierarchy.

**Therapeutic implications:** (1) Inhibiting developmentally constrained cell state transitions (e.g., blocking HDAC1 to suppress acinar-to-ductal plasticity in pancreatic cancer) may restrict the plasticity that underlies acquired drug resistance. (2) Positions along the developmental map correlate with tumor aggressiveness (neuroblastoma undifferentiated vs. ganglioneuroma differentiated). (3) Spatial co-option of morphogenetic signals (nodal-SMAD2, Wnt) may maintain intratumor heterogeneity through patterning axes, providing targets.

## Limitations

1. **Observational / correlative synthesis:** No new primary data are generated. The case for developmental constraint rests on post-hoc correspondence between cancer cell states and developmental atlases; confounding by shared gene expression programs (e.g., stress, EMT) is acknowledged but not quantitatively excluded in all cases.
2. **Cell-of-origin often unknown:** For several of the seven cancer types, the cell of origin remains contested or unknown (glioblastoma, pancreatic ductal adenocarcinoma). The model's predictions are post-hoc fits; prospective tests require genetically defined cell-of-origin systems.
3. **Constraint strength is not quantified:** The authors do not provide a metric for how tightly the developmental map restricts the observed state repertoire — i.e., how far outside the predicted branch any cancer cell states actually fall, or how often. The model is framed qualitatively.
4. **AML limitation acknowledged:** The model does not explain why AML cells restricted to myeloid states do not access lymphoid states, even though both share an upstream HSC origin. Additional lineage-commitment constraints (not just developmental adjacency) must operate.
5. **Microenvironmental and immune contributions:** The paper focuses on malignant cell states and largely brackets the contributions of the tumor microenvironment in establishing and sustaining developmental state distributions, treating these as secondary.
6. **Chromatin mechanism is speculative:** The proposed link between chromatin remodeler mutations and constraint relaxation is inferential; no direct chromatin accessibility measurements across the seven cancer types are presented.
