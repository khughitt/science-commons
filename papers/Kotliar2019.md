---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Kotliar2019
kind: paper
title: Identifying gene expression programs of cell-type identity and cellular activity
  with single-cell RNA-Seq
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Kotliar2019
tags: []
ontology_terms:
- cell-type identity
- cellular activity
- consensus factorization
- convergent transcriptional programs
- dimensionality reduction
- gene expression programs
- non-negative matrix factorization
- scRNA-seq
---
## Key Findings

### Data-derived findings (D)

- **D1. Consensus dramatically increases reproducibility.** Single-run NMF and LDA show high inter-replicate variability; merged/split GEP solutions are common. After consensus (k-means + median over 200 replicates), the fraction of replicates yielding a component with Pearson r > 0.9 to its cluster median rises substantially for both NMF and LDA. cNMF consistently outperformed single-run NMF in GEP deconvolution accuracy across all simulated signal levels.

- **D2. cNMF leads all methods for activity GEP gene identification.** At 5% FDR on simulated data (signal level log₂FC=1.0): cNMF 61% sensitivity, cICA 57%, ground-truth clustering 56%, Louvain clustering lower. cNMF also outperformed other methods on identity GEPs for the 4 cell types expressing the activity GEP.

- **D3. Cell usage inference is quantitatively accurate.** With a 10% usage threshold, cNMF classified 91% of cells expressing the activity GEP correctly and 94% of non-expressing cells correctly. Pearson correlation between simulated and inferred usage across activity-expressing cells: R=0.74 (all simulations combined) / R=0.68 (example simulation).

- **D4. cNMF is robust to doublets.** Doublets are correctly modeled as mixtures of two identity GEP vectors. GEP inference remained accurate in a simulated dataset composed of 50% doublets.

- **D5. Rare cell types cause missed GEPs.** In simulations with biologically realistic cell-type proportions (derived from Hrvatin et al. clustering), rare cell-type identity GEPs were missed by cNMF, cICA, and Louvain clustering. When GEP distinctness was increased (log₂FC location parameter=2.0), recovery improved to levels comparable to the uniform-frequency benchmark.

- **D6. K choice is stable within ± ~4 of selected value.** Varying K by ±4 around the chosen value: each increment adds/removes approximately one marginal GEP; core GEPs have Pearson r > 0.7 with their counterparts across the range.

- **D7. In brain organoid data (52,600 cells), three activity GEPs recovered:** two cell-cycle programs (G1/S and G2/M — distinguished by GO enrichment: DNA Replication p=3×10⁻⁵² vs. Mitotic Nuclear Division p=4×10⁻⁶¹) and one hypoxia program (not anticipated by original analysis). The 28 identity GEPs refined the 10 original cluster annotations, including splitting a "mesodermal" cluster into immature/fast-twitch/slow-twitch skeletal muscle programs.

- **D8. In visual cortex data, cNMF recovered depolarization-induced programs.** An early response program (ERP), a superficial-layer-dominant late response program (LRP-S), and a deeper-layer-dominant late response program (LRP-D) — the latter correlation suggesting anatomical or developmental regulation of depolarization response.

### Author interpretations (L)

- **L1. Identity/activity taxonomy is biologically fundamental.** The authors argue the distinction is a natural consequence of transcriptional co-regulation and maps to the empirical structure of single-cell data — cells with mixed profiles genuinely reflect multiple simultaneous programs rather than intermediate states. (The discussion acknowledges the boundary is not always sharp: oncogenic transformation, morphological gradients, and stochastic TF fluctuations do not fit neatly into either class.)

- **L2. NMF non-negativity is the key inductive bias.** The authors argue non-negativity yields naturally interpretable usage and component matrices as probability-like distributions (sum-to-one after normalization), contrasting with ICA (negative components/usages) and PCA (orthogonality constraint forces linear combinations of true GEPs, not aligned components). This is offered as the primary reason cNMF is preferred over cICA despite comparable accuracy.

- **L3. The three novel visual cortex programs may reflect neurosecretory phenotype, new synaptogenesis, and a stress response.** These are speculative functional annotations; no experimental validation is provided in this paper.

- **L4. The hypoxia program in brain organoids is unexpected and indicates a biologically important but previously uncharacterized activity.** The authors suggest organoid culture conditions generate hypoxic niches not captured by bulk analysis. This is plausible but inferred from gene-set enrichment alone.

- **L5. Matrix factorization will supersede clustering as the standard scRNA-seq analysis paradigm for mixed-state data.** The authors argue clustering "often fails" for activity GEPs and that factorization is the natural generalization — a claim supported by their benchmarks but extrapolated beyond the tested scenarios.

## Limitations

1. **Linearity assumption.** cNMF models cells as linear mixtures of GEPs. Transcriptional repression (one GEP suppressing genes induced by another) is not representable. Authors acknowledge this and point to VAEs as a potential future extension.

2. **Rare cell-type GEPs missed.** Validated quantitatively in simulations with realistic cell-type frequency distributions. Rare programs require higher within-program signal (larger fold-change) to be recovered.

3. **K selection remains subjective.** Two diagnostic aids are provided (error/stability curve + scree plot), but the final choice depends on biological judgment and robustness checks at K ± a few. No formal model-selection criterion.

4. **Count distribution not modeled.** NMF uses a Gaussian (Frobenius) error model; scRNA-seq data follows negative binomial / Poisson distributions. Hierarchical Poisson Factorization may improve accuracy; authors flag this as a known gap.

5. **Sparsity not enforced.** NMF yields low but non-zero usages for many GEPs in each cell, over-fitting. Regularization is mentioned as a future direction.

6. **Outlier threshold τ is dataset-specific.** Requires visual inspection of KNN-distance histogram; not fully automatable. ρ=0.30 worked across all tested datasets as a default.

7. **No tumor / cancer data in this paper.** The identity/activity taxonomy was developed on brain organoids and normal visual cortex; applicability to cancer, where cell-state continuity and oncogenic programs blur the identity/activity boundary (authors' own caveat), was demonstrated post-hoc by Kinker 2020 and Gavish 2023.
