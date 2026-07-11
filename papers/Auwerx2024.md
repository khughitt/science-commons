---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Auwerx2024
kind: paper
title: Rare copy-number variants as modulators of common disease susceptibility
version: "1.0.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: Auwerx2024
tags: []
authors:
- Auwerx, Chiara
- Jõeloo, Maarja
- Sadler, Marie C.
- Tesio, Nicolò
- Reymond, Alexandre
- Kutalik, Zoltán
dataset_usage:
- ref: dataset:uk-biobank
  role: analyzed
doi: 10.1186/s13073-023-01265-5
ontology_terms:
- copy-number-variation
- genome-wide-association-study
- genomic-disorders
- pleiotropy
- variable-expressivity
paper_kind: ''
venue: Genome Medicine
year: 2024
---
## Key Findings

- **73 genome-wide-significant CNV signals** (p ≤ 7.5e-6): **70 CNV–disease associations spanning
  40 of the 60 assessed diseases, plus 3 associations with the "disease burden" count**. They map
  to **45 unique, non-overlapping CNV regions (CNVRs)**, nine of which (20%) correspond to known
  genomic disorders.
- **Every association was risk-increasing** — no protective CNV was found — and time-to-event
  analysis showed CNVs always shifted disease onset earlier. *Caveat:* earlier onset is also the
  only validation criterion satisfied by half the signals (see tiers), so for that subset the
  claim is partly circular.
- **Evidence is tiered, and mostly not top-tier.** Of the 73 signals: **17 tier 1** (validated by
  all three statistical approaches), **20 tier 2** (two), **36 tier 3** (time-to-event only). Only
  **32/73 (44%)** survive the experiment-wide threshold (p ≤ 1.2e-7).
- **Per-signal replication largely failed.** Of 73 signals, 49 were testable in the Estonian
  Biobank (n = 90,211); **3 replicated strictly (p ≤ 1.0e-3) and 4 more reached nominal
  significance — 7/49 = 14%.** The authors argue validity from *aggregate enrichment* over chance
  (2.9-fold at α=0.05, p=0.011; 16.3-fold at α=5e-3, p=1.1e-4) and attribute the low count to
  EstBB's limited power. **Individual associations should not be treated as independently
  replicated.**
- **The CNVs are very rare:** lead-probe frequencies 0.01%–0.36%, with **87% (39/45) of CNVRs at
  ≤0.1%**. Associations rest on small numbers of diseased carriers.
- **"~16% act indirectly through BMI" is a significance-loss criterion, not demonstrated
  mediation.** Only 25 of the 73 signals were even eligible for the test, and adjusting for BMI
  **did not significantly change CNV effect sizes**; 12 of those 25 merely fell below genome-wide
  significance after adjustment, which is the sole basis for the label. Read it as "plausibly
  BMI-confounded," not "acts through BMI." Only one CNVR lost all its associations (the
  SH2B1-overlapping distal 16p11.2 BP2-3 deletion, a known severe-obesity locus).
- **The global contribution of rare CNVs is small — and the denominator is variance, not cases.**
  The CNV burden explains **~0.02% of the *variance* in disease burden** (adjusted R² / McFadden
  pseudo-R²), rising to ~0.1% for schizophrenia and bipolar disorder. Individually, though, the
  deletion burden associates strongly with disease burden (β = +0.03 diseases per deleted gene,
  p = 3.7e-27), and 20 individual diseases associate with ≥1 burden metric. Overall **49/60
  diseases (82%)** associate with CNVs via GWAS or burden.
- **Known-GD regions drive the burden effect.** The burden restricted to the nine GD-overlapping
  CNVRs raised risk for 25 diseases plus disease burden; correcting the total burden for the
  GD/CNVR partitions removed the bulk of the signal.
- **16p11.2 BP4-5 is the most pleiotropic locus:** deletions raise risk of **12 diseases** across
  multiple organ systems plus disease burden (+3 diseases per deletion, p = 1.2e-26); five of
  these plus the burden survive BMI adjustment. Duplications instead drive psychiatric risk.
