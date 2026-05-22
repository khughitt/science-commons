---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:JimenezSanchez2026
type: paper
title: Transcriptomic Plasticity Is a Hallmark of Metastatic Pancreatic Cancer
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: JimenezSanchez2026
tags: []
datasets:
- dataset:egad00001011109
- dataset:htan
ontology_terms:
- archetype analysis
- clonal phylogenetics
- epithelial-mesenchymal transition
- metastasis
- organ-specific adaptation
- pancreatic ductal adenocarcinoma
- single-cell RNA-seq
- transcriptomic plasticity
---
## Key Findings

### Cohort and clonal structure
- 62 clones resolved, 4 primary clones (2 metastatic, 2 non-metastatic). Metastatic primary clones had significantly more CNAs than non-metastatic clones (amplification of KRAS^G12V locus universal in all metastatic clones).
- Liver metastases most closely related to metastasizing primary clones — liver likely the initial metastatic site, consistent with the known PDAC liver-first pattern.
- Peritoneal metastases composed of several phylogenetically diverse clones (some unique to each peritoneal site), suggesting limited intermetastatic seeding and strong local adaptation.
- Each metastatic site seeded by multiple clones in independent events. Stomach wall metastases show extensive parallel seeding from the primary.

### Archetype programs (what distinguishes metastatic vs. primary plasticity)
- 19 integrated archetype clusters across sites, broadly categorized as: core EMT programs (AC1/4/16 — mesenchymal, MYC-high, HLA-I–high); cell-cycle; gastrointestinal adaptation; lipid metabolism; stress/UPR programs.
- **Site-shared archetypes** (AC1, AC4, AC16): expressed across ≥5 sites; all EMT/mesenchymal. Metastatic clones from the primary already expressed mesenchymal phenotypes, whereas non-metastatic primary clones retained epithelial phenotypes. This suggests EMT programs are pre-established in disseminating clones (not solely acquired post-arrival), while additional organ-specific programs are acquired at the metastatic site.
- **Site-specific archetypes:**
  - AC5 (stomach wall): gastrointestinal program — intestinal (CDH17, RHPN2, MYC17, TMEM45B), stomach (CRAC2B, TF2F2B, MYO1A, TM4SF20), and gallbladder (TMC5, FCGBP, MUC5B) modules. PDAC cells acquire transcriptional programs of GI epithelium non-native to the pancreas.
  - AC2 (peritoneum): lipid metabolism and oxidative stress/detoxification — fatty acid and cholesterol biosynthesis (HMGCS1, SQLE, FDFT1, ACAT2, MVD, FADS2, SCD, FASN, PCSK9), aldo-ketoreductases (AKR1B10, AKR1C1, AKR1C3), prostaglandin regulators (PTGIS, PTGR1), redox balance (GCLM, GCLC, GPX2, GSR). Program recapitulates adipocyte metabolic features; adipose tissue fraction is elevated in peritoneal vs. primary tumor sections by histopathology.
  - Lipid anabolism (AC2) validated in a second independent patient with peritoneal PDAC metastasis (untreated, succumbed within 3 months), confirming the phenotype is not patient-specific or treatment-driven.

### Plasticity is non-genetic (the central mechanistic claim)
- **Mantel test:** Phylogenetic distance matrices and phenotypic composition (archetype) distance matrices are weakly correlated (Mantel statistic = 0.13, p < 1×10^-5), meaning clones that are closely related genetically do NOT necessarily express similar phenotypes — phenotype is largely independent of genotype.
- **AC2 lipid-anabolism clones:** AC2-enriched clones (>10% AC2 cells) are spread across **all three major clades** of the phylogeny (early branches AND late branches), and diverse clones populate both peritoneal sites (A and B). This is inconsistent with clonal selection model, which would predict site-specific clades.
- **PLASTRO scores vs. CNA burden:** Cells with few CNAs have low PLASTRO scores; more advanced clones (extensive CNAs) score high (Pearson r = 0.575, p = 1×10^-6). Higher genomic instability correlates with higher transcriptomic plasticity — interpreted as genomic instability creating a permissive chromatin state for phenotypic exploration, not as specific genotype encoding the phenotype.
- **Per-clone archetype entropy:** Mean observed entropy = 1.42 (SD not reported). Significantly higher than "site-constrained random shuffle" null model (μ = 0.97), but lower than "random assignment" null (μ = 2.42). Clones are more phenotypically diverse than their site composition would predict, but less diverse than random — cells exhibit meaningful but bounded plasticity within clones.
- **PLASTRO global Mantel test statistic:** 0.13 (scale –1 to 1, 0 = no correlation between phylogenetic and phenotypic distance within clones). This quantifies the degree to which plasticity — not lineage — dominates phenotypic state.

