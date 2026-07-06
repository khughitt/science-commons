---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Bowling2020
kind: paper
title: An Engineered CRISPR-Cas9 Mouse Line for Simultaneous Readout of Lineage Histories
  and Gene Expression Profiles in Single Cells
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Bowling2020
tags: []
ontology_terms:
- CARLIN
- CRISPR lineage tracing
- barcode diversity
- clonal dynamics
- hematopoiesis
- single-cell multiomics
---
## Key Findings

### Data-derived findings (D)

- **D1 — Barcode diversity:** Computational extrapolation of the observed allele frequency distribution estimated a maximum of **44,000 ± 400 distinct alleles** achievable by the CARLIN system. Across three induced mice, 88% of edited alleles were unique to a single mouse, indicating predominantly stochastic NHEJ outcomes per cell.
- **D2 — Editing efficiency:** With 7-day doxycycline induction, 31–88% of transcripts were edited across tissues. At a single-cell level, 32–63% of cells showed detectable CARLIN alleles alongside a full transcriptome readout (capture efficiency range across experiments).
- **D3 — Tree reconstruction fidelity:** Sequential 6-hour doxycycline pulses (interspersed with 24-hour washout) enabled hierarchical lineage reconstruction; the algorithm achieved false-positive rates of 0.6% and false-negative rates of 18% in benchmarks. Contralateral tissue pairs were most closely related in reconstructed embryonic trees, consistent with known developmental clonal relationships.
- **D4 — Hematopoietic clonal heterogeneity at steady state:** Individual HSC clones showed non-uniform anatomical distributions across bones (p < 10⁻⁶), indicating spatial clonal bias not detectable without lineage tracing.
- **D5 — Injury-driven clonal bottleneck:** After 5-FU myeloablation, only 12 of 92 HSC clones accounted for 45% of all HSC-rooted cells, compared to 4% HSC–progeny co-occurrence at steady state (31% after injury). A small subset of highly active HSC clones dominates post-injury regeneration.
- **D6 — Transcriptomic differentiation of active vs. inactive clones:** Differential expression comparing proliferating (active) vs. quiescent (inactive) HSC clones identified 45 Bonferroni-significant genes, including *Plac8*, *CD48*, *Mllt3*, and *Cdk6*. Sorting by proliferation markers alone (without CARLIN lineage information) failed to recover any of these genes, demonstrating the added value of joint lineage + transcriptome readout.

### Author interpretations (L)

- **L1 — Platform generality:** Authors claim CARLIN is broadly applicable across all tissue types and developmental contexts, and that inducibility makes it superior to constitutive CRISPR-based systems for staged in vivo experiments. [Plausible but only demonstrated in developmental/hematopoietic settings in this paper; cancer-model applications require additional crosses.]
- **L2 — Functional clone identity:** Authors interpret the non-uniform distribution of clones post-injury as reflecting intrinsic functional heterogeneity among HSCs (i.e., some clones are intrinsically more regenerative) rather than selective advantage. [This interpretation is reasonable but underdetermined — intrinsic differences and positive selection during regeneration cannot be cleanly separated without further perturbation experiments.]
- **L3 — Transcriptomic signature causality:** The 45-gene signature in active HSC clones is presented as identifying regulators of HSC activity. [These are correlates of activity within the labeled pool; causal roles require functional validation.]
- **L4 — Comparison to Polylox/transposons:** Authors assert CARLIN's transcribed barcodes are a key advantage over Polylox and Sleeping Beauty transposon systems. [Technically correct on the sequencing workflow point; whether this translates to discovery advantages in all contexts is context-dependent.]
- **L5 — Sequential labeling generalizability:** The multi-stage embryonic labeling demonstrates proof-of-concept for temporal depth; authors imply this extends to cancer models and other adult tissues. [Not demonstrated in this paper — requires further validation in specific GEMM crosses.]

## Limitations

- **No per-division edit rate reported.** The resolution floor — the most critical parameter for determining whether short-lived plasticity bursts (< 5 divisions) would be detectable — is not characterized.
- **Cancer-model application not demonstrated.** Potential complications from tumor microenvironment, aneuploidy, or increased Cas9 off-target activity in rapidly dividing cancer cells are untested.
- **32–63% single-cell capture efficiency.** Up to two-thirds of cells in a given experiment will lack a readable CARLIN barcode, introducing ascertainment bias that could affect inferences about rare active clones.
- **18% false-negative rate in tree reconstruction.** Missing lineage edges could collapse real clonal structure, potentially underestimating plasticity heterogeneity.
- **Multi-tissue non-hematopoietic analyses are shallow.** Bulk editing across 10 tissues is shown, but only hematopoietic clonal dynamics receive deep single-cell analysis in this paper.
- **Comparison to KP-Tracer / Yang2022:** CARLIN itself predates KP-Tracer; authors do not discuss cancer lineage-tracing in this paper and no direct comparison to KP-Tracer exists here. [KP-Tracer, described in Yang2022, builds directly on the CARLIN architecture.]
