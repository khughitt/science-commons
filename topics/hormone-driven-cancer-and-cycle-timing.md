---
schema_profile: science-entity-base/1.0+topic/2.0
id: topic:hormone-driven-cancer-and-cycle-timing
type: topic
title: Hormone-driven cancer and menstrual-cycle timing of therapy
version: "1.0.0"
created: "2026-05-28"
updated: "2026-05-28"
tags: []
ontology_terms:
- ESR1-mutation
- breast-cancer
- cancer
- chronotherapy
- endocrine-resistance
- estrogen-receptor
- oestrous-cycle
- tumour-microenvironment
related:
- hypothesis:h02-rhythm-confounding-of-biomarkers
- hypothesis:h03-menstrual-cycle-systemic-control
- question:07-cycle-aware-precision-medicine
- question:09-hormone-driven-disease-dynamics
- theme:reproductive-cycles
source_refs:
- cite:Bernhardt2020
- cite:Bornes2024
- cite:Clusan2023
- cite:Miziak2023
---
## Summary

Estrogen-receptor-positive (ER+) breast cancer is the field's most documented case of a hormone-driven disease whose biology, biomarkers, and treatment response are modulated by the reproductive hormone cycle. Four papers define this space from complementary angles: two mechanistic reviews establish how ERα and GPER transduce cyclic estrogen into oncogenic gene programs and how ESR1 mutations eventually decouple tumours from that hormonal drive; a clinical review documents that standard diagnostic biomarkers and genomic assay scores fluctuate measurably across menstrual-cycle phases in premenopausal patients; and a Nature primary study demonstrates in multiple mouse models and two retrospective human cohorts that the oestrous/menstrual-cycle stage at chemotherapy initiation causally determines tumour drug sensitivity, with macrophage influx, vascular remodelling, and EMT-state shifts as the mechanistic arms.

Together these papers make a unified argument: the menstrual cycle is not a nuisance covariate but an active upstream driver that (a) generates oscillatory tissue signals measurable in tumour biomarkers, (b) reshapes the tumour microenvironment independently of tumour-cell hormone receptor status, and (c) defines clinically exploitable windows for diagnosis and chemotherapy timing.

## Current State of Knowledge

### ER signaling: genomic and non-genomic arms

ERα (encoded by *ESR1*) is the primary oncogenic driver in ~70-75% of breast cancers. Ligand-bound ERα dimerises, translocates to the nucleus, and binds estrogen-responsive elements (EREs) to upregulate proliferation and survival genes (MYC, Cyclin D1, FOXM1, BCL2, IGF-1, CXCL12). It also tethers to AP1 and SP1 transcription factors at serum-responsive elements. In parallel, a membrane-anchored ERα pool and the G-protein-coupled receptor GPER activate PI3K/AKT, Ras/MAPK, and cAMP cascades within minutes of estrogen binding, without nuclear translocation. Both arms converge on cell-cycle progression and survival. GPER is independently expressed in breast cancer cells and mediates rapid signaling; tamoxifen acts as a GPER agonist, contributing to acquired resistance in some ER+ tumours. Coregulator networks (coactivators AIB1/SRC-3, PELP1; corepressors NCOR1, BRCA1) and post-translational modifications of ERα (phosphorylation at S118, S167, Y537; ubiquitylation; sumoylation) further tune transcriptional output.

### ESR1 mutation and endocrine resistance

ESR1 mutations cluster in the ligand-binding domain and are rare in primary tumours (<5%) but prevalent in ~21-50% of metastatic or endocrine-treated tumours. D538G and Y537S are most common. Mutant ERα is constitutively active, more stable, binds coactivators more avidly, resists fulvestrant, and shifts target gene sets toward motility and metastasis. Resistance beyond ESR1 mutation involves PI3K/AKT/mTOR and Ras/MAPK pathway hyperactivation, CDK4/6-RB-E2F alterations, and coregulator imbalance. CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) combined with aromatase inhibitors or next-generation SERDs (elacestrant, FDA-approved 2023) are current first- and second-line standards for ESR1-mutant metastatic disease.

### Cycle/oestrous-stage modulation of tumour biology and chemo sensitivity

The menstrual cycle generates a ~28-day (human) or ~4-6-day (mouse) oscillation in estrogen and progesterone that reshapes tumour-intrinsic gene expression, microenvironment composition, and drug accessibility:

- **Biomarker oscillation:** ER and PR positivity, Ki67, HER2 expression, and 21-gene Oncotype DX scores all vary across menstrual-cycle phase in premenopausal patients. Cross-sectional biopsies without cycle-phase annotation yield measurements confounded by the phase at which the sample was collected.
- **Proliferative state:** Tumour cell proliferation (EdU, PHH3) peaks at oestrus/follicular phase and falls at dioestrus/luteal phase, mirroring normal mammary gland cycling. Intravital imaging confirms this as synchronised clone expansion rather than stochastic noise.
- **EMT state:** Mesenchymal (E-cad-low) tumour-cell fraction rises at dioestrus, increasing intrinsic chemoresistance.
- **Tumour vasculature:** Intratumoural vessel diameters contract at dioestrus, impairing drug delivery.
- **Macrophage infiltration:** Tumour-associated macrophages accumulate at dioestrus; anti-CSF1R depletion restores oestrus-level chemo sensitivity, establishing macrophage flux as a causal effector of the cycle-phase effect. The immunosuppressive macrophage surge persists after chemotherapy disrupts the cycle, explaining why the initial-stage effect endures across multi-cycle treatment.

The biological mechanism is not dependent on tumour-cell hormone receptor expression: HR-negative (Brca1−/−Trp53−/−) mouse tumours and transplanted tumours in ovariectomised hosts show the same oestrus-favourable pattern, confirming that the cycle modulates the tumour microenvironment rather than acting solely through direct tumour-cell steroid signaling.

## Key References

- Miziak 2023 — comprehensive ER signaling review covering ERα/ERβ/GPER1, genomic/non-genomic arms, PTM regulation, ESR1 mutation landscape, and therapeutic landscape [@Miziak2023]
- Clusan 2023 — concise mechanistic map of ER signaling pathways, ERα isoforms (ERα46, ERα36), GPER tamoxifen agonism, and resistance mechanisms [@Clusan2023]
- Bernhardt 2020 — clinical review: menstrual cycle as under-appreciated confounder of ER/PR/Ki67/Oncotype DX in premenopausal breast cancer diagnosis and surgical timing [@Bernhardt2020]
- Bornes 2024 — Nature primary study: oestrous cycle stage causally determines mammary tumour chemosensitivity via macrophage, vascular, and EMT mechanisms; retrospective human progesterone-phase signal [@Bornes2024]
