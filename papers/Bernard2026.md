---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Bernard2026
kind: paper
title: Unsupervised learning reveals novel disease-associated proteins in high-dimensional
  human proteomic data
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Bernard2026
tags: []
authors:
- Elvis Bernard, Yiling Wang, Manlin Chen, Shunqing Xu
doi: 10.1038/s41598-026-41385-7
ontology_terms:
- biomarker-discovery
- disease-clustering
- plasma-proteomics
- unsupervised-learning
venue: Scientific Reports
year: 2026
dataset_usage:
- ref: dataset:uk-biobank
  role: analyzed
  overlap: unknown
---
## Key Findings

1. **DIRAM vs. DIRCOD produce clusters of different scales.** DIRAM delivers more compact, homogeneous clusters (smaller N); DIRCOD produces larger clusters with more statistical power for rare-disease detection, at the cost of imputation bias. Both identify overlapping disease-enriched groupings, validating the overall approach.

2. **Celiac disease.** Clusters A27, B7, A10, A11 are enriched for celiac diagnosis (OR 4.3–8.8, p 4.5e-5 to 1.2e-21 after Bonferroni). Key differentially distributed proteins include IGF2BP3 (a stabiliser of the intestinal barrier protein CLDN11; previously linked to intestinal permeability), NRXN3, LRP2BP, and CACNB1. NRXN3 and LRP2BP are newly nominated; LRP2BP is related to LRP1, previously associated with celiac. Correlation analysis shows strong co-regulation gain (r≈0.7 increase) among most proteins in celiac clusters, indicating altered protein network topology.

3. **Hypertension.** Clusters B6 and B5 are positively enriched (OR 1.2–1.3, p 2.5e-6 to 3.9e-3); B1 and B2 are protective (OR 0.7–0.8, p 5.6e-9 to 8.6e-12). Key proteins: UBE2L6 (known hypertension GWAS gene; removing it from the analysis reduces OR by 0.01, dropping from 1.036 to 1.026 after Bonferroni), HNRNPUL1 (coronary heart disease variants), BECN1 (pulmonary hypertension). PNLIPRP1 and PNLIPRP2 emerged prominently from GWAS; their contrasting levels in B1/B2 versus B5/B6 suggest a potential protective role. Cluster B15 had low hypertension incidence despite hypertension-like protein signatures, consistent with multifactorial disease compensation. Correlation changes in hypertension are modest (max r change ≈0.12), consistent with its polygenic character.

4. **Leukemia.** Clusters A15, A13, A5, A1, A37, B10 are enriched (OR 7.2–13.3, p 1.2e-4 to 2.6e-8). Key proteins with decreased inter-cluster correlations (Δr ≈ −0.3): LRCH4 (previously linked to leukemia), WDR46 (gastric carcinoma, colorectal cancer, hepatocarcinogenesis), SERPINB1 (SERPINE family; pan-cancer relevance), NUB1 (breast cancer biomarker). The low participant count for leukemia precluded a full PCA disease-axis analysis. Correlation loss among key proteins (up to −0.3) suggests co-regulation breakdown in leukemia clusters.

5. **A composite protein axis predicts disease prevalence.** For hypertension and celiac disease, the first PC of the within-cluster protein matrix correlates monotonically with disease prevalence across quantile bins, and this relationship is preserved when the same PCA transformation is applied to the full UK Biobank population. This establishes a protein combination score as a disease predictor from unsupervised clusters.

6. **Severely-ill clusters (A8, B9) lack a clear unifying factor.** These clusters have high prevalence of organ transplants (25%), acute renal failure (49.6%), and surgical complications (38%), yet no clear medication signal was detected — possibly because UK Biobank drug prescription records are incomplete.

7. **Sex-linked signals in non-focal diseases.** Clusters B3 and B6 showed OR 13.29 for hepatitis (K73) and 9.46 for splenic disease (D73), respectively, both in women. The authors treat these as candidate pleiotropic effects of the 420 differentially distributed proteins, not definitive findings given low incidence counts.

## Limitations

- **Three diseases only; rare diseases under-powered.** Only celiac, hypertension, and leukemia were analysed in depth. Leukemia results are explicitly acknowledged as under-powered due to low participant count. Generalisation to other disease classes (oncology, autoimmunity, metabolic) is asserted but not demonstrated.
- **Bonferroni correction is conservative for disease-specific work.** The authors note that Cluster A7 crossed the Bonferroni threshold for hypertension but had uncorrected p=10^-4 for celiac — a borderline cluster that BH correction would have retained. Researchers with targeted disease focus may need to apply FDR rather than Bonferroni.
- **DIRCOD imputation bias.** KNN imputation may introduce artificial covariance among imputed values. The authors address this by always characterising communities on non-imputed data, but residual bias cannot be fully excluded.
- **ICD-10 diagnostic coding is administrative, not clinical.** Diagnosis codes reflect hospital coding practice, not systematic clinical ascertainment. Mild or outpatient-only disease cases are likely undercounted; severity-linked coding biases could inflate ORs for severe disease clusters (A8, B9).
- **Drug prescription data is incomplete.** UK Biobank prescription records are acknowledged to be unreliable for severe-disease clusters; this is an unresolved confound.
- **Cross-disease protein specificity not evaluated.** A protein identified as elevated in celiac clusters might also be elevated in leukemia or hypertension clusters; specificity of each candidate biomarker across all diseases was not reported.
- **No MeSH/OMIM crosswalk provided.** The ICD-10 disease labels used here are not directly mapped to MeSH or OMIM identifiers, which would be required for integration with PubTator's MeSH-based disease similarity matrices.
