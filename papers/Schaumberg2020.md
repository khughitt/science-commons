---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Schaumberg2020
kind: paper
title: Interpretable multimodal deep learning for real-time pan-tissue pan-disease
  pathology search on social media
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Schaumberg2020
tags: []
authors:
- Schaumberg et al.
doi: 10.1038/s41379-020-0540-1
ontology_terms:
- disease-state-classification
- pan-tissue-analysis
- similarity-search
- transfer-learning
pmid: ''
venue: Modern Pathology
year: 2020
dataset_usage:
- ref: dataset:pubmed-oa-histology
  role: analyzed
  overlap: unknown
- ref: dataset:twitter-pathology-images
  role: analyzed
  overlap: unknown
---
## One-Sentence Summary

A multimodal ResNet-50 + Random Forest system trained on social-media and PubMed pathology images classifies disease state (nontumor / low-grade / malignant) across ten tissue types with AUROC ~0.80 and is the first pan-tissue pan-disease pathology case similarity search prospectively tested on a live social media bot.

## Key Findings

1. **Disease state classification across tissue and stain types.** The ensemble deep-learning + Random Forest hybrid achieves overall weighted AUROC 0.8085 (mean ± stdev = 0.8035 ± 0.0043 across 10-fold CV) for three-class disease state prediction (nontumor, low grade, malignant) spanning 10 tissue types and 16+ stain types — bone/soft tissue, breast, dermatological, gastrointestinal, genitourinary, gynecological, head/neck, hematological, neurological, and pulmonary.

2. **H&E vs. other stain discrimination is near-perfect.** AUROC for H&E vs. all other images: mean 0.9735 (tenfold) / 0.9549 (leave-one-pathologist-out, LOO). H&E vs. IHC: AUROC 0.9977 (tenfold) / 0.9907 (LOO). This classifier was used to identify 113,161 H&E figures from 1,074,484 PubMed OA articles, expanding the searchable PubMed dataset by an order of magnitude.

3. **Tissue type prediction AUROC = 0.81.** Ten-fold CV tissue type AUROC: 0.8134 (mean ± 0.0007 across replicates); individual tissue AUROCs range from ~0.75 (neurological, n = 348) to ~0.90+ (breast, head/neck).

4. **Case similarity search: precision@k = 1 = 0.7618 ± 0.0018 vs chance 0.397 ± 0.004.** Leave-one-pathologist-out search precision for the best method (HandEng + Hist + Tissue + ImageNet Ens) significantly exceeds permutation null (p = 0.0001817, U = 100, two-sample Wilcoxon). Adding tissue type covariate improves precision@1 from 0.5640 to 0.6533 (p < 0.0002); marker mention adds further to 0.6908.

5. **Histopathology-trained deep features cluster by disease state; ImageNet-only features do not.** UMAP of 100 histopathology-trained deep features shows clean disease state separation (malignant / low grade / nontumor), whereas 2048-dimensional ImageNet-pre-trained features and 2412 hand-engineered features do not separate disease state. This validates the need for domain-specific fine-tuning.

6. **Deep features encode edges, colors, and tissue; LBPP and color histograms dominate non-deep features.** Random Forest feature importance: after histopathology training, tissue type covariate drops in importance while texture hand-engineered features (Local Binary Patterns Pyramid, color histograms) rise — suggesting the deep network absorbs tissue identity, freeing the RF to rely on tissue-specific texture.

7. **Three sanity checks and five interpretability levels.** The system flags searches with low prediction uncertainty (ensemble spread), misclassification risk (disease state predicted incorrectly), and spatial heatmap disagreement. Spatial patch-level activation maps localise disease-state predictions within images, enabling deductive/demonstrative interpretability for individual pathologist cases.

8. **Social media bot @pathobot tested prospectively.** When mentioned on Twitter with a pathology image, the bot returns disease state prediction (normal/artifact/infection/injury/nontumor, preneoplastic/benign/low-grade-malignant-potential, or malignant) plus ranked similar cases from social media and PubMed. First pathology study prospectively tested in full public view on social media.

## Limitations

- **Scope limited to histopathology images.** The pan-disease taxonomy here is a pathological disease state spectrum (nontumor → malignant) — it does not model disease identity, etiology, or molecular subtype. The project needs disease identity similarity, not just severity classification.
- **Social media sampling bias.** Cases on Twitter are unusual or challenging cases pathologists find worth sharing; normal and common cases are under-represented. This biases the dataset toward interesting outliers and may over-represent rare diseases or dramatic presentations.
- **Three-class coarseness.** Nontumor / low grade / malignant collapses >10,000 disease entities into 3 bins. It cannot resolve within-class disease boundaries relevant to the project's disease-taxonomy goals.
- **No explicit disease identity labels.** The classifier predicts severity state, not disease name or ICD/MeSH identity. The project needs disease-disease similarity at the entity level, not stage level.
- **Label noise from social media.** Hashtag/keyword labelling may be incorrect or vague. Authors acknowledge disagreement among pathologists and adopt majority-vote curation.
- **Pathologist-specific staining/lighting artifacts.** Despite LOO cross-validation, imaging artifacts from specific microscopes and staining protocols remain a confound — the paper flags this explicitly.
- **Region-of-interest bias.** Pathologists choose which image region to share; this introduces selection bias that may systematically differ from whole-slide scanner capture.
- **No quantitative disease-name-level clustering.** The paper does not cluster diseases by identity or provide a disease taxonomy; it classifies images into three severity states. The pathobotology.org platform was announced but the dataset was not yet fully public at time of publication.
