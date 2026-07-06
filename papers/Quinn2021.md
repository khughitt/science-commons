---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Quinn2021
kind: paper
title: Single-cell lineages reveal the rates, routes, and drivers of metastasis in
  cancer xenografts
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Quinn2021
tags: []
ontology_terms:
- CRISPR barcoding
- cancer evolution
- clonal dynamics
- lineage tracing
- lung adenocarcinoma
- metastasis
- metastatic tropism
- phylogenetic reconstruction
- single-cell RNA-seq
- xenograft
---
## Key Findings

### Data-derived findings (D)

- **(D)** Of ~2,150 implanted clones, only ~100 successfully engrafted in vivo (Spearman ρ = −0.026 between pre-implantation and final clone size), demonstrating that in vitro fitness does not predict in vivo fitness.
- **(D)** TreeMetRates varied widely and continuously across clones ("a wide range of metastatic phenotypes"), from effectively non-metastatic clones confined to primary-site lobes to highly metastatic clones disseminated across all six tissue sites.
- **(D)** When identical A549-LT clones were implanted into separate mice, their TreeMetRates remained nearly identical (Δ = 0.0005, p = 0.0049), demonstrating that metastatic propensity is heritable and clone-intrinsic rather than stochastically determined per experiment.
- **(D)** Pre-implantation in vitro transcriptional signatures were mildly but significantly predictive of subsequent in vivo metastatic rate, indicating that metastatic state differences pre-exist implantation.
- **(D)** Differential expression analysis identified candidate positive metastasis drivers (IFI27, REG4, TNNT1) and negative regulators (NFKBIA, ID3, KRT17). CRISPR knockdown of IFI6 and IFI27 decreased Boyden-chamber invasiveness (p = 0.001 and 0.005 respectively); knockdown of KRT17, ID3, and ASS1 increased invasiveness — functionally validating transcriptional drivers in orthogonal assays.
- **(D)** Clone #7 exhibited subclonal bifurcation: two descendant clades within the same clone showed divergent TreeMetRates correlated with two heritable gene expression modules (Module 1: lower metastatic rate; Module 2: higher metastatic rate), demonstrating intra-clone transcriptional evolution of metastatic capacity.
- **(D)** FitchCount tissue transition matrices were distinct per clone: multiple metastatic topologies (direct seeding, reseeding, cascade, parallel seeding) were observed across and within clones. The mediastinal lymph tissue was a frequent dissemination nexus, but clone-specific tropism varied.

### Author interpretations (L)

- **(L)** The authors interpret the heritable TreeMetRate stability across mice as evidence that "pre-existing and heritable differences in gene expression" — not microenvironmental chance — are the primary determinant of clone-specific metastatic capacity.
- **(L)** Clone #7 bifurcation is interpreted as in vivo transcriptional evolution of metastatic phenotype from a pre-existing bifurcation point, representing phenotypic evolution within a single clone without (necessarily) new driver mutations.
- **(L)** The mediastinal lymph tissue is proposed as a likely dissemination nexus or intermediate step for lung-to-distant-site metastasis — but FitchCount is an inference from static endpoints, not direct observation of transit.
- **(L)** The authors argue that the tissue microenvironment "amplifies" intrinsic transcriptional differences (mild in vitro signature → strong in vivo differentiation), implying a gene-environment interaction model for metastatic capacity expression.
- **(L)** Future applications suggested: patient-derived xenografts, syngeneic lines, spatial sequencing integration, earlier disease progression stages. These are speculative extensions not demonstrated in this paper.

## Limitations

1. **Single cancer type, single cell line.** A549 KRAS-mutant LUAD in immunodeficient xenograft — no intact immune system, no autochthonous tumor development. Metastatic rates and routes may differ substantially in immunocompetent syngeneic or autochthonous settings.
2. **Static barcode — no temporal resolution.** Cannot detect temporal evolutionary phases within the 54-day window. Limits direct comparison to KP-Tracer and utility for testing h012's cyclical structure.
3. **Single timepoint.** No longitudinal sampling; cannot distinguish early vs. late metastatic events or determine whether clonal composition shifted over time.
4. **Shallow phylogenetic depth.** Mean tree depth 7.25 vs. 12–15 for KP-Tracer — fewer informative lineage-resolving events per cell.
5. **Xenograft biology vs. natural tumor progression.** Direct lung injection of 5,000 cells bypasses early transformation and immune surveillance; does not model the early progression phases most relevant to h012's plasticity-burst.
6. **FitchCount is an inference.** Tissue transition probabilities are derived algorithmically from static endpoint phylogenies, not observed directly. The mediastinal lymph nexus role and cascade vs. parallel seeding conclusions are computational reconstructions with associated uncertainty.
