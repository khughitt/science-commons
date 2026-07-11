---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Hoover2009
kind: paper
title: Identity, Structure, and Causal Representation in Scientific Models
version: "1.0.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: Hoover2009
tags: []
dataset_usage: []
ontology_terms: []
paper_kind: ''
---
## Key Findings

**Structural account subsumes Simon.** Simon's original account of causal order applied only to linear recursive (DAG) systems. The structural account handles cyclical/simultaneous systems (systems with no self-contained subsystems under Simon's definition) and cross-equation restrictions (nonlinearity in parameters), which Simon could not.

**Independence from functional form.** The partial solution — and thus the causal order it reveals — is uniquely recoverable from the complete solution regardless of how the system of equations is initially written. Different notational choices cannot change the causal verdict; the privileged parameterization is the anchor.

**Modularity holds at parameter level, not mechanism level.** Woodward requires that causal systems be modular (each equation can be disrupted without affecting others). The structural account shows Woodward's definition of direct cause is too strong: it rules out causal systems that display genuine causal structure but fail the come-what-may intervention test (e.g., carburetors, steam engines, Lucas-critique monetary systems). Modularity holds conventionally at the parameter level (the Reichenbach Convention forces it) but not necessarily at the level of mechanisms or equations. This vindicates Cartwright's critique of Woodward while preserving the structural account's content.

**Identity conditions for causal mechanisms.** Two mechanisms are causally identical iff they share the same variable set, parameter space (same parameters, not just same values), and functional form — differing only in token parameter values. This precise identity criterion is unavailable in graph-only or equation-only representations.

**Causal identity without token intervention.** Woodward's account requires defining cause through a token intervention on a variable. The structural account defines cause through type-level parameter subset relations; token interventions are not definitionally required. This allows counterfactual causal questions (comparative statics, causal questions about sex/race/species) to be well-posed even where no physical transformation is possible, provided causal identity (shared functional structure and parameter space) is established.

**Lucas critique as structural phenomenon.** Cross-equation restrictions arise when a parameter appears in multiple equations (e.g., forward-looking expectations). In such systems, "wiping out" one causal arrow per Woodward's intervention does not merely alter a parameter value — it can destroy the meaning of parameters in other equations. The structural account represents this directly: a come-what-may intervention on one equation can structurally alter the causal order of the remaining system, not just its parameterization.

## Limitations

The paper is a theoretical/philosophical analysis with worked mathematical examples but no empirical applications or computational implementations:
- The formal account is stated for finite systems of equations with a fixed structure; it does not directly address the case where structure itself is uncertain (as in causal discovery from data).
- The paper assumes a structural causal model perspective throughout and does not fully engage with the potential-outcomes (Rubin) framework, which is widely used in epidemiology and social science.
- The Reichenbach Convention (variation-free parameters) is asserted as a representational choice, not motivated by an underlying metaphysics; the paper does not address what to do when genuinely non-separable parameters are encountered (e.g., quantum entanglement, social mechanisms with constitutive interdependence).
- The treatment of cyclical systems (simultaneous causation) stops at identification of mutual-cause structure; it does not provide identification or estimation strategies for such systems (this is acknowledged as outside scope).
- The paper's engagement with Cartwright focuses on the carburetor and toaster examples; it does not address Cartwright's positive account (capacities / nomological machines) in depth, which is the subject of `question:0019-powers-vs-laws-causal-edge-ontology`.
