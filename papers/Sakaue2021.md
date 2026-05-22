---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Sakaue2021
type: paper
title: A cross-population atlas of genetic associations for 220 human phenotypes
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Sakaue2021
tags: []
authors:
- Sakaue et al.
datasets:
- dataset:biobank-japan
- dataset:finngen
- dataset:sakaue2021-cross-pop-meta
- dataset:uk-biobank
doi: 10.1038/s41588-021-00931-x
ontology_terms:
- dimensionality-reduction
- disease-similarity
- genetic-correlation
- phenome-wide-association
- pleiotropy
venue: Nature Genetics
year: 2021
---
## One-Sentence Summary

A cross-population GWAS atlas of 220 deep phenotypes in BioBank Japan with meta-analyses against UK Biobank and FinnGen (n=628,000 total) identifies ~5,000 new loci and uses truncated SVD decomposition of the GWAS summary-statistic matrix to derive latent genetic components that regroup diseases across ICD-10 boundaries, providing a hypothesis-free genetic basis for reconsidering human disease classification.

## Key Findings

1. **Scope expansion — 220 deep phenotypes, 519 genome-wide significant loci in EAS.** BBJ curated 159 binary disease endpoints (38 target diseases enriched by past medical history + 121 novel EMR-derived endpoints), 38 quantitative biomarkers, and 23 medication-usage phenotypes. Using SAIGE (v0.37) for binary traits and BOLT (v2.3.4) for quantitative traits on ~179,000 Japanese individuals, the study identified 519 genome-wide significant loci across disease endpoints, including 113 and 281 that were new in East Asians and globally, respectively (P < 5×10⁻⁸). Cross-population meta-analyses (n_total=628,000) identified a further 1,730 disease-associated, 12,066 biomarker-associated, and 1,018 medication-associated loci, of which 571, 4,471, and 301 were novel.

2. **Near-perfect cross-population replication.** Of 2,305 genome-wide significant variants identified in BBJ, 2,171 (94.2%, P < 10⁻³²⁵ by sign test) replicated in the same effect direction in European datasets. Genetic correlations were globally high (median r_g=0.82 between BBJ and EUR GWASs; Supplementary Table 6), indicating broadly shared genetic architecture across ancestries for these phenotypes.

3. **Pleiotropic landscape is widespread and under positive selection.** The metric SDS (singleton density score) χ² values were significantly enriched as the number of genome-wide associations per variant increased — in both Japanese and Europeans — indicating that highly pleiotropic loci were disproportionately under recent positive selection. The most pleiotropic single locus in Japanese individuals was rs671 in ALDH2 (47 associations); for Europeans, rs9265949 at the MHC locus had 46 associations. ALDH2 and MHC are established targets of positive selection in East Asians and both populations, respectively.

4. **HLA fine-mapping across 159 disease endpoints and 38 biomarkers.** Classical HLA alleles were imputed from 1000 Genomes Project Phase 3 data (n=1,037), enabling fine-mapping across the full MHC region. In BBJ, 75 independent signals were identified; in UKB, 129 signals. HLA-B in class I and HLA-DRB1 in class II carried the most associations in both biobanks. A key novel finding: HLA-DRβ1 Ser57 was confirmed to associate with pulmonary tuberculosis (OR=1.20, P=7.1×10⁻¹⁹) in BBJ — the third line of evidence for HLA's role in TB susceptibility. HLA-DRβ1 Ser57 also associated pleiotropically with Graves' disease, hyperthyroidism, Hashimoto's disease (in opposite direction), and Sjögren's syndrome, linking autoimmune and infection-related phenotypes through a shared MHC variant.

5. **ABO blood type PheWAS reveals new associations.** Blood type was estimated from three SNPs (rs8176747, rs8176746, rs8176719 at 9q34.2) and used for PheWAS across diseases and biomarkers in both biobanks. Associations confirmed include: blood-type A: increased gastric cancer risk; blood-type O: increased gastric ulcer risk; blood-type B: increased ALP levels (P<5×10⁻⁴ in both BBJ and UKB). Multiple liver function markers (ALP, GGT, AST, ALT), lipid markers, and several blood cell parameters showed significant ABO associations across populations.

