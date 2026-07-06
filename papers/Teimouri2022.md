---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Teimouri2022
kind: paper
title: Can we understand the mechanisms of tumor formation by analyzing dynamics of cancer initiation?
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Teimouri2022
tags: []
ontology_terms:
- Moran process
- cancer initiation
- first-passage probability
- fitness parameter
- fixation probability
- fixation time
- free-energy landscape
- mutation order
- stochastic mapping
- two-hit hypothesis
---
## Key Findings

### Surprising anti-correlation: risk vs. initiation time

Theoretical calculations and analysis of data from 28 cancer types find no correlation between cancer lifetime risk and mean cancer initiation time (Spearman coefficient ~0.2, far from the expected −1). Higher-lifetime-risk cancers do not form faster — the two quantities are governed by independent dynamical quantities (fixation probability vs. conditional fixation time), analogous to the thermodynamic vs. kinetic independence of chemical reaction rates from equilibrium constants.

### Neutral mutations are slowest to fix

Counterintuitively, neutral mutations (r = 1) produce the slowest cancer initiation dynamics among all fitness values. For r = 1 the system reduces to an unbiased random walk, which is inherently slow. Both advantageous (r > 1) and disadvantageous (r < 1) mutations produce faster conditional fixation dynamics — for r < 1, rare fixation events must happen quickly because at each intermediate step the system can reverse direction, making slow approaches impossible (those trajectories extinguish rather than fix).

### Mutation order matters for two-hit cancers

For cancers requiring sequential mutations A then B (sequence AB) vs. B then A (sequence BA):
- If r_A > r_B, sequence AB is more probable (Δ_p > 1) but also has a longer mean initiation time (Δ_T > 1, i.e., T_AB > T_BA).
- The anti-correlation between probability and speed of fixation for the two sequences is explained by the effective free-energy landscape: the more probable sequence (AB when r_A > r_B) has a higher first barrier (slower kinetics), while the less probable sequence (BA) has lower barriers throughout.
- The overall fixation probability for two mutations is determined entirely by the properties of the first mutation in the sequence (eq. 5: Π_n = (1 − 1/r₁^n)/(1 − 1/r₁^N)), not by the second. This makes mutation order a key determinant of cancer type identity.

### Free-energy landscape analogy

The cancer initiation process can be mapped to motion along an effective one-dimensional free-energy coordinate with barriers. Barriers correspond to mean fixation times on each branch; valleys correspond to irreversible transition points. This provides a physically interpretable picture: the rate-limiting step is the highest barrier, and the same barrier height governs both the relative speed of competing mutational sequences and the apparent paradox that more probable paths are slower.

### Future directions identified

Authors explicitly call for extension to: (1) parallel (branched) mutation models where multiple mutations accumulate simultaneously; (2) spatial tissue structure models; (3) coupling to mechanical views of cancer dynamics.

## Limitations

- **Single-tissue, single-clone model:** The model assumes a fixed-size, well-mixed population. Spatial tissue structure (gradients, stem-cell niches, crypts) is explicitly flagged as a future direction but not addressed. Real tissues are not well-mixed, and spatial effects are known to alter fixation dynamics substantially.
- **Sequential (not parallel) mutation model:** The two-mutation extension still assumes strict sequentiality — the second mutation can only appear after the first has fully fixed. The authors note this is unrealistic (multiple mutations often accumulate in parallel) and flag branched models as future work.
- **Perspective genre — no new data:** This is a conceptual Perspective article, not a primary research paper. The numerical results on 28 cancer types are drawn from ref. [12] (Teimouri et al. 2019 Sci. Rep.); the two-mutation sequential model results are from ref. [13] (Teimouri & Kolomeisky 2021 Phys. Biol.). The present paper synthesizes and interprets those results but does not add new computations.
- **Cancer initiation defined as full fixation:** Equating cancer onset with complete fixation of mutated cells (n = N) is a strong simplification. In practice, a tumor can become clinically relevant long before all N stem cells are mutated. Partial fixation thresholds are not considered.
- **Mutation rate treated as fixed and uniform:** μ is taken as a universal constant (~10⁻⁸–10⁻¹⁰) across all cancers and all mutation types. In practice, mutation rates vary substantially by cancer type, genomic context, and DNA repair proficiency — a key variable the model elides.
- **No microenvironmental or immune terms:** The model is purely cell-autonomous. Selection coefficients r are not conditioned on immune surveillance, stromal context, or metabolic state — all of which are known to affect clonal dynamics.
- **Fitness parameters are not independently calibrated per cancer type:** The framework provides a language for interpreting cancer-type differences in risk and initiation time, but the individual fitness values are inferred from epidemiological data (ref. [12]), not from experimental growth assays or genomic data.
