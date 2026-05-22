---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Jensen2025
type: paper
title: Genetic modifiers and ascertainment drive variable expressivity of complex disorders
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Jensen2025
tags: []
authors:
- Jensen et al.
datasets:
- dataset:all-of-us
- dataset:estonian-biobank
- dataset:jensen2025-dd-cohort
- dataset:mycode
- dataset:simons-searchlight
- dataset:simons-simplex-collection
- dataset:spark
- dataset:uk-biobank
doi: 10.1016/j.cell.2025.09.012
ontology_terms:
- ascertainment-bias
- copy-number-variant
- genetic-modifier
- neurodevelopmental-disorder
- variable-expressivity
pmcid: ''
pmid: ''
venue: Cell
year: 2025
---
## One-Sentence Summary

Secondary variants in the genomic background — rare coding SNVs, CNVs, STRs, and PRSs — confer phenotype-specific risks in individuals with primary pathogenic variants (16p12.1 deletion and others), with modifier effects shaped by the primary-variant context and confounded systematically by cohort ascertainment.

## Key Findings

1. **Secondary variants explain a portion of phenotypic variance in 16p12.1 del. probands.** Among 442 individuals in 124 families (DD cohort), probands showed increased burden of missense LF variants (p = 0.034) and higher schizophrenia PRS (p = 0.009) compared with carrier parents. STRs explained 12% of variance in nervous system defects but less than 4% of variance for other features.

2. **Distinct secondary variant classes map to distinct phenotypic domains.** Rare coding variants (logOR = 0.633, p = 0.034) drove nervous system features; STRs drove nervous system and growth/skeletal features (logOR = 0.600 and 0.878 respectively); schizophrenia PRS was negatively associated with behavioral phenotypes (logOR = −0.566, p = 0.045). Combined models explained 5%–13% of variance per phenotypic domain (McFadden's pseudo-R²).

3. **Network analysis reveals proband-specific modifier pathways.** Secondary variants in probands disrupted unique pathways per individual — proband-specific "hub genes" (e.g., HRAS for ASD, AKT1 for ID/DD) mediated interactions between 16p12.1 genes and secondary variants. No overlap between first-degree connector genes was found across probands (0/40 genes per 16p12.1 gene), with only 5.8% (17/295) overlap at second degree. Each proband's phenotypic presentation reflects a personalized genomic architecture.

4. **Secondary variants cluster in neuronal subtypes and 16p12.1 NPC co-expression modules.** SNVs (missense LF) were enriched in excitatory (p = 1.22 × 10⁻⁴, FDR = 1.95 × 10⁻³) and inhibitory (p = 2.04 × 10⁻⁹, FDR = 1.14 × 10⁻²²) neurons. Gene co-expression modules from 16p12.1 NPC transcriptome data showed significant enrichment: VWA3A (p = 0.017, FDR = 0.045), CDR2 (p = 1.27 × 10⁻²², FDR = 1.43 × 10⁻²¹), MOSMO, POLR3E, UQCRC2 (p = 4.17 × 10⁻⁷, FDR = 1.88 × 10⁻⁶).

5. **Ascertainment bias systematically reverses genotype-phenotype associations across cohorts.** In 976 16p12.1 del. carriers across five cohorts (DD, SPARK, UKB, MyCode, AoU), prevalences of the same phenotype differed substantially. For example, anxiety in children: DD adults p = 9.80 × 10⁻⁵ vs UKB n.s. Deletion carriers in UKB (healthy-biased ascertainment) showed decreased missense burden vs controls (p = 0.008); carriers in AoU (disease-biased) showed increased SNV burden (p = 3.91 × 10⁻⁵). Nine meta-analysis associations were robust across children's cohorts (DD and SPARK), including intelligence PRS with ADHD (p = 0.048, FDR = 0.856) and gene duplications in constrained genes with ID/DD (p = 0.006, FDR = 0.586).

6. **Phenotype-variant associations differ by primary variant context.** Across 1,479 probands with other primary variants (16p11.2 del., dup., CHD8 SNVs, large CNVs), the secondary-variant landscape differed from 16p12.1. Among 16p11.2 deletion probands, schizophrenia PRS was associated with higher full-scale IQ (β = 0.327, p = 0.031, FDR = 0.578); secondary deletions were associated with decreased IQ (β = −0.288, p = 0.039, FDR = 0.578). In 1,528 SSC probands without primary variants, secondary variants showed minimal associations (only LF duplications with lower BMI: β = −0.086, p = 0.032), supporting a primary-variant-interaction model.

7. **13 multiplicative interaction effects identified.** Primary SNVs + secondary gene deletions on full-scale IQ (β = −0.052, p = 0.005, FDR = 0.033); primary SNVs + LF variants on SRS (β = 0.064, p = 0.002, FDR = 0.011); primary SNVs + secondary STRs on repetitive behavior (β = −0.057, p = 0.002, FDR = 0.015). Interactions were generally primary-variant-specific.

## Limitations

- Under-powered for enrichments of individual variants or genes for specific phenotypes (single-cohort sample sizes of n = 20–250).
- STRs and structural variants called from short-read sequencing have limited accuracy; long-read sequencing would improve these estimates.
- Differences in genotyping methods across cohorts preclude direct burden comparisons without harmonization.
- Environmental, sex-specific, and population-stratification effects on secondary variants are not modeled.
- The study design cannot identify non-additive synergistic interactions at scale; only 13 multiplicative interactions were detected, likely a substantial underestimate.
- The 16p12.1 deletion is a specific rare CNV; generalizability to common disease or to diseases without a dominant primary variant is not demonstrated.
