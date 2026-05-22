---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Xian2024Preprint
type: paper
title: Language-model-based patient embedding using electronic health records facilitates phenotyping, disease forecasting, and progression analysis
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Xian2024Preprint
tags: []
authors:
- Xian et al.
datasets:
- dataset:emerge-network-ehr
- dataset:uw-ehr
doi: 10.21203/rs.3.rs-4708839/v1
ontology_terms:
- comorbidity-pattern
- disease-subtype
- patient-representation-learning
- phenotype-cluster
venue: Research Square (preprint)
year: 2024
---
## One-Sentence Summary

Preprint precursor to Xian2025 (npj Digital Medicine): an unsupervised three-step pipeline (vocabulary autoencoder → transformer → sentence-BERT) trained on 102,740 eMERGE patients yields patient embeddings achieving median AUROC = 0.87 for disease onset prediction and 0.84 for bulk phenotyping across 1,855 phecode classes, while revealing comorbidity subtypes with distinct survival trajectories in CRC and SLE — reproduced in 840,000 external UW patients.

## Key Findings

1. **Sequence recovery confirms embedding fidelity.** Internal eMERGE: median precision = 0.958, mean = 0.917; median recall = 0.937, mean = 0.895. External UW: median precision = 0.903, mean = 0.862; median recall = 0.896, mean = 0.852. Minor performance drop on external data; no retraining required.

2. **Disease onset prediction (1 year ahead): median AUROC = 0.87.** Logistic regression on year-prior patient vectors across 1,855 phecode phenotypes. Best: pregnancy complications (AUROC = 0.93). Worst: congenital anomalies (AUROC = 0.82). External UW median AUROC = 0.84.

3. **Bulk phenotyping: median AUROC = 0.84.** Logistic regression on time-averaged embeddings. Best: pregnancy complications (AUROC = 0.90). Worst: congenital abnormalities (AUROC = 0.77). External UW median AUROC = 0.83.

4. **CRC comorbidity sub-phenotyping (eMERGE n = 2,837, k = 4 by BIC).** Cluster 2 (median onset age = 51): earliest onset, HIV-enriched, significantly worse survival (log-rank p ≈ 4.72e−93 in UW). Cluster 1 (onset age = 62): secondary malignancy/metastasis phenotype. Cluster 0 (onset age = 60): genitourinary and endocrine comorbidities. Cluster 3 (onset age = 72): cardiovascular and metabolic comorbidities. Preprint text and published text match on all four cluster descriptions.

5. **SLE comorbidity sub-phenotyping (eMERGE n = 1,806, k = 4 by BIC).** Cluster 0 (onset age = 37): epilepsy-associated, youngest. Cluster 1 (onset age = 57): dermatologic, ocular (cataracts, glaucoma, dermatochalasis). Cluster 2 (onset age = 40): pregnancy complications, menstrual disorders. Cluster 3 (onset age = 44): renal axis (nephropathy, dialysis, end-stage renal disease). External UW (n ≈ 2,546) reproduces two of four clusters faithfully; survival differences confirmed.

6. **CRC longitudinal progression trajectories.** PCA on 10-year post-onset vectors (n = 110): PC1/PC2 explained primarily by cluster group, then age/sex/sites. Pre-diagnosis comorbidity divergence is weak (max shared frequency ≈ 21%); divergence strengthens post-onset (up to 55%), indicating disease context amplifies pre-existing biological heterogeneity rather than creating it.

## Limitations

Same as Xian2025. Key issues:

- EHR codes only — no genotype or molecular data; clusters may reflect shared clinical practice rather than shared biology.
- 12-site eMERGE training introduces site-level coding heterogeneity (PC3 of CRC longitudinal vectors is site-explained).
- No phecode-to-MeSH crosswalk provided; direct comparison with PubTator MeSH-keyed axes requires an additional mapping step.
- Sparse-patient performance: transformer attention degrades for patients with few codes per year.
- Training data access-controlled (eMERGE dbGaP); UW data institutional.
