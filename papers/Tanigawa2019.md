---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Tanigawa2019
type: paper
title: Components of genetic associations across 2,138 phenotypes in the UK Biobank highlight adipocyte biology
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Tanigawa2019
tags: []
datasets:
- dataset:uk-biobank
ontology_terms:
- GWAS
- adipogenesis
- biobank
- dimensionality-reduction
- genetic-architecture
- phenome-wide-association
- pleiotropy
---
## Key Findings

1. **Genome-phenome latent structure is recoverable at scale.** K=100 TSVD components on the 2,138-phenotype UK Biobank summary statistic matrix explain 41.9% (all variants), 62.8% (coding), and 75.5% (PTVs) of variance. The first five components capture anthropometric/body-composition axes, eye measurements, bioelectrical impedance, reticulocyte counts, and body-fat-vs-lean partitioning.

2. **BMI genetic architecture decomposes into interpretable sub-components.** For BMI, the top component (PC2; phenotype squared cosine score 0.47) is driven by fat mass and percentage measurements (61.5% phenotype contribution). PC1 corresponds to fat-free mass (healthy part of body weight; 32.7% fat-free contribution). PC30 (0.04) is linked to non-melanoma skin cancer and childhood sunburn phenotypes (28.7% fat mass). The top three components together explain >69% of BMI's genetic associations.

3. **Myocardial infarction and gallstone genetic components are biologically coherent.** MI top components associate with lipid metabolism (PC22: high cholesterol, statin/atorvastatin intake, APOC1), alcohol (PC100), and sleep/food intake (PC83) — 36% of MI genetic associations collectively. Gallstones top components include fresh fruit, water, and bioelectrical impedance (51% of associations). GREAT ontology enrichment for MI confirms cardiac enrichment (artery occlusion fold=10.57, p=2.28×10⁻¹⁴; aortitis fold=9.36, p=3.41×10⁻³¹); for BMI, enriched terms include brachypodia (fold=9.05, p=1.4×10⁻²²), increased birth weight (fold=6.21, p=1.3×10⁻¹⁰), and increased liver weight (fold=2.27, p=1.67×10⁻²²).

4. **DeGAs component-specific enrichment terms are highly specific (low Jaccard overlap).** Median pairwise Jaccard index of GREAT-enriched gene sets across 100 DeGAs components = 0.029, confirming that latent components capture distinct biological processes rather than a shared generic gene set.

5. **PTVs point to *GPR151* and *PDE3B* as top obesity candidates.** For the PTV dataset, PC1 (28% phenotype contribution) and PC3 (12%) are the top key components for BMI; top contributing PTVs are in *PDE3B* (19.0%), *GPR151* (12.3%), and *ARTBT1* (8.5%) for PC1 and in *TMEM91*, *EML2-AS1*, *KIAA0586* for PC3. PheWAS of rs114285050 (*GPR151* stop-gain) confirms strong associations with waist circumference (beta = −0.065, p=2.5×10⁻⁸), whole-body fat mass (beta = −0.069, p=1.4×10⁻⁷), trunk fat mass (beta = −0.071, p=1.5×10⁻⁷), and BMI (beta = −0.129, p=4.2×10⁻⁸); heterozygous carriers (n=7,560) show 0.324 kg m⁻² lower BMI than average (p=4.13×10⁻⁷). PheWAS of rs150090666 (*PDE3B* stop-gain, n=947 heterozygous) shows 0.647 kg m⁻² higher BMI (p=2.09×10⁻⁴).

6. **Functional validation: *GPR151* is required for preadipocyte-to-adipocyte conversion.** siRNA knockdown of *Gpr151* by three independent siRNAs in 3T3-L1 preadipocytes drastically impaired adipocyte differentiation: reduced expression of Pparg, Cebpa, and Fabp4 (all p<0.001–0.01), markedly reduced lipid droplet formation (Oil Red O; p<0.001), and dramatically lower basal and ISO-stimulated lipolysis (p<0.001). *GPR151* mRNA is low in preadipocytes but rises ~10-fold during human SGBS adipogenesis. *GPR151* overexpression in sorted APC+ cells showed endogenous expression is sufficient for differentiation (overexpression did not further enhance it).

7. ***PDE3B* plays a role in differentiated adipocytes, not preadipocyte conversion.** *PDE3B* mRNA increases ~3,000-fold during human SGBS adipogenesis but its knockdown did not impair preadipocyte differentiation or lipolysis in 3T3-L1 cells, consistent with its known function as a cAMP/cGMP hydrolyzing enzyme in mature adipocytes. *PDE3B* PTVs associate most strongly with hip circumference (lower-body subcutaneous fat deposition) rather than central obesity.

## Limitations

- **White British-only cohort:** All 337,199 individuals are self-reported White British; generalizability of latent components to other ancestries is not established.
- **GWAS summary statistics, not individual-level data:** DeGAs operates on summary Z-scores; it cannot distinguish causal variants from LD proxies, and genetic correlations among components are not fully disentangled.
- **K=100 fixed truncation:** The choice of K=100 is empirical (computational efficiency); components beyond K=100 are discarded. Biological signal in lower-variance components is not characterized.
- **Functional validation scoped to adipocyte biology:** The paper validates only the two top candidates from the adiposity component. The biological interpretability of components for disease outcomes (MI, gallstones) relies entirely on GREAT enrichment and PheWAS; no direct functional experiments were done for those traits.
- **3T3-L1 and SGBS are immortalized cell lines:** Adipocyte findings may not translate directly to in vivo human adipose biology; *GPR151* overexpression data are confounded by partial infection in the cell population.
- **Coding and PTV strata are very small:** 784 PTVs in the UK Biobank at MAF>0.01% leaves the PTV analysis severely underpowered for anything but the strongest effect variants.
