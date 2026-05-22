---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Ciriello2021
type: paper
title: The many faces of cancer evolution
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Ciriello2021
tags: []
datasets: []
ontology_terms:
- cancer evolution
- cell plasticity
- epigenetic reprogramming
- epithelial-to-mesenchymal transition
- intra-tumor heterogeneity
- nongenetic adaptation
- single-cell genomics
- treatment resistance
---
## Key Findings

### Taxonomy of cancer evolution modes

The paper does not propose a formal numerical taxonomy of named modes (e.g., "linear / branching / neutral / punctuated / Big Bang") — that vocabulary belongs to parallel literature on genetic ITH. Instead, Ciriello & Magnani articulate a **two-axis framework** for understanding tumor cell diversity and evolution:

| Axis | Genetic arm | Plastic arm |
|---|---|---|
| Nature of change | Discrete, irreversible somatic mutations | Continuous, reversible epigenetic / transcriptional reprogramming |
| Heritability | Clonally inherited once fixed | Meiotically heritable via epigenetic marks; reversible under new cues |
| Detectability | Clone phylogenies from SNVs | Requires longitudinal single-cell or epigenomic readouts |
| Tractability to selection | Standard Darwinian fitness model | Darwinian-compatible *plus* Lamarckian-like induction |
| Primary drivers | Mutational processes, replication errors | Cell-of-origin programs, microenvironmental cues, therapy |

Within the plastic arm, they distinguish two sub-modes:
- **De-differentiation**: acquisition by a differentiated cell of progenitor/stem-cell features
- **Trans-differentiation**: acquisition of features characteristic of a distinct lineage

### EMT as the paradigm case of plastic evolution

- EMT is not a binary switch between epithelial and mesenchymal states; it is a continuum of intermediate, co-expressed partial states, demonstrable at single-cell resolution.
- EMT programs are tissue-dependent: the same phenotypic endpoint is reached via heterogeneous transcriptional and epigenetic routes in different tumor types (e.g., Snail/Zeb roles differ in breast vs. pancreatic cancer; different chromatin accessibility contexts confer different EMT trajectories in KRAS/p53 skin tumors depending on cell of origin).
- Cancer stem cell (CSC) dedifferentiation overlaps with EMT via shared programs (Zeb, Wnt), and the CSC model must be reconsidered as a continuum rather than a unidirectional hierarchy.
- EMT is reversible (MET documented) and can be induced non-cell-autonomously by microenvironmental signals.

### Nongenetic adaptation in treatment resistance: ER+ breast cancer case study

- ER+ breast cancer (~70% of cases) is treated with endocrine therapies that induce cytostasis (dormancy) rather than cytotoxicity; ER (ESR1) is mutated in only ~1% of treatment-naive tumors.
- In ~40% of relapsing tumors, genetic drivers of resistance are identifiable; the majority of relapses are therefore not explained by pre-existing genetic clones being selected.
- Dormancy — cells surviving in a non-cycling minimal-residual-disease state — is proposed as the substrate for nongenetic adaptation: cells exploit developmental epigenetic programs rather than accumulating new mutations.
- A "pre-adapted cell" population (expressing a defined transcriptome lacking late-resistance mutations) is selectively enriched in early drug response before classical clonal evolution resumes.
- The authors hypothesize a two-phase model: (1) nongenetic epigenetic adaptation during dormancy (Phase 1, cytostatic pressure); (2) resumed classical Darwinian clonal evolution after awakening (Phase 2, proliferative pressure).
- Similar persister-cell phenomena documented in PC9 NSCLC (EGFR inhibitor, gefitinib) and melanoma (BRAF inhibitor, vemurafenib).

### Single-cell + lineage tracing as the enabling technology

- To distinguish *feature selection* (clonal sweep of a pre-existing epigenomic subpopulation) from *plastic reprogramming* (transcriptional reprogramming within a lineage), barcode strategies coupled to longitudinal scRNA-seq are required.
- Memory-seq / genetic barcode + scRNA-seq frameworks can in principle detect whether phenotypic changes are population-level sweeps or within-lineage state transitions.
- H3K27ac ChIP-seq deconvolution can track clonal vs. subclonal epigenomic evolution in bulk tumors.
- Spatial genomics integration is needed to capture TME-driven, non-cell-autonomous plastic events.

## Limitations

- The paper is a perspective and does not present primary data; all mechanistic claims are inferences synthesized from cited studies.
- The EMT case study is treated as representative of plastic evolution broadly, but the authors acknowledge that EMT programs are highly tissue-dependent, so generalizing the paradigm to other plastic processes requires caution.
- The "two-phase" model of dormancy → awakening is explicitly speculative for most cancer types beyond ER+ breast cancer; the authors acknowledge limited evidence in glioblastoma and colon cancer and pose it as an open question.
- The proposed lineage-tracing + single-cell frameworks are described as technically immature for routine clinical use; most evidence is from cell lines or limited model organisms.
- The paper focuses on solid tumors; hematologic malignancies are not discussed, limiting direct applicability to the myeloma context in this project's ancestry.
- The distinction between "true plasticity" (within-lineage reprogramming) and "Darwinian selection of epigenetic subclones" is highlighted as the central unresolved experimental challenge — the paper advocates for the right technology but does not resolve the question empirically.
