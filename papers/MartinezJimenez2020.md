---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:MartinezJimenez2020
kind: paper
title: A Compendium of Mutational Cancer Driver Genes
version: "1.1.0"
created: "2026-07-11"
updated: "2026-07-16"
bibkey: MartinezJimenez2020
tags: []
ontology_terms:
- IntOGen
- cancer driver genes
- cancer hallmarks
- dN/dS
- mode of action
- mutational landscape
- oncogene
- pan-cancer
- positive selection
- somatic mutation
- tumor suppressor
paper_kind: review
---
## Methods

The compendium is built by applying seven complementary positive-selection methods to 28,076
tumours across 221 cohorts spanning 66 cancer types, via the IntOGen pipeline.

### Cohorts

Samples are drawn from TCGA (10,010 samples / 32 cohorts), ICGC (3,988 / 42), Hartwig Medical
Foundation (3,742 / 30), PCAWG (2,554 / 31), cBioPortal (3,570 / 34), Pediatric cBioPortal
(1,087 / 26), St. Jude (622 / 16), TARGET (246 / 2), and literature cohorts (2,257 / 8). Of these,
157 cohorts are primary tumours and 33 are metastatic or relapse (4,340 samples); paediatric
malignancies account for 2,799 samples across 48 cohorts. A cohort is a set of samples of one
cancer type processed through a uniform sequencing and calling pipeline. Each cohort is analysed
independently, because re-calling mutations across heterogeneous pipelines is not feasible at this
scale.

### Pipeline

*Stage 1 — pre-processing.* Each cohort is filtered for duplicate samples from the same tumour,
samples with an abnormal missense-to-synonymous ratio, and hypermutators. Mutations overlapping
a Panel of Normals are removed.

*Stage 2 — seven parallel driver-identification methods*, each exploiting a different selection signal:

| Method | Signal exploited |
|---|---|
| dNdScv | Negative-binomial dN/dS with regional (chromatin/expression) covariates |
| OncodriveFML | Functional-impact score bias across observed mutations |
| cBaSE | Bayesian inference of non-synonymous counts given synonymous counts |
| OncodriveCLUSTL | Positional recurrence along the linear DNA/protein sequence |
| HotMAPS | Positional recurrence in 3D protein conformation |
| smRegions | Enrichment of mutations in annotated Pfam functional domains |
| Mutpanning | Non-synonymous recurrence plus deviation from the neutral trinucleotide context |

*Stage 3 — weighted-vote combination.* Per-cohort p-value lists are combined by a weighted
Stouffer's Z-score. Weights are assigned per cohort using Schulze's voting method, optimised so
that enrichment of known Cancer Gene Census (CGC) genes at the top of the consensus ranking is
maximised. No single method may exceed 0.30 of the total credibility simplex. Final q-values use
Benjamini-Hochberg correction. Genes are stratified into Tier 1 (q < 0.05), Tier 2 (CGC genes with
CGC-specific q < 0.25), and Tier 3 (remaining candidates meeting a rank cutoff).

*Post-processing filters.* Candidates must survive: removal of non-expressed genes (TCGA
expression, ≥80% of samples at log2 RSEM ≤ 0 for matched tumour types); exclusion of genes highly
tolerant to SNPs (gnomAD oe > 1.5); removal of mutations overlapping Panel-of-Normals germline
variants; blacklisting of known false-positive categories (long genes such as TTN, OBSCN, RYR2;
olfactory receptors; non-Tier1 CGC genes lacking CancerMine literature support); discarding of
non-CGC genes with >3 mutations in a single sample; and exclusion of genes where >50% of
mutations in AID-active lymphoid cancers match COSMIC Signature 9.

On 32 TCGA WES cohorts the weighted combination achieves a higher CGC-Score than any
individual method in 23/32 (71%) cohorts and higher than all other combination strategies tested in
30/32 (93%) cohorts, while never being the most enriched in known non-cancer genes.

### Mode-of-action classification

Mode of action (MoA) is inferred per gene from consequence-type-specific dN/dS ratios estimated
by dNdScv across pan-cancer TCGA cohorts, with epsilon = 0.1:

- **Act (activating / oncogene):** omega_missense − omega_nonsense > epsilon.
- **LoF (loss-of-function / tumour suppressor):** omega_nonsense − omega_missense > epsilon.
- **Amb (ambiguous):** |omega_missense − omega_nonsense| < epsilon, or omega_missense < 1.

Inference is reconciled with the Cancer Genome Interpreter (CGI) prior: agreement yields the
consensus label; absence from CGI yields the inferred label; conflict defers to the CGI prior.

The compendium, per-tumour-type driver rosters, mutational features, and the pipeline itself are
available at intogen.org.

## Key Findings

### Compendium size and CGC validation

