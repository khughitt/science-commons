---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:MartinezJimenez2023
type: paper
title: Pan-cancer whole-genome comparison of primary and metastatic solid tumours
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: MartinezJimenez2023
tags: []
datasets:
- dataset:hartwig
- dataset:pcawg
ontology_terms:
- driver mutations
- genomic instability
- metastasis
- mutational signatures
- pan-cancer
- structural variants
- treatment resistance
- whole-genome doubling
- whole-genome sequencing
---
## Key Findings

### Cohort characteristics
- Metastatic tumours were on average 1.67 years older at biopsy; biopsy locations were 12.2% local (primary tissue), 16.2% lymph node, and 55.7% distant.
- Metastatic cohort displayed higher mean clonality across all 23 cancer types vs. primary, consistent with a single major subclone seeding event or severe evolutionary constraints imposed by anticancer therapies.

### Tumour mutation burden (TMB) — modest increase
- Small-variant TMB (SBS + DBS + indels) increased only modestly in mets: fold changes of 1.25 ± 0.47 (SBS), 1.55 ± 0.86 (DBS), 1.45 ± 0.53 (indels).
- Only 5 cancer types showed a consistent significant increase in all three mutation types (breast, cervical, thyroid, prostate, pancreatic neuroendocrine).
- 15 of 23 cancer types had no significant increase in mutation burden for any type — TMB is not a reliable indicator of progression stage.

### Mutational signatures — treatment is the dominant exogenous driver
- Signatures attributed to cytotoxic treatments were significantly enriched in 10 cancer types.
- Platinum-based chemotherapy (SBS31/35/5, DBS5) was the strongest single effect: +551 ± 575 SBS and +32 ± 22 DBS mutations per sample (mean ± s.d.).
- Radiotherapy (IDS8) enriched in 6 cancer types; 5-fluorouracil (SBS17a/b) and polycyclic aromatic hydrocarbons from chemotherapy (DBS2) also showed cancer-type-specific metastatic enrichment.
- APOBEC (SBS2/13) significantly elevated in 6 cancer types in mets (+325 ± 178 mutations/sample), including breast, colorectal, stomach, kidney, prostate, and pancreatic neuroendocrine — consistent with enhanced APOBEC activity during advanced-stage progression.
- Clock-like SBS1 enriched in breast, prostate, kidney, and thyroid metastatic cancers independently of age, suggesting accelerated cell-division rates in those mets.

### Chromosomal karyotype — largely conserved
- Chromosome arm aneuploidy profiles are generally conserved between primary and metastatic settings — the karyotype is defined early at primary tumorigenesis.
- Five cancer types showed substantial karyotypic changes at the metastatic stage: kidney renal clear cell, prostate, and thyroid (91%, 43/47 of significant discrepancies in kidney), plus breast and pancreatic neuroendocrine.
- Metastatic WGD rates are elevated pan-cancer; increased aneuploidy scores and LOH are also elevated, but WGD-independent arm-level changes make a further contribution.

### Structural variants — the most pervasive quantitative difference
- SV burden increased extensively in mets: fold change 2.5 ± 1.3 (mean ± s.d.) across 13 of 23 (56%) cancer types.
- Small deletions (<10 kb) were the most enriched SV subtype: fold change 2.7 ± 1.2 in 15 of 23 cancer types.
- Complex SVs (chromothripsis-class, ≥20 breakpoints) enriched in metastatic prostate (>3-fold enrichment).
- LINE insertions: 12.2-fold increase in stomach, 12.5-fold in bladder urothelial carcinomas.
- Increased SV burden was found even in cancer types lacking substantial karyotypic changes (e.g., oesophageal, lung squamous), indicating SV accumulation is partly decoupled from large-scale aneuploidy.

