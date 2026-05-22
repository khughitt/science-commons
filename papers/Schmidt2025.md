---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Schmidt2025
type: paper
title: Fast tumor phylogeny regression via tree-structured dual dynamic programming
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Schmidt2025
tags: []
datasets:
- dataset:schmidt2025-simulated
ontology_terms:
- binomial loss
- bulk DNA sequencing
- clonal tree inference
- convex optimization
- dynamic programming
- perfect phylogeny regression
- tumor phylogenetics
---
## Key Findings

### Regression speed

- **ℓ₂ loss:** fastppm-L2 was on average 111.1× faster than projectppm (the prior specialized ℓ₂ solver), ranging from 33.3× (n = 100) to 163.2× (n = 4000). Against general-purpose solvers, fastppm yielded ~858× speedup over Mosek on average.
- **Binomial loss:** General-purpose solvers (ECOS, Mosek, Clarabel) failed to terminate without error on 54/270 instances. CVXOPT terminated on all but was 400.1× (ADMM), 43.8× (50-PLA), 22.3× (100-PLA), and 13.6× (PPLA) slower than the four fastppm variants. Solution quality within 4% of CVXOPT objective for PLA variants; PPLA matched or slightly bettered CVXOPT.
- All fastppm variants achieved at least one order of magnitude improvement over general-purpose solvers while producing solutions of equivalent or near-equivalent accuracy.

### Pipeline integration speedups

- **Sapling\*:** Average 406× runtime improvement for n = 50 mutations; Sapling without fastppm could not process instances beyond n = 50 within a 13-h time limit, while Sapling\* successfully completed all instances with n = 500 mutations.
- **CITUP\*:** 5–10× runtime improvement over CITUP within a 12-h limit, with improved rate of successful termination and similar reconstruction accuracy.
- **Orchard\*:** 3–5× runtime improvement, similar tree recovery accuracy.

### Low-coverage and real-data accuracy

- At 20× simulated coverage (n = 50, m = 50), Sapling\* achieved mean F1 = 0.90 vs. Orchard F1 = 0.84 and Orchard\* F1 = 0.82 — attributable to direct modeling of the binomial read-count likelihood rather than approximating it via ℓ₂.
- On POP66 colorectal xenograft (n = 65, m = 8), Sapling\* achieved better binomial negative log-likelihood (NLL: 10720.6) vs. Orchard (10793.5) and Orchard\* (10790.9), with inferred frequencies 20% closer to full-coverage observed frequencies. Sapling\* completed in ~3 min, Orchard in ~4 min 38 s, Orchard\* in ~1 min 49 s.
- Phylogenies inferred by Sapling\* and Orchard/Orchard\* differed substantially (e.g., Sapling\* recovered a KDR mutation that Orchard placed as truncal CNR1 vs. truncal KDR), demonstrating that loss function choice matters for biological interpretation in shallow-coverage settings.

## Limitations

- **Fixed-topology regression only:** TSDDP solves PPR for a fixed tree T; it does not itself search tree space. The speedup benefits downstream pipelines that call PPR repeatedly (Sapling, CITUP, Orchard), but tree search heuristics and their accuracy characteristics remain those of the host pipeline.
- **Infinite sites assumption (ISA):** The ISA is assumed throughout — each mutation is gained once and never lost. The ISA is violated in the presence of copy-number loss or parallel evolution, though the authors note that CNA-corrected read counts mitigate this in practice.
- **No within-sample subclonal phasing:** fastppm (like all PPR-class methods) works from bulk sequencing and cannot resolve subclonal architecture below the resolution of population-averaged VAFs. Single-cell data are needed for within-sample heterogeneity.
- **Single-threaded benchmarks:** Runtime comparisons were conducted single-threaded. Multi-threaded or GPU-accelerated general-purpose solvers might close the gap, though TSDDP's O(nk log²(nk)) vs. O(n²) advantage is asymptotic and independent of parallelism.
- **PLA-k approximation accuracy:** For non-linear losses (binomial, beta-binomial) approximated via PLA-k, solution quality degrades as the loss surface deviates from piecewise linearity with k segments. PPLA is more accurate but adaptive segment counts complicate runtime guarantees.
- **Under-determined reconstruction:** The authors acknowledge that phylogenetic reconstruction is highly under-determined (many trees may explain the data equally well, Qi et al. 2019). fastppm improves regression speed but does not address non-uniqueness of the solution space.
