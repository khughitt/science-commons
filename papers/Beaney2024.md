---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Beaney2024
type: paper
title: Comparing natural language processing representations of coded disease sequences for prediction in electronic health records
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Beaney2024
tags: []
authors:
- Beaney et al.
datasets:
- dataset:cprd-aurum
doi: 10.1093/jamia/ocae091
ontology_terms:
- disease-co-occurrence
- multiple-long-term-conditions
- patient-representation
venue: Journal of the American Medical Informatics Association
year: 2024
---
## Key Findings

1. **Sequence-based models beat bag-of-words, but margins are small.** EHR-BERT topped all tasks (AUC 0.866 for mortality, 0.646 ED attendance, 0.739 emergency admission); BEHRT was close second. LDA was worst among embedding methods, often behind binary disease indicators (AUC 0.852 for mortality).

2. **Disease frequency counts performed worst among embedding methods** — counting repeated occurrences of a code added noise, not signal, consistent with code repetition in EHRs reflecting practice organization and quality incentives rather than disease severity.

3. **Disease categories (N=212) ≈ Medcodes (N=9,462).** Across virtually every embedding method and outcome, models trained on smaller vocabularies of clinician-defined categories performed as well as those using full Medcode vocabularies (e.g., EHR-BERT diseases AUC 0.866 vs EHR-BERT Medcodes AUC 0.863 for mortality). This holds despite a 45× vocabulary size difference.

4. **Prediction of new disease incidence was universally poor.** APS for new-diagnosis outcomes (hypertension, diabetes, depression) was very low across all models (e.g., EHR-BERT diseases APS 0.037 for new hypertension). The embeddings capture prevalent burden, not undiagnosed preclinical trajectories.

5. **Sociodemographic augmentation in EHR-BERT slightly improved AUC** but sensitivity analyses showed that for BEHRT/EHR-BERT (which incorporate age and sociodemographics in pre-training/MLM), adding those covariates to the downstream classifier made little additional difference.

6. **Transformer models show promise for clustering/stratification**, not just prediction. The authors note that unsupervised multi-purpose representations that generalize across multiple outcomes could support patient segmentation independent of fine-tuning.

## Limitations

- **Single primary care source:** CPRD captures coded GP diagnoses; secondary care diagnoses, symptoms, labs, and prescriptions are excluded from the disease sequences. The system admits this is a small slice of available EHR information.
- **Age range restriction for mortality:** Mortality analysis restricted to 60+ due to low event rate in younger ages, limiting generalizability.
- **Prediction task as proxy for representation quality:** Using logistic regression AUC as the sole measure of embedding quality favors predictive signal over structural interpretability. Embeddings that encode meaningful disease taxonomy might score lower on raw AUC than embeddings that pick up confounders correlated with outcomes.
- **Code frequency biases:** Repeated coding in EHRs reflects GP practice incentives and patient demographics, not disease severity. The paper's finding that frequency counts perform poorly reflects this — but LDA and transformer models trained on the same biased sequences inherit at least part of the same bias. Directly analogous to the publication-gravity confounder in the pan-disease PubTator corpus.
- **1-year follow-up only:** Longer follow-up (3–5 years) would likely widen gaps between models but also worsen absolute performance as uncertainty grows.
- **No fine-tuning:** All embeddings are evaluated without fine-tuning on the target tasks. Fine-tuned models (as in BEHRT's original paper) report AUCs of 0.82–0.88 for hypertension, diabetes, depression — higher than the 0.76–0.79 seen here for EHR-BERT without fine-tuning.
- **COVID-19 caveat:** Models trained on pre-2015 EHR data may not generalize to post-pandemic coding practice; event rates for recurrent codes fell in some EHR studies post-2020.
