---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Giere2004
kind: paper
title: How Models Are Used to Represent Reality
version: "1.0.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: Giere2004
tags: []
dataset_usage: []
ontology_terms: []
paper_kind: ''
---
## Key Findings

**The four-place schema.** The core claim is that "S uses X to represent W for purposes P"
is the irreducible unit of scientific representation. Abstracting away to a two-place
"X represents W" loses the agent (who picks relevant similarities) and the purpose
(which determines which similarities are relevant). There is no representation without
a representing agent with a goal.

**Models as abstract objects.** Giere holds that models are abstract objects, not
linguistic entities. Any given abstract model can be characterized by many different
linguistic or mathematical expressions; conversely, two equations may characterize the
same model. Models are created-interpreted: they are not merely formal structures
but already come "with content." This means models are ontologically distinct from
the representations (words, diagrams, equations) used to characterize them.

**Principles as templates, not laws.** Newton's three laws, Maxwell's equations, the
principle of natural selection — these are not empirical generalizations but templates
for constructing models. They define very abstract objects (by specifying the quantities
and relations that models built under them must exhibit), and they function by
constraining and shaping the models constructed from them. This dissolves the old
debate about whether laws are empirical claims or definitions: the question is ill-posed
for principles; what is empirically testable are always specific models built with those
principles plus specific conditions.

**Similarity and agent choice.** Models represent via designated similarities. A scientist
uses a model to represent a target by picking out specific features of the model and
claiming those features are similar to features of the real system to some specified
degree of fit. No objective similarity measure is required; the lack of such a measure
does not introduce unacceptable relativity because claims about features of the world
remain as objective as they ever were. The agent specifying which features are to be
compared does the "loading" that makes representation directional.

**Purpose-relativity without conflict.** Water can be modeled as a collection of
molecules (for Brownian motion) and simultaneously as a continuous fluid (for pipe
flow) without contradiction, because both representations are relative to distinct
purposes. There is no privileged "what water really is" beyond the sense in which a
molecular perspective is asymmetrically more general (one can in principle explain why
a macroscopic fluid model works from within molecular principles, but not vice versa).
This asymmetry justifies a form of realism about the molecular level without requiring
that the fluid model be false.

**Perspectival realism.** The account is realist — claims of similarity extend to
unobservable features (DNA structure, atomic bonding angles) — but bounded: where
two models differ only in regions in principle undetectable (e.g., outside our light
cone), there is no scientific basis for preferring one. Representation claims are limited
to what is in principle detectable by any means compatible with our best physical
theories.

**Evidence as decision.** A brief coda (§7) notes that evidentiary relationships should
also be understood pragmatically — as human decisions to accept or reject hypotheses
in light of interests — deferring to *Explaining Science* (1988) for the full argument.

## Limitations

- The paper's scope is narrow (11 pp.); it establishes the four-place schema but does
  not develop a full theory of representation, similarity, or evidence. For the
  full similarity-vs-isomorphism debate, see Suárez (2003) [cited] and Nguyen & Frigg (2022).
- Giere does not address multi-model consistency or how agents should reason when two
  models of the same target give conflicting predictions for the same purpose — the
  toolkit's "incompatible models" problem (discussed in Frigg and Hartmann's SEP entry [@Frigg2025], §5.1)
  is not resolved here.
- The account of similarity is intentionally permissive (no objective measure required),
  which leaves open how agents should quantify degree-of-fit when models are used for
  quantitative prediction. The toolkit's belief machinery must supply this.
- The paper does not address computational or knowledge-representation questions; it
  cannot advise on how to encode the four-place schema in a graph store or what
  fields to add to a patch schema.
