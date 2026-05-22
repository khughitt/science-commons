---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Strobl2023
type: paper
title: Treatment of evolving cancers will require dynamic decision support
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Strobl2023
tags: []
datasets: []
ontology_terms:
- ADAPT framework
- adaptive therapy
- dynamic decision support
- mathematical oncology
- maximum tolerated dose
- treatment scheduling
- tumor evolution
- tumorscape
---
## Key Findings

**Conceptual/architectural:**

- The MTD paradigm is simultaneously evolution-agnostic (fixed schedule) and reactive-only (adjusts only on toxicity or gross progression). It is effective for rapid tumor burden reduction but fails when tumor heterogeneity and acquired resistance dominate disease dynamics — the majority of advanced cancer patients.
- Every historical scheduling paradigm encodes a different mathematical model of tumor biology (homogeneous → heterogeneous → microenvironmental → complex eco-evolutionary); none is universally correct because each captures a different subset of the tumorscape.
- Personalized scheduling therefore requires matching the *model* to the individual patient's tumorscape, not applying one model universally.

**The ADAPT framework specifics:**

- Decision variables: dose level, dosing frequency, treatment on/off timing, drug combination ratios — all potentially tunable per cycle.
- Model class: mechanistic ("mimic the processes, not the data") — includes models of molecular evolution, protein signaling networks, eco-evolutionary tumor dynamics, and pharmacokinetics/pharmacodynamics. Statistical/ML models are regarded as insufficient for the forward-prediction task.
- Cadence: iteration is patient-specific; re-evaluation occurs not only at toxicity or progression but also when the current schedule performs well (to avoid fitness valley crossing by resistant clones).
- Treatment goal is an explicit ADAPT variable that can shift over time (cure → control → palliation), which alters the objective function for optimization.
- The Evolutionary Tumor Board (ETB) is the most developed instantiation: it constructs a 'virtual cohort' of historical patients parameterized by disease-specific mathematical models, matches the real patient against virtual analogues, and uses 'virtual clinical trials' (NCT04343365; 21 patients enrolled at time of writing).

**Prerequisites / data requirements identified:**

- Quantitative tumor burden monitoring (not just response/no-response): volumetric imaging, ctDNA, and disease-specific blood biomarkers at higher frequency than current standard of care.
- Spatial and temporal tumor heterogeneity measurements: spatial transcriptomics, single-cell sequencing, liquid biopsy, histoecology — to parameterize the eco-evolutionary model components.
- Longitudinal data infrastructure: shared, standardized clinical trial data repositories (Project DataSphere, YODA, Vivli cited) to build and validate population-level priors for model initialization.
- Interdisciplinary team: mathematicians + evolutionary biologists embedded into the clinical decision-support workflow (tumor board model).

**Challenges explicitly named:**

- Butterfly effect / chaos: stochastic mutational events make long-horizon predictions unreliable; ADAPT is framed as providing decision support at the *next cycle* horizon, not long-term forecasts.
- Multi-lesion heterogeneity: different metastatic lesions may have different tumorscapes and require different schedules simultaneously — an open problem the paper frames as requiring spatiotemporal mathematical models.
- Financial and regulatory barriers: ctDNA and MRI monitoring at ADAPT-required frequency are expensive and not routinely covered; no regulatory pathway for model-guided dosing below the approved dose yet exists.
- Evidence base: all ADAPT-aligned examples cited are phase I/II or early clinical, with no randomized evidence yet that dynamic model-guided scheduling improves survival over static MTD protocols at scale.

## Limitations

- The ADAPT framework is a conceptual architecture, not a validated clinical protocol; no randomized trial evidence demonstrates that ADAPT-guided scheduling improves outcomes over standard of care.
- The paper does not address cancer types where evolutionary dynamics are poorly characterized (e.g., hematologic malignancies with complex clonal architectures like MM), limiting direct applicability to some project contexts.
- The mathematical models invoked are heterogeneous in scale and formalism; the paper does not specify how to choose among competing model structures for a given patient, nor how to handle disagreements between models (the multi-model ensemble problem is acknowledged but not solved).
- The tumorscape visualization (spider plot) is a useful heuristic but does not encode the dynamical couplings between axes — two patients with identical spider plots may have qualitatively different evolutionary trajectories if the coupling between, say, adaptability and microenvironment differs.
- All clinical examples cited involve either small pilot studies or rule-of-thumb adaptive protocols (e.g., PSA-guided treatment holidays), not full ADAPT-cycle implementations; the ETB enrolled 21 patients with no efficacy outcome data reported.
- The paper does not discuss cost-effectiveness or health-system scalability; the monitoring intensity required for ADAPT may be feasible at major cancer centers but not in most clinical settings globally.
