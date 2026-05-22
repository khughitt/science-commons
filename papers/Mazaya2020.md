---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Mazaya2020
type: paper
title: Effects of ordered mutations on dynamics in signaling networks
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Mazaya2020
tags: []
datasets:
- dataset:kegg-pathway
- dataset:mazaya2020-signaling
ontology_terms:
- Boolean network model
- drug-target genes
- feedback loops
- mutation order effects
- mutation-sensitivity
- oncogenes
- order-specificity
- signaling network dynamics
- tumor suppressors
---
## Key Findings

### Baseline distributions

- Cumulative probability of δ ≥ 0.1 in HCS, KEGG, TGL: 0.56, 0.62, 0.39, respectively — nonzero sensitivity is common, not exceptional.
- Cumulative probability of Δ ≥ 0.1: 0.38, 0.54, 0.32 — order matters in a substantial fraction of pairs, even though Δ is generally lower than δ.

### Path-length effect

- Pairs where the first mutation occurs in the "longer-path direction" (i.e., l(v_i, v_j) > l(v_j, v_i)) show significantly higher mutation-sensitivity than the "shorter-path direction" across all three networks (all P < 0.003 at most T values, Mann-Whitney U).
- Intuition: a longer upstream path from v_k to v_l means v_k has weaker direct influence on v_l, so the second mutant v_l "escapes" the first mutation's dampening effect, inducing larger attractor shifts.

### Number-of-paths effect

- "Fewer-paths direction" (n(v_i, v_j) < n(v_j, v_i)) shows significantly higher mutation-sensitivity than "more-paths direction" (all P < 3×10⁻⁵ at most T values). Consistent with prior work showing path multiplicity dilutes dynamical influence.

### Feedback-loop (FBL) effect

- FBL-involved gene pairs show significantly **lower** mutation-sensitivity than Non-FBL pairs (all P < 0.0001 across all networks and T values).
- FBL-involved pairs also show significantly **lower** order-specificity than Non-FBL pairs (all P < 0.02 at most T values).
- FBL structure dampens both the magnitude of attractor change and the asymmetry between mutation orders — feedback loops buffer sequential mutation dynamics.

### Drug-target gene analysis

- Number of drug targets in a network is **negatively correlated** with mutation-sensitivity, meaning drug-target-dense networks are less dynamically sensitive to perturbation.
- Non-DT→DT pairs show the highest mutation-sensitivity; DT→Non-DT the lowest. The order of drug-target mutation is more critical (higher order-specificity) than non-drug-target mutation order.
- Same-drug gene pairs (both genes targeted by the same drug) show higher mutation-sensitivity and order-specificity than different-drug pairs, consistent with functional redundancy creating stronger attractor dependence on mutation order. (TGL excluded: no same-drug pairs in that network.)

### Tumor suppressor / oncogene ordering — the central cancer-relevant result

- **TSG→OCG** (tumor suppressor mutated first, oncogene second) produces significantly **lower** mutation-sensitivity than **OCG→TSG** (oncogene mutated first, then tumor suppressor) across all three networks (all P < 0.003; Fig. 6a–c).
- In other words: when the tumor suppressor is knocked out first, the network is **less dynamically disturbed** by the subsequent oncogene knockout. Conversely, oncogene mutation first, followed by tumor suppressor loss, produces a larger and more disruptive attractor shift.
- TSG order-specificity is significantly higher than OCG order-specificity (all P < 0.0001; Fig. 6d–f), confirming the dynamics are highly sensitive to whether the tumor suppressor or the oncogene is mutated earlier.
- **Interpretation:** tumor suppressors mutated first can suppress or dampen the amplification of oncogene dynamics when the tumor suppressor loss precedes the oncogene event — a formal dynamical mechanism consistent with the canonical "gatekeeper" role of tumor suppressors.

### Validation with random networks

Results were replicated in 250 Barabási-Albert random networks (|V|=50, |A|=100), confirming findings are not specific to the biological topology of HCS/KEGG/TGL (Supplementary Figure S1).

## Limitations

- **Boolean abstraction:** Gene expression is binarized (on/off); continuous, graded, or stochastic regulation is not captured. This is particularly constraining for modeling incomplete loss-of-function (heterozygous mutations) or partial oncogene amplification.
- **Synchronous update:** All nodes update simultaneously at each time step, which is biologically less realistic than asynchronous update schemes. The authors acknowledge this and flag asynchronous updating as future work.
- **NCF rule specification:** The actual canalyzing (I_m) and canalyzed (O_m) Boolean values are drawn independently and uniformly at random, because inferring them from real data is difficult. This introduces artificial uncertainty in rule specifics even when network topology is empirically derived.
- **Double-knockout only:** Only pairwise knockouts (two simultaneous loss-of-function mutations with a time lag) are studied. Three-mutation or gain-of-function (oncogenic activation) dynamics are not modeled.
- **No epigenetic or microenvironmental layer:** The model captures only gene-level network topology; chromatin state, methylation, or niche signals — all relevant to cancer evolution — are absent.
- **Excludes gene pairs with common child nodes:** Pairs sharing a common downstream NCF child were excluded to avoid a specific confound, which may systematically remove functionally important co-regulated pairs.
- **Random initial state sampling:** Results are averaged over 1000 random initial network states; sensitivity to initial state distribution is not explored.
- **No fitness or selection model:** The model quantifies dynamical attractor changes but does not connect attractor shifts to cell fitness, proliferative advantage, or selection. The link between attractor shift and cancer-relevant phenotype is inferred, not derived.
