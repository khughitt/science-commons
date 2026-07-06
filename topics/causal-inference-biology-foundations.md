---
schema_profile: science-entity-base/1.0+topic/2.0
id: topic:causal-inference-biology-foundations
kind: topic
title: Causal Inference Frameworks for Molecular Biology — Philosophical and Methodological Foundations
version: "1.0.0"
created: "2026-05-18"
updated: "2026-05-18"
tags: []
ontology_terms: []
related:
- decision:D8
- hypothesis:h4-attractor-convergence
- inquiry:h1-prognosis
- topic:causal-inference
source_refs:
- paper:Feuerriegel2024
- paper:Laubach2021
- paper:Mooij2024
- paper:Ross2021
- paper:Touré2021
---
## Summary

Causal inference in molecular biology spans at least three distinct intellectual traditions
that are frequently conflated: (1) the philosophical analysis of what causal concepts mean
in biology (mechanism vs. pathway, Woodward's interventionism, causal specificity); (2)
the statistical and graphical frameworks for identifying causal effects from data (DAGs,
do-calculus, potential outcomes); and (3) causal machine learning for individualized
treatment-effect estimation. Each tradition has its own vocabulary, commitments, and failure
modes. MM30's current inference architecture draws implicitly from all three but has not
articulated which framework governs which claim. This document makes that mapping explicit,
evaluates the fit between each framework and MM30's data architecture, and surfaces the
implications for the H4 attractor inquiry.

---

## Key Concepts

### 1. Mechanism vs. Pathway (Ross 2021)

The most consequential philosophical distinction for MM30 is Lauren Ross's separation of
two causal concepts that biologists routinely use but rarely distinguish:

**Mechanism:** Specifies *how* X causes Y by describing the components, their activities,
and their organization. A mechanism explains by decomposing: the E2F1 → PHF19 mechanism
includes E2F1 binding to PHF19 regulatory regions, transcriptional activation, Tudor-domain
reading of H3K36me3, and PRC2 recruitment. The explanation is complete when each step is
decomposed to an acceptable level of description. Mechanisms are singular: one mechanism
explains one phenomenon.

**Pathway:** Specifies *that* and *through what sequence* X causes Y by tracking the flow of
some conserved quantity (signal, substance, information) through a series of steps. A
signaling pathway tracks signal propagation; a metabolic pathway tracks chemical substrate
flow; a causal pathway in epidemiology tracks counterfactual dependence through a series of
nodes. Critically, pathways can **branch, converge, and describe multiple routes** through
the same causal system — something mechanism models do not naturally represent.

Ross's key argument: philosophical accounts that treat all biological causal concepts as
mechanisms (the Machamer-Darden-Craver tradition) miss an important class of explanatory
structures. Pathways answer a different question than mechanisms: not "how does X cause Y?"
but "via what route does X's influence reach Y, and which routes are open?" Pathway
representations enable causal selection (which route matters most?) in a way mechanisms
do not.

This distinction has a practical implication: the same biological system can be described
using both concepts simultaneously, but they support different inferences. A mechanism
description supports claims about necessity and sufficiency of components; a pathway
description supports claims about alternative routes, compensatory responses, and the
effect of blocking one node on overall signal flow.

**Where mechanism applies in MM30's claim stack:**
- H1 intra-axis edges: PHF19-KD → IFN derepression (Ren 2019), EZH2 degradation →
  E2F suppression (Yu 2023 MS177). These are mechanism claims because they describe
  specific molecular components and their activities, not generic signal flow.
- The catalytic-vs-scaffold distinction (t205): MS177 degrades EZH2 protein (removes the
  scaffold); C24 inhibits catalytic activity only. This is mechanistic: which component
  is necessary for which downstream effect.

**Where pathway applies in MM30's claim stack:**
- The H1↔H2 bridge question ("ribosome → E2F1"): this is a pathway question — does the
  ribosome program's influence reach E2F1, and if so through what route? t172/t204
  found that the bulk anti-coupling is composition-driven, not a within-cell molecular
  mechanism. The distinction is essentially: the pathway exists at the patient/tumor
  level as a composition gradient, not at the within-cell mechanism level.
- H4's convergence structure: multiple cytogenetic subtypes (different starting points)
  converge on PR/RRPC (shared endpoint). This is a pathway-level claim — about the
  structure of routes through the landscape — not a mechanistic claim about specific
  molecular components.
- The survival meta-analysis rankings: the SumZ/std-metafor rankings identify pathway-level
  associations (which gene's influence reaches survival outcomes). They are silent on mechanism.

**The analytical implication for MM30:** When a claim is at the pathway level (route
structure, alternative paths, convergence), the evidence standard is different from
mechanism claims. Pathway claims can be partially supported by observational data that
establishes route-existence (the influence propagates); mechanism claims require
intervention experiments that establish component-necessity. The failure to distinguish
these levels is the root cause of the "observational route closed, interventional route
open" structure of D8 — the ribosome → E2F1 question is a pathway question masquerading
as a mechanism question.

---

### 2. DAG-Based Causal Identification (Laubach 2021)

The second tradition derives from Pearl's do-calculus and structural causal models,
operationalized for working scientists. Laubach et al. [Laubach 2021] provide the clearest
exposition for biologists unfamiliar with the epidemiological tradition. Four tasks must be
kept separate:

| Task | Goal | Causal knowledge required | Hallmark question |
|------|------|--------------------------|-------------------|
| Description | Summarize data | None | What is the distribution of X? |
| Prediction | Maximize out-of-sample accuracy | Some | What value of Y should I expect? |
| Association | Quantify crude X-Y relationship | None | Are X and Y correlated? |
| Causal inference | Estimate do(X) effect on Y | Substantial | What happens to Y if I intervene on X? |

The error modes are asymmetric. Adding covariates to a **prediction** model generally
improves it; adding the wrong covariate to a **causal** model can introduce severe bias
(collider bias is the canonical case). This means the same regression formula can be
appropriate or inappropriate depending solely on which task is being performed.

**DAG construction discipline.** The key methodological requirement is that causal
structure must be specified *before* data analysis. A DAG encodes:
- Arrows (X causes Y)
- Missing arrows (no direct causal path from X to Y)
- Implicit assumptions (no unmeasured confounders between pairs of nodes not connected by a
  common cause)

Given a DAG, the adjustment set for estimating a target effect is determined by the
backdoor and front-door criteria (or more generally, by d-separation). **Three structural
roles create confusion:**

- **Confounder:** Common cause of X and Y. Must be adjusted for. Adjusting blocks the
  backdoor path that would otherwise confound the X→Y effect estimate.
- **Collider:** Common effect of X and Y (or of two variables on a path of interest).
  Must NOT be adjusted for. Adjusting on a collider opens a spurious path between its causes.
- **Mediator:** On the causal path between X and Y. Adjusting for a mediator blocks the
  (possibly intended) causal path; whether to include it depends on whether the estimand
  is total or direct effect.

**Identification vs. estimation.** A causal effect is *identified* if it can in principle
be computed from the observed data distribution (given the DAG). Identification is a
logical/algebraic question, separate from estimation (the statistical question of how to
compute it from finite data). Many effects that are not identified from observational data
become identified given interventional data (even a single randomized experiment on a
subset of nodes).

**The unconfoundedness assumption.** For any observational causal claim, the key threat is
unmeasured confounding. A measured confounder can be adjusted for; an unmeasured one
cannot. Sensitivity analysis methods (e-values, Rosenbaum bounds) quantify how strong an
unmeasured confounder would need to be to overturn a finding — but they cannot prove
unconfoundedness.

---

### 3. Causal Discovery — Structure Learning from Data

Where DAG-based identification assumes the causal graph is known and asks "given this
graph, can I identify this effect?", causal discovery algorithms ask the reverse question:
"given data, what causal graphs are consistent with it?"

Standard causal discovery algorithms (PC, FCI, GES, LiNGAM, NOTEARS) attempt to recover
a DAG (or equivalence class of DAGs) from observational data by testing conditional
independences. The approach has known limitations that are especially severe in molecular
biology [Mooij 2024]:

1. **Faithfulness violations.** Biological feedback loops create cycles that violate the
   acyclicity requirement of DAGs. Most organisms use feedback for robustness; post-
   translational modification networks are rarely acyclic. Standard methods either fail or
   require specialized cycle-aware extensions.

2. **Latent confounding.** Most biological datasets have unmeasured variables (cell-state
   composition, technical batch effects, unsequenced regulatory RNAs). FCI handles latent
   confounders but produces less informative equivalence classes.

3. **High dimensionality + small n.** A bulk RNA-seq dataset with 20,000 genes and 200
   samples is a causal discovery nightmare: p >> n means almost any conditional independence
   test is unreliable. Sparsity priors help but must be specified.

4. **Non-linearity.** Many biological relationships are saturating, threshold-like, or
   Boolean. LiNGAM and score-based methods that assume linearity will misidentify these.

5. **Evaluation against synthetic data.** The causal discovery literature has been
   criticized for benchmarking primarily on synthetic datasets (SERGIO, GeneNetWeaver) that
   satisfy all algorithmic assumptions. Real biological datasets routinely violate them.

**The interventional data advantage.** A key insight from the formal theory: even one
interventional (do-calculus-style) experiment can dramatically increase identifiability.
Perturb-seq datasets (combining CRISPR perturbations with scRNA-seq) supply the kind of
interventional data that makes causal discovery tractable. This is why the field is moving
toward perturbation atlases as the gold standard for GRN inference.

---

### 4. Causal Machine Learning for Treatment Outcomes (Feuerriegel 2024)

Causal ML extends the potential outcomes (Rubin) framework with flexible function
approximation. The key quantity is the **Conditional Average Treatment Effect (CATE)**:

```
CATE(x) = E[Y(1) - Y(0) | X = x]
```

where Y(1), Y(0) are potential outcomes under treatment/control and x is a patient
covariate profile. Standard regression estimates E[Y | X, T] — a prediction, not a causal
effect. The difference matters: a drug that is prescribed to sicker patients will look
less effective in observational data because "is prescribed" correlates with worse
prognosis; CATE estimation requires removing this confounding.

Main method families:
- **Meta-learners** (S/T/X/R-learner): decompose CATE estimation into standard regression
  subproblems. T-learner fits separate models per arm; X-learner cross-fits; R-learner
  is doubly robust.
- **Doubly Robust (DR) learners**: combine an outcome model and a propensity score model;
  consistent if either is correctly specified.
- **Causal forests** (Wager & Athey): tree-based nonparametric CATE estimators with
  asymptotically valid confidence intervals.

**RCT vs. observational data.** In RCTs, treatment is randomized; unconfoundedness holds
by design. In observational data, three assumptions are required: (1) unconfoundedness
(no unmeasured confounders of treatment and outcome), (2) positivity/overlap (all patients
have positive probability of each treatment), (3) consistency (the potential outcome under
treatment t equals the observed outcome when treatment = t). All three are
untestable from data alone.

**The negative control design.** A practical approach when RCT data is unavailable:
identify outcome variables that should not be affected by the treatment under any causal
model. If negative controls show apparent "effects," the design is confounded.

---

### 5. Causal Annotation in Biological Databases (Touré 2021)

A practically underappreciated issue: the "causal" annotations in pathway databases
(KEGG, Reactome, SIGNOR, WikiPathways) use heterogeneous and often inconsistent causal
semantics [Touré 2021]. Key findings:

- **SIGNOR and Causal Biological Networks (CBN)** provide explicit causal statements
  (subject → predicate → object with effect sign). These are the most formally curated.
- **KEGG and WikiPathways** encode "activity flow" — directed regulatory relationships —
  but the direction is often topological/functional rather than formally causal (it does
  not distinguish "A activates B" from "A correlates with B's activation in pathway context").
- **Reactome** uses process description (detailed biochemical); extracting causal
  statements requires additional inference.
- **Logical operators are underspecified:** whether two upstream activators are AND or OR
  gates is almost never annotated. This matters for Boolean attractor models.
- **MI2CAST standard:** the recommended minimum information standard for causal interaction
  curation. Compliance is low across major databases.

For MM30: the H1 DAG is more formally curated than any of these databases — it has
explicit effect signs, pre-registration, and interventional anchoring. But when importing
external pathway knowledge to ground edges (e.g., PHF19 → EZH2 based on SIGNOR), the
causal semantics of the imported annotation should be checked against MI2CAST criteria.

---

### 6. Multiscale Causation in Biology

A 2025 Acta Biotheoretica paper proposes a physical theory of causation that handles
multiscale biological systems by applying a **conservation of causation** principle:
causal flow is conserved across scales in dynamically coarse-grained systems. Both pure
upward causation (micro-to-macro) and pure downward causation (macro-to-micro) are
formally forbidden in this framework; instead, causation flows through a continuous
multiscale chain.

The practical implication: bulk RNA-seq measures a macro-level quantity (sample-average
expression) that is a coarse-graining of single-cell states. Causal claims about bulk
expression must be interpreted as claims about the coarse-grained level, not about
within-cell molecular mechanisms. This is the formal justification for why the
observational route to within-cell mechanism (the H1↔H2 bridge question) cannot be
answered by bulk data alone — bulk measurements access a different causal scale than the
within-cell mechanisms being claimed.

---

## Current State of Knowledge

### What is well-established

1. **The DAG + do-calculus framework** for causal identification is mathematically mature
   (Pearl 2000, Spirtes et al. 2000). The formal theory of when observational data can
   identify causal effects is settled.

2. **The mechanism/pathway distinction** (Ross 2021) is philosophically well-grounded and
   operationally useful. It has been tested against a wide range of biological examples.

3. **Causal ML for CATE estimation** is statistically well-developed [Feuerriegel 2024].
   Multiple estimators (causal forests, DR-learners) have semiparametric efficiency theory
   and asymptotic guarantees under unconfoundedness.

4. **Identification fails under unmeasured confounding.** All three traditions agree that
   observational data alone cannot rule out unmeasured confounders; interventional data
   (experiments, natural experiments, genetic instruments) is necessary for identification.

5. **Interventional data dramatically increases identifiability.** Even partial intervention
   data (experiments on a subset of nodes) can sharply narrow the equivalence class of
   causal graphs consistent with the data.

### What remains uncertain or contested

1. **Whether biological GRNs can be recovered from observational expression data.**
   The consensus from causal discovery benchmarks is: probably not in general. High
   dimensionality, latent confounders, and feedback cycles collectively make standard
   algorithms unreliable on real biological data without strong priors or interventional
   supplementation.

2. **Which estimand is most defensible for bulk RNA-seq associations.** Does a Cox
   regression coefficient for gene g's expression on overall survival estimate anything
   causal, or is it an observational association? The answer depends on whether sufficient
   confounders are measured and adjusted for, which is rarely fully verifiable.

3. **The appropriate level of causal description for cancer biology.** Is "PHF19 causes
   poor prognosis" a mechanism claim, a pathway claim, or a purely predictive association?
   The field tends to use causal language ("PHF19 promotes proliferation") without
   specifying the evidence standard.

4. **Causal ML assumptions in high-risk cancer settings.** Unconfoundedness and positivity
   are assumed; both may be violated for treatment choice in relapsed/refractory MM where
   frail patients receive only certain regimens.

---

## Key References

[Ross 2021] Lauren N. Ross. "Causal Concepts in Biology: How Pathways Differ from
Mechanisms and Why It Matters." *British Journal for the Philosophy of Science* 72(1), 2021.
DOI: 10.1093/bjps/axy078

[Laubach 2021] Zachary M. Laubach, Eleanor J. Murray, Kim L. Hoke, Rebecca J. Safran,
Wei Perng. "A biologist's guide to model selection and causal inference." *Proceedings of
the Royal Society B* 288(1943):20202815, 2021. PMC7893255

[Feuerriegel 2024] Stefan Feuerriegel et al. "Causal machine learning for predicting
treatment outcomes." *Nature Medicine* 30:958–968, 2024.
DOI: 10.1038/s41591-024-02902-1

[Touré 2021] Vasundra Touré et al. "The status of causality in biological databases:
data resources and data retrieval possibilities to support logical modeling." *Briefings
in Bioinformatics* 22(4):bbaa390, 2021. DOI: 10.1093/bib/bbaa390

[Mooij 2024] Joris M. Mooij et al. "The Landscape of Causal Discovery Data: Grounding
Causal Discovery in Real-World Applications." arXiv:2412.01953, 2024.

[Pearl 2009] Judea Pearl. *Causality: Models, Reasoning, and Inference* (2nd ed.).
Cambridge University Press, 2009.

[Woodward 2003] James Woodward. *Making Things Happen: A Theory of Causal Explanation.*
Oxford University Press, 2003.

---
