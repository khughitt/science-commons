---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Jadhav2018
type: paper
title: Pan-disease clustering analysis of the trend of period prevalence
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Jadhav2018
tags: []
arxiv: '1809.06852'
authors:
- Jadhav et al.
datasets:
- dataset:taiwan-nhird
doi: 10.48550/arXiv.1809.06852
ontology_terms:
- disease-co-occurrence
- epidemiological-trend
- functional-data-analysis
- period-prevalence
venue: arXiv preprint (stat.AP)
year: 2018
---
## Key Findings

1. **Simulation performance.** The proposed method achieves near-zero clustering error across most scenarios. Under Simulation I, Scenario 1 (equal cluster sizes), sigma = 0.3: proposed error = 9.0 vs Alt.1 = 455.2, Alt.2 = 2151.8, Alt.3 = 125.1, Alt.4 = 1277.2, Alt.5 = 144.3/154.4, Alt.6 = 656.7. At sigma = 0.4 the proposed method degrades more sharply (error = 298.8 in Scenario 1) because two clusters become nearly indistinguishable. Under Simulation II (more time points), the proposed method converges to zero error at T >= 40, while most alternatives plateau or worsen.

2. **35 nontrivial clusters recovered from NHIRD.** Clusters 1-14 (201 diseases total) show predominantly increasing prevalence trends. Clusters 15-21 (55 diseases) show decreasing trends. Clusters 22-30 contain diseases with relatively flat prevalence. Clusters 31-35 (12 diseases) display "irregular" non-monotone trends. An additional 27 diseases are singletons, most of them high-prevalence conditions (e.g., acute upper respiratory infections, essential hypertension, gingivitis) whose idiosyncratic within-year variation precludes assignment to any group.

3. **Biologically interpretable clusters.** Several clusters align with known shared etiologies:
   - Cluster 9: HPV-associated malignant neoplasm of the uterus, cancer of tongue/nasopharynx, acute prostatitis, orchitis/epididymitis — all HPV-associated or genitourinary-infection-linked.
   - Cluster 11: hyperglyceridemia + disorder of lipid metabolism + myocardial infarction + hypertension + chronic kidney disease + cerebrovascular disease + acute renal failure — metabolic-cardiovascular cascade.
   - Cluster 12: sleep disorders + depression + major depressive disorder — neuropsychiatric symptom cluster.
   - Cluster 15: CNS infection/poliomyelitis + encephalitis — infectious neurological sequelae.
   - Cluster 18: acute rheumatic heart disease + heart valve disorders + ischemic heart disease + acute pulmonary heart disease — rheumatic heart disease progression cluster.
   - Cluster (irregular): varicella trend (fluctuation 2000-2004, then steady decrease from 2005), interpretable through Taiwan's staged vaccine rollout.

4. **Novel/unanticipated clusterings.** Acquired coagulation factor deficiency and renal osteodystrophy show highly similar trends but no established shared mechanism in the literature — flagged as a target for future investigation. Cysts of oral soft tissues and duodenal ulcer co-cluster in a decreasing-trend group (cluster 20) without clear explanation.

5. **Comparator clustering yields very different results.** Alternative methods identify 10-20 clusters (vs 35+27 for proposed). Pairwise normalized discrepancy between proposed and Alt.1 = 0.17, Alt.2 = 0.14, but Alt.3 = 0.82, Alt.4 = 0.78, Alt.6 = 0.90 — indicating that proposed, Alt.1, and Alt.2 form one group while the mixture/density approaches diverge substantially.

6. **Temporal trend vs absolute magnitude as disease-similarity axes.** The paper argues that absolute prevalence is driven largely by time-invariant factors (genetics, baseline susceptibility), whereas temporal variation in prevalence reflects time-varying factors (environment, diet, prevention programs, improved diagnostics). Clustering on normalized trends thus targets a biologically distinct and more "actionable" similarity axis from clustering on raw prevalence values.

## Limitations

- **Single-population validity.** All data are from Taiwan, 2000-2013. Disease prevalence trends are sensitive to population demographics, healthcare access, environmental exposures, and local policy (e.g., Taiwan's vaccination rollout). Results may not generalize to other populations or time windows.
- **Temporal confounding by diagnostic change.** Rising prevalence of many chronic conditions (Alzheimer's, chronic kidney disease, HIV) is partly attributable to improved diagnostics and coding practice rather than true biological increase. The method cannot disentangle these.
- **14 time points per disease is short.** The basis expansion and cross-validation approach is designed for this short-series setting, but the statistical power to detect subtle trend differences is limited. The authors note unreliability for very rare diseases even within the large NHIRD sample.
- **ICD-9-CM / PheWAS disease vocabulary.** Grouping 14,000+ raw codes into 1,723 PheWAS codes introduces discretization choices that affect what "diseases" appear and how granular the clustering can be. MeSH-coded literature data (as in this project) would use a different taxonomy.
- **Trend similarity does not imply causal relationship.** Two diseases can share a prevalence trend because of genuine shared etiology, shared confounders (e.g., aging population), shared diagnostic improvements, or chance. The interpretations offered in Section 4 are plausible but not validated by mechanistic evidence.
- **Cluster number is data-adaptive but tuning-sensitive.** Although lambda is chosen by cross-validation, the split-half criterion is a heuristic. The authors acknowledge that performance degrades at high noise (sigma >= 0.4 in simulation), and the alternative methods that require a pre-specified K can match or exceed proposed performance when K is known.
- **Preprint, not peer-reviewed.** The arXiv submission (September 2018) does not appear to have been published in a peer-reviewed venue as of the knowledge cutoff. [UNVERIFIED — publication status should be confirmed]
