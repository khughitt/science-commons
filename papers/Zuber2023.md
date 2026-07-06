---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Zuber2023
kind: paper
title: 'Multi-response Mendelian randomization: Identification of shared and distinct
  exposures for multimorbidity and multiple related disease outcomes'
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Zuber2023
tags: []
authors:
- Zuber et al.
doi: 10.1016/j.ajhg.2023.06.005
ontology_terms:
- Bayesian-model-selection
- Mendelian-randomization
- causal-inference
- multimorbidity
- pleiotropy
pmcid: PMC10357504
pmid: ''
venue: The American Journal of Human Genetics
year: 2023
dataset_usage:
- ref: dataset:gigastroke
  role: analyzed
  overlap: unknown
- ref: dataset:million-veteran-program
  role: analyzed
  overlap: unknown
- ref: dataset:uk-biobank
  role: analyzed
  overlap: unknown
- ref: dataset:zuber2023-nmr-metabolomics
  role: analyzed
  overlap: unknown
---
## One-Sentence Summary

Zuber et al. introduce MR2 (multi-response Mendelian randomization), a Bayesian sparse Gaussian copula regression method that jointly models multiple disease outcomes to identify exposures that are shared causes of multimorbidity versus exposures with distinct, disease-specific causal effects — producing more accurate causal effect estimates and greater statistical power than single-outcome MR by explicitly accounting for residual correlation between outcomes induced by unmeasured pleiotropy.

## Key Findings

1. **MR2 outperforms all alternatives on power and causal-effect estimation.** Across all simulation scenarios with pleiotropy or dependence, MR2 achieves the highest AUC for distinguishing true from false causal exposures and the lowest SSE for estimating direct causal effect sizes. Relative AUC gain over single-trait MV-MR is ~7.15% (undirected pleiotropy) and ~4.45% (directed pleiotropy). MR2 is most powerful for detecting distinct causal effects (on average 37.3% of simulated cases).

2. **Shared exposures detected with higher power than competing multi-response methods.** mSSL gives overly sparse solutions (too few shared effects), while MRCE is liberal (too many). MR2 achieves the best balance; MR-BMA performs well on dependence (scenario V) but not on pleiotropy scenarios.

3. **Application 1 — cardiometabolic exposures, five CVDs.** ApoB is identified as the single most important shared exposure for CAD, PAD, and HF (mPPI 0.99, 0.98, 0.81; jPPI 0.78), with posterior mean direct effects of 0.48 (CAD), 0.23 (PAD), and 0.12 (HF). SBP has the strongest pan-disease signal with jPPI = 0.77 for all five outcomes. Residual partial correlations (ePPI ≥ 0.78 at 5% FDR) reveal CAD-HF (0.26) and CAD-PAD (0.25) dependence not explained by any included exposure, consistent with known CAD-to-HF causal pathways and shared horizontal pleiotropy between CAD and PAD.

4. **Application 2 — lipoprotein subfractions, five CVDs.** XS.VLDL.Ps is identified as a shared exposure for PAD and HF (jPPI 0.14). L.LDL.Ps and IDL.Ps are selected as distinct exposures for CAD (mPPIs 0.41 and 0.59; direct effects 0.63 and 0.40). Residual correlations are high across all outcome pairs (ePPI ≥ 0.85 for almost all), indicating that non-lipoprotein pleiotropic pathways dominate disease-disease dependence for these molecular exposures.

5. **Theoretical result: unmeasured pleiotropy always induces residual correlation, regardless of sample overlap.** The residual correlation formula (Equation 8) shows the correlation is a positive function of the pleiotropic effect magnitude and is non-zero even when individual-level response errors are uncorrelated — a result that holds with both overlapping and non-overlapping summary-level datasets.

6. **MR2 corrects for residual confounding caused by non-genetic factors.** Social determinants of health (e.g., socioeconomic status, environment, behavior) contribute to inter-disease correlation but are not genetic and therefore cannot be "explained away" by any MR exposure selection; MR2 explicitly models this baseline correlation through R rather than forcing it to zero.

## Limitations

- **CVD-centric application scope.** Both real-data applications focus on five cardiovascular disease outcomes; generalizability to other multimorbidity clusters (e.g., metabolic-psychiatric, immune-neurological) is demonstrated only in simulation. The project's pan-disease scope spans hundreds of MeSH disease pairs.
- **No temporal or disease-onset ordering.** MR2 identifies shared genetic causal exposures but cannot resolve whether disease A temporally precedes disease B at the individual level. The ePPI residual graph is undirected; it does not encode which disease causes the other.
- **Weak instrument bias.** Weak IV bias in MV-MR can go toward any direction depending on exposure-outcome correlation structure; MR2 inherits this limitation. Extension to weak-instrument-robust estimators is flagged as future work.
- **Reverse causation between responses not modeled.** The MR2 DAG explicitly excludes direct effects between outcomes (bottom right submatrix of the adjacency matrix is constrained to zero). Disease-to-disease causal paths (e.g., CAD causing HF) are relegated to the residual correlation term, not explicitly estimated.
- **IV selection requires domain knowledge.** For application 2 the authors pre-select ApoB-associated IVs based on the hypothesis from application 1; results are conditional on this IV choice and may differ with LDL-based selection.
- **Summary-level only; no individual-level multimorbidity data.** MR2 uses cross-cohort summary data where the q outcomes may be from entirely different individuals; it cannot capture within-individual disease clustering directly.
- **Computationally intensive MCMC.** The MCMC algorithm scales with the number of IVs and outcomes; feasibility for genome-wide IV sets or large outcome panels (e.g., > 20 diseases) is not demonstrated.
- **MeSH crosswalk required for project integration.** The five CVD outcomes use clinical phenotype definitions from GIGASTROKE, MVP, and UK Biobank GWAS, not MeSH disease identifiers; bridging to the project's PubTator-derived MeSH similarity matrices requires a crosswalk.
