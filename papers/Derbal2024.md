---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Derbal2024
kind: paper
title: Adaptive Control of Tumor Growth
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Derbal2024
tags: []
ontology_terms:
- adaptive control
- adaptive therapy
- combination therapy
- pathway entropy
- phenotypic plasticity
- tumor state feedback
---
## Key Findings

- **Adaptive therapy can be treated as adaptive feedback control.** Therapeutic actions are control inputs, tumor state is the system state, and monitoring provides feedback for dose and timing decisions.
- **PID-like control can be layered onto Lotka-Volterra tumor models.** The paper illustrates how drug dose could be modulated based on error between current and desired tumor burden.
- **A control framing exposes stability and convergence issues.** Tumor dynamics are nonlinear, stochastic, time-varying, and patient-specific; these properties make naive adaptive-control translation risky.
- **Pathway entropy is proposed as a monitoring biomarker.** The author argues that tumor entropy, estimated from genomic alterations and tracked through liquid biopsy/radiogenomics, could approximate phenotypic plasticity and near-future growth trajectory.
- **Adaptive combination therapy is framed as two-level adaptation.** One level switches among therapy classes; another modulates drug dose and timing.
- **The approach aims to avoid deliberately maintaining high tumor burden.** Unlike classic competitive-suppression AT, entropy-guided one-step control is proposed as a way to adapt without requiring a large sensitive-cell reservoir.

## Limitations

- The entropy biomarker is proposed rather than clinically validated as a control variable.
- The paper does not provide a patient-cohort test of the adaptive-control framework.
- Stability, safety, and persistent-excitation requirements for clinical control are acknowledged but not solved.
- The model assumes that repeated noninvasive profiling can estimate the relevant tumor-state variables with sufficient accuracy.
