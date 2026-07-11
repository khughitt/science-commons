---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Frigg2025
kind: paper
title: Models in Science (Stanford Encyclopedia of Philosophy)
version: "1.0.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: Frigg2025
tags: []
dataset_usage: []
ontology_terms: []
paper_kind: literature-review
---
## Key Findings

**Representation**: Models represent via partial, distorted resemblance or structural
isomorphism, not mirror-image copying. Idealizations (Aristotelian: strip irrelevant
properties; Galilean: deliberate distortion) are the rule, not the exception. Many models
cannot be de-idealized back to a "true" description because the idealizations are ineliminable.

**Ontology**: Models are not a single ontological kind. Scientists use material objects,
fictional/abstract objects, set-theoretic structures, and stylized descriptions interchangeably
as models. The fiction view (Frigg, Godfrey-Smith) treats models as analogous to fictional
characters — this is not a claim of falsity but of imaginative mode.

**Epistemology**: Models serve as vehicles for surrogative reasoning: we study the model to
learn about the target. Learning has two steps — learning about the model (through
construction and manipulation) then translating that knowledge to the target (dependent on
what representational relation holds). Models explain not only despite their falsity but often
because of it (Cartwright, Elgin). Elgin's "felicitous falsehoods" emphasize that understanding
is holistic and models produce it by revealing systematic epistemic structure, not by
enumerating true facts. Trade-offs among accuracy, generality, and simplicity are
ineliminable (Levins 1966): no model maximizes all three simultaneously.

**Models and Theory**: The semantic view construes a theory as a family of models, not
sentences. Models are often independent of or prior to theory: interpretative models
(Cartwright) are required to apply abstract theory to concrete systems and are not derivable
from the theory alone; models as mediators (Morgan and Morrison 1999) are autonomous
agents that theories do not determine ("theories are not vending machines"). In complex
domains (climate, laser systems), models and theories become entangled and the boundary
dissolves.

**Patchwork of Models**: Cartwright (1999) and Hacking (1983) argue that science is a
patchwork of locally valid, domain-specific models, each holding ceteris paribus in its
domain, with no systematic deductive relations between them — "The Dappled World". This
contrasts with a unified-theory picture. Counter-proposals establish various inter-model
relations (reductive, approximative, "story" relations), suggesting the patchwork may be
partially connectable; whether a general account is possible is open and may be tractable
within a Bayesian framework.

**Realism and Laws**: The incompatible-models problem (Morrison 2000) challenges simple
realism: different successful models of the same target can be mutually inconsistent.
Perspectival realism (Giere, Massimi) is the current middle position. Laws are better
understood as ceteris paribus or as open-ended statements instantiated in models
(Cartwright, Giere, Teller), not universal truths about the world.

## Limitations

As a philosophical survey entry, this article:
- Does not engage with computational or software implementation questions; it cannot advise
  on how to represent patches in a knowledge graph or what serialization format to use.
- The "patchwork" metaphor is treated at a high level of abstraction; the entry does not
  specify how patches connect or how evidence crosses patch boundaries — those are
  open problems the toolkit must solve operationally.
- The fiction view and the semantic view are treated as competing positions on model
  ontology; the entry is neutral. For the toolkit, a pragmatic position (models are
  mathematical + provenance-annotated + uncertainty-bearing structures, regardless of
  their ontological status) is sufficient.
- Discussion of Bayesian inter-model relations (§5.2) is nascent and points to open research;
  the toolkit's federation design is ahead of the philosophy literature here.
