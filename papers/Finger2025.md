---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Finger2025
type: paper
title: Tissue mechanics in tumor heterogeneity and aggression
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Finger2025
tags: []
datasets: []
ontology_terms:
- CAF
- ECM stiffness
- EMT
- YAP/TAZ
- cancer stem cells
- extracellular matrix
- fluid pressure
- genomic instability
- mechanotransduction
- plasticity
- solid stress
- tumor heterogeneity
- viscoelasticity
---
## Key Findings

### Mechanical taxonomy: roles in heterogeneity vs. aggression

| Mechanical parameter | Primary driver of heterogeneity | Primary driver of aggression | Both | Key mechanism |
|---|---|---|---|---|
| **ECM stiffness** (elastic modulus, Pa) | Yes — spatial stiffness gradients (STIFMaps) correlate with EMT/slug marker heterogeneity | Yes — activates Rho/ROCK, YAP/TAZ, PI3K/AKT, MAPK/ERK, FAK; drives survival, invasion, metastasis | Yes | Integrin-β1/αv ligation, discoidin receptor activation, syndecan engagement |
| **Viscoelasticity** (stress relaxation) | Yes — increases with tumor grade and progression; surrounds PanINs | Yes — amplifies TGF-β activation via ECM mechanical force; drives pro-metastatic programs | Yes | Latent TGF-β activation by mechanical force on ECM-stored TGF-β |
| **Solid stress** (compressive + tensile) | Yes — promotes genomic instability via nuclear rupture | Yes — impedes lymph drainage, elevates interstitial fluid pressure, drives hypoxia | Yes | Nuclear deformation → replication stress → chromosomal gains/losses; vascular collapse → hypoxia → HIF |
| **Fluid/interstitial pressure** | Limited direct evidence for heterogeneity per se | Yes — impedes drug delivery; alters immune cell chemoattractant gradients | Aggression-dominant | Dense ECM + solid stress → elevated ISF pressure → poor vascular perfusion |
| **Shear stress** | Yes — TAM amoeboid migration along linearized fibronectin bundles | Yes — contributes to invasion and metastatic dissemination | Both | Oriented ECM bundles as migration highways for tumor cells and immune cells |
| **Traction forces** (cell-generated) | Yes — myCAF and MSC traction reorganizes ECM into linearized bundles | Yes — long-range forces guide tumor cell migration direction | Both | Rho-ROCK-MyosinII actomyosin contractility; LOX/LOXL2 crosslinking |

### Heterogeneity-driving mechanisms in detail

1. **Stiffness heterogeneity within tumors:** STIFMaps (machine-learning convolution of collagen architecture) reveal profoundly heterogeneous stiffness within the same tumor stroma. Heterogeneously stiff regions correlate with elevated β1-integrin activation and EMT (SLUG-positive) marker expression. The invasive front of breast tumors is significantly stiffer than the tumor core, which is paradoxically compliant. Stiffness heterogeneity in Her2+ breast cancer predicts poor patient outcome.

2. **Genomic instability from mechanical confinement:** Tumor cells migrating through a dense, stiffened ECM exhibit nuclear envelope rupture — this favors genomic alterations by increasing replication stress. Tumor cells forced through rigid small pores accumulate chromosomal losses and gains reminiscent of genomic instability. High solid stress is associated with compromised mitotic integrity and sustained chromosomal anomalies. Chronic inflammation potentiated by tissue fibrosis and ECM stiffening additionally elevates mutational load via myeloid-mediated ROS-stimulated DNA damage. Women with high mammographic density (stiffer stroma) have elevated rates of DNA double-strand breaks in mammary epithelial cells, attributed to ROS from infiltrating macrophages.

3. **CSC frequency expansion:** Stiff ECM directly promotes self-renewal (stiff fibrin → enhanced melanoma CSC renewal; hepatoma and breast CSCs show enhanced stemness in stiff matrix; stiff matrix increases CSC marker expression). ECM-CSC interactions engage specific transmembrane receptors to promote CSC properties; ECM tension promotes ERK-RANK signaling to increase CSC frequency. Mechanotransduction can both expand pre-existing CSC subpopulations (selection) and transdifferentiate non-CSC cancer cells into CSCs (plasticity). The CSC niche at the pre-metastatic site is similarly modified by tumor-shed extracellular vesicles that remodel resident fibroblasts and induce CAF activation.

4. **CAF and MSC heterogeneity as heterogeneity amplifier:** Three CAF subtypes (myCAFs, iCAFs, apCAFs) have distinct mechanical and secretory profiles. myCAFs synthesize and deposit ECM, activate YAP-Rho-ROCK-MyosinII, and remodel ECM into linearized collagenous/fibronectin highways. iCAFs secrete IL-6, IL-8, CCL2, CXCL12 that alter immune composition. MSCs deposit and remodel ECM similarly to myCAFs. CAF plasticity (reprogramming between subtypes) is itself a source of heterogeneity and a reason anti-CAF therapies have yielded contradictory results.

