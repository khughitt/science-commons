---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Koskinen2022
kind: paper
title: Data-driven comorbidity analysis of 100 common disorders reveals patient subgroups
  with differing mortality risks and laboratory correlates
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Koskinen2022
tags: []
authors:
- Koskinen et al.
doi: 10.1038/s41598-022-23090-3
ontology_terms: []
venue: Scientific Reports
year: 2022
dataset_usage:
- ref: dataset:hus-ehr
  role: analyzed
  overlap: unknown
---
## Key Findings

1. **Comorbidity burden is ubiquitous.** In 99 of 100 index diseases, the median number of co-diagnoses per patient during 4-year follow-up was ≥ 2 (overall median across datasets = 2; maximum median = 5 for lipoprotein metabolism disorders E78, heart failure I50, and angina pectoris I20). 65% of patients had more than one diagnosis and 41% had more than two distinct diagnoses during follow-up.

2. **2–31 comorbidity subgroups per disease.** The VAE + consensus HDBSCAN approach identified between 2 and 31 patient clusters per index disease, with atrial fibrillation (I48) producing the most subgroups (31 clusters). Asthma produced 27 clusters. The number of outliers (unassigned patients) ranged from 0–39%, with a median of 20%.

3. **Asthma (J45) case study — 27 subgroups with distinct atopic profiles, age structure, and lab markers.** Key clusters highlighted:
   - Cluster 1: young patients (< 40) with rhinitis as primary co-morbidity; predominantly allergic asthma (J45.0); highest log OR for vasomotor/allergic rhinitis J30 (log OR = 4.09, p = 2.9E-11).
   - Cluster 2: allergic asthma with lower sensitization levels; 20–59 year age range.
   - Cluster 5: high atopic burden including dermatitis and rhinitis with high eosinophils.
   - Cluster 10: patients > 50 with mixed asthma/COPD phenotype (COPD J44, log OR = 3.66, p = 2.8E-9); non-allergic.
   - Cluster 11: females > 40 with chronic rhinosinusitis/nasopharyngitis; mixed allergic/non-allergic.
   - Cluster 20: obese 50-70-year-olds with sleep apnea, hypertension, and osteoarthritis.
   - Laboratory readouts (FDR 0.1%): eosinophils, aeroallergen screen, and Birch IgE stratified sharply across allergic vs. non-allergic clusters.

4. **Atrial fibrillation (I48) case study — 31 subgroups, major survival differences.** Key observations:
   - Cluster 1: young patients (30–49), other arrhythmias (I49) as predominant co-morbidity; 90% 4-year survival.
   - Cluster 2: characteristic narrow age distribution peaking at ~30–40 years (10 years earlier than the cohort mode); elevated CRP, proBNP, and troponin T relative to other clusters (FDR 0.1%), suggesting early-onset atrial fibrillation with myocardial stress — the authors propose this group may represent a distinct biological subtype worth prospective study.
   - Cluster 10: patients with heart failure (I50) and ischaemic heart disease as predominant comorbidities; shortest life expectancy — only ~40% survived beyond 4 years post-index diagnosis.
   - Survival divergence across clusters was large even within a single age group/sex stratum (Supplementary Fig. 1).
   - Most common co-diagnoses overall: other cardiac arrhythmias (I49), heart failure (I50), hypertension (I10), sleep disorders (G47), and mental/behavioral disorders due to alcohol use (F10).

5. **Depression (F32) third example — adolescent female peak.** Age-specific incidence of new depressive episodes showed a sharp peak in late-teenage females, with the highest number at age 17. Incidence in females at that age was approximately 3× male incidence at the same age and 5× female incidence over age 30 or under 12. The authors attribute this to a multifactorial combination of biological, societal, and health-care-organization factors.

6. **Cluster-specific laboratory associations are unexpected and interpretable.** Even parameters not used in clustering showed significant inter-cluster variation. Example: mean corpuscular volume (MCV) and renal function markers differed significantly between asthma clusters, likely reflecting infection severity differences. The authors interpret these as phenotypic signatures that could be linked to treatment outcomes and biological mechanisms.

7. **An online tool was released.** Results for all 100 diseases are browsable at https://hus100.med.helsinki.fi, allowing clinicians and researchers to explore cluster-specific comorbidity heat maps, survival curves, and laboratory distributions interactively.

## Limitations

- **Single institution, secondary-tertiary only.** HUS is a secondary-tertiary hospital; primary care data are absent. This systematically excludes milder presentations and early-stage disease, biasing toward multimorbid, sicker patients. Community-level prevalence estimates are unrepresentative.
- **Finnish population only.** Genetic and healthcare-access homogeneity of the Finnish cohort limits direct generalizability. Disease co-occurrence patterns may differ in populations with different ancestry, comorbidity background, or healthcare system structure.
- **ICD-10 as a feature.** ICD-10 codes capture clinical framing, not underlying biology. Co-occurring diagnoses may reflect shared symptoms, shared medical work-up patterns, or shared therapeutic care pathways rather than shared etiology. A patient coded for both hypertension and atrial fibrillation may have those conditions causally linked or incidentally co-diagnosed.
- **No genetic or molecular data.** The paper operates entirely in the phenotypic space; no genotype, transcriptomic, or proteomic data is integrated. The "laboratory correlates" (troponin T, CRP, proBNP, etc.) are clinical biomarkers, not molecular phenotyping.
- **4-year follow-up is short.** For chronic progressive diseases, 4 years may not be sufficient to observe outcome differences between subgroups; slow progressors may be misclassified as low-risk.
- **VAE + HDBSCAN stability.** The authors apply a consensus index to assess robustness, but 2D latent representation (chosen for visualization) is a severe dimensionality constraint. The choice to fix latent dimension at 2 may merge or split clusters in ways that do not reflect true patient structure. No ablation comparing 2D to higher-dimensional latent spaces is presented.
- **Binary feature encoding.** Whether or not a patient received a given ICD code during follow-up is binarized, discarding timing, sequence, severity, and frequency of co-diagnoses. Temporal structure (e.g., which disease came first) is not used.
- **FDR stringency varies.** Different FDR thresholds are applied to different tests (0.1% for laboratory comparisons; 0.1% for cluster characterization) across a very large number of comparisons (101,087 and 174,144 respectively). Reported significant associations may still include FP due to the scale; no independent replication is shown.
- **Online tool (hus100.med.helsinki.fi) accessibility.** As of the paper's publication, results are accessible at the URL above, but long-term hosting is not guaranteed; data availability statement defers to institutional permission processes.
