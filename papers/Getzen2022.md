---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Getzen2022
kind: paper
title: 'Mining for Health: A Comparison of Word Embedding Methods for Analysis of
  EHRs Data'
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Getzen2022
tags: []
authors:
- Getzen et al.
doi: 10.1101/2022.03.05.22271961
ontology_terms:
- disease-prediction
- electronic-health-records
- structured-medical-codes
- word-embedding
venue: medRxiv (preprint)
year: 2022
dataset_usage:
- ref: dataset:mimic-iii
  role: analyzed
  overlap: unknown
---
## One-Sentence Summary

By treating structured medical code sequences from MIMIC-III as word corpora, this paper shows that simple static embeddings (Word2Vec, FastText, GloVe) match or beat contextual models (ELMo, BERT) for disease prediction in small EHR datasets, and that temporal decay weighting and disease-specific models consistently outperform the multi-disease PDPS baseline.

## Key Findings

1. **Static embeddings competitive with contextual models at small data scale.** Across six disease prediction tasks (Diabetes, Chronic Kidney Disease, Heart Failure, Lipid Metabolism Disorder, Fluid/Electrolyte Disorder, Cardiac Dysrhythmia), Word2Vec, FastText, and GloVe achieved comparable AUC (roughly 0.63–0.80 depending on disease) with lasso and DL classifiers. ELMo (static mode) performed variably — well for some diseases, worse for others. BERT static embeddings showed the weakest performance overall (AUC near 0.66 for Diabetes vs 0.76 for Word2Vec), attributable to insufficient pre-training data: the MIMIC-III corpus yielded ~1.2M tokens with vocabulary of 2,730 unique codes, far smaller than the billions of tokens used in Google's published BERT models.

2. **Contextual ELMo embeddings improve over static ELMo.** When ELMo is used in contextual (sentence-aware) mode rather than averaged-static mode, prediction AUC improved for most diseases. BERT contextual embeddings, by contrast, tended to worsen relative to BERT static — reinforcing the data-volume interpretation: the model is too large to benefit from limited contextual fine-tuning on MIMIC-III alone.

3. **Temporal decay weighting consistently improves performance, with disease-specific magnitude.** Incorporating exponential temporal decay (decay factor λ = 5) into patient vector construction improved AUC and F1 across all methods compared to unweighted summation. The improvement was larger for acute/episodic conditions (Lipid Metabolism Disorder) than for chronic conditions (Cardiac Dysrhythmia), consistent with the intuition that recency matters more for diagnoses driven by recent events. Deep learning models showed particularly large drops when temporal weighting was removed.

4. **Disease-specific models outperform the PDPS multi-disease baseline.** The Patient Diagnosis Projection Similarity (PDPS) method from Farhan et al. (2016), which projects patient vectors into diagnosis-vector space using cosine similarity and enables multi-label prediction in a single model, was significantly outperformed by disease-specific supervised models (lasso or DL) built on the same word embeddings. Disease-specific models trade multi-task generality for per-disease accuracy.

5. **Computational cost: static methods far faster, GloVe fastest on CPU.** On CPU, GloVe is the fastest model to train, followed by Word2Vec and FastText; ELMo and BERT are substantially slower. BERT is faster than ELMo on GPU. Static embeddings also require far less inference time because they do not need to process the full sequence for each unique event, only the unique event vocabulary. For practitioners without GPU resources, Word2Vec/FastText/GloVe represent the best accuracy-to-cost trade-off.

## Limitations

- **ICU-only population (MIMIC-III).** MIMIC-III captures critically ill patients in intensive care, heavily biasing toward acute and serious comorbidities. Disease proximity learned from this corpus reflects ICU-context clinical practice, not general-population comorbidity patterns. Generalisation to outpatient or population-level disease similarity is not established.
- **Small corpus for contextual models.** 1.2M tokens with 2,730 unique codes is far below the data requirements for BERT or ELMo to converge. The paper's conclusion that contextual models do not help over static models is corpus-size-confounded — it does not imply contextual embeddings are inherently inferior for structured medical data.
- **No explicit disease-disease similarity matrix.** The paper evaluates embeddings via downstream prediction tasks, not via intrinsic disease-similarity quality. The embedding space might support a disease-disease proximity matrix, but this is not constructed or evaluated.
- **No comparison to clinical expert-defined disease groupings or molecular reference.** Prediction AUC measures discrimination for a fixed outcome definition; it does not reveal whether the learned disease embedding space reflects pathophysiological structure or clinical coding conventions.
- **Preprint, not peer-reviewed.** Posted March 2022; peer-review status not confirmed as of 2026-05-17.