### Driver gene landscape
- Mean driver alterations per sample: 4.5 (primary) vs. 5.3 (metastatic) — moderate increase.
- 8 of 23 cancer types (34%) showed a statistically significant increase in driver count.
- Largest increases: prostate (3.16 mean difference), pancreatic neuroendocrine (2.16), thyroid (1.7), kidney renal clear cell (1.87).
- Pan-cancer metastatic-enriched drivers: TPS3, CDKN2A, TERT (enriched across multiple cancer types, consistent with pan-hallmark aggression).
- Four driver genes found exclusively mutated in mets (not in primary): PTPRD (kidney renal clear cell), CREBBP (pancreatic neuroendocrine), RET (thyroid), TP53 alterations (thyroid). [Note: TP53 also appears in the pan-cancer enriched list above — thyroid specifically.]
- Only 12 genes showed significant frequency bias in at least one cancer type (22 gene-and-cancer-type pairs total); 86% of significant pairs showed enrichment toward higher metastatic frequency.
- Actionable driver variants were more prevalent in mets overall, with high variability across cancer types.

### Treatment-enriched drivers (TEDs) — therapy selection as a major force
- 61 TEDs identified across 33 treatment groups from 8 cancer types.
- 54% (33/61) were coding mutations; 26% copy number amplifications; 14% non-coding; 6% recurrent homozygous deletions.
- Known resistance drivers confirmed: AR activating mutations (prostate, anti-androgen therapy); ESR1 mutations (ER+ breast, aromatase inhibitors); EGFR T790M (lung adenocarcinoma, EGFR inhibitors); ERBB2 amplifications (breast, anti-HER2).
- Novel candidate TEDs: TYMS amplification (breast, pyrimidine antagonist); ACTL6A promoter mutations (triple-negative breast, platinum); FGFR2 promoter mutations (breast, CDK4/6 inhibitors); PRNC1 and MYC co-amplifications (prostate, androgen deprivation).
- 53% of metastatic patients with annotated treatment had at least one TED; 32% had a known resistance driver; 21% had a candidate resistance driver.
- After removing TEDs, the primary-to-metastatic driver difference reduced by 36% (from 5.3 to 5.0 mean drivers in mets, vs. 4.5 in primary), confirming therapy selection as a major — but not sole — driver of enrichment.

### Cancer-type heterogeneity: a spectrum of primary→metastatic transformation
The paper classifies cancer types along a spectrum from "largely conserved" to "extensively transformed" genomic portraits:

- **Highly consistent** (conserved across primary and metastatic stages): ovarian serous carcinoma is the clearest example.
- **Moderately different**: lung adenocarcinoma.
- **Extensively transformed** at late stage: breast, prostate, thyroid, kidney renal clear cell, and pancreatic neuroendocrine carcinomas show intensive genomic landscape transformation.

## Limitations

1. **Unpaired cohorts:** Primary (PCAWG) and metastatic (Hartwig) samples come from different patients, not matched biopsies from the same individual. This is the study's central confound — systematic "born to be bad" biases cannot be fully excluded. The authors note this explicitly and show that pipeline harmonisation minimises technical biases, but biological confounders (patients selected for resection vs. systemic therapy) remain.

2. **Treatment information incompleteness:** Treatment data available for only 83.7% of metastatic patients; the 16.3% missing could include treated patients misclassified as untreated, potentially underestimating TEDs.

3. **No longitudinal tracking:** Without matched primary→metastatic pairs from the same patient, the analysis cannot distinguish evolution-during-progression from selection of pre-existing subclones or from tissue-of-origin sampling biases.

4. **Subclonal driver mutations potentially missed:** Low-frequency subclonal drivers below the clonality threshold would systematically undercount drivers, especially in heterogeneous primaries.

5. **Causal vs. correlational drivers:** The TED catalogue identifies enrichment, not causation — candidate TEDs still require orthogonal experimental validation.

6. **Sample sizes for rarer cancer types:** Some cancer-type-specific comparisons involve small numbers (e.g., cholangiocarcinoma: 26 primary vs. 66 metastatic; uterine: 42 vs. 32) limiting power for low-frequency events.
