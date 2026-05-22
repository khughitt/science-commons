---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Wang2024MPN
type: paper
title: 'Order-of-Mutation Effects on Cancer Progression: Models for Myeloproliferative Neoplasm'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Wang2024MPN
tags: []
datasets: []
ontology_terms:
- JAK2 V617F
- Moran process
- TET2
- bistability
- clonal evolution
- epigenetic memory
- gene expression regulation
- mutation order effects
- myeloproliferative neoplasm
- non-additivity
- non-commutativity
---
## Key Findings

1. **Bistability is a sufficient mechanism for mutation-order effects on gene expression.** A nonlinear autoregulatory term in an ODE for gene expression produces bistability; mutations that shift the effective production rate λ across bifurcation thresholds in different sequences drive the system to different attractors. This is non-additive and non-commutative by construction, without requiring any mutation to directly "sense" the other's presence.

2. **Epigenetic inheritance is the required memory mechanism.** For bistability to produce order effects across cell lineages, the expression state must be transmitted from mother to daughter cells. The authors justify this via known mechanisms of methylation pattern copying during DNA replication (Probst et al. 2009; Vandiver et al. 2016).

3. **Gene expression observations (1)–(4) are explained by four simple ODE variants** differing only in the sign/magnitude of JAK2 and TET2 contributions to λ. No mechanistically distinct model is required for each observation type.

4. **Observation (3) requires a hidden intermediate gene (Y), tentatively identified as E2F1 and/or PRMT5.** The model predicts that knockdown of PRMT5 or E2F1 after a JAK2 mutation should decrease expression of AURKB, MCM2, MCM4, MCM5, and TK1 — a testable prediction.

5. **Three distinct Moran process mechanisms can all reproduce cell-population and age-at-diagnosis order effects.** Differential mutation rates (Mechanism B) is the authors' preferred explanation; it requires the smallest sample size (~12) to distinguish JAK2-first from TET2-first patients statistically.

6. **The Markov chain model (Appendix B) shows that apparent order effects can arise even when the long-run equilibrium is the same for JT and TJ patients**, because the relaxation time between expression wells (~10^5 τ ~ month) is comparable to or longer than a human lifespan. Mutation order shapes which well is occupied at clinically relevant timescales, not the ultimate thermodynamic steady state.

7. **Order-of-mutation effects generalize beyond MPN.** The authors cite adrenocortical carcinomas (Ras before p53 → malignant/metastatic; p53 before Ras → benign) and other cancers (Levine et al. 2019; Turajlic et al. 2018; Caravagna et al. 2018) as analogous contexts where the same bistability framework should apply.

## Limitations

- **Single-gene ODE models are phenomenological.** The f(x) autoregulatory function (Eq. 3) is chosen for analytical convenience, not inferred from JAK2/TET2 expression data. The bistability threshold values (λ ≈ 1.6 and 2.4) are not fitted to any clinical dataset; they are illustrative.
- **No quantitative fit to Ortmann et al. data.** The models reproduce the *qualitative* direction of observations (1)–(6) but are not fitted to measured gene expression levels, cell percentages, or ages at diagnosis. Quantitative agreement is assumed rather than demonstrated.
- **Moran process ignores spatial structure.** Hematopoietic stem cell niches have spatial organization; the well-mixed Moran model cannot capture niche competition or positional effects on clonal dynamics.
- **Intermediate gene Y only partially verified.** Mechanisms (i)–(iii) in the proposed JAK2 → PRMT5 → E2F1 → target gene pathway have experimental support, but mechanisms (iv) (JAK2 directly weakly down-regulates targets) and (v) (TET2 down-regulates E2F1 directly or via PRMT5) are model predictions without direct experimental verification in MPN. The authors explicitly flag (iv) and (v) as assumptions.
- **Markov chain model (Appendix B) uses heuristic parameter choices.** The Gaussian rate functions and their parameters (μ₁ = 1000, μ₂ = 2000, σ values) are chosen to reproduce qualitative expression distributions, not inferred from single-cell data.
- **Order inference from bulk sequencing is noisy.** The paper's clinical motivation rests on Ortmann et al.'s inferred mutation orders from cell population composition; patients with ambiguous cell compositions (JAK2-only, TET2-only, and double-mutant cells simultaneously) were excluded. This selection may bias the observations.
- **Model does not incorporate immune microenvironment.** The authors note in the Discussion that immune interactions could further shape both gene expression and clonal dynamics via bistability-generating mechanisms, but these are deferred to future work.
- **No longitudinal validation.** All models are validated against cross-sectional population-level observations. Longitudinal single-patient data would be needed to confirm bistable switching and clonal succession dynamics predicted by the Moran process.
