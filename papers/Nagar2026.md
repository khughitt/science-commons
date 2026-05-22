---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Nagar2026
type: paper
title: Patterns in Individual Blood Count Trajectories in the UK Biobank Characterise Disease-Specific Signatures and Anticipate Pan-Cancer Risk
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Nagar2026
tags: []
arxiv: '2604.11824'
authors:
- Nagar et al.
datasets:
- dataset:uk-biobank
doi: 10.48550/arXiv.2604.11824
ontology_terms:
- complete-blood-count
- haematological-biomarker
- immune-index
- longitudinal-trajectory
venue: arXiv preprint (q-bio.QM)
year: 2026
---
## One-Sentence Summary

Longitudinal analysis of routine CBC data from 19,367 UK Biobank participants using linear mixed-effects models and a composite immune score reveals disease-specific haematological trajectories that diverge years before cancer diagnosis and differ systematically across cancer, cardiovascular, and infection disease classes.

## Key Findings

1. **Pan-disease haematological signatures are real and pre-diagnostic.** Nearly all CBC analytes differed significantly (p < 0.05, Bonferroni-corrected Mann-Whitney U) across disease groups at baseline: 15-16 markers distinguished each pairwise comparison (Cancer vs Rest, CVD vs Rest, Infection vs Rest). Within-group longitudinal Friedman tests identified 19 significant analyte-timepoint changes in cancer, 17 in CVD, and 11 in infection groups.

2. **MCH is a cross-disease marker with consistently downward trajectory.** Mean corpuscular haemoglobin (MCH) declined over time in both cancer and CVD groups, with non-overlapping IQR bands versus Rest in normalised trajectory plots. MCH was significant in LME models for both cancer (strong interaction) and CVD (male-predominant), consistent with prior literature linking reduced MCH to poor survival outcomes.

3. **Blood cancers vs solid tumours have distinct signatures.** Blood cancers showed lymphocyte-dominated dynamics (lymphocyte count had the highest LME interaction significance), alongside erythroid suppression (haemoglobin, haematocrit, RBC significantly lower than both Rest and solid tumours). Solid tumours showed combined erythroid and immune shifts (RBC, haemoglobin strongest; also lymphocyte and monocyte percentages, eosinophil count). These profiles separated with non-overlapping IQR bands in normalised plots.

4. **Myeloma is included as a named haematological malignancy subgroup.** Blood cancer was subdivided into: diffuse (non-follicular) lymphoma, **multiple myeloma and plasma cell neoplasms**, lymphoid leukaemia, myeloid leukaemia, and follicular lymphoma. LME models identified sex- and disease-specific analyte interactions for each subtype. The lymphocyte-dominated CBC signature in blood cancers captures the immune phenotype shared by myeloma and related plasma-cell neoplasms.

5. **A compact analyte subset captures most discriminatory signal.** For each cancer type, a disease-specific immune score was built by sequentially adding the top LME-ranked analytes. Separation from Rest (Cohen's d) plateaued after the first 2-3 markers, with additional analytes providing minimal or occasionally negative incremental gain. The top-two-analyte immune score already achieved strong separation in most malignancies. This holds across solid tumours and blood cancers alike.

6. **CVD shows predominantly erythroid and platelet-related shifts.** Primary signals were RBC, haemoglobin, haematocrit, platelet count, mean platelet volume, and neutrophil/monocyte percentages. Prevalent CVD had stronger effects than incident CVD. Sex-stratified LME modelling showed males had a broader significant analyte set; MCV, MCH, and haemoglobin were significant mainly in males.

7. **Chronic infection produces the weakest and most heterogeneous signal.** Only two analytes reached LME significance in the chronic infection model (monocyte count and monocyte percentage). Within-group longitudinal changes were significant in chronic viral infection (decreases in MCH, platelet count, mean platelet volume, monocyte count), but no reliable results were obtainable for chronic bacterial infection due to small sample size (n = 386).

8. **Individual haematological setpoints motivate personalised scoring.** Intra-subject CBC variation is narrower than inter-subject variation across reference ranges; the authors' prior work demonstrated individual-level homeostatic CBC setpoints stable for up to 20 years. The disease-specific immune score here is computed as deviation from individual baseline, not population reference values — a key methodological distinction.

## Limitations

- **Small subgroup sizes.** Blood cancer n=232 total; specific subtypes (myeloma, myeloid leukaemia) will be substantially smaller. LME results for named subtypes are shown as heatmaps but subtype-level statistical power is limited. The paper notes these are the "10 most common cancer types within UK Biobank" — myeloma is not among the most prevalent cancers generally, so the myeloma-specific signal is potentially noisy.
- **Only 3 timepoints, high attrition.** ~90% loss to follow-up per wave; the two later visits had to be merged. This severely constrains temporal resolution and power to detect gradual pre-diagnostic trends.
- **No absolute performance metrics reported.** The immune score framework is validated via Cohen's d separation and violin plots, not via AUC, sensitivity/specificity, or calibration. It is unclear how the CBC-based risk score performs in absolute terms for individual-level prediction.
- **Prevalent cases conflate disease and treatment effects.** Prevalent cancer and CVD groups' CBC alterations may reflect treatment (chemotherapy, anticoagulants) rather than disease biology per se. The authors acknowledge this but cannot fully separate these effects.
- **Age range 40-69 only.** Consistent with UK Biobank recruitment; no younger or older population data.
- **Chronic infection small and heterogeneous.** Bacterial infection n=386 yielded no reliable results. The chronic infection category mixes TB, HIV, viral hepatitis, herpes, and sequelae — substantially heterogeneous in biology and mechanism.
- **No genome/gene-level data used.** This is a purely phenotypic CBC study; it does not test molecular mechanisms underlying the CBC signatures. The immune score is a measurement construct, not a mechanistic model.
