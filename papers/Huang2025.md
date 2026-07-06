---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Huang2025
kind: paper
title: Single-cell multi-omic integration analysis prioritizes druggable genes and
  reveals cell-type-specific causal effects in glioblastomagenesis
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Huang2025
tags: []
ontology_terms:
- GWAS
- Mendelian randomization
- causal inference
- cells of origin
- drug repurposing
- glioblastoma
- sc-eQTL
- single-cell multi-omics
- tumor microenvironment
dataset_usage:
- ref: dataset:huang2025-glioma-gwas
  role: analyzed
  overlap: unknown
---
## Key Findings

### Candidate gene counts

- **Pan-glioma:** 24 putatively causal genes; 6 high-confidence (EGFR, TERT, MDM4, SOX8, CDKN2A, STMN3).
- **GBM:** 26 putatively causal genes; 5 high-confidence (EGFR, CDKN2A, JAK1, TERT, STMN3).
- **Non-GBM:** 33 putatively causal genes; 4 high-confidence (CDKN2B, IDH1, NPAS3, ZGPAT).
- **41 novel** glioma-associated molecules prioritized relative to prior tissue-level studies; no high-confidence targets overlap between GBM and non-GBM subtypes (consistent with biological subtype heterogeneity).
- Genes enriched in cerebral cortex (FC = 2.74, P adj = 3.96E-2), supporting tissue-specific drug-target potential.
- CRISPR/RNAi: 88.5–93.8% of identified genes enriched across multiple tumor cell types; 51.72% (30/58) selective or essential in glioma lines; 53.6% of novel genes showed selective dependency or essentiality in glioma.

### Cells of origin

- Malignant cells (P adj = 1.03E-09), **astrocytes** (P adj = 1.14E-11), and **OPCs** (P adj = 1.51E-10) show significant association with GBM GWAS risk via snRNA-seq trait enrichment.
- OPCs show significant GBM heritability enrichment by scATAC-LDSC (44.10-fold; P = 0.038, P_coeff = 0.042); astrocytes trend but do not reach significance (31.97-fold; P = 0.075).
- Pseudotime trajectories from GBM snRNA-seq corroborate astrocyte and OPC as cells of origin.

### Cell-type-specific causal effects (sc-eQTL)

- **14 cell-type–gene pairs** involving **12 genes** identified via sc-eQTL colocalization; 58.3% novel relative to bulk tissue analyses.
- Three high-confidence cell-type-specific causal genes:
  - **EGFR** — astrocyte-specific causal effect; rs6964933 (within EGFR gene body) is the astrocyte-specific causal variant (PIP = 0.10).
  - **CDKN2A** — OPC-specific causal effect.
  - **JAK1** — excitatory neuron-specific causal effect.
- **85.7% (12/14) of cell-type-specific effects involve non-GBM-relevant cells** (oligodendrocytes, neurons, other glia), not the canonical astrocyte/OPC populations.
- Oligodendrocytes account for 8/12 (66.7%) of cell-type-specific causal genes.

### EGFR: germline vs. somatic duality

- Germline-level: increased astrocyte-specific EGFR expression (genetically predicted) is **inversely** associated with GBM susceptibility — higher constitutive expression in normal astrocytes is protective at the germline level.
- Somatic-level: EGFR is amplified in ~50% of GBMs; pseudotime and TME ligand-receptor analyses show EGF pathway interactions (EGFR + ligands) are upregulated in the TME during tumor progression — a distinct somatic oncogenic dynamic that emerges after malignant transformation.
- The germline-protective / somatic-oncogenic duality illustrates why bulk tissue GWAS-to-gene mapping can be misleading without cell-type context.

### TME cell communication

- 1,129,369 cells; 846 signaling genes analyzed.
- Significantly elevated cell-cell communication in GBM TME vs. healthy brain, particularly between neurons and trait-relevant cells (astrocytes, OPCs).
- Neuron–astrocyte–OPC communication elevation is consistent with neuronal hijacking as a glioma growth mechanism.

### Causal phenotypes (MR-PheWAS)

- Telomere length: only trait with robust causal evidence for pan-glioma after Bonferroni correction (OR = 1.888, 95% CI 1.521–2.344; P_IVW = 8.37E-9).
- Suggestive: cognitive proficiency / educational attainment / intelligence inversely associated with non-GBM risk; schizophrenia positively associated with non-GBM risk.

### Drug repurposing

- 87 drugs targeting 28 prioritized genes identified in clinical trials: 57 for tumor therapy, 21 for brain diseases, 18 for glioma.
- Example: Tertomotide hydrochloride (TERT inhibitor, approved for pancreatic cancer) crosses BBB effectively — flagged as repurposing candidate.

## Limitations

- GWAS subtypes based on pre-WHO-2021 classification (IDH-mutant high-grade astrocytoma may be misclassified as non-GBM); authors argue this likely does not bias PRS estimates given IDH1 appearing only in non-GBM.
- Brain-specific multi-omics bias: detected genes are enriched in brain tissue/cells, which is appropriate for target discovery but may miss plasma-accessible targets not requiring BBB crossing.
- sc-eQTL power is inherently limited for rarer cell types; the 14 identified cell-type–gene pairs likely undercount true cell-type-specific effects.
- Relaxed replication threshold (P = 0.05) between GWAS/QTL datasets due to sample size disparity — some candidates may be false positives.
- Causal phenotype claims (MR-PheWAS) are associational; LCV analysis reduces but does not eliminate confounding by shared genetic architecture.
- All analyses are cross-sectional; no longitudinal or clonal evolution data — cannot directly address mutation timing relative to epigenetic/expression state changes.
