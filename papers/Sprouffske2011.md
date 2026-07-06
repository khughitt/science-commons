---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Sprouffske2011
kind: paper
title: Accurate Reconstruction of the Temporal Order of Mutations in Neoplastic Progression
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Sprouffske2011
tags: []
ontology_terms:
- agent-based model
- cell lineage reconstruction
- clonal evolution
- colorectal cancer
- cross-sectional inference
- intratumor heterogeneity
- loss of differentiation
- mutational order
- neoplastic progression
- phylogenetic methods
---
## Key Findings

- **Simulated tumor heterogeneity:** At cancer detection, each tumor comprised a mean of 256 distinct clones (SEM = 17); the largest clone made up 67% (SEM = 2%) of the tumor. Shannon diversity index mean = 1.7 (SEM = 0.1). Fifty distinct temporal orders of phenotypic mutations were found across 91 cancers, with no single universal order.
- **Cross-sectional path model fails:** The cross-sectionally inferred order was: loss of differentiation → evasion of apoptosis → limitless replicative potential → sustained angiogenesis → genomic instability → self-sufficiency in growth signals → insensitivity to antigrowth signals. Only 7.3% ± 1.0% of cells per tumor acquired mutations in this order; 41% of tumors had zero cells consistent with the path model; 68% of tumors had ≤1% of cells consistent.
- **Oncogenetic tree improves slightly but still fails:** 11.5% ± 2.2% of cells per tumor were consistent with the oncogenetic tree, still with 41% of tumors having zero consistent clones.
- **Cell lineage reconstruction succeeds:** The intratumor phylogenetic approach recovered the true temporal order in 99.7% ± 0.1% of cells. Increasing from 5 to 10 sampled cells improved this only marginally (to 99.9%).
- **Loss of differentiation is the most common first step:** In 72% of cells that survived to cancer, loss of differentiation was the first phenotypic mutation acquired. The paper argues this may be a near-universal first lesion across cancer types because disrupting differentiation is necessary to allow further somatic evolution.
- **Necessary and sufficient mutations for cancer in the model:** Loss of differentiation, evasion of apoptosis, and sustained angiogenesis were the necessary and sufficient phenotypes for progression to cancer in simulations.
- **Two evolutionary regimes coexist:** Both clonal selective sweeps (transient homogenization) and clonal interference (multiple competing subclones preventing fixation) were observed, sometimes within the same tumor. Intratumor diversity generally increased over time, with occasional dips when a dominant clone (especially after loss-of-differentiation) briefly fixed.
- **Transient clones cause cross-sectional artifacts:** Clones that temporarily expanded early in progression and then went extinct (due to competition or telomere failure) are "detected" at intermediate-size cross-sections, injecting false signals into the inferred ordering.
- **Empirical support:** Re-analysis of Smith et al. (2002) colorectal data found only 26.2% of real patient biopsies consistent with the canonical Fearon-Vogelstein path — consistent with the simulation prediction that cross-sectional path models poorly reflect true tumor histories.

## Limitations

- The agent-based model simulates a colon crypt at population sizes below clinical detection thresholds; sensitivity analyses support generalization to larger sizes, but the model does not incorporate spatial geometry beyond crypt scale.
- The model tracks phenotypes (hallmarks), not specific genes or mutations. It cannot address whether specific driver genes (APC, KRAS, TP53) follow a preferred order even within the hallmark framework.
- Perfect-information assumption for cell lineage reconstruction is optimistic; experimental noise in single-cell or multi-biopsy sequencing will reduce accuracy below the 99.7% simulation figure.
- Only colorectal cancer parameters are used; the generalization to other cancer types is argued biologically (especially for loss of differentiation as the first step) but not computationally demonstrated.
- The model does not incorporate immune selection, epigenetic variation, stromal interactions, or spatial tumor architecture beyond the crypt, all of which may shape the actual evolutionary regime sequence.
- No fitness landscape is explicitly modeled; fitness effects of each hallmark are fixed parameters rather than context-dependent or epistatic values.
- The empirical validation (Smith et al. 2002 re-analysis) is observational; the paper cannot directly demonstrate that cell lineage reconstruction in real patient samples achieves the predicted 99.7% accuracy.
