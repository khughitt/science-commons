---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Watson2020
type: paper
title: The Evolutionary Dynamics and Fitness Landscape of Clonal Hematopoiesis
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Watson2020
tags: []
datasets:
- dataset:watson2020-ch-cohorts
ontology_terms:
- Bayesian inference
- CHIP
- age-resolved inference
- clonal dynamics
- clonal hematopoiesis
- drift
- fitness coefficient
- fitness landscape
- hematopoietic stem cell
- positive selection
- selection coefficient
- variant allele frequency
---
## Key Findings

### Fitness landscape — top 20 most commonly observed CH variants (Fig. 2A)

| Variant | s (% per year) | Per-site mutation rate μ (×10⁻⁹/yr) |
|---|---|---|
| SRSF2 P95R | **23.1** | 2.5 |
| SF3B1 K700E | **22.9** | 3.5 |
| DNMT3A R882C | **18.7** | 5.9 |
| SRSF2 P95H | 16.1 | 7.5 |
| DNMT3A R729W | 16.0 | 14.9 |
| DNMT3A R326C | 15.8 | 11.8 |
| SF3B1 K666N | 15.4 | 4.7 |
| SRSF2 P95L | 15.1 | 6.8 |
| DNMT3A R320* | 15.0 | 8.5 |
| GNB1 K57E | 15.0 | 7.8 |
| DNMT3A R882H | 14.8 | 18.8 |
| JAK2 V617F | 14.6 | 13.6 |
| IDH2 R140Q | 14.5 | 5.2 |
| DNMT3A R736H | 14.1 | 17.3 |
| DNMT3A Y735C | 12.9 | 13.9 |
| DNMT3A R736C | 12.3 | 8.5 |
| DNMT3A W860R | 12.1 | 39.6 |
| DNMT3A R771* | 12.0 | 13.1 |
| DNMT3A R598* | 11.9 | 22.8 |
| DNMT3A P904L | 11.2 | 45.2 |

Notably, **DNMT3A R882C is fitter than the more common R882H** (s = 19 ± 1% vs s = 15 ± 1% per year) but is observed less frequently because of its lower mutation rate — a clear example of the mutation-rate / fitness-effect decoupling that the per-variant framework was designed to expose.

### Spectrum of fitness effects per gene (Fig. 2B)

For each of the 10 most-mutated CH genes, the per-variant fitness distribution was binned into low (s ≤ 4%), moderate (4 < s < 10%), and high (s ≥ 10%):

- **DNMT3A:** ~60% low, ~33% moderate, ~7% high — highest moderate-to-high fraction, with ~40% of nonsynonymous variants in the moderate-to-high range.
- **TET2, ASXL1, TP53:** ~93% low, ~7–10% moderate-to-high — distributions much more skewed toward low fitness than DNMT3A. Most nonsynonymous variants in these three genes are effectively neutral over a human lifespan.
- **TP53 high-fitness variants** are strongly enriched for missense in the DNA-binding domain (figs. S24/S25), consistent with recent functional and clinical data.

### Pre-leukemic risk stratification

By pooling across nine independent studies, the paper identifies **≥2,500 variants** within these 10 genes that confer moderate-to-high fitness. Individuals harbouring at least one of the **top 20 high-fitness variants** are **≈4-fold more likely to develop AML** vs those harbouring lower-fitness variants (one-sided Fisher's exact test, p < 10⁻⁵).

### HSC population parameters

- Inferred **Nτ ≈ 100,000 ± 30,000 years** (consistent with single-HSC phylogeny estimates of similar magnitude).
- Assuming ≈16 mutations per cell per year and HSC division ≈13 times per year, the bound **τ < 4 years** (assuming s_max ≈ 25%) implies **N < 1.3 million HSCs** — consistent with phylogenetic estimates of ~25,000 HSCs.
- **Synonymous variants** behave as ≈ neutral hitchhikers with characteristic max VAF φ ≈ 0.03 ± 0.005% — broadly agreeing with the prediction t/(2Nτ) ≈ 0.025% at age 50 from the Nτ inference.

### Validation: age-resolved CH prevalence

Predicted CH prevalence rises **linearly with age** at the rate 2Nτμs for a given sequencing sensitivity. The actual age-prevalence data from Coombs2017 (VAF LOD ≈0.1%) and Young2016/2019 (VAF LOD ≈2%) match this linear-with-age prediction (Fig. 3); the slope corresponds to a fitness effect of s ≈ 14% per year for DNMT3A R882, in agreement with the VAF-spectrum-derived value (independent cross-check).

### In HSCs, fitness dominates drift

Quantitatively: a neutral variant takes ~100,000 years to drift to VAF = 50%, and >2,000 years to be detectable at VAF = 1% (standard sequencing threshold). The vast majority of CH variants reaching VAF > 0.1% over a human lifespan are therefore positively selected. However, infrequently mutated yet highly fit variants likely exist below most cohort detection limits and are systematically missed by the counting approach.

### Sensitivity-driven prediction

At a sensitive sequencing threshold of VAF ≥ 0.01%, CH variants would be **detectable in young adults and ubiquitous in individuals over 50**. The framework also predicts that **<15% of individuals aged ≥80 will harbour clones with two or more mutations within the same cell** at this sensitivity — a testable cooperativity boundary.

## Limitations

- **Cell-intrinsic fitness assumption:** The framework assumes per-variant fitness effects are cell-intrinsic and constant over the lifespan. The authors explicitly note that fitness is context-dependent and that cell-extrinsic effects (aging, chemotherapy, infection, inflammation) likely shape some `s` values; specific known examples (PPM1D, TP53, CHEK2, ASXL1) are flagged as influenced by external factors. This is the empirical opening for `question:062-ch-fitness-nonstationarity-age-conditional`.
- **No interaction between clones:** The branching-process formulation treats each clone as evolving independently. Competitive suppression or ecological facilitation between co-resident clones (the concern of `question:026`) is invisible to this framework.
- **N and τ confounded.** Population genetics analyses can only reliably infer the product `Nτ`, not `N` and `τ` separately. The bound `N < 1.3 million` requires the additional assumption `s_max ≈ 25%`. Subsequent literature must respect this confounding.
- **N or τ may have more complex meanings under multi-layer HSC dynamics.** The authors acknowledge that models with switching between active and quiescent states or progenitor reversion would yield the same data but with `N` and `τ` reinterpreted; distinguishing such scenarios requires longitudinal data.
- **Coarse counting of low-frequency variants.** Variants in known AML drivers FLT3 and NPM1 are nearly absent from CH cohorts, suggesting these confer no unconditional selective advantage in HSCs and are AML-late acquisitions; but the counting method has known sensitivity limits, and rare-but-fit variants may be missed (≈6× larger sample at LOD ≈0.01% would be required to quantify even rare variants).
- **Stretched-exponential approximation.** The per-gene fitness spectrum is fit to a stretched exponential — an analytic convenience whose appropriateness for novel genes is empirical, not derived from first principles.
- **Constant fitness over time.** Even where intrinsic fitness is constant, slow loss/gain of epigenetic marks could change `s` over time; specific variants notably JAK2 V617F may exhibit small exponential growth rates in longitudinal data inconsistent with the constant-`s` assumption.
