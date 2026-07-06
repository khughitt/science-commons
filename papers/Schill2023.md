---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Schill2023
kind: paper
title: Overcoming Observation Bias for Cancer Progression Modeling
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Schill2023
tags: []
ontology_terms:
- Mutual Hazard Networks
- cancer progression modeling
- causal inference
- collider bias
- cross-sectional sequencing
- observation bias
- somatic mutation ordering
- tumor observation event
dataset_usage:
- ref: dataset:msk-impact
  role: analyzed
  overlap: unknown
---
## Key Findings

### COAD — TP53 as observation driver

- In cMHN, APC, KRAS, and TP53 mutually suppress each other and most other events — a counterintuitive result given their known cooperative roles.
- In oMHN, TP53 is instead the strongest observation promoter (Ω = 17), with KRAS (2.4) also elevated. APC effect on observation is moderate (2.2).
- After absorbing TP53's effect into the observation node, the spurious suppression between APC and TP53 is eliminated and the model instead infers **synergy** between them — consistent with experimental evidence that TP53 mutations are under especially strong positive selection in APC-mutant colorectal cancers (Iranzo et al. 2022).
- Chronological ordering is inverted relative to cMHN: oMHN places APC early (gatekeeper) and TP53 late (observation trigger), matching the canonical Fearon–Vogelstein COAD progression sequence.
- Two prototypical routes: (1) APC–KRAS–TP53 triplet as sufficient to elicit observation; (2) BRAF–RNF43 Serrated Neoplasia Pathway, where no dominant observation driver emerges and more events accumulate before detection.

### LUAD — EGFR as observation driver

- cMHN models EGFR as broadly suppressive of most other events (mutual exclusivity in data).
- oMHN identifies EGFR as the strongest observation promoter (Ω = 11), with KRAS (3.4) also elevated, explaining most apparent mutual exclusivities as collider artifacts.
- oMHN infers synergy between EGFR and TP53 instead of the cMHN antagonism — consistent with known co-occurrence in clinical LUAD.
- Residual genuine antagonism between EGFR and KRAS is preserved in oMHN and is supported by independent synthetic-lethality evidence (Unni et al. 2015).
- EGFR-driven tumors are observed alone and early; KRAS-driven tumors accumulate more co-mutations (ATM, STK11, KEAP1) before detection.

### Model fit validation

oMHN achieves slightly better held-out log-likelihood than cMHN in both cancer types (COAD: −5.10 vs. −5.14; LUAD: −3.94 vs. −3.96), confirming that the added complexity is not overfitting.

## Limitations

- **Non-identifiability is not fully resolved:** The oMHN and its cMHN equivalent have identical observational likelihoods. Regularization breaks the tie via parsimony, not by additional data; the chosen model is the simplest, not the uniquely correct one. Interventional predictions differ between the two parameterizations and cannot be validated without experimental perturbation.
- **Cross-sectional only:** Like all CPMs in this class, oMHN infers population-level ordering from snapshots; within-patient longitudinal data are not used and the inferred chronological order cannot be validated per patient.
- **Remaining confounders:** The authors acknowledge that collider bias is one of several confounders in clinical sequencing datasets (latent environmental factors, cell-of-origin heterogeneity, mutational process variation are noted as future work).
- **Pairwise interactions only:** MHN interaction structure is pairwise (each Θ_ij is a single multiplicative scalar). Higher-order epistasis, OR/XOR logical structures (as in PMCE), and clonal heterogeneity are not modeled.
- **Binarized input:** VAF and subclonal structure are discarded; the model operates on presence/absence of mutation per tumor.
- **No temporal intervals between observations:** The model uses only a single observation time point per tumor. If paired biopsies (primary/metastasis) were available, non-identifiability could be partially resolved (as noted in Rupp et al. 2021 for cMHNs).
