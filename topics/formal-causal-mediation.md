---
schema_profile: science-entity-base/1.0+topic/2.0
id: topic:formal-causal-mediation
type: topic
title: Formal Causal Mediation Analysis — NDE/NIE, 4-Way Decomposition, and Sensitivity Analysis
version: "1.0.0"
created: "2026-05-18"
updated: "2026-05-18"
tags: []
ontology_terms: []
related:
- decision:D8
- hypothesis:h2-cytogenetic-distinct-entities
- inquiry:h1-prognosis
- interpretation:2026-04-11-mediation-null-model-result
- interpretation:2026-04-12-t165-phf19-survival-prolif-mediation
- topic:causal-inference
- topic:causal-inference-biology-foundations
source_refs:
- paper:Imai2010
- paper:Richiardi2013
- paper:Shi2021
- paper:VanderWeele2014_fourway
- paper:VanderWeele2014_multiple
- paper:VanderWeele2016
- paper:Yoshida2022
---
## Summary

Mediation analysis asks how much of an exposure's effect on an outcome passes through a
specific intermediate variable (the mediator) and how much operates through other routes.
The informal Baron-Kenny approach (1986) conflates this question with a regression
comparison that silently assumes no exposure-mediator interaction, no unmeasured
mediator-outcome confounding, and linear effects throughout. These assumptions fail in
exactly the situations MM30 cares about: gain(1q) interacts with proliferation, PHF19 acts
on survival through both proliferation and immune-evasion branches, and all mediators are
observationally measured in bulk RNA-seq with unmeasured composition confounding.

The formal framework — developed by Robins, Pearl, VanderWeele, and Imai — replaces the
regression comparison with a counterfactual definition of direct and indirect effects that
makes all identifying assumptions explicit. The VanderWeele 4-way decomposition further
separates the exposure effect into four orthogonal components, of which only the final
one ("pure indirect effect") maps to what Baron-Kenny calls mediation. Sensitivity analyses
(Imai's sequential ignorability parameter, VanderWeele's bias formulas) bound the claims
when identifying assumptions are not credible.

For MM30, the key practical conclusions are: (1) the difference and product methods that
MM30 currently uses are numerically equivalent under linearity and are the correct
estimators of NDE/NIE in linear models with no exposure-mediator interaction — so existing
estimates are not wrong; (2) the t125 null model retraction is essentially a rediscovery of
the exposure-mediator interaction / stratum-specific baseline problem that 4-way
decomposition handles formally; (3) formal NDE/NIE analysis is most warranted for the
PHF19 mediation chain (where an exposure-mediator interaction is plausible) and for any
future claims involving the gain(1q) × proliferation interaction; (4) the R tooling
(`regmedint`, `CMAverse`) integrates cleanly with Cox outcomes and MM30's existing
R-heavy pipeline.

---

## Key Concepts

### 1. The Problem with Baron-Kenny Regression Comparison

The Baron-Kenny (BK) approach estimates mediation via two regression models and two
conditions:

```
Model 1:  Y = β₀ + β₁X + ε
Model 2:  Y = β₀ + β₁'X + β₂M + ε
```

The indirect effect is estimated as either β₁ - β₁' (difference method) or α₁ × β₂
(product method, where α₁ is the X → M coefficient). For continuous outcomes and a
single continuous mediator, these are algebraically equivalent and produce consistent
estimates of the average causal mediation effect (ACME) — IF the model is correctly
specified.

The approach fails under three conditions that the formal framework addresses explicitly.

**Failure mode 1: Exposure-mediator interaction.** If X and M interact in their effect
on Y, adding M as a covariate introduces a product term that the simple regression
comparison cannot decompose. The BK "direct effect" becomes an estimand that varies
with the level of M at which it is evaluated — it is not a well-defined quantity without
specifying a reference level. The 4-way decomposition handles this by separating the
pure direct, interaction, mediated interaction, and pure indirect components (section 3
below).

