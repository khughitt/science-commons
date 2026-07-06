---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Cheek2025
kind: paper
title: Age distinguishes selection from causation in cancer genomes
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Cheek2025
tags: []
ontology_terms:
- AML
- cancer driver genes
- carcinogenic effect
- clonal hematopoiesis
- dN/dS
- normal tissue evolution
- patient age distribution
- selection vs causation
- somatic copy number alteration
dataset_usage:
- ref: dataset:cheek2025-normal-blood-cohorts
  role: analyzed
  overlap: unknown
- ref: dataset:cosmic
  role: analyzed
  overlap: unknown
- ref: dataset:target-aml
  role: analyzed
  overlap: unknown
- ref: dataset:tcga
  role: analyzed
  overlap: unknown
- ref: dataset:uk-biobank
  role: analyzed
  overlap: unknown
---
## Key Findings

### Selection ≠ causation: NOTCH1 as paradigm case

NOTCH1 shows strong positive selection in normal esophageal epithelium yet has low carcinogenic effect (w near 1 or slightly cancer-inhibiting) in ESSC. Murine experiments confirm that NOTCH1 mutations inhibit tumor growth despite clonal expansion in normal tissue. Multiple other "purported drivers" (EP300, FAT1, PIK3CA in ESSC) fall near w = 1 in the carcinogenic effect analysis, consistent with recent functional and epidemiological evidence that these are selected for in normal tissue without strong causal contribution to malignancy.

### Genes with high carcinogenic effects

- **ESSC:** TPS3 and NFE2L2 have w in the hundreds; strong carcinogens. PIK3CA is near 1 — limited causal contribution to ESSC despite selection.
- **AML:** FLT3, CEBPA, IDH2, NPM1 are among the most strongly carcinogenic (w ~ 1,000–10,000). ASXL1, DNMT3A, TET2, SF3B1 are approximately 10× less carcinogenic despite being among the most frequently selected in normal blood. DNMT3A is the most frequently clonally expanded gene in normal blood but has relatively modest carcinogenic effect.
- **Colorectal:** TP53 and SMAD4 have large carcinogenic effects; KRAS, APC also high. ARID1A does not significantly differ from w = 1; FBXW7 and PTEN appear ~10× less carcinogenic than TP53.

### Age divergence between driver genes is largest in AML

Pan-COSMIC analysis shows AML has the greatest variance in patient age between driver genes (Fig. 3a). Within AML, KIT mutations have a mean patient age of 36 years vs. TET2 at 63 years — a ~27-year spread driven by the combination of selection in normal blood and carcinogenic effect differences. This spread is diagnostic: it confirms that patient age carries causal information.

### Young-age bias as a causation test in cancer-only data

Six of 21 AML driver genes show significant young-age bias relative to synonymous mutations in cancer genomes (without normal tissue reference), and these genes tend to have higher carcinogenic effects. In breast invasive carcinoma: GATA3 and TP53 show significant young-age bias; PIK3CA does not. In glioblastoma: TP53, IDH1, BRAF show young-age bias; EGFR does not. AML genes under positive selection in normal blood (dN/dS > 1 from Fabre et al.) have older mean ages in AML, while genes with high carcinogenic effects have younger mean ages — the two signals point in opposite directions.

### Carcinogenic effects are stable across young-onset and adult-onset AML

Carcinogenic effect rankings are strongly correlated between adult AML (mean age 61) and childhood AML (mean age 11): rho = 0.72, P = 0.00034. Mutation frequency rankings between the two age groups are not correlated (rho = 0.12, P = 0.62). This dissociation is the key result: carcinogenic potency is a conserved molecular property of the mutation; frequency in any given age group is dominated by normal-tissue clonal dynamics.

### SCNAs: deletions of TSGs show young-age bias concordant with point mutations

Pan-cancer analysis comparing age bias of SCNA deletions vs. SNV/small indels in TSGs shows strong positive correlation (rho = 0.62, P = 2.6 × 10⁻⁶), supporting the framework's generalization to chromosomal alterations. Amplifications of oncogenes do not show concordant age bias (rho = −0.13, P = 0.45), consistent with oncogene amplifications exerting more heterogeneous effects than TSG loss-of-function.

### AML childhood vs. adult — normal blood evolution explains age-dependence

The age-dependence of purported causal mutations in AML can be explained largely by selection dynamics in normal blood rather than requiring distinct causal mutations in childhood cancer. The framework's prediction — that carcinogenic effect rankings should agree across age strata even when mutation frequency rankings do not — is empirically validated.

## Limitations

- The carcinogenic effect estimator (odds ratio of cancer vs. normal tissue mutation frequencies) assumes no confounding between mutation z and other variables that influence cancer risk. If z co-occurs with another causal mutation, w-hat may be biased in either direction; this limitation is acknowledged and not fully resolved.
- Normal tissue data remain limited for most cancer types and the age-distribution-only test (without normal tissue) has reduced sensitivity for modestly carcinogenic mutations.
- The branching process model uses simplified parameterization (one stem cell pool, exponential growth of clones); real tissues have multiple compartments and heterogeneous division rates.
- Age of cancer onset is shaped by germline genetics and exogenous carcinogen exposure, which are not modeled and could create structured confounding in the age distributions.
- The carcinogenic effect collapses multi-step carcinogenesis to a single number per mutation; interaction effects between mutations (epistasis in the carcinogenic path) are not captured.
- SCNA analysis is limited to whole-chromosome and chromosome-arm alterations; focal SCNAs were not analyzed due to interpretability constraints in gene-boundary assignment.
- Near 30% of COSMIC samples lack age annotation, potentially introducing systematic bias if age-at-diagnosis is not missing at random.
