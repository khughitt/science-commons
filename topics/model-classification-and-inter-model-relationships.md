---
schema_profile: science-entity-base/1.0+topic/2.0
id: topic:model-classification-and-inter-model-relationships
kind: topic
title: Classification of Mathematical Models and Their Inter-Relationships
version: "1.0.0"
created: "2026-05-18"
updated: "2026-05-18"
tags: []
datasets: []
ontology_terms:
- functor
- mathematical-model
- model-coupling
- morphism
- symmetry-group
related:
- topic:parameter-ontology
source_refs:
- paper:BaezStay2010
- paper:Bronstein2021
- paper:Courtney2017
- paper:Legatiuk2025
- paper:Schembera2024
- paper:Spivak2014
- paper:Legatiuk2021
- paper:Papillon2024
---
## Summary

The question of how to systematically classify mathematical models of natural systems — and
formalize the relationships between them — spans category theory, ontology engineering, geometric
deep learning, and knowledge graph research. This topic is central to the project's primary
research question: whether a structural ontology of models and parameters can reveal previously
unappreciated analogies. Several independent research threads converge here, from Legatiuk's
categorical formalization of model relations, through Baez & Stay's "Rosetta Stone" across
physics/topology/logic/computation, to applied ontology projects like MathModDB and SBO that
provide operational vocabularies for model metadata.

## Key Concepts

### 1. Model as Mathematical Object

A **mathematical model** is a formal description of a system — typically a set of equations
(ODE, PDE, SDE, algebraic), a state space, parameters, and boundary/initial conditions. The
challenge is that the "same" physical phenomenon admits many models at different levels of
abstraction (continuum vs. discrete, deterministic vs. stochastic, linearized vs. full). Any
classification scheme must handle this multiplicity.

### 2. Classification Lenses

Models can be classified along several orthogonal axes:

- **Mathematical structure**: PDE vs. ODE vs. algebraic; linear vs. nonlinear; parabolic vs.
  hyperbolic vs. elliptic.
- **Dynamical behavior**: fixed points, limit cycles, chaos, pattern formation.
- **Symmetry and invariance**: which symmetry groups leave the model equations invariant
  (translation, rotation, Galilean, Lorentz, gauge). This is the lens used by geometric deep
  learning [@Bronstein2021].
- **Scale/self-similarity**: microscopic vs. mesoscopic vs. macroscopic; renormalization group
  connections.
- **Domain**: physics, chemistry, biology, ecology, etc.
- **Computational framework**: as classified by SBO (logical, continuous, discrete, hybrid)
  [@Courtney2017].

A key open question is whether these lenses are independent or share deeper common structure
(see Q1 in `specs/research-question.md`).

### 3. Category-Theoretic Formalization

Category theory provides the most rigorous framework for relating models to one another:

- **Legatiuk (2021, 2025)**: Formalizes each mathematical model as an object in a category, with
  morphisms representing typed relationships between models (specialization, approximation,
  coupling). Introduces practically relevant properties (completeness, consistency of coupled
  models) at the categorical level. Extended in a 2025 Springer monograph to cover coupled
  multi-physics models [@Legatiuk2021; @Legatiuk2025].

- **Baez & Stay (2010)**: The "Rosetta Stone" paper demonstrates that closed symmetric monoidal
  categories provide a common language for physics, topology, logic, and computation. The same
  diagrammatic calculus (string diagrams / Feynman diagrams) describes quantum processes,
  cobordisms, proofs, and programs [@BaezStay2010].

- **Spivak (2012, 2014)**: Ologs (ontology logs) use category theory as a human-readable
  knowledge representation framework. *Category Theory for the Sciences* grounds these ideas in
  applied modeling across scientific domains [@Spivak2014].

- **Fong & Spivak (2019)**: *Seven Sketches in Compositionality* extends applied category theory
  to compositional systems — directly relevant to how models compose and couple.

### 4. Geometric and Algebraic Taxonomy

- **Bronstein et al. (2021)**: The Geometric Deep Learning (GDL) blueprint classifies neural
  network architectures by the symmetry group they respect (the "5G" taxonomy: Grids, Groups,
  Graphs, Geodesics, Gauges). This provides a model for how *any* mathematical model can be
  classified by its invariance structure [@Bronstein2021].

- **Papillon et al. (2024)**: *Beyond Euclid* extends this taxonomy to topological and algebraic
  structures beyond symmetry groups, proposing a graphical taxonomy that unifies geometric,
  topological, and algebraic perspectives. This is a useful template for our own
  classification effort [@Papillon2024].

### 5. Ontologies and Knowledge Graphs

Operational efforts to build machine-readable model taxonomies:

- **MathModDB / MaRDI** (Schembera et al., 2024): A knowledge graph for mathematical models and
  algorithms in applied mathematics. Defines entity types (Mathematical Model, Mathematical
  Formulation, Research Problem, Quantity, Algorithm) and connects them via "computational
  tasks." Contains 1200+ elements and 250+ research assets [@Schembera2024].

