---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Placido2024
type: paper
title: 'Disease Trajectories from Healthcare Data: Methodologies, Key Results, and Future Perspectives'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Placido2024
tags: []
authors:
- Jørgensen et al. (Placido, Brunak group)
datasets: []
doi: 10.1146/annurev-biodatasci-110123-041001
ontology_terms:
- ICD-10
- disease-trajectory
- multimorbidity
- temporal-disease-association
venue: Annual Review of Biomedical Data Science
year: 2024
---
## One-Sentence Summary

A comprehensive review of European disease trajectory research covering methodologies for extracting directional disease-sequence associations from EHR data, key results across risk identification, disease progression, clustering, and prediction applications, and future challenges around data quality, cross-country validation, and causal inference.

## Key Findings

1. **Directionality adds independent signal.** Temporal order of diagnoses outperforms diagnosis-as-bag-of-words for predicting mortality in ICU (ref 19) and pancreatic cancer onset 3–60 months ahead (ref 20). The direction between a disease pair can reverse by sex (ref 18), so sex-stratified trajectories are non-redundant.

2. **Sex differences are pervasive.** Women receive first hospital diagnoses later than men on average (more disease-free years or delayed ascertainment). Cardiovascular disease risk increases more in women than men when diabetes, hypertension, and metabolic disorders are present (ref 52). Some disease pairs have opposite temporal order for men vs women (ref 18). One study identified 199 male and 164 female multimorbidity clusters with different leading diseases (ref 53).

3. **Clustering reveals multimorbidity archetypes.** From 5.1 M Austrian patients, 132 multimorbidity clusters were identified; high-mortality clusters comprised hypertensive + cerebrovascular + malignant disease combinations (ref 52). Depression trajectories produced three main clusters: cardiometabolic, chronic inflammatory, and tobacco abuse (ref 54). Gout and COPD are key early diagnosis nodes whose timely diagnosis reduces unfavorable downstream trajectories in Danish data (ref 16).

4. **Underdiagnosis/misdiagnosis detection.** A subset of COPD patients with trajectories dissimilar to common COPD patterns had higher post-COPD mortality; lab values resembled lung cancer patients, suggesting misdiagnosed lung cancer (ref 88). This is a direct application of trajectory-deviation as a diagnostic flag.

5. **Molecular-level integration is nascent.** Genetic interpretation accounts for ~46% of comorbidities in selected large cohorts; disease interaction networks inferred from differential gene-expression similarity capture comorbidities not well-explained by genetics alone (ref 73). Inverse comorbidities (CNS disorders vs solid cancers) show mirrored transcriptomic up/downregulation, but these patterns cannot easily be extracted from medical records because low co-occurrence may reflect coding practices, not true biological antagonism (ref 74–76).

6. **Cross-country generalizability is limited.** Trajectories often replicate within national summary data but diverge across systems due to differences in disease frequency, coding practice, and national ICD amendments. The DL pancreatic cancer model trained on Danish data lost accuracy in VHA (US), partly due to US overcoding relative to Denmark (ref 20, 40, 56, 62).

7. **Primary care and prescription data are underused.** Most studies rely on secondary care diagnoses. Primary care data captures earlier prodromal symptoms before formal diagnosis; prescription trajectories can reveal drug-shift patterns and initial treatment failures (ref 13). Clinical narratives contain ICD-18 symptom codes ("Symptoms, signs and abnormal laboratory findings") largely absent from structured EHR (ref 35, 37).

## Limitations

- **Causal inference gap.** Trajectories establish temporal precedence, not causation. Directionality is confounded by disease prevalence (common diseases appear "early" by chance — explicitly noted as the hypertension/heart-disease example, ref 27) and by coding practices that may record complications after the primary diagnosis.
- **Secondary care bias.** The majority of studies use hospital-admission diagnoses, which capture severe phenotypes. Prodromal or mild disease and primary-care-managed conditions are systematically underrepresented.
- **Cross-country replication failure modes.** National ICD amendments and different coding cultures limit generalizability. Trajectories that replicate within public summary data from the same country do not constitute independent validation.
- **Inverse comorbidities are methodologically fragile.** Low co-occurrence could reflect true biological antagonism, coding practice (conditions treated before co-occurrence is captured), or limited follow-up windows. The review explicitly flags this.
- **ML models lack interpretability at the trajectory level.** DL models learn temporal patterns but do not directly output disease trajectories; their predictions are less interpretable than rule-based trajectory summaries (Figure 4 complexity/interpretability tradeoff).
- **Ontology drift.** ICD-10 code meanings change over time (e.g., E11 redefined in 2014); long follow-up studies spanning ICD revisions carry coding-change confounds.
