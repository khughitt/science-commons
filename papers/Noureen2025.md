---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Noureen2025
kind: paper
title: Stratification of telomerase activity in cancer reveals associations with senescence
  and genomic instability
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Noureen2025
tags: []
ontology_terms:
- ALT (alternative lengthening of telomeres)
- EXTEND score
- TERT
- cellular senescence
- copy number alteration
- genomic instability
- pan-cancer
- replicative immortality
- telomerase activity
- tumor mutation burden
dataset_usage:
- ref: dataset:ccle
  role: analyzed
  overlap: unknown
- ref: dataset:gtex
  role: analyzed
  overlap: unknown
- ref: dataset:noureen2025-scrna
  role: analyzed
  overlap: unknown
- ref: dataset:tcga
  role: analyzed
  overlap: unknown
---
## Key Findings

### Telomerase strata are cancer-type-specific

- 11 of 33 TCGA cancer types are significantly enriched for high telomerase activity (Group 1: COAD, READ, STAD, LUSC, LUAD, HNSC, THYM, UVM, LAML, UCEC, TGCT); FDR < 0.05, Fisher's exact test. TGCT is the most extreme: 72% high vs. 28% low.
- 22 cancer types (Group 2: KICH, KIRC, KIRP, LGG, THCA, PCPG, PAAD, and others) are predominantly low telomerase activity (average odds ratio = 0.6).

### Genomic instability tracks with high telomerase activity

- **TMB:** 15/33 cancer types show significantly higher TMB in the high telomerase group (FDR < 0.05; average Hodges-Lehmann estimate = 1.12). TP53 mutations most prevalent in high group (9 cancer types); KRAS, PKHD1L1, RB1, TTN enriched in high group; PTEN and ATRX enriched in low group (consistent with ALT phenotype).
- **CNA:** 15/33 cancer types show significantly higher CNA fraction in the high telomerase group (FDR < 0.05; average effect size = 0.63); LUAD and LUSC most pronounced.
- **LOH:** 13/33 cancer types show significantly higher LOH in the high telomerase group (FDR < 0.05; average effect size = 0.55). No cancer type shows LOH enrichment in low group.
- **Telomere length:** Low telomerase activity is associated with longer telomeres in 5 cancer types (TGCT, LUAD, LUSC, BRCA, GBM; FDR < 0.05, Wilcoxon), consistent with ALT enrichment in the low group. THYM is an exception (low group has shorter telomeres).
- **TERT promoter mutations:** Significantly enriched in the high telomerase group in LGG (odds ratio = 28.5) and THCA (odds ratio = 11.6); FDR < 0.01.
- **ATRX mutations:** Significantly enriched in low telomerase group in GBM, LGG, and SARC (FDR < 0.01), consistent with ALT-associated telomere maintenance.
- **Survival:** High telomerase activity associated with worse overall survival in 10 cancer types (MESO, THCA, PAAD, PRAD, PCPG, KIRC, KIRP, KICH, SARC, ACC; log-rank P < 0.05, 95% CI); opposite pattern in LAML, THYM, and TGCT.

### Low telomerase activity maps onto a senescence-like state

- Senescence score (SenMayo 125-gene signature) significantly enriched in low telomerase group in 26/33 TCGA cancer types (FDR < 0.05; Student's t-test).
- CCLE cell lines: low telomerase / high senescence confirmed (p < 2.22e-16). Fibroblasts show the highest senescence and lowest telomerase; hematopoietic lines show the reverse.
- Single-cell validation (GBM and HNSC scRNA-seq): inverse telomerase–senescence relationship replicates at single-cell resolution; non-cycling cell populations show significantly higher senescence scores (GBM: p < 2.2e-16; HNSC: p < 2.2e-16).
- Spatial transcriptomics (lung and breast): EXTEND and senescence scores are spatially anticorrelated; cell cycle activity mirrors EXTEND and is anticorrelated with senescence across spatial regions.
- Senescence–telomerase anticorrelation also observed in pediatric neuroblastoma (Spearman R = −0.53, P = 2.3e-07) and in GTEx normal tissues (lung, esophagus, skin, brain: p < 0.001 for low vs. high telomerase OA group comparisons).
- During human development (liver, heart): Spearman R = −0.65 (P < 1.1e-06 and P = 3e-06 respectively) between EXTEND and senescence across fetal/young/adult stages — relationship is conserved outside cancer.

### Immune and stress-signaling associations

- Low telomerase activity is significantly associated with the C3 (inflammatory, low-proliferative) immune subtype across 18 cancer types (FDR < 0.05, Fisher's exact test).
- Low telomerase group is enriched for ROS and MAPK signaling pathways (both FDR < 0.05 across 33 cancer types); ROS and senescence scores are strongly correlated pan-cancer (Rho = 0.9, P = 9.94e-09), and the relationship persists within individual cancer types (Spearman FDR < 0.05).
- Sankey summary: low telomerase → high senescence → elevated ROS/MAPK → C3 inflammatory immune context — a coherent low-telomerase molecular phenotype across cancer lineages.

## Limitations

- EXTEND is expression-based (gene expression matrix input) and cannot distinguish telomerase activity driven by canonical TERT regulation from other expression confounders; it also cannot directly classify ALT-positive tumors (a noted limitation the authors flag explicitly).
- ALT mechanism is not directly compared — the pan-cancer ALT classification and validated ALT expression signatures are not available for systematic integration, so a substantial fraction of the low-telomerase group may use ALT for immortality.
- Unsupervised k = 2 stratification is a pragmatic choice; true telomerase activity likely spans a continuum, and the binary split may mask subtype heterogeneity within the two groups.
- Survival analysis uses univariate Cox regression and does not control for stage, tissue-of-origin, or mutation burden; confounding by these variables is acknowledged.
- Single-cell and spatial datasets are limited to GBM, HNSC, lung, and breast; the senescence anticorrelation at single-cell resolution has not been validated in most of the 33 cancer types.
- Causal direction is not established: it is unclear whether low telomerase activity drives senescence programs or whether senescent cell state represses telomerase expression.