- **SBO** (Systems Biology Ontology): Six orthogonal vocabularies for reaction participants,
  quantitative parameters, mathematical expression types, modeling frameworks, entity types, and
  interaction types. Integrated into SBML. Directly relevant to our parameter ontology work
  [@Courtney2017].

- **QUDT** (Quantities, Units, Dimensions, Types): Provides standardized quantity-kind
  vocabulary. Already referenced in our parameter registry design.

### 6. Model Relationships (Edge Semantics)

Relationships between models form a rich typed vocabulary:

| Relationship | Description | Example |
|---|---|---|
| **Specialization** | Model A is a special case of Model B | Fick's law ← general diffusion |
| **Approximation** | A approximates B under conditions C | Linearized ← nonlinear |
| **Limit** | A is obtained from B in some limit | Classical ← quantum (ℏ→0) |
| **Coupling** | A and B are coupled into a multi-physics model | Navier-Stokes + heat equation |
| **Duality** | A and B are dual formulations | Lagrangian ↔ Hamiltonian |
| **Analogy/Functor** | Structure-preserving map between domains | Electrical ↔ mechanical oscillator |
| **Dimensional reduction** | A obtained by integrating out dimensions from B | 2D shallow water ← 3D Navier-Stokes |
| **Coarse-graining** | A is a coarse-grained version of B | Langevin ← molecular dynamics |

These correspond to different morphism types in a categorical formalization.

## Current State of Knowledge

**Well-established:**

- Category theory is the right mathematical framework for formalizing inter-model relationships.
  This is broadly accepted in mathematical philosophy and increasingly in applied mathematics.
- Symmetry/invariance provides a powerful classification axis, well-demonstrated by GDL and
  physics (Noether's theorem, gauge theory).
- Operational ontologies (SBO, QUDT, MathModDB) work well within specific domains but remain
  siloed across disciplines.
- Individual model relationships (limits, approximations, dualities) are well-understood
  pairwise but not systematically cataloged.

**Emerging:**

- Applied category theory is maturing rapidly (Topos Institute, ACT conferences since 2018).
  Tools for compositional modeling are becoming practical.
- Knowledge graphs for mathematical models (MathModDB) are recent (2023-2024) and actively
  evolving.
- The "Beyond Euclid" graphical taxonomy approach — classifying structures by their mathematical
  properties rather than application domain — is a promising template.

**Uncertain / Open:**

- Whether a single unified classification scheme can span the full diversity of mathematical
  models (from PDEs to stochastic processes to agent-based models to algebraic structures).
- How to handle models that exist at multiple levels of abstraction simultaneously.
- Whether the knowledge graph of models itself has emergent structural properties (Q5 in our
  research question).
- How parameter-mediated connections (shared parameters across models) map onto categorical
  morphisms.

## Controversies & Open Questions

1. **Granularity problem**: At what granularity is a "model" a node in the graph? Is
   "Navier-Stokes" one model or a family? Does each boundary condition variant count?
   Legatiuk's categorical approach handles this via sub-object structure, but practical
   implementations must make choices.

2. **Completeness of relationship types**: The relationship vocabulary above (specialization,
   approximation, limit, coupling, duality, analogy, reduction, coarse-graining) is a starting
   point. Are there fundamental relationship types missing? Adjunctions and natural
   transformations from category theory suggest additional structure.

3. **Cross-domain validity**: Analogies between models from different domains (e.g., electrical
   circuits ↔ mechanical oscillators ↔ chemical kinetics) are powerful but can be misleading.
   Under what conditions is a "structural analogy" genuinely informative vs. superficial? Baez's
   Rosetta Stone framework gives partial answers via functorial mappings, but the question
   remains open for less clean correspondences.

4. **Computational tractability**: A full categorical treatment of 247 models with all their
   relationships would be a large structure. What tooling exists for computing with such
   categories? (CatLab.jl, AlgebraicJulia, and the ACT community's tools are relevant.)

5. **Parameter ontology as classification axis**: Our project uniquely explores whether shared
   parameters (e.g., diffusion coefficient appearing in Gray-Scott, Navier-Stokes, and Fick's
   law) constitute a meaningful classification axis. This is not well-explored in the literature
   — most classification schemes ignore parameters entirely, focusing on equation structure.

## Key References

- [@Legatiuk2021] — Categorical formalization of model relations; the most directly relevant
  theoretical framework.
- [@Legatiuk2025] — Extended treatment including coupled models (Springer monograph).
- [@BaezStay2010] — The "Rosetta Stone" demonstrating cross-domain categorical analogies.
- [@Spivak2014] — Category theory as applied knowledge representation (ologs).
- [@Bronstein2021] — Geometric Deep Learning blueprint; symmetry-based model taxonomy.
- [@Papillon2024] — "Beyond Euclid" graphical taxonomy extending GDL to topology and algebra.
- [@Schembera2024] — MathModDB knowledge graph for mathematical models.
- [@Courtney2017] — SBO ontology for systems biology models and parameters.
