---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Baumeler2025
kind: paper
title: Flow of dynamical causal structures with application to correlations
version: "1.0.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: Baumeler2025
tags: []
ontology_terms: []
---
## Key Findings

1. The flow graph makes the dynamical aspect of cyclic causal structures explicit:
   directed cycles in a causal model represent *potential* information paths, not
   actual causal loops; the flow "unravels" which paths are realised under each
   sequence of interventions.
2. The superflow is a purely qualitative object — its construction requires only
   the causal structure (digraph), not the numerical or functional parameters.
   Qualitative causal-order questions can therefore be answered at the
   structural level alone.
3. **Theorem 3 (Causal correlations):** If every leaf of a flow F is a trivial
   (single-vertex) graph, then the process produces only causal correlations, i.e.,
   correlations that decompose as a convex mixture in which each term fixes a
   definite causal order among the agents.
4. The theorem also holds for superflows (since a superflow is a supergraph of
   the flow), making it applicable without model parameters.
5. There exist causal structures with chordal directed cycles that, by Theorem 3,
   still produce only causal correlations — filling a gap left by the prior
   chordless-cycles sufficient condition.
6. The companion C implementation of Algorithm 2 is openly available [Ref 29].

## Limitations

The paper is restricted to classical-deterministic models; the authors explicitly
defer the quantum case.
Algorithms are exponential in the number of agents, limiting practical
applicability to small causal structures.
The results concern *possible* correlations, not their statistical
estimation — the paper is a theoretical contribution with no empirical component.
The practical operationalisation for software tooling (e.g., how to index or
store flows in a graph database) is not addressed.
