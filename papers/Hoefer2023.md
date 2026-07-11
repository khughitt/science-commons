---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Hoefer2023
kind: paper
title: Causal Determinism (Stanford Encyclopedia of Philosophy)
version: "1.0.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: Hoefer2023
tags: []
ontology_terms: []
paper_kind: review
---
## Key Findings

1. **Formal structure of determinism.** Three components are required: (a) a well-defined world state at each time, (b) laws of nature that are true at all places and times, and (c) logical entailment from (a)+(b) to the state at all other times (§2.5). The modality behind "determination" is logical entailment, not merely nomological necessity.

2. **Determinism is not predictability.** Laplace's demon conflates epistemic access with ontological necessity; no finite embedded agent can have such access. Determinism can hold without predictability and predictability can hold without determinism (§1, §3).

3. **Classical mechanics has multiple determinism breakdowns.** "Space invaders" (time-reverse of escape-to-infinity), supertasks, and Norton's dome (a ball at a frictionless apex that may spontaneously start moving, with no violation of Newton's laws) all produce models where a well-defined initial state does not fix the future (§4.1).

4. **Chaos makes the deterministic/stochastic distinction epistemically inaccessible.** Suppes (1993) proved that some systems can equally well be modeled as deterministic classical processes or as indeterministic semi-Markov processes, regardless of how many observations are made (§3.3). A finite embedded observer cannot decide between the two hypotheses. Deterministic chaos displays sensitive dependence on initial conditions (SDIC) and generates behavior indistinguishable from genuine stochasticity.

5. **QM is interpretation-dependent.** Standard Copenhagen posits irreducibly stochastic wavefunction collapse; Everettian (many-worlds) QM is fully deterministic; Bohmian QM is deterministic and empirically equivalent to Copenhagen for all standard predictions (§4.4).

6. **GR fails determinism frequently.** The hole argument (Earman & Norton 1987) shows manifold substantivalism induces unconstrained indeterminism; naked singularities threaten determinism; cosmic censorship hypotheses remain unproven (§4.3).

7. **Objective chance and determinism are compatible under Humean accounts.** Non-trivial probabilities — those strictly between 0 and 1 — can coexist with deterministic laws if the law-theoretic view is Humean; Hoefer defends this at length in subsequent work cited in [@Hoefer2023]. Determinism does not force all chances to collapse to 0 or 1 unless one adopts a "pushy explainers" view of laws (§5).

8. **Time-symmetric determinism challenges the causal asymmetry intuition.** Fundamental physical theories are bi-directionally deterministic; the asymmetry of causation (past → future) is pragmatic and perspectival, not ontological (§6).

## Limitations

1. The entry covers philosophical and physical-theory perspectives only; it does not address computational causal discovery, structural causal models (Pearl-style), or Bayesian networks.
2. The discussion of chance is primarily about fundamental physics (radioactive decay, QM); direct translation to probabilistic graphical models over observational data requires additional work.
3. The entry provides no operational criteria for typing edges in a research-grade causal graph as deterministic, probabilistic, or chaotic — that gap is a design question for the toolkit.
4. The free-will discussion (§6) is of philosophical interest but has no direct bearing on the toolkit's causal inference layer.
