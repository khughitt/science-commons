---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Williams2016
kind: paper
title: Identification of neutral tumor evolution across cancer types
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Williams2016
tags: []
ontology_terms:
- 1/f VAF distribution
- Big Bang model
- bulk sequencing
- clonal selection
- intratumour heterogeneity
- mutation rate
- mutational timeline
- neutral evolution
- pan-cancer analysis
- power-law distribution
- subclonal architecture
- variant allele frequency
dataset_usage:
- ref: dataset:tcga
  role: analyzed
  overlap: unknown
- ref: dataset:williams2016-cohorts
  role: analyzed
  overlap: unknown
---
## Key Findings

### 1. The 1/f Power-Law Fits Broadly Across Cancer Types

- **CRC (WES, n = 108):** 38/108 (35.1%) neutral. CIN: 31/82 (37.8%); MSI: 3/19 (15.7%). MSI fraction is lower, consistent with high mutation burden creating more passenger driver opportunities.
- **Gastric cancer (WGS, n = 78):** 60/78 (76.9%) neutral. MSS: 57/68 (83.8%); MSI: 3/10 (30%). Higher neutral fraction than WES cohorts, consistent with higher mutation counts at greater sequencing depth enabling more sensitive fitting.
- **Pan-cancer TCGA (WES, n = 819):** 259/819 (31.6%) neutral. Cancer types showing predominantly neutral dynamics: stomach, lung, bladder, cervical, colon. Cancer types showing predominantly non-neutral dynamics: renal, melanoma, pancreatic, thyroid, glioblastoma.

### 2. Mutation-Rate Estimation from Single Biopsies

Under neutral evolution, the slope of M(f) directly estimates μ_e (the effective mutation rate per cell division, scaled by effective division efficiency β). Key measured values:

| Cancer Type / Subtype | Median μ_e | Notes |
|---|---|---|
| CRC CIN (WES) | 2.31 × 10⁻⁷ | — |
| CRC multi-region cohort | 2.07 × 10⁻⁷ | — |
| CRC MSI (WES) | 3.65 × 10⁻⁶ | 15-fold higher; mismatch repair deficiency |
| Gastric MSS (WGS) | 7.82 × 10⁻⁷ | — |
| Gastric MSI (WGS) | 3.30 × 10⁻⁶ | 4-fold higher |
| Lung adenocarcinoma (WES) | 6.79 × 10⁻⁷ | Highest among TCGA types |
| Lung squamous (WES) | 5.61 × 10⁻⁷ | — |
| Low-grade glioma (WES) | 9.22 × 10⁻⁸ | Lowest |
| Prostate (WES) | 1.04 × 10⁻⁷ | — |

C>T transitions dominated single-base substitution rates; C>A was specifically elevated in lung cancer (tobacco smoke signature).

### 3. Mutational Timelines From Single-Biopsy Data

Equation N(t) = 1/(πf) converts allele frequency into estimated tumour size at the time of mutation. Applied to individual CRC cases: classical drivers (APC, KRAS, TP53) located in the first malignant cell (clonal), consistent with multi-region sampling evidence. Several recurrent putative drivers placed during the neutral growth phase, suggesting context-dependent (not universal) driver status.

### 4. Neutral vs. Non-Neutral Distributions Are Biologically Interpretable

The non-neutral cancer types identified (renal, melanoma, glioblastoma) align with independent biological evidence of strong ongoing selection: convergent evolution across tumour regions (renal, Gerlinger et al. 2012) but not in lung (a predominantly neutral type). Non-neutral dynamics are predicted by subclone clusters producing an overrepresentation of mutations at higher frequency than the 1/f null.

### 5. Under Neutrality, All ITH Is Passenger-Dominated

The model's central interpretation: in neutral tumours, all genomic heterogeneity is generated stochastically without differential fitness effect. Extensive ITH is the expected outcome of neutral growth, not evidence of selection. The same tumour may have acquired putative driver mutations during neutral growth that are, in context, functionally inert.

## Limitations

- **Model assumes exponential growth.** The derivation requires N(t) = e^(λβt); logistic, contact-inhibited, or spatially constrained growth dynamics will distort M(f). Most solid tumour growth is not purely exponential, especially at large sizes or in spatially structured architectures.

- **Single-region bulk sequencing only.** The model is blind to spatial ITH patterns; variants undetected due to spatial isolation will not contribute to the VAF spectrum. Multi-region studies can reveal selection patterns invisible to single-biopsy analysis.

- **Effective division fraction β is unobservable.** μ_e = μ/β; without independent β estimates, the true per-base mutation rate μ cannot be recovered. A 1-in-100 effective division fraction would make true μ 100-fold lower than μ_e.

- **Low VAF variants inaccessible at standard depth.** Standard WES (~100×) cannot reliably call variants below ~10% VAF; very small subclones are invisible. This means the model operates on the visible tail of the VAF spectrum, potentially missing recent selection events or rare neutral subclones.

- **R² threshold is conservative and type-specific.** Tumours with few mutations (low mutation burden or low depth) are more likely to be mis-called as non-neutral simply from statistical noise on the fit; the WGS gastric cancer cohort shows higher neutral fraction partly due to higher depth and mutation counts.

- **Cannot distinguish mechanisms of non-neutrality.** Deviation from 1/f indicates departure from neutral dynamics but does not specify whether the cause is subclonal selection, spatial niche structure, variable mutation rate across subclones, or mixture of multiple independently initiated expansions.

- **Copy number alterations handled by exclusion, not modelling.** CNA regions are excluded from the fit; the model does not integrate CNAs as evolutionary events. Aneuploidy-driven selection would be missed.

- **Applicability to haematological malignancies unclear.** All 14 cancer types are solid tumours; the model's assumptions (single-origin clonal expansion, bulk biopsy) may not translate to blood cancers with different spatial and population dynamics.

- **MSI and MSS tumours behave differently.** MSI tumours show lower neutral fraction across all cancer types tested; the 1/f model may be less appropriate for hypermutated tumours where the sheer rate of mutation increases the probability of passenger mutations acquiring fitness effects.
