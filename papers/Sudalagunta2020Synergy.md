---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Sudalagunta2020Synergy
kind: paper
title: A pharmacodynamic model of clinical synergy in multiple myeloma
version: "1.0.0"
created: "2026-05-29"
updated: "2026-05-29"
bibkey: Sudalagunta2020Synergy
tags: []
ontology_terms:
- combination-synergy
- drug-combinations
- ex-vivo-drug-sensitivity
- multiple-myeloma
- pharmacodynamic-modeling
---
## Key Findings

- **Ex vivo synergy rate (LD50 metric):** 21.43% of combinations (roughly 1 in 5) were synergistic ex vivo by median LD50 at 96 h at p < 0.05.
- **Ex vivo synergy rate (AUC metric):** 18.42% of combinations were synergistic ex vivo by AUC.
- **Clinical synergy rate:** Clinical synergy was predicted for only 1 in 10 combinations (8.69% of those with PK data), reflecting the dampening effect of pharmacokinetics and real-world dosing schedules.
- **Top clinically synergistic combinations identified:** daratumumab/bortezomib, carfilzomib/panobinostat, selinexor/dexamethasone, and selinexor/liposomal doxorubicin — all four consistent with subsequent or contemporaneous clinical trial evidence.
- **Clinically beneficial (not necessarily synergistic) combinations:** five additional pairs identified as superior to either single agent in clinical simulation, including carfilzomib/dexamethasone, bortezomib/dexamethasone, carfilzomib/pomalidomide, bortezomib/pomalidomide, and dexamethasone/venetoclax.
- **SAM validation:** Checkerboard assay shows SAM accurately predicts off-diagonal concentration responses from fixed-ratio parameterization alone; Pearson r uniformly > 0.93 across 25 concentration duplets.
- **Dynamic synergy:** Synergy is a time-varying phenomenon; the pharmacokinetic trajectory of drug concentrations traverses regions of synergy and antagonism in 3D concentration-time space, so the net clinical effect can be synergistic even when the combination is locally antagonistic at some concentrations.
- **Ex vivo AUC as a clinical response classifier:** Ex vivo combination AUC is an excellent classifier of CR/VGPR vs. worse (ROC AUC = 0.9804, p = 0.0006). Ex vivo synergy (ΔAUC Synergy) was the better classifier between PR/MR and SD/PD (ROC AUC = 0.8167, p = 0.0452).
- **Patient heterogeneity dominates:** Most combinations are not synergistic across the majority of patients, but may be synergistic for a specific patient subpopulation; synergy maps (3D heat maps over concentration × time) differ substantially even among similarly classified (e.g., early relapse/refractory) patients.

## Limitations

- **Two-drug scope by direct fitting:** SAM is parameterized for pairs; three-drug extensions rely on an independence assumption for higher-order terms (validated conceptually but not fully tested empirically in this paper).
- **PK data availability bottleneck:** Clinical synergy simulation requires phase I PK data for the combination, restricting the analysis to 46 of 130 combinations tested.
- **Fixed-ratio parameterization of SAM:** SAM's interaction parameters are estimated from fixed concentration-ratio ex vivo data; the checkerboard validation is limited to two patients per combination pair, which may not capture full inter-patient variation.
- **Cell culture microenvironment:** Ex vivo reconstruction captures bone marrow microenvironment via patient plasma and co-cultured stromal cells, but cannot fully replicate in vivo immune interactions, drug distribution, or clonal evolution under treatment pressure.
- **MM-specific cohort:** All 203 patients are MM; generalizability of the specific interaction parameter estimates to other cancer types is undemonstrated, though the SAM mathematical framework is disease-agnostic in principle.
- **No direct prospective clinical validation:** Clinical predictions are benchmarked against published trial outcomes at the cohort level, not against prospective individualized predictions in this study.
- **Cytotoxic assay endpoint:** LD50/AUC endpoints measure cell kill; non-cytotoxic combination effects (e.g., differentiation, immune modulation) are outside the model's scope.