- **568 mutational driver genes** across 66 cancer types from 28,076 tumours.
- ~75% of the 568 are already annotated in CGC v87, validating the pipeline.
- **152 potential new drivers** not annotated in the CGC at publication. Five are discussed with
  independent supporting evidence: RASA1 (lung/HNSCC, LoF, RAS/MAPK regulator), KDM3B
  (pilocytic astrocytoma/medulloblastoma), FOXA2 (uterine carcinoma), KLF5 (cervical/bladder/lung
  squamous), and BRD7 (melanoma/liver).
- **>80% of driver gene–tumour type associations are novel** relative to CGC annotations, showing
  that the per-tumour-type breadth of known drivers is far wider than documented. KMT2C, for
  example, shows signals in 31 tumour types but is CGC-annotated only for medulloblastoma.

### Tissue specificity of drivers

- **360 of 568 genes (63%)** drive only **one or two tumour types**.
- **12 genes are cancer-wide drivers** active in **more than 20 malignancies**: TP53, KRAS,
  PIK3CA, PTEN, KMT2D, KMT2C, LRP1B, ARID1A, RB1, FAT4, NF1, and CDKN2A. Maximum
  prevalences range from 0.92 (KRAS) to 0.25.
- **Cancer-specific highly prevalent drivers** are frequent in one or very few types: GNAQ (50% of
  uveal melanoma), GNA11 (uveal melanoma), GTF2I (47% of thymomas), CCND3 (47% of Burkitt
  lymphoma), MYC (60% of Burkitt lymphoma), PTCH1 (basal cell carcinoma, max prevalence 0.56).
- The same gene can drive by different mechanisms in different types: EGFR shows extracellular
  domain clusters in glioblastoma but kinase domain clusters in lung adenocarcinoma.

### Mutational features distinguish oncogenes from tumour suppressors

Oncogene clusters are narrow and concentrate a high fraction of a gene's mutations (KRAS codons
12–13: 5 nt, 85% of mutations in a colorectal cohort of 496; IDH1 codon 132: 100% of mutations in
an AML cohort of 257), reflecting the limited number of gain-of-function positions. Tumour
suppressor clusters are wider and hold a smaller fraction (TP53: 28 nt, 28% of mutations in
pilocytic astrocytoma; SPOP: 44 nt, 83% in prostate adenocarcinoma), and are enriched for
nonsense mutations.

### Recurrently affected protein domains

- The **P53 domain** is enriched across **42 cancer types** — more than any other domain, driven
  entirely by TP53.
- The **tyrosine kinase domain** of 13 genes is enriched across 24 tumour types; BRAF has the
  widest reach (14 types).
- RAS, cadherin, and C2H2 zinc finger domains each show enrichment across 13 cancer types.

### Drivers in non-malignant tissue

Several driver genes are positively selected in histologically normal somatic tissue, implying that a
driver mutation alone is insufficient for transformation: tissue-specific selective constraints and
cooperating events are required.

### Treatment-resistance drivers in the metastatic context

ESR1 (breast) and AR (prostate) are rarely mutated in primary tumours but are clear drivers in
treatment-resistant metastatic cohorts.

### Acknowledged gaps

Low-frequency drivers (<10% mutational prevalence), drivers in under-represented populations,
metastatic- and paediatric-specific drivers, non-coding driver elements, and the temporal ordering
of multi-driver cooperativity remain open challenges.

## Limitations

- **Point mutations and short indels only.** Copy-number alterations, structural variants,
  translocations, epigenetic silencing, and non-coding drivers are excluded, so the compendium is a
  subset of the full driver landscape. Short indels are also excluded from background modelling,
  because accurate background-rate modelling for indels is harder.
- **Cohort-level analysis.** Each cohort is analysed independently owing to technical heterogeneity
  in mutation calling; cross-cohort pooling is not feasible at this scale, limiting power for rare
  drivers and introducing noise that per-cohort analysis only partially mitigates.
- **Static snapshot.** The findings reflect publicly available data through ~2019. Genes mutated at
  <10% frequency in current cohorts are likely under-represented.
- **CGC as imperfect ground truth.** CGC v87 is used for both weight calibration and validation, yet
  is itself incomplete and contains false positives; the overlap analysis is a relative benchmark, not
  an absolute validation.
- **Mode of action is inferred, not experimentally validated.** Classification from mutational
  features is a proxy; some genes (e.g. KDM3B) have conflicting functional evidence, some cannot
  be cleanly classified (Amb), and MoA can differ between tumour types for the same gene.
- **LRP1B caution.** Flagged as a recurrent cancer-wide hit that may be a long-gene calling
  artifact; the authors note the discussion is unsettled.
- **Non-European populations under-represented**, explicitly flagged by the authors, particularly
  for drivers in specific ethnic backgrounds.
- **Somatic only.** Germline and non-somatic drivers are out of scope.
