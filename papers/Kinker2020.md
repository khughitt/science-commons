---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Kinker2020
kind: paper
title: Pan-cancer single-cell RNA-seq identifies recurring programs of cellular heterogeneity
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Kinker2020
tags: []
ontology_terms:
- CCLE
- EMT
- cancer cell lines
- cancer cell states
- cell plasticity
- expression programs
- intra-tumor heterogeneity
- non-negative matrix factorization
- pan-cancer
- senescence
- single-cell RNA-sequencing
dataset_usage:
- ref: dataset:ccle
  role: analyzed
  overlap: unknown
---
## Key Findings

### Data-derived findings (D)

- **(D1) 12 RHPs identified across 198 cell lines / 22 cancer types.** The programs cover: two cell-cycle programs (G1/S, G2/M), epithelial senescence (EpiSen), two EMT programs (EMT-I, EMT-II), stress response, interferon signaling, protein folding/unfolding (proteotoxic stress), and epithelial differentiation-related programs. [Note: exact catalog of all 12 names [UNVERIFIED from PMC HTML rendering — requires direct access to main text Table or Fig 3].]
- **(D2) 7/10 non-cycling RHPs show highly significant overlap with tumor-derived programs** (FDR-adjusted p < 10⁻⁹). This is the primary quantitative evidence that cell-line programs generalise to patient tumors.
- **(D3) Discrete subpopulations are rare (11% of lines) and predominantly genetically driven (39% associated with CNA subclones).** Continuous NMF programs are the dominant mode of intra-line heterogeneity and are largely non-genetic (only 8% tied to CNAs).
- **(D4) EpiSen program predicts cetuximab response in HNSCC.** In a 40-patient cohort (recurrent/metastatic HNSCC, cetuximab + chemo), EpiSen-high tumors predicted long progression-free survival: AUC = 0.86, sensitivity 79%, specificity 77%.
- **(D5) G1/S program shows an in vitro-specific signature shift.** Cell-line G1/S programs emphasise histone H1 genes; tumor G1/S programs emphasise MCM complex genes — consistent with cell-line adaptation to rapid in vitro growth altering the exact transcriptional realisation of the cell-cycle program.
- **(D6) EMT-I / pigmentation programs show anti-correlated expression in melanoma** both in cell lines and in patient tumors, replicating a previously described plastic EMT–pigmentation axis.
- **(D7) Cell lines show fewer apparent G0 cells than matched tumor profiles** despite similar program structure — consistent with in vitro selective pressure for active proliferation eliminating dormancy-associated states.

### Author interpretations (L)

- **(L1) Continuous programs primarily reflect cellular plasticity rather than clonal selection.** The authors argue that because NMF programs are largely un-linked to CNAs (only 8%), they represent non-genetic, plastic heterogeneity. This inference assumes CNA detection is comprehensive — but small-scale mutations, epigenetic clones, or silent copy-number changes could drive apparently "plastic" programs. [INQUIRY: The 8% CNA-linked figure understates genetic contributions if silent mutations drive programs — has this been addressed in follow-up work?]
- **(L2) Cell-line RHPs are valid proxies for in vivo transcriptional programs.** The 7/10 overlap with tumor programs (D2) is taken as evidence that cell-line culture conditions do not fundamentally distort the transcriptional programs. The authors acknowledge this is partial — 3/10 non-cycling RHPs do not replicate in tumors, and the G1/S shift (D5) shows culture-specific adaptation.
- **(L3) EpiSen predicts therapy response via senescence biology.** The clinical validation (D4) is interpreted as evidence that the EpiSen program reflects a genuine biology of epithelial senescence that influences drug response, not as a generic proliferation signature. This causal attribution is an interpretation from correlative clinical data.
- **(L4) The proportion of cells in heterogeneous programs is stable across culture conditions.** The authors suggest that for long-term propagated cell lines, program proportions stabilise, making them reproducible in vitro models of intra-tumoral heterogeneity. This is asserted but not demonstrated with systematic temporal perturbation experiments in this paper.
- **(L5) Discrete genetic subclones in cell lines recapitulate intra-tumor clonal architecture.** The observation that 26% of cell lines carry detectable CNA subclones is interpreted as in vitro persistence of in vivo genetic heterogeneity — but cell-line propagation-induced CNA changes cannot be ruled out as an alternative source.

## Limitations

### Cell-line generalizability (core limitation)

- **Culture selection pressure alters program composition.** Cell lines are passaged for rapid growth, which reduces apparent G0 cells (D7) and shifts the G1/S program signature (D5). Any program favoured by in vitro growth conditions will be over-represented, any program requiring microenvironmental signals will be under-represented or absent.
- **Absence of stromal/immune TME.** Cell lines lack the microenvironmental context that drives many in vivo programs (hypoxia gradients, immune-cell secreted factors). The interferon-response and immune-interaction programs detected in cell lines may differ from their in vivo counterparts in magnitude and context.
- **3/10 non-cycling RHPs do not replicate in patient tumors** (the 7/10 replicate rate means ~30% of cell-line programs may be culture artefacts or at minimum are not detectable at the sensitivity of the patient-tumor datasets used for comparison).
- **Co-culture duration effects.** Cells are co-cultured for a limited period before single-cell capture; the authors acknowledge this could affect program proportions but do not systematically characterize temporal stability.

### Genetic heterogeneity detection

- CNAs are inferred from scRNA-seq expression windows (100-gene sliding windows), which has lower sensitivity than WGS or FISH. The 8% figure for NMF programs linked to genetics likely **underestimates** true genetic contribution from SNVs, small indels, and sub-CNA epigenetic clonal expansions.

### Scale and diversity

- 198 cell lines from 22 cancer types is broad but CCLE composition reflects historical cancer-type accessibility (solid tumour lines dominate); hematologic malignancy lines and rare cancer types are under-represented.
- Within-cancer-type depth is uneven; some cancer types are represented by very few lines, potentially making the recurrence threshold of ≥8 lines impossible to reach for cancer-type-specific programs.

### In vivo extension

- The paper explicitly cautions that cell-line programs may not capture the full program diversity seen in patient tumors. Gavish 2023 subsequently discovers several programs (e.g., subdivided stress, alveolar-like, hypoxia-specific) not present in Kinker 2020, consistent with cell-line programs being a compressed subset of the in vivo landscape.
- No longitudinal or treatment-perturbation data — impossible to assess whether RHP proportions are stable under therapy or during progression, which is the core question for q037.
