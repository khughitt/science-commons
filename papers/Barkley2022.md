---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Barkley2022
kind: paper
title: Cancer cell states recur across tumor types and form specific interactions
  with the tumor microenvironment
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Barkley2022
tags: []
ontology_terms:
- EMT
- NMF
- cancer cell states
- convergent cancer phenotypes
- interferon response
- pan-cancer
- single-cell RNA-seq
- spatial transcriptomics
- tumor microenvironment
dataset_usage:
- ref: dataset:barkley2022-scrna
  role: analyzed
  overlap: unknown
---
## Key Findings

### Data-derived findings (D)

- **(D1) 16 pan-cancer consensus modules identified:** cycling, stress response, interferon response, hypoxia, oxidative phosphorylation, metal-response, alveolar, basal, squamous, glandular, ciliated, complete EMT (cEMT), partial EMT (pEMT), astrocyte-like (AC), oligodendrocyte progenitor cell (OPC)-like, and neural progenitor cell (NPC)-like. Gene set sizes ranged from 9 to 297 genes.
- **(D2) States transcend tumor-of-origin:** UMAP of NMF module scores clusters cancer cells by module state, not by patient or cancer type — demonstrating that these transcriptional programs recur across histological contexts.
- **(D3) Most modules span multiple cancer types:** AC-, OPC-, and NPC-like modules are brain-tumor-enriched; most other modules (stress, IFN, EMT, hypoxia, cycling) were observed across multiple organ systems and histologies.
- **(D4) IFN-response module co-localises with macrophages and T cells:** positive Pearson correlation between interferon-response module score and macrophage neighborhood score in all 10 spatial samples; significant (p < 0.05) in 8/10. CODEX validates T cell co-localisation at single-cell resolution.
- **(D5) Interferon response is lymphocyte-dependent in vivo:** IFN-response module frequency was significantly lower in Rag1−/− mice vs. wild-type KP tumors (p < 10−10, Kolmogorov-Smirnov test). All IFN-response genes remained coordinately expressed in lymphocyte-depleted tumors, implying the state itself is intact but its induction requires lymphocytes.
- **(D6) Microenvironmental induction is location-dependent:** IFN-response module frequency varied by orthotopic tumor implantation site (pancreas vs. peritoneum vs. liver) in the same cell line, demonstrating niche geography shapes state induction.

### Author interpretations (L)

- **(L1) The 16 modules define a "pan-cancer cell state atlas"** — the authors frame these as the dominant axes of transcriptional variation in cancer, analogous to a universal coordinate system for tumor cell phenotypes. [Interpretation: the set is likely incomplete given 15 cancer types; rare/lineage-restricted states will be missing.]
- **(L2) Module co-expression drives continuous, not discrete, variation** — authors conclude that cancer cell states cannot be defined as discretely as cell types; continuous combinatorial expression of modules explains the observed variation. [This is an interpretive framing of UMAP topology; discrete vs. continuous is partly a function of sampling density and biological noise.]
- **(L3) IFN-response co-localisation with immune cells reflects functional signaling** — authors infer that lymphocytes induce the IFN-response state in adjacent cancer cells via paracrine IFN-γ. The Rag1−/− result supports necessity of lymphocytes but does not distinguish signaling-mediated induction from selection/immunoediting.
- **(L4) Cancer cell states are shared across tumor types because they represent universally available stress-response and developmental programs** — the authors invoke convergent co-option of conserved programs to explain cross-histology recurrence. This causal claim is not directly tested.
- **(L5) The niche-dependent induction of states (location experiment) implies the TME is an instructive actor** — the authors interpret the location-dependence of IFN-response frequency as evidence that the microenvironment shapes state occupancy, not just co-localises with it. The direction of causation (niche → state vs. state → niche recruitment) remains unresolved.

## Limitations

### Author-stated

1. **Causality of TME coupling is unresolved:** "It remains unclear to what extent the heterogeneity among cancer cells results from heterogeneity in the signals they receive, or from intrinsic differences between the cells."
2. **Signaling vs. immunoediting ambiguity:** "These findings do not discriminate between signaling mechanisms eliciting an interferon response and long term immunoediting leading to selection of the state."
3. **Continuous state spectrum:** "Cancer cell states cannot be defined as distinctly as cell types," meaning module boundaries are inherently approximate.

### Additional limitations (not author-stated)

4. **No comparison to Gavish/Kinker meta-programs:** The paper does not benchmark its 16 modules against Gavish 2023 NMF meta-programs or Kinker 2020 cell-line heterogeneity programs; the degree of redundancy/novelty across these three contemporaneous atlases is unquantified.
5. **62 tumors across 15 types is unevenly powered:** Rare cancer types contribute few samples; modules unique to undersampled types would be missed.
6. **Visium spatial resolution (~55 µm spots):** Neighborhood and proximity scores are at spot-not-cell resolution; fine-grained cell–cell contact interactions are not resolved. CODEX provides single-cell validation for T-cell co-localisation only.
7. **Untreated primary tumors only:** Module landscape may shift substantially post-treatment; no metastatic samples included.
8. **Mouse KP model for mechanistic validation:** KP (KrasG12D; Trp53fl/fl) NSCLC model may not recapitulate all IFN-response coupling dynamics seen in human tumors.