### Plasticity is the cause, not the consequence, of metastatic colonization (authors' argument)
- Metastatic primary clones already display mesenchymal phenotypes in the primary tumor; non-metastatic primary clones are epithelial. This is consistent with plasticity being *pre-requisite* for dissemination, not simply a response after arrival.
- Organ-specific programs (AC2, AC5) are acquired after site-specific colonization (AC2 clones from opposite peritoneal flanks share the same transcriptional adaptation despite being phylogenetically distant). These programs are interpreted as responses to local environmental cues (adipokines, lipid availability, GI epithelial signals) rather than pre-specified genetic programs selected before dissemination.
- The authors explicitly propose a paradigm: "strong environmental effects are imposed on highly plastic cancer cells during metastatic dissemination" — plasticity enables flexible response, and the environment provides the selecting signal at each site.

### Comparison to "primary plasticity"
- The paper does not directly compare plasticity levels in primary vs. metastatic cells using the same quantitative PLASTRO framework (PLASTRO is applied to clones, not per-site). However, the observation that KRAS amplification (a universal metastatic clone feature) correlates with PLASTRO score suggests metastatic cells are *quantitatively more plastic* than primary non-metastatic cells, not just different in the programs they express.
- Site-specific programs (AC5 GI, AC2 lipid) are predominantly found in metastatic sites and largely absent from primary PDAC — suggesting these represent genuinely *metastasis-specific* plasticity outputs, not amplification of programs already active in the primary.

## Limitations

- **N=1 patient.** All conclusions rest on a single 35-year-old patient with unusually aggressive metastatic PDAC at diagnosis, an age and presentation that are not typical. The authors argue the transcriptional programs match those of published 43-patient cohorts (Gavish et al. 2023; refs 48, 78) but this cross-cohort validation is at the level of program identity, not plasticity quantification.
- **Rapid autopsy timing.** All samples collected postmortem (within 2 hours of death, biospecimens within 1 hour). Transcriptomes reflect a specific terminal disease state; early metastatic colonization dynamics are not captured. mRNA decay gradients across sites could bias archetype assignments.
- **CNA noise.** IntegrateCNV produces false negatives for deletions (acknowledged); PICASSO uses minimum-clone-size filter (75 cells) and minimum-confidence filters that may discard biologically real small subclones. The 62-clone solution is an approximation.
- **No temporal sampling.** The rapid autopsy captures a single time point; the causal claim (plasticity enables colonization) is inferred from spatial patterns, not longitudinal observation. The claim that mesenchymal primary clones *became* metastatic (rather than being a selected metastatic subpopulation that returned mesenchymal cells to the primary) cannot be fully ruled out.
- **Clonal selection not ruled out, only quantified as minor.** The Mantel r = 0.13 is weak but non-zero (p < 10^-5). Some phenotypic variance *is* lineage-associated; the paper shows plasticity dominates but does not show selection is absent.
- **Non-epithelial compartments not characterized.** Stromal, immune, and endothelial cells were identified but not systematically analyzed. Whether the plasticity of cancer cells depends on stromal signals from the niche (vs. cell-autonomous) is not tested.
- **One pancreatic cancer subtype.** KRAS^G12V + TP53 missense (standard PDAC), no BRCA2/SMAD4/CDKN2A variant analysis with phenotypic correlation. Whether plasticity magnitude differs by mutational background is unknown.
