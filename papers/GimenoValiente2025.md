---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:GimenoValiente2025
type: paper
title: DNA methylation cooperates with genomic alterations during non-small cell lung cancer evolution
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: GimenoValiente2025
tags: []
datasets:
- dataset:tracerx
ontology_terms:
- DNA methylation
- NSCLC
- TRACERx
- allosteric chromatin transition
- dosage compensation
- epigenomic evolution
- intratumor heterogeneity
- somatic copy number alterations
---
## Key Findings

### Methylation landscape and heterogeneity
- Unsupervised clustering of the 5,000 most variable CpGs identifies three CpG clusters (Cluster 1: promoter CpGs hypomethylated in normal, hypermethylated in tumor — enriched for developmental genes SOX1, SOX9, HOXD3/8, TBX4 and TSGs; Cluster 2: LUSC-specific hypomethylation; Cluster 3: cohort-wide hypermethylation).
- Histological subtype (LUAD vs. LUSC) is the only clinical feature distinguishing tumors in methylation PCA.
- ITMD ~25-fold higher inter-tumor vs. intra-tumor, indicating substantial inter-patient variation but significant intra-patient heterogeneity. Intergenic/enhancer regions show the highest methylation variability; promoters show the lowest, indicating tighter regulatory constraint.
- ITMD correlates with SCNA-ITH but not with SNV-ITH — methylation heterogeneity tracks structural rather than point-mutation instability.

### MethSig cancer gene identification
- MethSig algorithm applied to CAMDAC-deconvolved data identified 99 candidate DNA methylation driver genes in LUAD and 118 in LUSC; 63 shared between subtypes.
- MethSig genes were significantly more ubiquitously methylated (clonal) within tumors than canonical TSGs or random genes — interpreted as early, clonally fixed methylation events.
- MethSig genes were significantly more downregulated in tumors than canonical TSGs or random genes.
- MethSig genes enriched in developmental transcription factors (PCDHGA3, EVX1, HOX clusters) and genes implicated in plasticity (ZNF-154) — early inactivation of developmental genes may lock cells into stem-like states.
- LUAD MethSig genes specifically enriched in HOX clusters; HOX gene methylation increased in samples with reduced tumor-infiltrating lymphocytes (TILs; P = 0.0065).

### Cooperation between methylation and CN alterations
- In canonical NSCLC TSGs: only 24.6% had concordant methylation + CN loss across tumors. Most tumors use a single mechanism for TSG inactivation.
- MethSig cancer genes showed a significantly higher proportion of concordant events (hypermethylation + CN loss co-occurrence) compared to canonical TSGs or random genes (P = 1.2 × 10⁻⁶ and P = 3.5 × 10⁻³).
- Parallel convergent events (same TSG inactivated independently by both mechanisms in different tumor regions) more prevalent in LUSC (4.6%) vs. LUAD (1.5%; P = 5.06 × 10⁻⁷), indicating stronger convergent selection on TSG silencing in LUSC.
- Linear effects model on multi-region data: **synergistic effect** of CN loss and DNA hypermethylation on downregulation of RPL22 and MGA (LUAD) and EPHA2 (LUSC) — double-hit expression suppression confirmed.

### AllChAT: oncogene amplification → chromatin closure → passenger gene hypermethylation
- Genes with higher expression that scales with amplification (oncogene behavior) show *reduced* methylation when amplified; genes with reduced or equivalent expression when amplified (dosage-compensated behavior) show *increased* methylation when amplified.
- Dosage-compensated yellow genes enriched in EMT, KRAS signaling, immune pathways, and transmembrane channels.
- RAC1 and CDK4 (recurrently amplified oncogenes) are significantly less methylated when amplified — consistent with expression-scaling oncogene behavior.
- Dosage-compensated essential genes (RPS3, near CCND1) significantly enriched at oncogene-proximal loci (P = 0.028).
- ChIP-seq validation: TMTC1 (essential gene 9 Mb from oncogene SOX9) and the essential gene DDX42 (9 Mb from SOX9) show AllChAT signatures. LRRC34 shows methylation-dependent dosage compensation co-amplified with PI3KCA in both tumor PDCs.
- Proposed mechanism: CN amplification → allosteric chromatin remodeling (closed H3K27me3 at neighbors) → hypermethylation of neighboring essential/passenger genes → their silencing, maintaining stoichiometric balance.

### M_R/M_N metric and positive selection
- M_R/M_N > 1 in MethSig cancer genes: genes with strong correlation between epimutation and gene expression are under positive selection for functional silencing. In LUAD, HOX genes PAX6 and ITGA8 (M_R/M_N > 1) enriched in cancer progression, morphogenesis, motility, transcriptional regulation.
- Three LUAD MethSig genes with M_R/M_N > 1 (CYP4F2, MSC, EIFSA2) associated with worse disease-free survival (multivariate Cox; P = 0.022, P = 0.02, P = 0.011).
- Validated: M_R/M_N ratio between test and validation cohorts (Spearman's rho = 0.603, P < 2.2 × 10⁻¹⁶). True positive rate 84%, true negative rate 80%; sensitivity 80.7%, specificity 83.3% (chi-squared P < 1.07 × 10⁻²²).

### Methylation in preinvasive lesions
- Expansion to a preinvasive NSCLC cohort: VIPR2 and ZNF714 were already methylated in preinvasive lesions (suggesting early methylation events).
- Co-occurrence with driver mutations in CDKN2A and STK11 was only significant in LUAD (P = 2.5 × 10⁻⁰³ and P = 1.9 × 10⁻⁰⁷), suggesting early DNA methylation events at specific loci can predict subsequent genomic trajectories.

## Limitations

- RRBS covers ~1.8 M CpGs, representing ~25% of non-CpG-rich regulatory regions (e.g., FANTOM5 enhancers), which limits detection of enhancer-level methylation changes. The authors acknowledge this explicitly.
- M_R/M_N metric relies on regulatory CpGs proximal to the TSS (±2.5 kb) and does not capture distal cis-regulatory changes (enhancers >2.5 kb, silencers). Cis-regulatory mutations in promoters could interfere with the metric.
- 1.3% of promoter CpGs are associated with chromatin modifiers and show a positive correlation between methylation and gene expression — this subset is excluded from M_R/M_N logic but could confound aggregate analyses if prevalent.
- AllChAT is validated in PDCs (primary patient-derived cultures) and EpiATLAS; the chain from CN amplification → chromatin change → methylation change is inferred from cross-sectional data with ChIP-seq as mechanistic evidence, not from time-resolved perturbation experiments. The temporal ordering (amplification precedes chromatin change precedes methylation) is biologically plausible but not directly demonstrated in a live-cell time course.
- The cohort is 59 patients (small for detecting rare gene-level events). Subtype-specific analyses (LUAD n=32, LUSC n=20) are further underpowered.
- The preinvasive lesion cohort is not fully characterized in the main text; the timing inference (methylation before vs. after genomic drivers in preinvasive settings) requires caution given likely cross-sectional design.
- CAMDAC relies on tumor purity and CN estimation accuracy; 26 samples were excluded due to low coverage or low tumor cell fraction.