- **Bidirectional dosage effects at 17q12** — the only signal supported by *every* line of
  evidence. Both deletions and duplications increase chronic-kidney-disease risk (OR_U-shape 6.5,
  95% CI [3.4; 12.1], p = 5.9e-9): CKD prevalence 33.3% in deletion carriers and 16.9% in
  duplication carriers versus 4.4% in copy-neutral individuals, both with earlier onset (HR ≥ 4.6).
  Replicated in EstBB (p = 8.6e-4). *HNF1B* is the putative causal gene.
- **Fine-mapping recovers candidate causal genes.** At 16p13.11, deletions raise risk of epilepsy
  (OR 6.2) and kidney stones (OR 5.9); a recurrent partial deletion of *ABCC6* exons 23–29 gives
  intermediate kidney-stone prevalence (4.3%) between full deletions (9.2%) and copy-neutral
  (2.3%) — implicating **ABCC6** with dose-graded penetrance. At 15q13 the non-neurological
  phenotypes map to BP4–D-CHRNA7, **not** to *CHRNA7*.
- **Biobank-scale phenotyping recovers clinically actionable rare-disease biology in the general
  population:** *BRCA1* deletions → ovarian cancer; *LDLR* deletions → ischemic heart disease;
  16p12.2 deletions → hypertension (OR 2.7) and cardiac conduction disorders (OR 3.3).
- **Disease-associated CNVR genes are under stronger evolutionary constraint** than
  frequency-matched background genes (231 genes; pLI p = 1.3e-4, LOEUF p = 1.9e-7) and are
  enriched for triplosensitivity — **but show no significant difference in haploinsufficiency
  (pHaplo)**.
- **The paper's interpretive claim:** rare genomic-disorder biology and common adult disease sit
  on one phenotypic spectrum at the same loci (variable expressivity), so GD carriers plausibly
  face under-recognized later-onset comorbidities.

## Methods

- **Design.** Genome-wide CNV association scans between the copy number of CNV-proxy probes and
  **60 curated ICD-10-based diagnoses across 12 ICD-10 chapters**, plus a quantitative "disease
  burden" trait (count of the 60 diagnoses per individual); followed by an individual-level CNV
  burden analysis.
- **Discovery cohort.** **331,522 unrelated white British UK Biobank participants** (54% female),
  after excluding related individuals (≤3rd degree), genotype missingness ≥0.02, non-white-British
  ancestry, CNV outliers, and self-reported blood malignancies. All diseases had >500 cases except
  SLE (422) and polycystic kidney disease (454).
- **CNV calling.** Microarray genotypes (UKBB Axiom / UK BiLEVE Axiom arrays); CNVs called with
  **PennCNV v1.0.5** (GRCh37); only **high-confidence calls (|QS| > 0.5)** retained.
- **Four CNV-action models** per disease: mirror (additive per copy), U-shape (any deviation from
  copy-neutral), duplication-only, deletion-only.
- **Association testing.** **Firth-fallback logistic regression** (PLINK v2.0) for diseases; linear
  regression for disease burden. Covariates selected per disease from age, sex, array and 40 PCs.
  Probes filtered on frequency ≥0.01%, LD-pruned, Fisher p ≤ 0.001, ≥2 diseased carriers.
  Independent signals resolved by stepwise conditional analysis.
- **Significance thresholds.** 18,725 probes → Neff = 6,633 → **genome-wide p ≤ 7.5e-6**; a stricter
  **experiment-wide p ≤ 1.2e-7** additionally corrects for the 61 traits.
- **Confidence tiers.** Each signal was re-tested by three approaches — a 2x3 genotypic Fisher test,
  linear regression on residualized disease status, and **Cox proportional-hazards time-to-event
  analysis of age at onset** — at a validation threshold of p ≤ 1e-4 that **the authors themselves
  describe as arbitrary**. Signals confirmed by 3/2/1 approaches were labelled tier 1/2/3.
  Replication rates by method: Fisher 28/70 (40%), residual regression 23/70 (33%), CoxPH 70/70
  (100%) — which is why tier 3 is so populous.
