---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Venkatachalapathy2024
type: paper
title: Inertial effect of cell state velocity on the quiescence-proliferation fate decision
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Venkatachalapathy2024
tags: []
datasets:
- dataset:venkatachalapathy2024-mcf7
ontology_terms:
- cancer dormancy
- cell state velocity
- energy landscape
- epigenetic heterogeneity
- non-equilibrium dynamics
- p21-Cdk2 toggle switch
- plasticity
- proliferation
- quiescence
- single-cell time-lapse microscopy
---
## Key Findings

### Data-derived findings (D)

- **(D1) Position alone incompletely predicts fate.** At hypoxia onset (t = 0 h), initial p21 expression and Cdk2 activity are significantly different between cluster QQ vs. PQ/PP (Kruskal-Wallis, P < 0.0001), but clusters PQ and PP are **not** statistically distinguishable by initial position (Fig. 3B). Fate divergence between PQ and PP therefore cannot be explained by instantaneous p21/Cdk2 abundance.

- **(D2) Cell cycle velocity predicts PQ vs. PP fate.** Cluster PP cells divided significantly more times in the 48 h pre-hypoxia window than PQ cells (Fig. 4B; Kolmogorov-Smirnov). PP mother cells had significantly shorter cell cycle times (<3 h before hypoxia induction) than PQ cells (Fig. 4C; Wilcoxon rank sum, P < 0.01). Higher velocity (faster cycle) → retained proliferative fate despite hypoxia → inertial effect.

- **(D3) Inertia is interpretable as velocity on the energy landscape.** On a 2D p21-Cdk2 landscape, cells moving rapidly along the proliferative trajectory "resist" the hypoxia-induced topographic change; slower cells comply. Sensitivity analysis of the ODE model shows that the 13 parameters identified by Heldt et al. as modulating landscape flux also modulate cell cycle velocity in the same direction (Fig. 4A), linking computational velocity (landscape flux) to experimental velocity (time to S-phase entry).

- **(D4) Extrinsic noise (parameter variability) dominates intrinsic biochemical noise.** Rescaling p21 traces to their individual maxima significantly reduces intra-cell CV (Fig. 4D), demonstrating that inter-cell differences in steady-state p21 levels (parameter heterogeneity = extrinsic noise) account for most population variance, not low-copy-number fluctuations (intrinsic noise). This contradicts the naive energy-landscape assumption that intra-valley width = intrinsic noise accessible to each cell.

- **(D5) Sister cells share fate more than expected by chance.** Among sister pairs born <3 h before hypoxia onset, 64% belonged to the same fate cluster vs. 36% expected by random (P = 1.78 × 0.64/0.36 = effectively P < 0.0001; permutation test with 10⁵ shuffles; Fig. 4E). Fate inheritance is driven by correlated parameter inheritance (epigenetic state heritability) combined with system bistability near the quiescence/proliferation boundary.

- **(D6) Velocity dependence is especially important under transient perturbations.** Under sustained chronic hypoxia, most PP cells eventually become quiescent (via prolonged G₂ arrest), suggesting velocity effects are most pronounced under transient or fluctuating stress — when the landscape changes before cells have time to re-equilibrate.

### Author interpretations (L)

- **(L1) Velocity encodes hidden epigenetic and signalling information.** Authors interpret velocity as a proxy for the aggregate state of all interacting biochemical species (Rb phosphorylation status, Cyclin D/E levels, E2F activity, basal stress signalling via p53/MYC) whose dynamics drive d[p21]/dt and d[Cdk2]/dt but are not directly measured. Velocity is thus a dimensionality-reduction that recovers collective state information lost in the 2D projection. [Interpretation is plausible given the systems-level framing; direct validation of this multi-species encoding claim would require simultaneous measurement of all implicated species, which is technically infeasible with current non-overlapping fluorophore constraints.]

- **(L2) Inertia is a general non-equilibrium phenomenon.** Authors extend the inertia concept beyond the cell cycle, citing analogous effects in p53 dynamics (p53 accumulation rate, not total p53, predicts apoptosis under cisplatin) and synthetic toggle switches. They argue inertia is expected in any bistable biochemical network under transient external perturbation. [This generalisation is reasonable on theoretical grounds but is not empirically tested across systems in this paper; each cited example requires independent mechanistic confirmation.]

- **(L3) Clinical implication: velocity-based pharmacodynamics.** Authors suggest that energy-landscape changes during and after drug administration can be analysed by tracking velocities of accessible reporters, potentially enabling inertia-exploiting therapeutic schedules — e.g., dosing regimens timed to the velocity state rather than the mean population state. [SPECULATION — this translational extrapolation is not developed beyond conceptual framing and requires substantial future work to operationalise.]

## Limitations

### Author-stated

1. **2D reduction discards high-dimensional information.** Authors acknowledge that p21 and Cdk2 are proxies for the full cellular state; additional species (Rb, Cyclin D/E, E2F, etc.) contribute to fate determination but cannot be simultaneously tracked with available non-overlapping fluorophores. The 2D landscape is necessarily a compressed projection.
2. **CoCl₂ hypoxia model has caveats.** CoCl₂ stabilises HIF-1α via a different mechanism from true O₂ deprivation (iron chelation rather than hypoxia-induced prolyl hydroxylase inhibition). GFP variants show reduced fluorescence under true hypoxia (improper folding) but not CoCl₂, so multi-fluorophore imaging required CoCl₂. Normoxic response after CoCl₂ washout is also altered by drug retention.
3. **Long-term chronic hypoxia is not well-characterised.** The experiment covers only 72 h of hypoxia; longer-term quiescence maintenance (weeks) and re-entry into the cell cycle are outside the scope. Authors note that PP cells eventually become quiescent under chronic hypoxia, so the velocity effect may be most relevant under transient/fluctuating stress.
4. **Cell cycle phase classification is approximate.** Cell cycle phase was inferred from Cdk2 activity trace shape using a threshold-based classifier (Cdk2 activity < 0.38 → G₀/G₁/S), not from direct FUCCI-class reporters. This introduces classification uncertainty, especially at phase boundaries.

### Additional limitations (not author-stated)

5. **MCF-7 is a single ER+ breast cancer line.** The generalisability of the inertial effect across cancer types, genomic subtypes, and in vivo 3D microenvironments is untested. MDA-MB-231 is used only as a negative control (no dormancy entry), not as a positive comparator for a different inertial regime.
6. **Extrinsic-noise decomposition relies on within-trace normalisation.** The rescaling approach (normalise each trace to its own maximum) conflates multiple sources of variation and assumes the maximum is comparable across cells, which may not hold if total p21 expression range differs systematically between cell states.
7. **Sister-cell analysis is underpowered for subcluster comparisons.** n = 60 pairs total; the subgroup analyses (both quiescent, both proliferative, divergent fates) have small n (3–51 per condition per normoxia/hypoxia contrast), limiting statistical precision.
8. **No in vivo validation.** All experiments are conducted in standard in vitro 2D culture. Tumour microenvironment context (3D architecture, nutrient gradients, immune interactions, variable hypoxic zones) may alter the velocity-fate coupling substantially.
