---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Jiang2025
type: paper
title: 'UKB-MDRMF: a multi-disease risk and multimorbidity framework based on UK Biobank data'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Jiang2025
tags: []
authors:
- Jiang et al.
datasets:
- dataset:all-of-us
- dataset:uk-biobank
doi: 10.1038/s41467-025-58724-3
ontology_terms:
- disease-risk-assessment
- joint-disease-prediction
- multimorbidity
venue: Nature Communications
year: 2025
---
## One-Sentence Summary

UKB-MDRMF is a joint multi-disease prediction and survival risk framework trained on 1,560 Phecode-based disease outcomes across six multimodal data categories from UK Biobank, demonstrating that simultaneously modeling disease comorbidities yields consistently higher predictive performance than single-disease approaches and produces data-driven multimorbidity clusters from neural network output embeddings.

## Key Findings

1. **Joint modeling outperforms single-disease models across all 21 disease types.** FCNN (disease prediction) and DeepSurv (risk assessment) trained jointly over all Phecodes significantly outperformed individually trained single-disease models (Wilcoxon p < 0.05 for all types). Joint prediction C-indices are consistently higher across 21 disease categories; improvement is statistically significant in every category (Fig. 2f).

2. **FCNN achieves median AUC > 0.70 after adding measurement data.** Stepwise addition of feature categories (basic → lifestyle → measurement → environment → genetic → imaging) shows the largest AUC gains from lifestyle and measurement. Pregnancy-related diseases reach median AUC ~0.95; genital diseases ~0.80. The overall median AUC exceeds 0.70 once measurement data is added.

3. **UKB-MDRMF outperforms domain-specific fine-tuned models on most diseases.** Table 1 comparison against published best-in-class approaches: CVD AUC 0.78 vs 0.73 (Mamouei et al. 2023), endometriosis AUC 0.85 vs 0.80 (Blass et al. 2022), atrial fibrillation AUC 0.78 vs 0.72 (Papadopoulou et al. 2022). Risk assessment C-index: 87.5% of diseases beat the You et al. 2023 40-disease model; CHD C-index 0.84 vs 0.83, T2D 0.94 vs 0.84, stroke 0.86 vs 0.71 (Sun et al. 2021). CAD (Petrazzini et al. 2022) was one case where the article's AUC (0.88) exceeded UKB-MDRMF (0.76).

4. **Six primary multimorbidity clusters emerge from neural network output embeddings.** t-SNE projection of FCNN and DeepSurv final layer features (Fig. 5a) reveals clustering not aligned with ICD-10 chapters. Cluster examples: (i) urogenital cluster mixing genital Phecodes with bladder neck obstruction and testicular endocrine diseases, (ii) mental illness cluster showing a dense comorbidity graph — anxiety disorder strongly connected to mood disorders, major depressive disorder, and bipolar. Cluster assignments are model-derived, not anatomy-derived.

5. **Age-stratified risk profiles show diverging trajectories across disease categories.** DeepSurv hazard extraction from 60 to 80 years reveals: digestive and circulatory disease risk accelerates with age; reproductive disease risk plateaus. This is depicted in Fig. 5c as risk profiles across 21 disease types at five-year intervals.

6. **SHAP analysis identifies cross-disease risk factor signatures.** Top 30 important variables across 21 disease types (Fig. 4a): basic information dominates pregnancy, vessel, and genital prediction; lifestyle (including mental health assessment "Bipolar and major depression status") and imaging variables (Heart MRI, carotid ultrasound, Brain MRI) are highly informative. Absence of bipolar/depression status reduces incidence across all diseases; waist circumference, BMI, and cholesterol increase risk broadly (Fig. 4c–d).

7. **All-of-Us external validation confirms framework generalizability.** Retraining FCNN/DeepSurv on All of Us data (diverse U.S. cohort) while preserving the UKB-MDRMF variable mapping shows consistent improvement from adding new data categories, with reproductive diseases again achieving highest AUC and C-index. Absolute performance is lower than in UKB, attributed to higher baseline accuracy from basic information in All of Us.

## Limitations

- **UK Biobank biases.** Volunteer cohort with documented socioeconomic and ethnic selection; not population-representative. Replication in All of Us improves this somewhat but both are distinct from the full global disease landscape.
- **Pre-baseline disease exclusion may hide comorbidity signal.** Excluding diseases diagnosed before enrollment eliminates historical comorbidity patterns that are clinically relevant (e.g., childhood-onset disorders as risk factors for adult diseases).
- **Phecode vocabulary.** 1,560 Phecodes are coarser than MeSH disease granularity; some diseases that are distinct in PubTator may be merged in Phecodes, and some Phecodes are broader than any single molecular entity. Cross-axis comparison with this project requires a non-trivial ontology crosswalk.
- **Multimorbidity clusters are model-derived, not validated against molecular or mechanistic ground truth.** The six neural network clusters are data summaries of phenotypic co-occurrence in UKB; they do not carry causal or molecular interpretation without additional validation.
- **No competing risks in survival model.** DeepSurv does not explicitly model competing risks, which can inflate hazard estimates for diseases where death from another cause is common in the older UK Biobank age range.
- **Temporal alignment excludes primary care follow-up from around 2016 onward.** Long-term outcomes post-2016 are not fully captured.
