---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Legrand2023
kind: paper
title: Time-resolved, integrated analysis of clonally evolving genomes
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Legrand2023
tags: []
ontology_terms:
- allele frequency
- clonal evolution
- dNdS selection
- evolutionary parameters
- expansion dynamics
- glioblastoma
- marbled crayfish
- mutation accumulation
- mutational signatures
- tumor cell survival
dataset_usage:
- ref: dataset:egas00001003184
  role: analyzed
  overlap: unknown
- ref: dataset:prjna356499
  role: analyzed
  overlap: unknown
---
## Key Findings

### *Procambarus virginalis* — mutation rate and speciation timing
- Mutation rate of *P. virginalis*: µ = [3.51 × 10^−8; 1.17 × 10^−4] /nt/y (lower bound = strictly filtered SNVs; upper bound = relaxed callable-sites denominator). The range overlaps arthropod germline rates and human somatic healthy-cell rates.
- Four distinct evolutionary phases detected in the M(1/f) curve; mutation rate varied significantly between phases while the dNdS ratio remained ~1 throughout, indicating **neutral evolution** (absence of positive or purifying selection) across phases.
- Bayesian coalescent TMRCA: **1988.0 (95% CI: [1986.1; 1989.8])** — a remarkably recent origin, consistent with first documented records of the species in 1995.
- Coalescent tree topology: Animals 1, 34, 35 (lab lineage) and German wild populations cluster together; Madagascar populations form a separate clade, with the Madagascan founding animal traced to a German pet shop (Petshop 2 nested within the Madagascar clade). This confirms a **single anthropogenic transport-and-release origin** for the global *P. virginalis* population.
- Clock-like (SBS1 + SBS5) signatures dominate the early mutation accumulation phases; their temporal structure is concordant with the coalescent date estimate.

### Glioblastoma — evolutionary parameter variation
- M(1/f) segmentation reveals **4–5 distinct evolutionary phases per GBM sample**; mutation rate per division decreased from phase 2 to phase 4 in most primary tumors, suggesting slowing clonal expansion or increasing cell number.
- **dNdS dynamics:** Most tumors showed neutral selection for most of the accumulation trajectory. Eleven primary tumor samples exhibited **negative selection** in early (low-frequency) intervals, consistent with purifying selection during initial low-mutational-load growth. Two primary samples showed evidence of positive selection. Among recurrent tumors: 7/9 showed negative selection in early intervals; 2/9 showed brief positive selection; **no recurrent sample showed sustained positive selection**, challenging the assumption that recurrence universally reflects strong positive clonal selection.
- **Expansion profiles (ωγN):** Unsupervised k-means clustering of 42 primary-tumor expansion curves identifies four trajectory subtypes: (A) Convex, (B) Peak, (C) Increase, (D) Paused Start. These may correspond to distinct growth or microenvironmental regimes, although clinical associations remain to be established.
- **Tumor cell survival ratio (γ_R/γ_P):** Across n = 20 samples with time-to-recurrence data, the survival ratio of recurrent vs. primary tumor cells was always > 1 (median lower bound 27.8 [IQR 17.4–54.0]; median upper bound 97.5 [IQR 60.9–189.0]), indicating that **tumor cells survive better at the start of recurrence than at the end of primary tumor growth** — consistent with post-surgical microenvironmental permissiveness (astrocyte injury, immune modulation) for tumor regrowth.
- γ_R/γ_P ratio was negatively correlated with time to recurrence (p_adj = 1.258 × 10^−3 and 8.649 × 10^−4 for linear and log-linear fits, R² = 0.44 and 0.61 respectively): higher survival ratio → shorter time to recurrence, providing a genomics-derived predictor of clinical tempo.

## Limitations

- The M(1/f) framework assumes ploidy is constant within a phase when computing allele frequency increments; the authors acknowledge that incorporating copy-number variation could improve accuracy, especially for tumor samples with widespread aneuploidy.
- dNdS calculation uses a non-bias-corrected quotient method (not dNdScv) because dNdScv could not be applied to the low-mutation-count triploid *P. virginalis* data; the longitudinal dNdS estimates may be noisier than bias-corrected alternatives.
- Mutational signature assignment in *P. virginalis* uses human COSMIC signatures as a proxy (arthropod-specific signatures are not available); the assumption that mutagenic mechanisms are conserved is biologically plausible but unverified in this system.
- Phase segmentation uses automated breakpoint detection (R `segmented`); the biological meaning of individual phase boundaries is inferred but not independently validated (e.g., via concurrent phenotypic or environmental data for crayfish, or clonal architecture data for GBM).
- The tumor cell survival ratio γ_R/γ_P requires prior assumptions about primary tumor age (2–7 years before diagnosis from Korber et al. 2019); results are sensitive to this prior.
- GBM expansion-profile clustering (k-means, 4 groups) is not yet linked to clinical subtypes, molecular markers, or treatment history — the biological interpretation of the four trajectory shapes remains speculative.
- The framework is applied to bulk WGS data; subclonal resolution is limited by allele frequency granularity. Integration with single-cell approaches would sharpen per-clone evolutionary parameter estimates.
