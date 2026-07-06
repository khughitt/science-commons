---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Demela2023
kind: paper
title: Cross-disorder genetic analysis of immune diseases reveals distinct gene associations
  that converge on common pathways
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Demela2023
tags: []
authors:
- Demela et al.
doi: 10.1038/s41467-023-38389-6
ontology_terms:
- autoimmune-disease
- eQTL-colocalization
- genetic-pleiotropy
- immune-mediated-disease
- latent-factor
venue: Nature Communications
year: 2023
dataset_usage:
- ref: dataset:decode-pqtl
  role: analyzed
  overlap: unknown
- ref: dataset:immune-mediated-disease-gwas
  role: analyzed
  overlap: unknown
- ref: dataset:onekik
  role: analyzed
  overlap: unknown
---
## Key Findings

1. **Three distinct genetic groupings of immune diseases.** Genomic SEM identifies three latent factors: F_gut (CD, UC, PSC; loading coefficients 0.57, 0.16, 0.72), F_aid (JIA, SLE, RA, T1D; loadings 0.17, 0.48, 0.67, 0.74), and F_alrg (asthma, eczema; loadings 0.49, 1.0). Inter-factor genetic correlations are low: F_gut–F_aid r = 0.39, F_gut–F_alrg r = 0.08, F_aid–F_alrg r = 0.09.

2. **Loci are highly factor-specific.** Of 301 conditionally independent signals, 67 are specific to F_gut, 60 to F_aid, and 67 to F_alrg. Only 4 overlap F_gut and F_aid, 2 overlap F_gut and F_alrg, 6 overlap F_aid and F_alrg, and only 1 is shared across all three. Only 9% of loci show significant Q_SNP heterogeneity, indicating the three-factor model accounts for 91% of SNP-level genetic structure.

3. **Factor-associated genes converge on the same pathways despite distinct loci.** KEGG pathway enrichment for all three factors identifies JAK-STAT signalling, Th1/Th2 cell differentiation, cytokine receptor interaction, and Th17 cell differentiation. The pathway enrichment is driven by different genes in each factor: STAT3 is associated with F_gut, STAT4 with F_aid, and STAT5A/STAT6 with F_alrg. In the JAK-STAT pathway, JAK2 is specific to F_gut/F_aid while TYK2 is specific to F_alrg.

4. **Cell-type enrichment converges on memory T cells and activated T cell subsets.** CELLECT analysis of PBMC scRNA-seq shows enrichment for CD4+, CD8+, and unconventional T cells across all three factors; NK cells enriched for F_gut and F_aid only. Regulatory T cells show the strongest enrichment. No enrichment observed in naive T cells or B cell populations. Tonsillar scRNA-seq confirms this enrichment pattern in CD4+ T cells, Tregs, and plasmablasts.

5. **46 eQTL colocalizations across immune cell types.** 46 in F_gut, 49 in F_aid, 20 in F_alrg (PP4 ≥ 0.9). Only 37 of 301 loci have any sc-eQTL detected, highlighting the need for larger eQTL cohorts. Example: BLK eQTL in memory B cells colocalizes with F_aid (PP4 = 0.98); increased BLK expression is protective against F_aid diseases, consistent with rare BLK loss-of-function variants causing SLE.

6. **Eight colocalized genes are known drug targets, four are novel candidates for repurposing.** Previously used targets: CTLA4 (abatacept; protects against F_aid), IL4R (dupilumab; protects against F_alrg), ERAP2, ITGA4. Novel repurposing candidates: BLK (protective for F_aid), CD48 (protective for F_aid; EAE models), PTGER4 (protective for F_gut; colocalizes in NK cells), and GBA. Of 13 colocalized pQTL genes, 3 are current drug targets (IL6R, IL2RA, ERAP2).

7. **Mendelian Randomization confirms directional effects for drug-relevant loci.** Increased LRRC32 expression (a TGF-β signalling regulator) raises risk for F_alrg diseases (MR beta significant); increased PTGER4 expression in NK cells protects against F_gut; increased BLK expression in memory B cells protects against F_aid. The CTLA4 locus MR shows increased CTLA4 expression is protective for F_aid, providing genetic support for abatacept-like CTLA4 enhancement.

## Limitations

- **European-ancestry GWAS only.** Genomic SEM and LDSC require samples of the same ancestry. All nine diseases use European-ancestry cohorts; whether the same three-factor structure holds in African-, East Asian-, or admixed-ancestry cohorts is untested.
- **Latent factors are not interpretable causal entities.** The three factors represent shared genetic predisposition, not disease mechanisms. Diseases within a factor may differ substantially in downstream biology even while sharing upstream GWAS signals.
- **Only 37 of 301 loci have sc-eQTL support.** The OneKIK cohort (n = 982) is underpowered for many cell-type-specific eQTLs; the 46 colocalizations are a lower bound. Many trans-diagnostic loci cannot yet be mechanistically resolved.
- **Coloc PP4 ≥ 0.9 threshold is stringent.** Some true colocalizations may be missed; the paper acknowledges that larger eQTL cohorts are needed.
- **pQTL analysis uses DECODE (Icelandic ancestry); no LD reference for Icelandic population.** The authors tested only the primary pQTL effect, not conditionally independent secondary signals — a known limitation noted in the text.
- **Disease factor loadings are low for some diseases.** PSC loads at 0.72 on F_gut but with residual variance; JIA at 0.17 and UC at 0.16 have weak factor loadings, suggesting incomplete capture by the three-factor model.
- **No longitudinal or multimorbidity structure.** The analysis captures cross-sectional genetic sharing; progression from one disease to another (e.g., UC → PSC, RA → JIA) is not addressed.
