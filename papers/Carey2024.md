---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Carey2024
type: paper
title: Principled distillation of UK Biobank phenotype data reveals underlying structure in human variation
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Carey2024
tags: []
authors:
- Carey et al.
datasets:
- dataset:add-health
- dataset:uk-biobank
doi: 10.1038/s41562-024-01909-5
ontology_terms:
- disease-classification
- factor-analysis
- latent-construct
- phenome
pmcid: ''
pmid: ''
venue: Nature Human Behaviour
year: 2024
---
## One-Sentence Summary

A multistage confirmatory factor analysis of 505 UK Biobank phenotypes (diagnoses, assessments, survey items) from 361,144 individuals distills the human phenome into 35 orthogonal latent factors that recapitulate known disease groupings, disentangle socioeconomic subdomains, and yield greater heritability and GWAS power than any individual component item.

## Key Findings

1. **35 orthogonal latent factors span the UKB phenome.** Exploratory then confirmatory factor analysis (CFA) of 505 items drawn from 72 UKB questionnaires and assessments identifies 35 factors explaining 18.5% of total variance (RMSEA = 0.015; CFI = 0.883 on the modelling subgroup; holdout RMSEA = 0.028, SRMR = 0.076). Factors load on an average of 32.49 items (range 3–84). An equivalent 36-component PCA explains 21.6% of variance, but factors allocate items to constructs more interpretably.

2. **Factors recover known medical disease groupings without expert curation.** Factor 12 groups hypertension correlates (self-report, blood pressure, BMI, high cholesterol, diuretics, calcium-channel blockers). Factor 16 groups coronary artery disease indicators (self-report angina/MI, ICD-10 codes, aspirin/beta-blockers/statins). Factor 11 groups asthma diagnosis and related medications. These emerge purely from phenotypic correlation structure, without manual annotation.

3. **SES decomposes into three distinct factors with different genetic and health profiles.** Factors 5 (occupation/work environment), 10 (educational attainment and cognitive performance), and 15 (social/economic stability — household income, home ownership, loneliness, never divorced) capture separable SES subdomains. Factor 10 shares the highest genetic correlation with previous EA GWAS (r_g = 0.93); Factor 15 is the most prospectively protective against mortality (HR = 0.75 [0.74–0.76]) and the most strongly protective against mental health hospitalisation.

4. **Factor scores are more heritable than constituent items.** All but one of the 35 factors show significant SNP heritability after multiple testing correction (mean h²_g = 0.10 [0.09]; 2-sample t-test P = 0.002 vs. mean item h²_g = 0.05 [0.07]). Factor scores identify 548 genome-wide significant loci across 2,329 total, of which 91.5% are significant in ≥ 3 of the 5 top-loading items, indicating recovery of shared genetic signal. Factor 23 (physical activity) alone identifies 34 significant loci — 25 not previously identified in GWAS of self-reported physical activity items — with heritability enrichment in CNS cell types (P = 2.52 × 10⁻⁵).

5. **Factor 20 (severe, life-threatening illness) has the highest prospective mortality hazard.** Cox-proportional hazards regression across all 35 factors identifies Factor 20 (items including number of surgeries and 'diagnosis with a life-threatening illness') as the strongest mortality predictor: HR = 1.62 [1.59–1.64]. Factor 9 (trauma) also shows HR = 1.36 [1.31–1.41], with uniquely broad phenotypic correlations spanning all ICD categories including circulatory, digestive, respiratory, and endocrine diseases, and strong CRP association (β = 0.11, p = 0.004).

6. **Factor 23 (physical activity) outperforms individual items and sum-scores for health prediction.** Factor 23 PGS explains R² = 3.4% for cardiovascular disease in Add Health vs. pseudo-R² = 1.4% for hours-of-activity alone; incremental R² for mortality prediction is 1.27 × 10⁻³ for the factor vs. 6.75 × 10⁻¹⁰–1.12 × 10⁻³ for individual items. LCV analysis supports a partially causal effect of recent strenuous sports participation on current self-rated health (LCV causality proportion = 0.37, P = 5 × 10⁻³).

7. **Factor genetic results generalise to an independent, non-UKB sample.** Polygenic scores for SES factors, trauma (Factor 9), and physical activity (Factor 23) built from UKB GWAS summary statistics outperform item-level PGS in predicting relevant outcomes (education, income, health behaviours, psychiatric diagnoses) in the Add Health cohort (N ≈ 4,700–4,800 per trait), demonstrating cross-cohort portability.

## Limitations

- **European-ancestry only.** All factor structures estimated in predominantly European-ancestry UKB participants. Generalisability to other ancestries untested; the authors flag this as a key limitation.
- **UKB participation bias.** UKB participants are healthier and more educated than the UK general population; 45.7% of the core (low-missingness) group report college/university vs. 30.7% of the non-core group. Factor structure may not represent the full SES or disease spectrum.
- **Orthogonality is imposed, not inferred.** Factors are constrained to be uncorrelated as a computational necessity (to reduce parameters in CFA). This is an artefact of the modelling framework, not a claim that the underlying constructs are truly independent. Interpretation of factor independence must account for this.
- **18.5% variance explained is low.** This is expected for a sparse latent model applied to a heterogeneous item set, but it means the factors capture a minority of the phenotypic landscape. The remaining variance is either noise, item-specific, or structured beyond the 35-factor model.
- **Factor content is consensus-labelled, not biologically validated.** Factor descriptions (e.g., "coronary artery disease," "trauma") are arrived at by expert consensus of the authorship team, not by formal external molecular validation. A factor labelled "asthma" could be capturing shared healthcare-seeking behaviour rather than shared airway biology.
- **Missingness handling is imperfect.** Pairwise deletion and CART-based imputation are used; neither is guaranteed unbiased under not-missing-at-random (NMAR) patterns, which are plausible for sensitive phenotypes (mental health, substance use, income).
