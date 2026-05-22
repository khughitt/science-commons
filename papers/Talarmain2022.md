---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Talarmain2022
type: paper
title: HOXA9 has the hallmarks of a biological switch with implications in blood cancers
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Talarmain2022
tags: []
datasets:
- dataset:talarmain2022-mpn
- dataset:tcga
ontology_terms:
- HOXA9
- acute myeloid leukaemia
- bistable switch
- boolean network
- clonal branching
- computational network model
- epigenetic memory
- mutation order
- myeloproliferative neoplasm
- positive feedback loop
---
## Key Findings

### HOXA9 bimodality and AML stratification

- HOXA9 expression is significantly bimodal in 173 AML patients (p < 2.2 × 10⁻¹⁶); bimodality is intrinsic, not driven by sequencing artefacts or external/clinical covariates.
- High HOXA9 is a marker of poor prognosis (HR 0.29 for low expression, log-rank p = 6 × 10⁻⁵), independent of FAB subtype or molecular classification.
- High HOXA9 associates with M0 and M5 FAB subtypes; low HOXA9 with PML-RARa, RUNX1-RUNXT1, and CBFB-MYH11 (CBF-AML) chromosomal abnormalities, consistent with the literature.
- Within individual FAB classes (M2, M4) high vs. low HOXA9 still separate survival, confirming the switch is not a surrogate for FAB class.

### JAK2/TET2/HOXA9 motif explains mutation-order branching

- The double mutant (JAK2 + TET2) has two distinct stable fixpoints depending on mutation acquisition order:
  - **JAK2-first then TET2:** HOXA9 locked HIGH → elevated erythroid differentiation, increased thrombosis risk, early clinical detection, ruxolitinib sensitivity (consistent with Ortmann 2015 clinical data).
  - **TET2-first then JAK2:** HOXA9 locked LOW → elevated CMP expansion, ruxolitinib insensitivity, late detection.
- The self-activating HOXA9 loop is the mechanistic memory store: JAK2 activation raises HOXA9 to a self-sustaining level; subsequent TET2 loss then cannot lower it (HOXA9 is independent of TET2). In TET2-first patients, HOXA9 is inactivated before JAK2 arrives, and JAK2's hyperactivation alone cannot overcome low-HOXA9 stability at the low concentration present.
- RUNX1 expression is unchanged by JAK2 mutation after TET2 loss (Fig. 3c), consistent with the "switching" property being HOXA9-loop-dependent.
- Removing the HOXA9 self-loop from the model eliminates or destabilises the bifurcation (Figs. S5–S7), demonstrating the loop is necessary for mutation-order sensitivity.

### NOTCH pathway and JAK2 → GMP link

- XGBoost applied to TCGA identifies JAK2 as highly correlated with the NOTCH pathway (second-ranked after RTK-RAS), with ITCH among the top SHAP-score genes in NOTCH.
- Literature search finds a pathway: JAK2 → STAT5 → MAPK → JNK1 → ITCH → NOTCH degradation, implicating NOTCH suppression as a tumour-suppressive consequence of JAK2/MAPK elevation, explaining GMP expansion observed in JAK2-mutant MPN.
- MPN mouse microarray (Chen 2015) validates NOTCH pathway and HOXA9 bimodality in the model's predictions.

### Experimental validation

- HOXA9 knockdown (shHOXA9) in JAK2-mutant haematopoietic stem/progenitor cells significantly increases colony formation relative to wild-type (q = 0.0171) and TET2-mutant (q = 0.0032) cells, consistent with the model prediction that JAK2 activates HOXA9 and that HOXA9 inhibition would disinhibit progenitor expansion.
- TET2-mutant response to HOXA9 knockdown is more complex (synergistically increased survival at q = 0.0032), consistent with the JAK2/TET2 interaction being non-linear.

### Additional predicted interactions

- Model predicts RUNX1 inhibits MYB, and MYB inhibits CMP expansion; RUNX1 is supported as an inhibitor of SPI1 and GATA1. These are consistent with conditional RUNX1 knockout causing enhanced CMP frequencies in mice (Ichikawa 2004, 2008).
- NOTCH predicted to have a suppressive role in MPN GMP cells — novel prediction, validated indirectly by SHAP analysis and MPN microarray.

## Limitations

- **Discrete model only:** The Boolean network uses 0/1/2 activity states and cannot capture gradients of expression, stochastic switching rates, or heterozygous/dosage effects. Continuous ODE or stochastic modelling could test robustness of the bistability to noise.
- **Small experimental validation:** Colony assays used 3 biological replicates per condition; the validation is supportive but not conclusive for the full mechanistic chain (JAK2 → STAT5 → HOXA9 → self-loop).
- **Mouse model discrepancy:** Model predicts HOXA9 is always activated by JAK2, but Chen 2015 mouse microarray data shows low HOXA9 expression in JAK2-mutant animals — the paper attributes this to assay system differences (murine vs. human) and does not fully resolve it.
- **AML cohort limited by size:** Low-HOXA9 peak contains only 31 patients; survival analysis within subgroups (FAB subtypes M2, M4) is underpowered.
- **Network edges from mixed species:** Regulatory interactions were compiled from mouse and human studies; not all edges have been independently validated in a single homogeneous system.
- **No single-cell resolution:** Whether HOXA9 bimodality reflects distinct clonal populations or cell-state switching within a polyclonal tumour cannot be resolved from bulk RNA-seq data.
- **Mutation order not directly measured:** The clinical validation relies on Ortmann 2015 cohort data where mutation order was inferred from clonal sequencing; direct in vivo experimental proof of the order-dependent HOXA9 locking is not presented.
- **NOTCH pathway prediction partially indirect:** The JAK2–NOTCH link is inferred from XGBoost ranking + SHAP + literature chain; no direct experimental intervention on the NOTCH pathway in JAK2-mutant MPN cells is reported here.
