---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Ogawa2022
kind: paper
title: Somatic Mosaicism in Biology and Disease
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Ogawa2022
tags: []
ontology_terms:
- clonal hematopoiesis
- driver mutations
- mutational signatures
- positive selection
- somatic mosaicism
- tissue-specific evolution
---
## Key Findings

### Taxonomy of somatic mosaicism

The review organises mosaicism along two axes:

1. **Structural axis (tissue architecture as evolutionary container)**
   - *Sheet/squamous epithelium* (skin, esophagus): clones expand freely in horizontal and vertical directions; high clone density; strong positive selection signals. NOTCH1 mutant clones reach 57.1/cm² in skin and cover 14–21% of esophageal cells by middle age.
   - *Glandular/restricted epithelium* (intestinal crypts, colonic crypts): clones expand only at crypt fission (infrequent); neutral drift dominates within a crypt; only ~1% of normal colonic crypts carry driver mutations (vs ~60% of endometrial glands — monthly menstrual selection cycle).
   - *Hematopoietic system* (blood, bone marrow): progenitors circulate freely; systemic clonal competition; most thoroughly studied tissue. Clonal hematopoiesis (CH) reaches ~10% prevalence by age 70.
   - *Liver (cirrhotic)*: clonal selection accelerated by repetitive cell death/regeneration cycles; clonal structure bounded by fibrosis borders.

2. **Fitness axis (neutral vs selected)**
   - *Neutral clones*: arise by random mutation; maintained at low VAF; no fitness effect. Most single-nucleotide variants in healthy tissue fall here.
   - *Clonal depletion*: disadvantageous mutations are actively purged (negative selection).
   - *Clonal expansion under positive selection*: detected by elevated dN/dS > 1, recurrence across individuals, and VAF enrichment disproportionate to mutation rate. Signals identified in every tissue examined (Table 1, last column).
   - *Clonal regression*: expanded clones can shrink if the selective environment changes (e.g., LOY cells decrease to nonsmoker baseline when smoking ceases; vitamin C suppresses TET2-deficient HSPC self-renewal).

### Positive-selection signals by tissue and how they are distinguished

| Tissue | Key positively selected genes | Signal distinguishing selection from drift |
|---|---|---|
| Skin | NOTCH1, FAT1, NOTCH2, TP53, RBM10, NOTCH3 | dN/dS > 1; VAF enrichment; clone density 57.1/cm² |
| Esophagus | NOTCH1, TP53, NOTCH2, FAT1, NOTCH3 | ~120 clones/cm²; 25–42% of cells; lifestyle-correlated clone size |
| Colon | ARID1A, FBXW7, PIGR, ZC3H12A | Restricted to crypt fission events; rare (1%) |
| Endometrium | PIK3CA, PIK3CB, ARID1B, FBXW7 | ~60% of glands; correlated with parity/menstrual cycle |
| Liver (cirrhotic) | PTEN, PKD1, ARID1A, KMT2D | Enriched vs HCC spectrum; protective in mouse CRISPR model |
| Blood | DNMT3A, TET2, ASXL1, JAK2V617F | 10% prevalence by 70; computational fitness modelling |
| Lung | NOTCH1, TP53, PPM1D | 22–30/cell/year; smoking-correlated (SBS4) |

Critical distinction: **elevated dN/dS > 1 in a gene is the primary evidence of positive selection**; clone recurrence across individuals without dN/dS elevation can still reflect a large neutral drift contribution in rapidly proliferating compartments.

### NOTCH1: tissue-specific positive selection with uncertain malignant relevance

NOTCH1 mutant clones dominate normal esophageal and skin epithelia — more abundant in normal tissue than in the corresponding carcinomas (esophageal squamous cell carcinoma). This paradox (Section 4.1.2) suggests that clones positively selected in normal tissue *context* may be depleted at malignant transformation or are outcompeted by TP53 mutant clones that dominate carcinoma. Positive selection in a normal-tissue niche is not sufficient evidence of malignant potential.

### Clonal hematopoiesis (CH): the selection/drift landscape in blood

- CH with characterised driver mutations (DNMT3A, TET2, ASXL1) is age-associated and reaches ~10% by age 70; incidence modelled as growth of clones arising at a given mutation rate and expanding at a fitness effect specific to each gene.
- Fitness effect of DNMT3A^R882H is high (common driver, high fitness); spliceosome mutations (SF3B1, SRSF2) have high fitness but low mutation rate.
- ~90% of CH cases may be driven by uncharacterised mutations (non-coding, epigenetic, structural) — targeted exome panels miss the majority.
- Loss of Y chromosome (LOY) in blood: prevalence 2.5% at 40, 43.6% by 70; associated independently with all-cause mortality, cardiovascular disease, Alzheimer's disease, and solid cancer risk; 156 LOY-associated germline GWAS variants identified — LOY is at least partly a heritable instability trait.
- Cancer therapy reshapes the CH landscape toward DDR gene mutations (PPM1D, TP53, CHEK2) under genotoxic selective pressure — a clear demonstration of extrinsic selection.

### Context-dependence of mosaicism consequences

A major theme is that the same driver clone can be beneficial, neutral, or harmful depending on tissue context:
- ARID1A/KMT2D mutations: protective against liver injury in cirrhosis mouse models.
- DNMT3A CH: accelerates cardiovascular disease via IL-6/NLRP3-mediated inflammation, but the same clone in transplant donors reduces disease relapse by enhancing graft-versus-host immune response.
- NOTCH1 expansion: may protect against esophageal squamous cell carcinoma rather than promoting it.
- LOY: reversible (regression upon smoking cessation), suggesting context-dependence of the selective pressure.

### Clonal regression as a distinct evolutionary mode

Clonal regression is described as a fourth evolutionary mode (beyond neutral, depletion, expansion): expanded clones can shrink when the environment changes. Examples: LOY regression after smoking cessation; TET2-deficient HSPC self-renewal suppressed by vitamin C restoring TET2 activity. This mode is therapeutically relevant — clones that appear irreversible may be pharmacologically reversible.

## Limitations

- Review does not present new primary data; all claims are synthesised from cited studies with heterogeneous sequencing technologies, sample sizes, and analytic approaches.
- Most positive-selection evidence (dN/dS) comes from targeted exome sequencing, which the authors note misses ~90% of driver mutations in CH (non-coding, structural, epigenetic variants); this likely applies to other tissues too.
- "Brain somatic mosaicism" is explicitly excluded; brain mosaicism arises primarily during development (single-cell level) rather than via post-developmental clonal competition, and requires a separate framework.
- The cardiovascular tissue mutational landscape is described as largely uncharacterised — a stated gap.
- Causality between CH clones and cardiovascular outcomes is plausible but mostly correlational; mechanistic studies are cited but limited to mouse models.
- The NOTCH1 paradox (protective in normal esophagus, not oncogenic) is noted but not resolved.
- LOY causal vs marker status for disease outcomes is explicitly left open.
