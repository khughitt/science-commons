---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Burrell2013
kind: paper
title: The causes and consequences of genetic heterogeneity in cancer evolution
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Burrell2013
tags: []
ontology_terms:
- branched evolution
- chromosomal instability
- clonal evolution
- genomic instability
- intratumour heterogeneity
- microsatellite instability
- mutation processes
- treatment resistance
---
## Key Findings

**Heterogeneity topology**
- Both inter- and intratumour heterogeneity are extensive; within-tumour subclones can intermingle spatially or be physically separated by barriers such as blood vessels.
- Branched (not only linear) evolutionary trajectories are documented across cancer types: colon adenoma-to-carcinoma transition, ALL, CLL, pancreatic cancer, and breast cancer.
- Multi-region sampling demonstrates that copy-number profiles of spatially separated biopsies can resemble different patients' tumours more than adjacent biopsies of the same tumour.

**Genomic instability as the driver of heterogeneity**
- Most solid and haematopoietic tumours display at least one form of genomic instability (chromosomal instability, CIN; microsatellite instability, MSI; or others).
- CIN arises through both mitotic (spindle attachment/checkpoint) and pre-mitotic (DNA replication stress, DSB repair, telomere dysfunction) mechanisms; the paper emphasises that structural and numerical CIN cannot be considered mechanistically separate.
- Twenty-plus mutation signatures were catalogued in 30 cancer types (citing Alexandrov et al. 2013), reflecting distinct exogenous and endogenous mutational processes.
- Genomic instability can be dynamic over tumour progression: mutation patterns shift between early and late stages; tetraploidy may precede chromosomal instability.

**Instability subtypes have distinct clinical correlates**
- MSI colorectal tumours associate with better prognosis and profuse immune infiltration compared with CIN tumours; this may relate to neoantigen repertoire from mismatch repair deficiency.
- ER− breast, squamous NSCLC, serous ovarian, and gastric cancers show an association where the highest quartile of CIN has better prognosis than intermediate CIN quartiles ("paradoxical" CIN-outcome relationship).
- Treatment can act as a transient exogenous source of instability: alkylating agents (temozolomide in glioblastoma) can select for loss of mismatch repair and drive hypermutation at relapse; AML chemotherapy raises base-transversion frequency at relapse.

**Therapy implications**
- Clonally dominant (truncal) events — EGFR/KRAS mutations in lung cancer, VHL loss in renal carcinoma — are more therapeutically tractable targets than subclonal lesions.
- Pre-existing low-frequency KRAS subclones conferring anti-EGFR antibody resistance were detectable in circulating tumour DNA 5–6 months post-treatment in colorectal cancer patients, demonstrating that resistance mutations exist before treatment in many cases.
- Phenotypic heterogeneity is not purely genetic: clonally homogeneous subclones can behave differently after chemotherapy through varied proliferation/quiescence states and epigenetic divergence — a non-genetic axis of heterogeneity.

**Optimal instability hypothesis**
- Excessive instability is lethal (mitotic catastrophe, mutational meltdown); there may be an optimal, tolerated level of instability that maximises evolvability without causing cell death.
- This framing implies that pushing instability beyond tolerance could be therapeutic (e.g., PARP inhibitors in BRCA-mutant tumours, centrosome clustering inhibitors in CIN tumours).

## Limitations

- Review was written in 2013; many cited NGS studies were small (8 AML patients, 11 glioblastomas, 21 breast cancers). The empirical base has expanded enormously since.
- The paper does not quantify the selection vs drift balance — drift is mentioned but not modelled; all examples are selected to illustrate Darwinian dynamics.
- Non-genetic heterogeneity (epigenetic, micro-environmental) is acknowledged late and briefly; the review is primarily a genomic-instability-centric account.
- CIN "paradox" (higher CIN → better outcome in some cancers) is noted but not mechanistically resolved.
- No single-cell resolution data; the subclonal inference relies on bulk multi-region sequencing and FISH, which limits resolution of low-frequency subclones.
- The "optimal instability" hypothesis is conceptual and not formally modelled.
