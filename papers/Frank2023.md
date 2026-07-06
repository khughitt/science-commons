---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Frank2023
kind: paper
title: Robustness and complexity
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Frank2023
tags: []
ontology_terms:
- complexity ratchet
- component decay
- constructive neutral evolution
- evolvability
- fitness landscape flattening
- hourglass architecture
- neutral drift
- paradox of robustness
---
## Key Findings

### The paradox of robustness (formal claim)

Robustness at the system level weakens selection on individual components, causing three possible outcomes:

1. **Component decay** — the component evolves toward a cheaper, sloppier, lower-performance state because the fitness cost of lower performance is reduced (economic/cost-benefit shift).
2. **Neutral drift** — changes that were previously deleterious become selectively neutral under the buffer, allowing genetic variation to accumulate.
3. **Irreversibility** — once components have decayed or drifted, removing the higher-level robustness mechanism would expose their degraded state; the added layer becomes locked in, ratcheting up complexity.

### Relation to constructive neutral evolution

Constructive neutral evolution (Gray, Stoltzfus, Doolittle et al., 1990s) arrives at a similar endpoint via a complementary route: a new buffering mechanism renders variants at a lower level neutral → those variants drift → removal of the buffer would now be deleterious → complexity is irreversibly increased. Frank sees constructive neutral evolution as emphasizing **genomic/informational** complexity (hardware level in Doyle's framing), while the paradox of robustness emphasizes **functional/physiological** complexity (software level). RNA editing and Hsp90 chaperones are the canonical examples of constructive neutral evolution; multi-layered cancer protection and RAID arrays are the paradox-of-robustness examples.

### Fitness-landscape framing

Robustness flattens the fitness landscape for component-level variants, reducing selection intensity, increasing variability, and shifting marginal costs/benefits. This provides a mechanistic link to neutral-network theory: flat landscapes allow wide neutral exploration that can enable subsequent evolutionary novelty (enhanced evolvability).

### Hourglass architectures

Two independent hourglass patterns are described and linked:

- **Developmental hourglass** — early developmental stages diverge rapidly across species; intermediate stages are highly conserved (the narrow neck); late stages diverge rapidly. The conserved intermediate stages act as robust buffering protocols, shielding early variation from downstream consequences, thereby releasing constraint on early-stage diversity.
- **Doyle/Csete hourglass** — all robust complex systems (engineering and biology) exhibit wide diversity at the hardware layer, a narrow conserved protocol layer, and wide diversity at the software/functional layer. Examples: TCP/IP in the internet, Linux kernel in mobile phones, ATP/ADP disequilibrium in metabolism, the DNA→RNA→protein central dogma.

Both hourglasses share the same logic: a conserved central protocol buffers the hardware layer from the software layer, allowing both to diversify nearly independently and causing irreversible complexity at the protocol level.

### Complexity ratchet and overwiring

Each successive addition of system-level robustness causes another round of component decay/drift and locks in one more irreversible layer. The cumulative result is a deeply layered, densely wired architecture — "overwired" genomes with vast numbers of regulatory inputs into any single gene. Frank suggests this may paradoxically enhance evolvability: overparameterized systems (deep dense networks in machine learning) learn complex patterns particularly well, and biological overwiring may have similarly accelerated adaptive evolution.

### Cancer as the primary motivating example

The cancer example runs throughout: multiple overlapping protections (cell-cycle checkpoints, apoptosis, DNA repair, immune surveillance) illustrate that adding one more protective layer reduces selective pressure on each existing layer, permitting those layers to decay and accumulate heritable variation in cancer predisposition. Different tissues/species have different numbers of protections — evidence that the count is evolutionarily labile — which is exactly what the paradox of robustness predicts.

## Limitations

- No formal model: the verbal argument is compelling but the shape of the fitness decay curve and the conditions under which decay versus drift occurs are unspecified. No quantitative predictions are derived.
- Empirical examples are sparse: the author explicitly acknowledges difficulty finding clear biological step-by-step examples of the paradox; the RAID array example is from engineering, not biology.
- Cancer predisposition is a conceptual illustration; Frank does not engage with specific mutational data, cancer type differences, or the quantitative relationship between protection-layer count and instability.
- The framework conflates selection-weakening (cost-benefit shift) with genetic drift (neutrality) — these have different evolutionary dynamics and population-size dependencies — but the distinction is not fully resolved.
- Machine-learning analogy (benign overfitting / deep networks) is speculative and the connection to biological evolvability is asserted without mechanism.
- Commentary format (15-reference limit enforced by editorial policy) means the literature synthesis is highly selective; additional references are relegated to an arXiv companion (arXiv:2304.09069).
