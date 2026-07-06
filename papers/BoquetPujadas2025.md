---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:BoquetPujadas2025
kind: paper
title: Multi-organ AI Endophenotypes Chart the Heterogeneity of Pan-disease in the
  Brain, Eye, and Heart
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: BoquetPujadas2025
tags: []
authors:
- Boquet-Pujadas et al. (MULTI consortium)
doi: 10.1101/2025.08.09.25333350
ontology_terms:
- Alzheimer-disease
- disease-heterogeneity
- endophenotype
- glaucoma
- heart-failure
- pan-disease
pmcid: ''
pmid: ''
venue: medRxiv (preprint)
year: 2025
dataset_usage:
- ref: dataset:a4-study
  role: analyzed
  overlap: unknown
- ref: dataset:adni
  role: analyzed
  overlap: unknown
- ref: dataset:blsa
  role: analyzed
  overlap: unknown
- ref: dataset:finngen
  role: analyzed
  overlap: unknown
- ref: dataset:pgc
  role: analyzed
  overlap: unknown
- ref: dataset:uk-biobank
  role: analyzed
  overlap: unknown
---
## One-Sentence Summary

Using weakly-supervised deep learning (Surreal-GAN) on multi-organ imaging and multi-omics data from 129,340 UK Biobank participants, the MULTI consortium derives 11 "Multi-organ AI Endophenotypes" (MAEs) — 6 brain, 3 eye, 2 heart — that capture reproducible pan-disease morphological heterogeneity, show distinct genetic and proteomic architectures, and predict AD progression, mortality, and medication status beyond age and sex.

## Key Findings

1. **11 reproducible MAEs across three organs.** Brain 1–3: global/regional atrophy patterns (associated with AD biomarkers — Brain 1 and 3 positively linked to CSF t-tau and p-tau181, r=0.15–0.17; Brain 5 inversely linked to CSF Aβ1-42, r=0.17). Brain 4–6: conserved or enlarged brain volume patterns (associated with psychiatric disease, "medicational compensation" effect). Eye 1: macular/retinal thinning (glaucoma). Eye 2: global thinning. Eye 3: macular thickening (diabetes-related macular edema, glaucoma with cupping). Heart 1: LV wall thickness increase. Heart 2: LA volume increase + decreased ejection fraction.

2. **PWAS — cross-organ disease landscape.** 3 significant brain MAE-DE associations, 127 eye MAE-DE, 66 heart MAE-DE (Bonferroni P<0.05/2101/11). Brain 6 positively linked to cerebral infarction (β=0.40±0.08; P=2.16×10⁻⁶). Primary open-angle glaucoma (H401) associated with both Eye 1 (β=0.44±0.09; P=3.74×10⁻⁷) and Eye 3 (β=0.33±0.07; P=6.02×10⁻⁹). Multiple sclerosis positively linked to all three eye MAEs. Heart 2 linked to angina pectoris (β=0.42±0.04; P=9.49×10⁻²⁴), acute subendocardial MI (β=0.41±0.07; P=2.47×10⁻⁸). Cancer endpoints (lung, uterine, leiomyoma) linked to brain and eye MAEs.

3. **ProWAS — 16 significant protein-MAE associations.** Heart 1 and Eye 2 both negatively associated with LPL (β≈−0.14 to −0.15; P<1.5×10⁻⁶). LPL expression highest in cardiomyocytes (655.2 nTPM) and heart tissue (394.5 nTPM), consistent with its role in triglyceride clearance from VLDL/chylomicrons. Eye 3 associated with AP3S2.

4. **GWAS — limited cross-organ genetic overlap.** 42/56/7 genomic loci for brain/eye/heart MAEs respectively. Only 5 brain, 1 eye, 1 heart cytogenetic regions jointly linked to all three organ MAE pairs. Weak pairwise genetic correlations across organs (exception: Brain 1–Heart 1, g_c=0.20±0.06; P=8.0×10⁻⁴). Within-organ g_c strong (Eye 1–Eye 2, g_c=0.31–0.38). h²_SNP: 0.26–0.53 (brain), 0.30–0.40 (eye), 0.28–0.39 (heart). Eye 3 shows the strongest negative selection signature (S=−0.88±0.10) and lowest polygenicity (Pi=0.002±0.0004), consistent with evolutionary conservation of retinal structure.