- **Literature-based support.** Manual-curation **overlap** with GWAS Catalog signals (p ≤ 1e-7) and
  OMIM morbid genes — **not formal statistical colocalization**, despite the abstract's wording.
- **Replication.** **Estonian Biobank** (193,844 European-ancestry genotyped → 156,254 passing CNV
  QC → **90,211 unrelated analysed**), same case/control definitions and matched model; Bonferroni
  replication threshold p ≤ 0.05/49 = 1.0e-3 over the 49 evaluable signals; enrichment assessed by
  one-sided binomial tests.
- **BMI confounding analysis.** For the 25 signals where BMI was associated with both the disease
  and the CNV genotype, models were refitted with BMI as a covariate; effect-size change tested by
  two-sided t-test. "BMI-driven" was defined as *loss of genome-wide significance* after adjustment.
- **Burden analysis.** Six per-individual burden metrics (CNV / duplication / deletion x Mb or genes
  affected) regressed on each disease and on disease burden; recomputed after removing CNVs
  overlapping GWAS signals and disease-associated CNVRs, and partitioned into known-GD vs non-GD
  regions.
- **Software:** PennCNV v1.0.5, PLINK v1.9/v2.0, ANNOVAR, LiftOver, R.
- **Data/code.** UKBB CNV-GWAS summary statistics on the GWAS Catalog (GCST90297568–GCST90297771);
  code at https://github.com/cauwerx/CNV_GWAS_common_diseases

## Limitations

**Stated by the authors:**

- **Microarray CNV calls cover only part of the CNV landscape** — mostly large CNVs or CNVs in
  high-probe-coverage regions. Small and multiallelic CNVs, detectable only by sequencing, are
  missed.
- **Microarray CNV calls have a high false-positive rate**, and the stringent QC used to suppress
  them costs power to detect true associations.
- **Cross-cohort replication is structurally hampered:** different biobanks use different arrays, so
  partial probe overlap limits replication power and prevents summary-statistic meta-analysis.
- **Low power, and Winner's curse.** The CNVs are rare and UKBB is not case-enriched, so the GWASs
  are low-powered and reported effects are **likely overestimated**. The authors note a partially
  offsetting bias — UKBB carriers may sit at the milder end of the clinical spectrum, which would
  *underestimate* effects — so the net direction of bias is unresolved.
- **Late-onset diseases are under-ascertained**; longer follow-up is needed (Alzheimer's,
  Parkinson's).
- **The duplication- vs deletion-driven "main model" label must be read with caution:** both CNV
  types may affect risk while only one type-specific model reaches significance.
- **Other confounders were not assessed** — the authors explicitly flag clinical biomarkers and
  **socioeconomic status**.
- **Regulatory-region disruption was not investigated** as a mechanism; only gene number/identity.
- **Binary disease endpoints lose power** and misclassify cases (undiagnosed, misdiagnosed,
  prodromal individuals).

**Fair inferences from the design (not framed as limitations by the authors):**

- **Most of the 73 signals should be treated as unreplicated.** Only 7 of 49 evaluable signals
  reached even nominal significance in the Estonian Biobank. Confidence in the catalogue rests on an
  *aggregate enrichment* argument, not on independent confirmation of individual associations.
- **Half the signals (36/73) are tier 3**, resting solely on the time-to-event analysis — which is
  also the analysis producing the "CNVs always cause earlier onset" claim, making that claim partly
  circular for that subset.
- **The discovery cohort is exclusively unrelated white British individuals** and the replication
  cohort is also European, so effect sizes and frequencies may not transfer to other ancestries.
- **The "16% BMI-mediated" figure is a significance-loss criterion, not demonstrated mediation** (see
  Key Findings).
- **The constraint, pleiotropy, and burden-partition analyses were not independently replicated** and
  are internal to UKBB.
- **UKBB's healthy-volunteer selection bias** means carriers of severe genomic disorders are likely
  underrepresented, bounding how far the adult-onset-comorbidity conclusion extends to clinically
  ascertained GD cohorts.
