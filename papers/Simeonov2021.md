---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Simeonov2021
kind: paper
title: Single-cell lineage tracing of metastatic cancer reveals selection of hybrid
  EMT states
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Simeonov2021
tags: []
ontology_terms:
- CRISPR barcoding
- EMT
- PDAC
- clonal selection
- hybrid EMT
- lineage tracing
- macsGESTALT
- metastasis
- phenotypic plasticity
- single-cell RNA-seq
---
## Key Findings

### Data-derived findings (D)

1. **Hybrid-EMT states are the primary metastatic state.** Metastatic dissemination — measured by clone/subclone representation at distant sites — peaked at H3/H4 hybrid states (pseudoEMT scores ~20–22). Highly epithelial (E/H1) and highly mesenchymal (M) subclones were both small and non-disseminated. **(D)**

2. **Clonal bottleneck is extreme.** Fewer than 1% of injected clones engrafted; 95 clones identified via 227 static barcodes. A single dominant clone (M1.1 / M2.2) comprised 80–90% of cells at metastatic sites. 51% of clones (48/95) failed to metastasize entirely despite carrying KrasG12D and Trp53R172H. **(D)**

3. **Hybrid-EMT states are clonally stable across sites.** The largest, most disseminated subclones maintained consistent hybrid-EMT transcriptional identity across the primary tumor and multiple metastatic sites. Close phylogenetic relatives (sister subclones from the same parent barcode) shared similar pseudoEMT scores. **(D)**

4. **S100 gene family is the top dissemination-associated factor.** S100a genes were 52-fold overenriched among dissemination-associated marker genes; M2 clones had significantly higher S100 expression than M1 clones (p = 9×10⁻⁹); all seven aggressive M2 clones had higher S100 than any M1 clone. Evidence for cross-clonal S100-mediated paracrine signaling was noted. **(D)**

5. **Metabolic shift at the hybrid transition.** Early-to-late hybrid (H2→H4) transition was accompanied by a shift from oxidative phosphorylation to glycolytic gene programs; proliferative gene sets (G2M, E2F, mitotic spindle) peaked in the H3 state. **(D)**

6. **TCGA survival correlation.** PDAC patients (n=173) enriched for H3/H4 gene signatures had significantly worse overall survival; mesenchymal (M) signature alone had no survival disadvantage. A similar pattern appeared in TCGA lung cancer but not in colorectal, breast, or prostate. **(D)**

7. **In vitro cells are more epithelial than in vivo.** Cultured macsGESTALT cells showed higher epithelial marker expression than even the most epithelial in vivo clones, confirming that the in vivo mesenchymal shift is not a culture artifact. **(D)**

### Author interpretations (L)

1. **Selection, not plasticity, explains hybrid-EMT enrichment at metastases.** Authors interpret the lineage-tracing data as evidence that rare hybrid-state clones are positively selected during metastatic colonization, rather than cells plastically transitioning to hybrid states after arrival. **(L)** (The evidence is consistent with selection, but the static endpoint harvest cannot directly observe within-clone state transitions, so plasticity contribution at single-cell level during colonization is not formally excluded.)

2. **Hybrid-EMT is a distinct "sweet spot" for metastasis.** Authors propose that partial EMT preserves the migratory/invasive capacity of mesenchymal cells while retaining proliferative and colonization capacity of epithelial cells; full EMT overshoots this optimum. **(L)**

3. **The EMT continuum has a non-monotonic fitness landscape.** Authors interpret the peaked metastatic fitness at H3/H4 as reflecting an underlying fitness landscape over the pseudoEMT axis with a maximum in the hybrid zone. **(L)**

4. **S100 proteins mediate cross-clonal paracrine communication.** Authors suggest S100 secretion from aggressive hybrid clones could propagate metastatic competence to adjacent non-aggressive clones via a field effect. **(L)**

5. **The hybrid-EMT selection principle is broadly conserved.** Authors extend the PDAC finding to lung cancer TCGA survival data as evidence of trans-cancer generality; they extrapolate from mouse transplant to human disease. **(L)** (Human validation is correlational, not mechanistic or lineage-traced.)

## Limitations

1. **Single-timepoint, no plasticity-rate measurement.** The 5-week endpoint snapshot cannot distinguish between a clonal-sweep of pre-existing hybrid cells vs. a stabilization of initially plastic cells at hybrid states. EffectivePlasticity (KP-Tracer) or longitudinal sampling would be needed.
2. **Transplant model (xenograft), immunocompromised host.** NOD/SCID mice lack T and B cells. Immune selection, which likely contributes to EMT state selection in immunocompetent settings, is absent. Limits generalization to human immunocompetent PDAC.
3. **n=2 mice (M1, M2).** Only two biological replicates; dominant clone identity differs between M1 (M1.1) and M2 (M2.2). Reproducibility of the hybrid-state selection conclusion across a larger cohort is not established.
4. **KPCY cells are a pre-established cell line.** Unlike KP-Tracer's autochthonous GEMM, the KPCY cells have already undergone in vitro selection before injection; their EMT state distribution at injection may not represent the full in vivo diversity of PDAC cells at primary tumor initiation.
5. **Macsco-GESTALT tree depth is limited by 5 CRISPR sites.** Subclonal resolution is shallower than KP-Tracer (up to 30 intBC sites), limiting phylogenetic depth for resolving early divergence events.
6. **Human TCGA correlation is exploratory.** PDAC survival association with H3/H4 signature is based on n=173 TCGA patients; no lineage-tracing validation in human disease; causality not established.
7. **S100 paracrine mechanism.** Cross-clonal S100 propagation is proposed but not mechanistically validated with perturbation experiments in this paper.