5. **Causal networks — Mendelian randomization.** 44 significant protein-MAE causal associations and 24 MAE-DE causal associations across 12 network types. Flagship example: FLRT2 protein → Brain 1 [OR=1.07 (1.04, 1.11); P=3.83×10⁻⁵] → migraine disorder [OR=1.17 (1.08, 1.25); P=8.76×10⁻⁵], validated by vertical pleiotropy (pQTLs not directly linked to migraine), 40 eQTL-linked SNPs in FLRT2 in putamen/basal ganglia/spinal cord (strongest P=2.68×10⁻¹¹), and PPI enrichment (P=8.62×10⁻⁸) implicating ADGRL3, UNC-5 family members, axon guidance and neuron projection pathways. Type 2 diabetes → Heart 1 [OR=1.08 (1.03, 1.12); P=1.225×10⁻³; N_IVs=62] confirmed.

6. **Clinical prediction.** AD progression (MCI→AD): Brain 3 HR=1.86 (1.41, 2.45; P=1.00×10⁻⁵), Brain 1 HR=1.33 (1.15, 1.54; P=1.40×10⁻⁴), Brain 2 HR=1.38 (1.08, 1.75; P=9.35×10⁻³) — risk factors; Brain 5 protective HR=0.69 (0.62, 0.78; P=8.48×10⁻¹⁰). Combined model (age+sex+Brain 3+Brain 1+Brain 2+Brain 5): CI=0.61±0.03 (100-repeat 20% holdout CV). Mortality: Heart 1 HR=1.14 (1.06, 1.23; P=9.04×10⁻⁴), Heart 2 HR=1.20 (1.12, 1.30; P=2.01×10⁻⁷); Heart 2 alone adds CI=0.73±0.032 over age+sex. Medication: Heart 2 explains incremental R²=30% for digoxin (P=2.05×10⁻¹⁹; N=4811); Brain 3 for antipsychotics (R²=1.08%; P=4.87×10⁻³; N=1243). Solanezumab (preclinical AD trial): participants with lower Brain 1–3 expression had slower cognitive decline; those with higher expression had faster decline at week 240 (PACC; Brain 2 strongest, t=3.519, P=0.004).

## Limitations

- **Preprint (not peer reviewed).** MR assumptions (no horizontal pleiotropy, instrument relevance, exclusion restriction) are partially checked but not fully falsified; sensitivity analyses shown for FLRT2 pathway only.
- **European ancestry only for primary GWAS.** Generalisation to other populations untested.
- **UKBB imaging modalities only.** Brain = MRI structural; Eye = OCT retinal thickness; Heart = cardiac MRI. Functional or molecular imaging not included. No tissue-level transcriptomics directly used to derive MAEs.
- **ICD-10 pan-disease groupings are coarse.** All G+F codes grouped into "brain pan-disease" patients — heterogeneous mix of neurodegenerative and psychiatric conditions; MAEs may conflate mechanistically distinct subtypes.
- **ProWAS uses plasma proteins (Olink), not tissue-level.** Blood-brain barrier limits brain protein detectability; the authors note heart MAEs showed more plasma protein associations, likely because heart diseases cause systemic circulating changes.
- **k hyperparameter chosen by R-index correlation, not held-out clinical utility.** The optimal k (6, 3, 2) may not be the biologically most interpretable decomposition.
- **Clinical prediction CIs are moderate.** Best AD progression CI=0.61; best mortality CI=0.73 — useful but not clinically actionable without further validation in independent prospective cohorts.
- **"Pan-disease" scope limited to three organ systems (brain, eye, heart).** Does not cover cancers, metabolic disease, autoimmune, or infectious disease — the scope of this project's disease taxonomy work.
