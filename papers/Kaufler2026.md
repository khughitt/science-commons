---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Kaufler2026
type: paper
title: 'POTTR: Identifying Recurrent Trajectories in Evolutionary and Developmental Processes using Posets'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Kaufler2026
tags: []
datasets:
- dataset:kaufler2026-aml-sc
- dataset:kaufler2026-tls
- dataset:tracerx
ontology_terms:
- clonal evolution
- combinatorial optimization
- lineage tracing
- mutation ordering
- partially ordered sets
- recurrent trajectories
- tumor phylogenetics
---
## Key Findings

### Comparison with MASTRO (NSCLC + AML)

- In NSCLC (89 trees), POTTR and MASTRO both identify 7 statistically significant maximum recurrent trajectories (p < 0.05). POTTR additionally finds **2 trajectories missed by MASTRO** (Fig. 4) by resolving the order of mutation clusters: (i) *COL5A2* after a *PIK3CA*-containing cluster (s=2, p=1.6×10⁻²) — COL5A2 activates the PI3K/Akt pathway and promotes erlotinib resistance; (ii) *NFE2L2* (encoding NRF2) after *PIK3CA, TP53, SOX2* mutations (s=4, p=2.7×10⁻⁴) — NRF2 is a key antioxidant transcription factor associated with tumor cell survival against chemotherapy. MASTRO reports a related NFE2L2 trajectory but cannot resolve the cluster, merging it into a single node.
- In AML (120 trees), POTTR and MASTRO both identify 34 maximum recurrent trajectories, with 33/34 (POTTR) and most (MASTRO) reaching p < 0.05. The single POTTR non-significant trajectory is *FLT3→NPM1* (the most frequent AML alteration pair). All 33 significant POTTR trajectories are exact MIS solutions; MASTRO's maximal trajectories are not consistently statistically significant.

### TRACERx421 NSCLC

- Largest maximum trajectory has 5 alterations at k=2. By k=6, trajectories have only 2 mutations; by k=36–193, only single-mutation trajectories remain.
- Key trajectories: TP53_M and CDKN2A_M missense mutations preceding PIK3CA_M (s=4, p=9×10⁻⁴); TP53_M and KRAS_M followed by UBR5_M (s=3, p=4.19×10⁻¹⁵) (Fig. 5).
- The TP53→PIK3CA co-occurrence with early TP53 correlates with longer disease-free survival in TRACERx data (Liao et al. 2020), while early PIK3CA correlates with shorter survival — POTTR recovers and extends this ordering.
- POTTR resolves mutation cluster uncertainty across patients: in CRUK0052, a TP53_M + KRAS_M cluster precedes UBR5_M; in CRUK0322, the order TP53_M→KRAS_M→UBR5_M is fully resolved.

### TLS developmental application

- POTTR identifies conserved differentiation routes across TLS biological replicates at k=6 (maximum trajectory size ~9 events) and k=7.
- In unperturbed TLS: an alternative somitogenesis trajectory where somites arise from a progenitor shared with endothelial cells (rather than neural tube progenitors) is identified — consistent with secondary in vivo endothelium pathways (Lagha 2009, Nguyen 2014).
- In WNT-activated / BMP-inhibited TLSCL: the alternative somite–endothelium trajectory is absent; POTTR infers the stereotypical neuro-mesodermal progenitor route, suggesting WNT/BMP signals suppress the alternative somitogenesis path.
- This application demonstrates POTTR's generality: the method applies without modification to developmental (non-cancer) lineage tracing data structured as DAGs.

### Performance / scalability

- Runtime is practical for TRACERx-scale data (<39 s trajectory finding per k on the NSCLC data with 469 trees). MASTRO becomes intractable on large inputs with many conserved trajectories because it enumerates all *maximal* trajectories; POTTR finds *maximum* trajectories, a tractable restriction.
- Largest trajectories shrink monotonically as k increases (by design). Trajectory sizes in both NSCLC and AML remain small (≤5 alterations at k=2), reflecting the low per-gene mutation frequency and sparse pairwise co-occurrence in these cohorts.

## Limitations

- **NP-hard core:** MkCIIS is NP-hard; exact ILP solution via Gurobi is practical for current dataset sizes but will require heuristics or approximation algorithms as cohorts scale beyond TRACERx421 (the authors acknowledge this).
- **Small trajectory sizes:** Largest trajectories contain only 4–5 alterations at k=2 in both NSCLC and AML, reflecting sparse co-occurrence. This limits the amount of h006-type regime-ordering information extractable from current datasets.
- **Statistical significance test limited to small trajectories:** MASTRO's permutation test requires enumerating all automorphisms of a trajectory and is only feasible for trajectories with <~10 nodes. This caps the statistical resolution for larger trajectories.
- **Infinite sites assumption:** Each mutation is assumed gained exactly once and inherited to all descendants. Parallel mutation events (observed in some subclonal contexts) violate this assumption and may produce false-positive ordering signals. POTTR introduces a multi-occurrence labeling system (gene_M, gene_N per mutation type) as a partial mitigation.
- **Input-tree quality dependence:** POTTR inherits all errors and biases in the upstream phylogenetic inference (CONIPHER, CITUP, SCITE). Oscillatory clonal dynamics (h008) or incorrect cluster definitions can introduce artifactual orderings.
- **Cluster resolution support small (1–2 patients):** In current datasets, resolutions of mutation clusters are supported by very few patients (1–2), which makes the resolved orderings uncertain. Larger cohorts or joint bulk+single-cell data would improve confidence.
- **No probabilistic framework:** POTTR solves a combinatorial optimization problem but does not provide a posterior distribution over trajectories or account for phylogenetic uncertainty probabilistically (as e.g. TreeMHN does). Extension to a Bayesian/probabilistic setting is noted as future work.
- **Developmental generalization preliminary:** The TLS application is demonstrated on a small dataset (12+11 replicates). The biological interpretation of the alternative somitogenesis route is consistent with prior work but not independently validated.