6. **TSVD decomposition of the GWAS matrix recovers disease biology.** A 22,980-variant × 159-phenotype summary statistic matrix (Z-scores with shrinkage) was decomposed by truncated SVD (DeGAs framework) into 40 latent components jointly explaining 36.7% of variance. The components recapitulate ICD-10 disease classification: component 1 = diabetes (E10/E11), component 2 = cardiovascular / lipid diseases (I00–I83). Functional annotation showed component 1 genes enriched in pancreas expression (P_enrichment=5.5×10⁻⁴), component 2 in aorta (P_enrichment=1.9×10⁻³). Projection of biomarker GWAS (38 biomarkers in BBJ + UKB; 22 metabolomics cohorts in ToMMo) into the component space confirmed biological interpretability (component 1 = glucose / HbA1c genetics; component 2 = blood pressure / lipids).

7. **Cross-disease subtyping via latent components — allergic disease example.** Component 27 was shared between RA and SLE; its genes were enriched in DHS (DNase I hypersensitive sites) signatures of lymphoid tissue (P_enrichment=1.3×10⁻⁴), suggesting a common immunological mechanism for the two autoimmune diseases despite their distinct clinical presentations. For allergic diseases, components 3, 16, 26, and 34 captured two biological axes: axis-1 (IgE secretion / T-helper 2 cell biology → Type I hypersensitivity: asthma, allergic rhinitis) vs axis-2 (IL-13 / interferon secretion / C-reactive protein → Type IV / cell-mediated delayed hypersensitivity: metal allergy, contact dermatitis, atopic dermatitis). This orthogonal decomposition was not captured in the ICD-10 classification, which groups all allergy types under J/L codes irrespective of mechanism.

8. **Genetic taxonomy broadly validates current disease classifications — but identifies convergences.** Using squared-cosine scores to align diseases to components, globally similar diseases (by ICD-10) were explained by the same components. However, some cross-category convergences emerged: cholelithiasis, cholecystitis, and gall bladder polyp converged on component 10 (intestinal cholesterol absorption, bilirubin metabolism), and varicose vein GWAS in BBJ (n_case=474; 0 genome-wide significant loci) was boosted by projecting into the component space defined by the more powered EUR GWAS (n_case=22,037; 70 loci), enabling cross-population transfer of genetic signal.

## Limitations

- **159 BBJ phenotypes are pre-selected target diseases** (curated from 47 recruitment diseases + PMH/EMR expansion). The phenotype set is not a random sample of disease space — rare diseases, poorly-ICD-coded conditions, and diseases with low Japanese prevalence are underrepresented. The genetic atlas is more reflective of common, well-studied diseases, which overlaps with the same publication-volume bias that affects PubTator.
- **TSVD components order is affected by phenotype input selection.** The paper notes this as a limitation: component order and identity depend on which 159 diseases were included. The same decomposition on a different disease set would produce different components. This means the extracted "latent genetic structure" is not a universal basis for disease space, but a basis for *these 159 BBJ phenotypes in this sample*.
- **Genetic correlation only measures common-variant-mediated sharing.** Rare-variant disease architecture (Mendelian disorders, channelopathies, lysosomal storage diseases — the Track B diseases in h01) is not well captured by standard GWAS / LDSC. For diseases where rare causal variants dominate (LQTS, Fabry), GWAS-based genetic correlation will underestimate shared architecture.
- **No direct disease-progression or causal direction.** The GWAS atlas captures symmetric genetic associations; it cannot distinguish whether shared genetic components reflect common pathogenesis, shared risk factors, or ascertainment-driven comorbidity. It therefore cannot address h02's directed disease relations axis.
- **MeSH → ICD crosswalk needed for integration.** The pan-disease project uses MeSH identifiers; Sakaue2021 uses ICD-10 and phecode. Crosswalking these vocabularies will introduce mapping noise, particularly for MeSH terms that span multiple ICD-10 codes or that lack phecode equivalents.