**Failure mode 2: Unmeasured mediator-outcome confounding.** Even if X is randomized,
M is not. An unmeasured variable U that causes both M and Y (a common cause of the
mediator and outcome) creates a backdoor path M ← U → Y that biases the indirect
effect estimate. This is the sequential ignorability violation. Unlike traditional
confounding (U causes both X and Y), this bias cannot be removed by randomizing X
— the mediator itself must be as-good-as-randomized given X and baseline covariates.
In MM30's observational setting, the proliferation score is both a mediator (in
PHF19 → prolif → OS) and a proxy for numerous unmeasured tumor processes; the
mediator-outcome confounding assumption is not credible to the same degree as in an
RCT.

**Failure mode 3: Non-linear effects and non-collapsible effect measures.** For binary
outcomes with logistic regression (odds ratios), the difference method (β₁ - β₁')
does not equal the product method (α₁ × β₂), and neither equals the natural
direct/indirect effect on a meaningful causal scale. This is the non-collapsibility
problem: odds ratios do not average across strata the same way risk differences do.
MM30's Cox model uses log hazard ratios, which have the same non-collapsibility
property when the baseline hazard is heterogeneous across strata. This is a real
issue for the mediation fractions (42%, 58%, 81.2%) cited in existing MM30 results.

---

### 2. Formal Definitions: NDE and NIE (Robins-Greenland, Pearl, Imai)

The formal framework defines effects using potential outcomes. For exposure X, mediator
M, and outcome Y:

- **Y(x, m)**: the potential outcome when X is set to x and M is set to m
- **M(x)**: the potential value of M when X is set to x
- **Y(x, M(x'))**: the "nested potential outcome" — the outcome when X=x and M takes
  the value it would naturally take if X=x'

With these, the **Natural Direct Effect (NDE)** at reference level x' is:

```
NDE = E[Y(x, M(x')) - Y(x', M(x'))]
```

This is the effect of changing X from x' to x while holding the mediator at the
value it would take under X=x'. It is "natural" because M is set to its natural
counterfactual value, not a fixed constant.

The **Natural Indirect Effect (NIE)** is:

```
NIE = E[Y(x, M(x)) - Y(x, M(x'))]
```

This is the effect on Y of changing M from M(x') to M(x) while holding X fixed at x.

The total effect (TE) decomposes as:

```
TE = NDE + NIE
```

The **proportion mediated** is NIE / TE.

Crucially: NDE and NIE coincide with the BK estimates ONLY under the assumption that
there is no exposure-mediator interaction AND the linear-no-interaction model is
correctly specified. When there is an interaction, NDE and NIE depend on the reference
level x' chosen, and the proportion mediated changes accordingly.

---

### 3. The 4-Way Decomposition (VanderWeele 2014)

VanderWeele's 4-way decomposition extends NDE/NIE to the case where X and M interact.
The total effect is decomposed into:

```
TE = CDE + PIE_interaction + MIE_mediated_interaction + PIE_pure_mediation
```

where:

| Component | Notation | Meaning |
|-----------|----------|---------|
| **Controlled Direct Effect** (CDE) | CDE(m*) | Effect of X on Y with M set to reference m* — "direct" in the sense of no mediation and no interaction |
| **Reference Interaction** (PIE_int) | RI | The part of X's effect that is due to interaction with M, evaluated at M(x'=0) — "interaction but not mediation" |
| **Mediated Interaction** (MIE) | MI | The part due to both interaction AND mediation — the synergy of shifting M toward a state where X has a larger effect |
| **Pure Indirect Effect** (PIE) | PIE | The part that is purely mediated — this is what BK calls the indirect effect, and it equals NIE under no interaction |

Under no exposure-mediator interaction, RI = 0, MI = 0, and the decomposition
collapses to TE = CDE + PIE, which is the classic NDE + NIE decomposition.

**The 4-way decomposition is the right tool when:**
- The exposure-mediator interaction is plausible a priori (e.g., gain(1q) modifies
  the gain(1q) × proliferation amplification pathway)
- The CDE is the primary estimand of interest (e.g., what would happen to survival
  if we fixed proliferation at a reference value regardless of gain(1q) status?)
- The claim involves understanding whether the benefit of blocking the mediator
  depends on interaction effects

For MM30, the 4-way decomposition is most relevant to the gain(1q) → PHF19 → survival
chain, where gain(1q) status may interact with proliferation (because gain(1q) itself
accelerates proliferation), and for the cross-stratum mediation comparisons that
generated the retracted 80/20 architecture claim (t125).

---

### 4. Sequential Ignorability (Imai et al. 2010)

The key identifying assumption for ACME (Average Causal Mediation Effect) in Imai's
framework is **sequential ignorability**:

```
Assumption 1 (Treatment ignorability):
  Y(x,m) ⊥ X | C  for all x, m
  M(x) ⊥ X | C  for all x

Assumption 2 (Mediator ignorability):
  Y(x,m) ⊥ M | X=x, C  for all x, m
```

where C is the set of observed baseline covariates.

Assumption 1 says the treatment (exposure) is ignorable given C — satisfied by
randomization, and defensible observationally when C captures all confounders of the
exposure-outcome relationship.

Assumption 2 is the non-trivial one: the mediator is ignorable given observed treatment
and covariates. This fails whenever there is an unmeasured common cause of M and Y
that is not in C. In MM30's observational setting:

- For **PHF19 → prolif → survival**: the mediator (proliferation) has unmeasured
  determinants (subclonal composition, cell-cycle inhibitor loss, treatment exposure
  history) that also affect survival. Mediator ignorability is unlikely to hold exactly.
- For **gain(1q) → proliferation (as mediator)**: cytogenetic status is a founding
  event (close to randomized given the disease's clonal origin), but proliferation's
  relationship to survival is confounded by ISS stage, treatment intensity, and tumor
  microenvironment.

**Practical implication:** Sequential ignorability cannot be verified from data alone.
The proper response is sensitivity analysis (section 5).

---

### 5. Sensitivity Analysis for Mediation

When mediator ignorability (Assumption 2) is uncertain, two sensitivity analysis
approaches quantify how robust the ACME estimate is to violations.

**Imai's sensitivity parameter ρ.** Imai et al. (2010) define the sensitivity parameter
ρ as the correlation between the error terms of the mediator model and the outcome
model. Under sequential ignorability, ρ = 0. The sensitivity analysis traces how the
ACME changes as ρ varies from -1 to +1, identifying the minimum |ρ| that would drive
the ACME to zero (or change its sign). A large |ρ| is required for sign reversal means
the result is robust; a small |ρ| threshold means it is fragile.

In R, `mediation::medsens()` computes this.

**VanderWeele's bias formula.** VanderWeele (2016) derives a closed-form expression
for the bias in the indirect effect due to unmeasured mediator-outcome confounding.
If the unmeasured confounder U has effect γ₁ on M and γ₂ on Y:

```
Bias ≈ γ₁ × γ₂ × Var(U | X, C) / Var(M | X, C)
```

This allows bounding: if the analyst can specify plausible ranges for γ₁ and γ₂
from domain knowledge, the bias interval quantifies how much of the claimed
indirect effect could be confounding.

**E-values for mediation.** The CMAverse package (Shi 2021) implements E-values
adapted to the mediation context: the minimum strength of unmeasured confounding
(as a risk ratio) that would explain away the natural indirect effect. An E-value
of 2.0 means an unmeasured confounder would need to at least double the risk of
both mediator-given-exposure and outcome-given-mediator to fully explain away the
ACME. In MM30's setting (bulk RNA-seq, many unmeasured cell-state factors), E-values
near 2-3 would be considered fragile.

---

### 6. Multiple Mediators (VanderWeele & Vansteelandt 2014)

When multiple mediators are plausible (e.g., both proliferation and IFN silencing
mediate PHF19 → survival), the single-mediator NDE/NIE framework extends to joint
mediators. Key results:

1. **Joint mediation through mediator block M = {M₁, M₂}:** The NDE can be defined
   with both mediators set to their reference values simultaneously. The NIE through
   the block = TE - NDE.

2. **Sequential (path-specific) mediation:** When M₁ → M₂ (proliferation → IFN or
   IFN → proliferation), the paths X → M₁ → M₂ → Y and X → M₁ → Y and X → M₂ → Y
   cannot in general be separately identified from observational data without
   additional assumptions (no unmeasured M₁-Y confounders after M₁ is conditioned on).

3. **Independence of mediators** (no M₁ → M₂ path): If the mediators are independent
   given X and C, then the sum of individual NIEs equals the joint NIE. When
   PHF19's proliferation effect and IFN effect are treated as independent branches
   (no direct proliferation → IFN coupling), this additivity holds and the 42/58
   decomposition is well-grounded.

4. **Exposure-mediator interaction in the joint case:** The 4-way decomposition
   extends to multiple mediators, but the number of interaction terms grows
   exponentially. Practical implementations cap at two mediators.

**Key insight for MM30:** If proliferation and IFN silencing are truly independent
downstream branches of PHF19's effect (which the H1 DAG posits), the joint mediation
framework supports the 42/58 split as an additive decomposition. But if proliferation
and IFN are coupled (e.g., faster cycling → more metabolic demand → less interferon
availability), a path-specific mediation analysis is needed and identifiability
constraints kick in.

---

## Current State of Knowledge

### What is well-established

1. **Formal NDE/NIE definitions** (Robins 1992, Pearl 2001) are mathematically settled.
   The counterfactual definitions are accepted across potential outcomes and graphical
   model traditions.

2. **The product and difference methods are valid under linearity with no X-M
   interaction** (Vanderweele 2016). Under these conditions, they estimate NDE and NIE
   exactly. This is reassuring for MM30's existing results: the t165 mediation
   decomposition (42%/58%) was computed via both methods with agreement to 3 decimal
   places — this self-consistency is exactly what the theory predicts when the linearity
   conditions hold.

3. **Sequential ignorability cannot be verified from data alone** (Imai 2010). All
   observational mediation results are conditional on this assumption; sensitivity
   analysis is not optional.

4. **The 4-way decomposition subsumes all previous decompositions** (VanderWeele 2014)
   as special cases. It reduces to NDE/NIE when there is no X-M interaction; it reduces
   to the CDE when neither mediation nor interaction is assumed; and it reduces to the
   total effect when no decomposition is specified.

5. **Mediation for Cox outcomes requires special handling.** Because the Cox partial
   likelihood conditions on the risk set, the non-collapsibility of the log-hazard ratio
   means that product and difference methods give different answers for Cox models
   unless care is taken. `regmedint` (Yoshida et al. 2022) implements the correct
   closed-form expressions for Cox outcomes.

### What remains uncertain

1. **How large are the sequential ignorability violations in typical observational
   genomics data?** Imai's sensitivity parameter ρ has been studied for social science
   data but there is little calibration for bulk RNA-seq settings where unmeasured
   composition confounding is pervasive.

2. **Path-specific effects for sequential mediators** remain difficult to identify
   without additional independence assumptions or instrumental variables.

3. **Bayesian mediation decomposition** (vs frequentist) is available (posterior
   product approach, as used in MM30's t165) but the literature on inference under
   sequential ignorability violations in a Bayesian framework is sparse.

---

## Key References

[Imai2010] Kosuke Imai, Luke Keele, Dustin Tingley. "A general approach to causal
mediation analysis." *Psychological Methods* 15(4):309–334, 2010. PMID: 20954780.

[VanderWeele2016] Tyler J. VanderWeele. "Mediation analysis: A practitioner's guide."
*Annual Review of Public Health* 37:17–32, 2016. PMID: 26653405.

[VanderWeele2014_fourway] Tyler J. VanderWeele. "A unification of mediation and
interaction: a 4-way decomposition." *Epidemiology* 25(5):749–761, 2014. PMID: 25000145.

[VanderWeele2014_multiple] Tyler J. VanderWeele, Stijn Vansteelandt. "Mediation analysis
with multiple mediators." *Epidemiologic Methods* 2(1):95–115, 2014. PMID: 25580377.

[Richiardi2013] Lorenzo Richiardi, Rino Bellocco, Daniela Zugna. "Mediation analysis
in epidemiology: methods, interpretation and bias." *International Journal of
Epidemiology* 42(5):1511–1519, 2013. PMID: 24019424.

[Shi2021] Baoyi Shi et al. "CMAverse: A suite of functions for reproducible causal
mediation analyses." *Epidemiology* 32(5):e20–e22, 2021. PMID: 34028370.

[Yoshida2022] Kazuki Yoshida, Justin Mathur. "regmedint: R package for
regression-based causal mediation analysis with effect measure modification."
*arXiv* 2022.
