---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Angaroni2022
kind: paper
title: 'PMCE: efficient inference of expressive models of cancer evolution with high
  prognostic power'
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Angaroni2022
tags: []
ontology_terms:
- cancer evolution inference
- conjunctive Bayesian networks
- cross-sectional sequencing
- logical formulas
- probabilistic graphical models
- survival stratification
dataset_usage:
- ref: dataset:tcga
  role: analyzed
  overlap: unknown
---
## Key Findings

### Simulation results

- PMCE significantly outperforms HCBNs and BNs across OR and XOR topological settings at all sample sizes and noise levels.
- For AND-only topology at large n, HCBNs show comparable accuracy (expected, as HCBNs are AND-specialized). PMCE remains competitive.
- Robustness to noise is high: adding false positives/negatives at ε up to 0.20 does not substantially degrade PMCE accuracy, especially at larger sample sizes.

### TCGA pan-cancer results

- **Predictability (Φ):** Varies substantially across cancer types. Lung squamous cell carcinoma Φ ≈ 0.97 (most patients follow a single path through TP53 mutation). Glioblastoma and colorectal adenocarcinoma Φ ≈ 0.05 — highly variable trajectories.
- **Predictability vs. mutation burden:** Overall correlation between Φ and median/mean number of total mutations is weak (R² = −0.087 and R² = −0.025, respectively), indicating tumor mutational burden is not a reliable predictor of evolutionary predictability.
- **Predictability vs. number of formulas in model:** Moderate anti-correlation (R² = −0.407): tumors with more logical formula paths in the HESBCN show lower predictability, as expected.
- **Survival stratification:** 7 of 16 cancer types yield statistically significant survival separation (P < 0.05 by log-rank): brain lower-grade glioma, breast invasive carcinoma, glioblastoma multiforme, kidney renal clear cell carcinoma, skin cutaneous melanoma, uterine corpus endometrial carcinoma, and lung squamous cell carcinoma. The three risk clusters show well-separated Kaplan–Meier curves in each case.
- **Glioma example:** HESBCN identifies OR-disjunction of IDH1 vs. IDH2 mutations as a key early branching event. IDH1-mutant branch strongly associated with low risk; IDH wild-type/EGFR-mutant branch defines "glioblastoma-like" high-risk cluster. This matches known TCGA glioma subtype biology (TCGA Research Network 2015).
- **Glioblastoma example:** XOR/OR formula involving TP53 OR PIK3R1 OR PTEN ⊳ ATRX as the main evolutionary trajectory discriminator. TP53's predictability contribution is globally low (it is a pivotal early/necessary event, so its presence/absence provides little discriminating trajectory information).
- **Kidney renal clear cell carcinoma:** High number of significant covariates, consistent with low predictability. VHL mutation associated with the low-risk cluster.
- **Skin cutaneous melanoma:** Two clusters; BRAF mutations associated with bad prognosis.
- **Molecular subtype dissection (pan-glioma):** PMCE applied to merged lower-grade glioma + glioblastoma dataset (510 + 338 samples) recovers subtype-specific non-overlapping evolutionary trajectories: IDH1-mutant branch enriched for TP53, ATRX (CIMPs), IDH wild-type branch for EGFR, NF1, PTEN, RB1 — consistent with known molecular subtypes.
- **Colorectal MSS vs. MSI:** HESBCN inferred from MSS (396 samples) recovers APC, TP53, KRAS as canonical drivers; MSI (62 samples) shows broader DMD, SPTA1, FBXW7, KMT2D trajectories — again consistent with known colorectal biology.

### Temporal ordering

- The evolutionary time τ (computed as sum of Poisson waiting times along the inferred trajectory) is selected as a significant covariate in 3 of 7 significant cancer types, suggesting tumor progression timing has independent prognostic value beyond mutation identity.

## Limitations

- **Cross-sectional only:** PMCE pools data across patients at a single time point. It cannot recover within-patient temporal ordering of mutations or validate that the inferred trajectory reflects true clonal succession in any individual. The method provides a *population-level* evolutionary model — not a single-patient trajectory.
- **Binarized input:** VAF information is discarded by binarization. This loses subclonal structure (heterozygous vs. homozygous, dominant vs. minor subclone) and intra-tumor heterogeneity. Authors explicitly note that combining PMCE with single-tumor VAF-based methods (e.g., Gerstung et al. 2020) would require future work.
- **No single-cell resolution:** Cannot distinguish whether OR-connected nodes reflect true alternative evolutionary routes across clones versus intra-patient mixed clonality (two concurrent clones, each having taken a different route).
- **Driver list dependency:** Model structure depends on the input list of putative driver genes (Bailey et al. 2018). Undiscovered or excluded drivers will not appear in the inferred DAG; false driver inclusions may introduce spurious edges.
- **XOR inference difficulty:** Simulation benchmarks show XOR-topology settings are the hardest for all methods including PMCE; spurious dependencies are more likely in XOR generative models due to complex co-occurrence patterns. XOR-inferred edges should be interpreted with more caution than AND/OR edges.
- **MCMC convergence:** Structure learning via MCMC provides no convergence guarantee for reaching the global MAP. Authors flag this as a known limitation and use multiple random restarts (local restart move) and BIC/AIC regularization.
- **Survival stratification scope:** Only 7 of 16 TCGA cancer types showed significant survival separation; for the remaining 9 no prognostic signal emerged from the evolutionary model covariates. Not all cancer types have evolvability-linked prognosis detectable with this approach.
- **No clonal dynamics / drift:** The framework is fully selection-based. Neutral evolution and genetic drift are not modeled — events that accumulate by drift would appear as dependencies if correlated with selected drivers.