### Clonal selection vs. plasticity: the paper's explicit position

The review explicitly endorses **both mechanisms as simultaneous and reinforcing**:

- **Selection component:** "The stiff ECM stroma contributes to tumor aggression and therapy resistance and drives metastasis and poor patient outcome" by "promoting the growth and survival of select genetically modified tumor cells, fostering genomic instability and/or increasing mutagenic load." The mechanically fitter cells (those able to engage integrin-based traction, resist anoikis, tolerate nuclear stress) are selectively expanded. The paper notes that cells with higher traction forces and cytoskeletal remodeling capacity have competitive advantages in dense ECM.

- **Plasticity component:** Mechanotransduction "can expand the frequency of pre-existing tissue stem cells, or it can promote an EMT in cancer cells to drive their transdifferentiation into CSCs." Ovarian CSCs undergo dramatic cytoskeletal remodeling that increases elastic modulus upon antitumor treatment with sphingosine — i.e., mechanical adaptation is a plastic, reversible response. Fluid shear stress application to MCF7 cells upregulates multiple CSC markers — not selection of pre-existing CSCs but mechanically induced state transition. The biomechanical properties of CSCs are described as "unique, plastic, and may serve as a promising target for future therapeutic manipulation."

- **The feedback loop:** The mechanically induced EMT and CSC expansion create more contractile cells (via Rho/ROCK) that further remodel and stiffen the ECM, which in turn reinforces selection for mechanically fit phenotypes and further induces plasticity — a positive feedforward between selection and plasticity driven by the mechanical niche.

### Mechanistic links to genomic instability

The paper provides three distinct mechanical routes to genomic instability:

1. **Physical nuclear confinement:** Dense ECM forces cells to migrate through narrow pores → nuclear envelope rupture → replication stress → chromosomal gains and losses (refs 10, 13, 15, 16, 120).
2. **Solid stress and mitotic disruption:** High solid stress → compromised mitotic integrity → sustained chromosomal anomalies (refs 13, 16).
3. **Myeloid ROS amplification:** Stiffened ECM → elevated tissue tension → pSTAT3 activation → increased cytokines → myeloid cell infiltration and activation → ROS-mediated DNA damage → elevated mutational load. Mammographic density/ROS link is directly cited (refs 121–124). The ROS route connects to q022 mechanistically: it is not just the chemical niche but the *physical* niche (stiffness) that drives myeloid mutagenesis.

### Therapeutic landscape (Table 1 summary)

Clinical trials targeting ECM molecules and mechanosignaling include:
- **ECM deposition inhibitors:** TGF-β inhibitors (Galunisertib, Fresolimumab, Bintrafusp alpha); Tenascin-C inhibitors (Clantero, F19-bintrafusp-2); HA/MMP inhibitors (PIDPD28, Neovastat, Tanezumab)
- **ECM crosslinking/stiffness inhibitors:** LOX inhibitors (PXS-LOX 1, PXS-5502A) — pan-LOX inhibitor Phase 1/2 in PDAC shows promising results, Phase 3 ongoing
- **Mechanosignaling inhibitors:** Integrin inhibitors (GLNG0157, ATN-161, E7820, anti-αv/β3); YAP-TAZ inhibitors (VT3989, CA3 and Verteporfin — Phase 1/2 recruiting); FAK inhibitors (Defactinib — Phase 2 recruiting in gastric and PDAC); ROCK inhibitors (Netarsudil, Rilumazole)
- Anti-CAF and immune checkpoint combinations are highlighted as most promising near-term strategy (FAP+ CAF-CXCL12 blockade with CXCR4 + PD-1 — Phase 2 PDAC)

## Limitations

- Narrative review from a lab heavily invested in the ECM-stiffness research program (Weaver group, UCSF); citations are not systematic and the review substantially cites its own prior work, especially on STIFMaps, YAP-TAZ, and mammographic density.
- The review does not clearly distinguish between ECM stiffness as a *cause* of intratumoral heterogeneity and stiffness as a *consequence* of cellular heterogeneity (mechanically active myCAFs and cancer cells themselves remodel the ECM). The directionality problem is acknowledged in passing but not resolved.
- Most genomic instability claims (nuclear rupture → CIN) are based on in vitro confinement assays or murine models; the in vivo quantitative contribution of mechanical confinement to mutational burden (vs. replication errors, vs. oncogene-driven instability) is not established.
- CSC-mechanics claims heavily conflate selection (expansion of pre-existing CSCs) and plasticity (induction of CSC state) without providing a framework for distinguishing these experimentally in vivo.
- The therapeutic section (Table 1) lists clinical trial statuses but does not appraise effect sizes, patient selection criteria, or why most MMP inhibitor and early anti-fibrotic trials failed — the failure mode analysis is underdeveloped.
- The review's scope is limited to ECM and cellular stroma mechanics; it does not treat fluid mechanics (shear stress from blood flow on endothelial cells) or neural mechanics systematically.
