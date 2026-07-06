---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Karczewski2024
kind: paper
title: Pan-UK Biobank GWAS improves discovery, analysis of genetic architecture, and
  resolution into ancestry-enriched effects
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Karczewski2024
tags: []
authors:
- Karczewski et al.
doi: 10.1101/2024.03.13.24303864
ontology_terms:
- SNP-heritability
- genetic-ancestry
- genome-wide-association-study
- phenome-wide-association
venue: medRxiv (preprint)
year: 2024
dataset_usage:
- ref: dataset:uk-biobank
  role: analyzed
  overlap: unknown
---
## Key Findings

1. **14,676 novel associations from multi-ancestry meta-analysis.** Of 237,360 significant LD-independent associations across 431 phenotypes, 14,676 (6.2%) were not significant in EUR-only GWAS. These arise from three mechanisms: (a) bolstered EUR signals crossing GWS threshold with mixed models, (b) ancestry-enriched variants at higher MAF in non-EUR groups, and (c) increased total sample size.

2. **Ancestry-enriched variants as a discovery lever.** Meta-analysis novel loci were 6-fold enriched for variants more common in AFR (4-fold in any non-EUR ancestry). Key example: rs193059864 near *CAMK2D* associated with triglycerides (meta-analysis p = 1.5 × 10⁻⁸; EUR p = 0.0017), with allele frequency 1.6% in AFR but only 1.4 × 10⁻⁴ in EUR — a 114-fold enrichment.

3. **3,112 associations novel relative to Open Targets Genetics.** Of 71,372 EFO-mapped LD-independent associations, 3,112 (4%) were not previously identified. The X chromosome disproportionately contributes: 573 of 2,448 X-chromosome associations (23%) were novel, likely due to historical exclusion of chrX from many GWAS.

4. **Pleiotropic G6PD signal highlights ancestry-specific biology.** A missense variant in *G6PD* (rs1050828; chrX) has frequency 16% in AFR but ~1.5 × 10⁻⁴ in EUR. It associates significantly with five phenotypes in AFR (glycated hemoglobin HbA1c, red blood cell count, RBC distribution width, high light scatter reticulocyte count, mean sphered cell volume; meta-analysis p = 1.1 × 10⁻²⁹⁹ for HbA1c) but is inaccessible to EUR-only analysis. Fine-mapping in AFR alone produces sensible credible sets; meta-analytic fine-mapping is unstable because the AFR group explains an outsized fraction of variance.

5. **Heritability landscape across ancestry and trait types.** SNP-heritability estimates are positively correlated across EUR and CSA (York regression slope = 0.49, p = 5 × 10⁻¹²). Biomarkers/continuous traits have highest heritability (EUR average h² = 0.19 and 0.16, respectively); disease (ICD) and prescription phenotypes have lowest (h² = 0.021 and 0.016). Within-EUR, heritability of high-quality traits is broadly consistent with prior published estimates.

6. **PITX2 allelic series.** rs77767351 near *PITX2* is genome-wide significant for keratometry (3mm weak meridian-right; p = 1.2 × 10⁻¹⁰; N = 89,664), not previously reported in GWAS. Common variant association with corneal curvature, while rare pLoF variants in *PITX2* cause Axenfeld-Rieger syndrome — demonstrating an allelic series spanning common trait variation to rare Mendelian disease.

7. **Meta-analysis vs mega-analysis.** The two-step meta-analysis outperforms a single-step mega-analysis in genomic control (λ_GC closer to 1) for most traits, with comparable or improved discovery. This result justifies the methodological design choice for multi-ancestry studies with highly imbalanced sample sizes.

## Limitations

- **Extreme ancestry imbalance.** EUR (420k) vs AFR (6.6k) — a 63-fold imbalance. Fine-mapping across ancestries is unstable when a minority ancestry group drives most of the variance (G6PD case). Power in non-EUR groups is substantially lower: fewer than 10% of non-EUR phenotypes have ≥ 3 associated loci vs 25% in EUR.
- **Preprint status.** As of the PDF (October 2024), this is not peer-reviewed.
- **Phenotype definitions vary.** Mapping to EFO/Open Targets Genetics required semi-manual curation of only 42% of traits; cross-study phenotype comparison remains a challenge.
- **Genetic ancestry as discrete bins.** The paper explicitly cautions that ancestry groups are a pragmatic statistical convenience and do not reflect discrete biological entities. Continuous admixture methods (e.g., Tractor, local ancestry) were only run as a pilot.
- **No pan-phenome genetic correlation matrix released.** The summary statistics enable computing cross-disease genetic correlations, but this analysis is not in the paper itself. Using Pan-UKB as a disease-similarity external axis requires downstream computation.
- **Disease (ICD/phecode) heritability is low.** Average h² = 0.021 for ICD disease phenotypes; many disease traits would not survive the heritability QC filter, limiting the usable disease set for a genetic-correlation axis.
