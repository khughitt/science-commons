---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Pietzner2021
type: paper
title: Mapping the proteo-genomic convergence of human diseases
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Pietzner2021
tags: []
authors:
- Pietzner et al.
datasets:
- dataset:fenland-study
- dataset:gtex
- dataset:nhgri-gwas-catalog
doi: 10.1126/science.abj1541
ontology_terms:
- disease-similarity
- genetic-colocalization
- phenome-wide-association
- protein-quantitative-trait-loci
pmcid: ''
pmid: ''
venue: Science
year: 2021
---
## Key Findings

1. **Scale and novelty of pQTL landscape.** 10,674 variant-protein associations covering 2,548 genomic regions and 3,892 distinct protein targets; 1,097 regions (≈43%) were novel at time of publication. 64% (867/1,356) of cis-pQTLs replicated in a prior Olink-based dataset (P < 0.05, directionally consistent).

2. **Pleiotropic loci are hubs of protein regulation.** 194 loci with cis-pQTLs associated with 2–50 protein targets (pleiotropic associated variants, PAVs), including major metabolic loci (ABO, GCKR, APOE). PAV-linked pQTLs are enriched for actively secreted proteins (39.6% vs 33.7%, P = 0.04) and enriched for protein-altering variants including disulfide bonds (4.2%), α-helices (3.1%), and β-strands (2.6%).

3. **Genetic architecture of the plasma proteome.** For ~1/3 of protein targets (n=1,249), >50% of genetic variance is explained by one or more cis-pQTLs. For 7.2% (n=282), protein- or pathway-specific trans-pQTLs account for most genetic variance. Median explained variance 2.7% (IQR 1.0–7.6%), reaching up to 70% for individual proteins (e.g. vitronectin).

4. **cis-pQTLs colocalize extensively with gene expression and splicing.** Half (50.1%) of all cis-pQTL signals are shared with an eQTL in at least one of 49 GTEx v8 tissues. Alternative splicing accounts for approximately 1-in-5 of these (20.1% = 212 cis-pQTLs with colocalized sQTLs), demonstrating plasma proteomics as a proxy for tissue-specific functional effects. 145 protein targets showed evidence of tissue-specific expression contributions, including vitamin K-dependent protein C (liver) and hepatitis A virus cellular receptor 1 / TIM-1 (transverse colon).

5. **cis-pQTLs prioritize candidate causal genes at GWAS loci.** Of 558 risk loci for 537 phenotypes with a colocalized cis-pQTL, 24.6% (≈137) implicated a protein/gene not reported or different from the gene prioritized by eQTL mapping. Example: PRSS8 (prostasin) prioritized for Alzheimer's disease risk at the KAT8 locus (r² = 0.96 with lead signal, PP = 98%); a 13% reduction in AD risk per 1 SD higher plasma prostasin was estimated (OR 0.87, 95% CI 0.82–0.91, P = 3.8 × 10^−8). Another example: RSPO1 for endometrial cancer (PP = 98.2%, 91% increased risk per 1 SD higher R-spondin-1, OR 1.91, P = 3.6 × 10^−8).

6. **Proteo-genomic map: 1,859 gene-protein-phenotype connections.** The map covers 412 protein targets and 506 curated phenotypes. It highlights large cross-disease biological convergence: shared genetic signals (PP >80%) for interleukin-family proteins (IL-12 p40, IL-23, IL-6 receptor subunits) link autoimmune diseases, whereas coagulation proteins (Prothrombin, PAI-1, Factor H) bridge cardiovascular and inflammatory phenotypes.

7. **Cross-disease convergence in the map: EFEM1/FBLN3 as a connective tissue hub.** The genetic signal at the EFEMP1 locus (rs3791679, MAF = 23.4%), encoding fibrillin-like extracellular matrix protein 1 (FBLN3), was shared across diverse connective tissue disorders consistent with abnormal elastic fiber morphology (Efem1 knockout mice display hernias and pelvic organ prolapse). A-allele carriers showed lower plasma FBLN3 and increased risk for carpal tunnel syndrome, hernias, varicose veins, contact lens use (proxy for myopia), inguinal hernia, and hypermobility — a biologically coherent cluster that had not been connected by previous individual GWAS.

8. **SULT2A1 and gallstones: mechanistic mode-of-action example.** The shared cis-pQTL at SULT2A1 colocalized with cholelithiasis (cholecystomy odds ratio per 1 SD higher protein: 2.12, P < 2 × 10^−37) and cholecystectomy (OR 2.09, P = 7.8 × 10^−38). Multitrait colocalization revealed concurrent association with plasma concentrations of multiple sulfated steroids (including sulfated conjugates of androgen and pregnenolone metabolites) and primary bile acids — pointing to supersaturated bile promoting cholesterol crystallization as the mode of action at SULT2A1.

9. **COVID-19 outcomes: multi-omics triangulation.** Integration of GWAS summary statistics for four COVID-19 outcome definitions identified NSF (N-ethylmaleimide-sensitive factor) and BCAT2 as suggestive candidates. ABO and OAS1 were replicated across different outcome definitions. The PNPLA3 trans-pQTL rs738408 (a known nonalcoholic fatty liver disease variant) was shared with 22/70 liver-expressed protein targets including metabolic and detoxification enzymes, providing a community-specific trans-pQTL example.

10. **Drug target identification and repurposing.** 60 protein targets linked to at least one phenotype; 22 to a disease; 31 candidates with repurposing opportunities (1–8 different indications, 32 different indications total). Established examples replicated include IL-6 receptor for rheumatoid arthritis and thrombin for deep venous thrombosis. Open Targets prioritization strategy applied.

## Limitations

- **European-descent cohort only (n=10,708 Fenland Study).** Replication in ethnically diverse populations is required, particularly for drug target prioritization. Common-variant pQTL effect sizes may not generalise.
- **Healthy, middle-aged cohort.** Participants are generally healthy adults (ages ~40–65). Plasma protein concentrations under disease states may differ substantially from the healthy baseline used to establish pQTL associations.
- **SomaScan aptamer specificity.** The affinity-reagent (aptamer) technology captures protein abundance but may miss isoforms not represented by the binding epitope, and is semiquantitative. The vitronectin PAV example (rs704, MAF 47.3%) suggests conformation-altering variants can modify measurement rather than expression — a known SomaScan artifact class.
- **Trans-pQTL biology is opaque.** 39% of classified pQTLs are "unspecific trans" — their biological mechanism is difficult to interpret. These may reflect general cis-genetic control of shared pathway outputs and could mislead cross-disease inference if used naively.
- **GWAS summary statistics limited to public catalog (January 2021).** Cancer, rare diseases, and understudied conditions are underrepresented in the map because GWAS coverage is uneven. The map is discovery-complete only for traits with large GWAS.
- **Colocalization at PP >80% is permissive.** The PP threshold retains some false positives; the authors acknowledge sensitivity to outcome definition in the COVID-19 examples, and causal-gene assignments retain uncertainty (14.2% of cis-regions had protein-encoding gene as one of several longer candidate lists).
- **No MeSH identifier crosswalk published.** The disease/phenotype nodes in the proteo-genomic map use GWAS catalog trait labels, not standardized MeSH or Disease Ontology identifiers. Linking this map to the pan-disease project's MeSH-based similarity matrices requires a mapping step (see h03 uncertainty on crosswalk).
