---
schema_profile: science-entity-base/1.0+topic/2.0
id: topic:target-trial-emulation-oncology
kind: topic
title: 'Target-Trial Emulation: Methodology for Causal Inference on Observational Treatment Data in Oncology'
version: "1.0.0"
created: "2026-05-18"
updated: "2026-05-18"
tags: []
datasets:
- dataset:mmrf-commpass-ia22
ontology_terms: []
related:
- decision:D2
- decision:D8
- question:treatment-response-incoherence
- task:t200
- task:t284
- topic:causal-inference
- topic:causal-inference-biology-foundations
- topic:treatment
source_refs:
- paper:Dickerman2019
- paper:Hernan2016AJE
- paper:Hernan2016JCE
- paper:HernanRobins2020
- paper:Hubbard2024
- paper:Kwee2023
- paper:TargetStatement2025
---
## Summary

Target-trial emulation is the canonical framework for turning observational longitudinal
treatment data into defensible causal claims. The core idea, developed by Hernán and Robins
[Hernan2016AJE], is to explicitly specify the randomized trial one would conduct to answer
a causal question, and then use observational data to emulate that trial as closely as
possible. The framework prevents a class of self-inflicted biases — immortal-time bias,
prevalent-user bias, depletion of susceptibles — that arise when observational analyses
deviate from basic principles of randomized-trial design [Hernan2016JCE]. In oncology, TTE
has grown rapidly; a 2023 systematic review identified 54 published cancer-treatment
applications [Kwee2023], and a 2025 consensus reporting standard (TARGET) was adopted by
JAMA [TargetStatement2025]. For MM30, TTE is operationally relevant for two queued tasks:
t200 (formal identification of the PHF19 → OS estimate on MMRF longitudinal data) and t284
(CATE feasibility assessment on the n=87 paired baseline/relapse cohort). The central
assessment of this synthesis: t200 is **technically feasible** in the MMRF IA22 cohort
if scoped narrowly to a well-defined treatment comparison, but D2's treatment-incoherence
finding imposes a hard constraint on which comparisons are emulable — specifically,
treatment-effect questions must be pre-registered against the CoMMpass structural features
(no non-responders in `fresp`, sequential visit intervals every ~3 months) rather than
borrowed from GEO datasets.

---

## Key Concepts

### 1. The Seven Target-Trial Components

Hernán and Robins specify seven protocol components that a TTE must make explicit
[Hernan2016AJE, HernanRobins2020 Ch.22]. Each component maps the target trial to the
observational data; failures in the mapping produce specific, classifiable biases.

| Component | Target-Trial Question | Observational Mapping | Key Failure Mode |
|-----------|----------------------|----------------------|-----------------|
| **Eligibility criteria** | Who would be enrolled? | Select patients at the time of eligibility | Prevalent-user bias if prior users included |
| **Treatment strategies** | What are the treatment arms? | Define initiation and continuation rules | Incommensurable arms (D2 problem) |
| **Assignment** | How is treatment assigned? | Assume conditional randomization given measured covariates | Unmeasured confounding |
| **Follow-up** | When does follow-up start and end? | Start at treatment initiation; end at event or censoring | Immortal-time bias if misaligned |
| **Outcomes** | What are the endpoints? | Use endpoint definition from the data | Misclassification, administrative censoring |
| **Causal contrast** | Which comparison is being estimated? | ITT or per-protocol estimand | Confounding-by-indication if undefined |
| **Statistical analysis** | How will the effect be estimated? | G-methods, Cox MSM, g-computation | Standard regression ignores time-varying confounding |

**MM application of the seven components for a concrete candidate comparison** (lenalidomide
maintenance vs. no maintenance after induction, MMRF IA22):

- **Eligibility:** Patients with ≥ partial response after first-line induction, measured at
  first post-induction visit. Exclude prior ASCT if ASCT is not in the emulated trial.
- **Treatment strategies:** Lenalidomide maintenance initiated within 3 months of last
  induction cycle vs. no maintenance (observation only). Must define sustained strategy
  (e.g., "maintain lenalidomide for at least 12 months unless intolerance/progression").
- **Assignment:** Conditional on baseline cytogenetic risk (gain(1q), ISS stage, age).
- **Follow-up:** Starts at post-induction eligibility visit; ends at progression, death,
  or administrative censoring at last visit.
- **Outcomes:** PFS (primary; progression or death); OS (secondary).
- **Causal contrast:** Intention-to-treat (per-protocol if adherence weights are applied).
- **Statistical analysis:** IPW marginal structural Cox model; g-computation as sensitivity.

### 2. G-Methods for Time-Varying Confounding

"G-methods" is the collective term for three estimators that handle the case where
time-varying covariates are both confounders (affect outcome) and mediators (affected by
prior treatment) [HernanRobins2020 Ch.23-24]. Standard regression fails in this setting
because adjusting for a time-varying mediator blocks the causal effect of interest.

**Why time-varying confounding is obligatory in MMRF.** In CoMMpass, clinical status is
assessed every ~3 months. A patient who starts a second treatment line at month 9 will have
interim clinical assessments that are caused by the first treatment and that predict whether
they continue on the first regimen. If those interim assessments (ISS response, M-protein
change, ECOG status) are adjusted for in a naive model, the effect of the first regimen is
partially blocked. G-methods are the correct solution.

**Three G-method families:**

**IPW / Marginal Structural Models (MSM):**
Create pseudo-populations in which the association between time-varying confounders and
treatment is eliminated. Each observation is weighted by the inverse of the probability of
receiving the observed treatment at each time point, given prior history. A standard Cox
model is then fit in the weighted pseudo-population. IPW is the most commonly implemented
option in clinical cancer research; it generalizes naturally to survival outcomes (the
marginal structural Cox model). Main limitation: extreme weights (positivity violations)
inflate variance; stabilized weights are required.

**G-computation (parametric g-formula):**
Model the joint distribution of all time-varying covariates and outcomes via sequential
regression, then use Monte Carlo simulation to marginalize over the covariate history under
each treatment strategy. Estimator is more model-dependent than IPW but handles complex
treatment strategies and can incorporate interactions. Required for strategies that IPW
cannot handle (e.g., dynamic treatment rules: "treat with lenalidomide unless creatinine
rises above X"). Computationally demanding; bootstrap confidence intervals.

**G-estimation of structural nested models:**
Estimates the direct effect of treatment at each time point while controlling for
treatment-outcome confounding by post-baseline variables. Less commonly implemented than
IPW or g-formula in clinical settings, but theoretically more efficient. Hernán and Robins
[HernanRobins2020 Ch.24] give the canonical exposition. In oncology, g-estimation is most
useful when the treatment effect is expected to vary over time (e.g., cumulative effect of
PHF19 high-expression on survival is different earlier vs. later in disease course).

**Doubly robust estimators** (AIPW, targeted maximum likelihood estimation, TMLE) combine
a propensity model and an outcome model, providing consistent estimates if either is
correctly specified. The DR framework is the causal ML framework (Feuerriegel 2024;
see topic:causal-inference-biology-foundations §4) and bridges TTE with CATE estimation.

### 3. The Cloning-Censoring-Weighting Trick for Sustained Strategies

When the causal question is about a **sustained strategy** (e.g., "maintain lenalidomide
for 12 months"), the TTE protocol creates "clones" of each eligible patient: one clone
assigned to each strategy at baseline. Clones who deviate from their assigned strategy are
censored at the time of deviation, and inverse-probability-of-censoring weights (IPCW)
adjust for the resulting selection. This two-weight design (IPTW for confounding +
IPCW for protocol deviations) is the standard approach for per-protocol TTE [HernanRobins2020
Ch.22]. For MMRF, the practical version assigns each patient at the eligibility period to
the "initiate maintenance" clone and the "defer/no maintenance" clone, then tracks
deviations from each strategy at each 3-month visit.

### 4. Canonical Biases and Their MM-Specific Forms

**Immortal-time bias** arises when follow-up begins before exposure ascertainment, creating
a period in which the patient must survive to be classified as exposed. In MM, this is
especially common in prevalent-user analyses: if a study defines "lenalidomide maintenance
users" by any use during the study period and assigns follow-up from diagnosis, all time
before maintenance initiation is immortal time for the exposed group, artifactually
inflating their apparent survival. TTE fixes this by starting follow-up at treatment
initiation (or the eligibility-period start) and applying the cloning approach.

**Prevalent-user bias (depletion of susceptibles):** Comparing current users of a treatment
to never-users is valid only for incident users at a common time origin. If treatment has
already been running for months, the current-user group has been depleted of early-relapsers
and poor responders. In MMRF, this is relevant for analyses of patients already in
maintenance when the cohort window opens: comparing maintenance continuers to discontinuers
systematically overestimates maintenance benefit. TTE requires identifying a common baseline
(e.g., the visit at which maintenance was first indicated) and using new-user / active-
comparator design principles.

**Confounding by indication:** Sicker patients receive different (or more aggressive)
treatments. In MMRF, gain(1q)+ patients are more likely to receive bortezomib-based
intensification and ASCT. Naive OS comparisons of bortezomib vs. non-bortezomib regimens
will be confounded by cytogenetic risk. IPW requires including cytogenetic status,
ISS stage, LDH, beta-2 microglobulin, and ECOG in the propensity model.

**The positivity (overlap) requirement:** Every eligible patient must have positive
probability of receiving each treatment strategy. In MMRF, this is threatened in the
post-relapse setting: patients with ultra-high-risk features (double-hit: del(17p) +
t(4;14)) may never receive certain regimens regardless of their other covariates. TTE
with positivity violations produces extreme weights and unstable estimates. Checking
the distribution of weights (mean, max, proportion > 10) is a required diagnostic.

### 5. Per-Protocol vs. Intention-to-Treat Estimands

**ITT estimand:** Effect of treatment assignment, regardless of adherence. In TTE,
corresponds to the effect of being assigned to a strategy (even if the patient later
deviates). Less sensitive to selection from deviation but doesn't answer the question
"what happens if everyone adheres?"

**Per-protocol (PP) estimand:** Effect of sustained adherence to the assigned strategy.
Requires IPCW to correct for the selection bias introduced by censoring deviators.
The PP estimand is usually more clinically actionable (what is the effect of actually
maintaining lenalidomide?), but requires the non-deviator censoring to be non-informative
given measured covariates — a stronger assumption than ITT.

For t200 specifically (PHF19 high vs. low as the "treatment"), the estimand is unusual:
PHF19 is a continuous biomarker, not a clinician-assigned treatment. TTE is still
applicable but the framing must be: "what is the effect of baseline PHF19 expression
level on OS, under the assumption that PHF19 acts as if it were randomly assigned
conditional on measured covariates?" This is essentially a propensity-weighted biomarker
analysis, not a standard treatment comparison. The key DAG condition: PHF19 expression
must be conditionally independent of unmeasured prognostic factors given the measured
adjustment set. The main threats are unmeasured gain(1q) sub-clonal architecture and
cell-state composition (see topic:causal-inference-biology-foundations §(a) and §(d)).

---

## Current State of Knowledge

### What Is Well-Established

**The TTE framework is methodologically mature.** Hernán and Robins' foundational
formalization in *Causal Inference: What If* (2020, Part III) and the 2016 AJE paper
[Hernan2016AJE] provide a settled theoretical basis. The TARGET reporting standard (2025)
[TargetStatement2025] was adopted by JAMA after consensus across 18 expert panelists,
signaling field-wide methodological agreement. The Dickerman 2019 Nature Medicine paper
[Dickerman2019] demonstrated that TTE corrects the statin-cancer discrepancy between
observational analyses and RCTs, providing a high-profile validation of the approach.

**TTE is increasingly applied in oncology.** As of 2023, 54 cancer-treatment TTE
applications had been published [Kwee2023], using registry data, electronic health records,
and longitudinal cohort studies. Overall survival is the most common primary endpoint
(63% of studies). Hematologic malignancies have seen growing TTE use (CLL: BTK-inhibitor
comparisons; DLBCL: R-CHOP sequencing; multiple myeloma: limited but growing).

**IPW with stabilized weights is the de facto oncology standard.** A marginal structural
Cox model weighted by stabilized IPTW (+ IPCW for per-protocol) is the most commonly
implemented approach because it maps directly to survival analysis infrastructure. The
g-formula is preferred when treatment strategies involve dynamic rules or complex
counterfactual interventions.

**TTE does not solve unmeasured confounding.** The TARGET statement and the NEJM
perspective [Hubbard2024] both emphasize this clearly: TTE eliminates design-related
biases (immortal-time, prevalent-user) but cannot eliminate confounding from unmeasured
variables. An observational TTE remains vulnerable to unmeasured confounders not in the
propensity model. Sensitivity analyses (E-values, Rosenbaum bounds, negative controls)
are required components of any credible TTE.

### What Remains Uncertain or Contested

**How large a cohort is needed for stable TTE estimates?** There is no settled power
formula for TTE with g-methods. Practical experience suggests:
- IPW with a binary treatment: minimum ~200-300 per arm after weighting to achieve
  stable estimates; smaller for subgroup analyses is increasingly unreliable.
- Per-protocol with IPCW: additional variance from two weight layers; effective n can be
  substantially below the observed n.
- G-computation: variance is driven by the complexity of the sequential regression models;
  n=100 is often cited as a rough minimum per arm for simple models.
  The MMRF IA22 cohort (n≈1,100 total, of which n≈600-700 have first-line data with
  adequate follow-up) is **adequate for a carefully-scoped ITT analysis** of a major
  treatment comparison (e.g., VRd-based vs. VCd-based induction). It is **marginal for
  per-protocol analyses** and **likely underpowered for subgroup TTE** (e.g., within
  gain(1q)+ or within HD+, each stratum ≈ 200-400 patients).

**Validity of TTE for biomarker exposures (the t200 question).** Standard TTE is
designed for treatment comparisons. Applying it to a continuous baseline biomarker (PHF19
expression) requires the "as-if-randomized" assumption, which is less plausible than
for clinician-assigned treatments: PHF19 level is determined by gain(1q) status, tumor
biology, and cell-state composition — none of which are randomized. The appropriate
framework for t200 is closer to a **propensity-score-weighted survival analysis** than a
full TTE. TTE's structural discipline (explicit protocol specification) still adds value
even in this setting by preventing immortal-time bias and clarifying the estimand.

**TTE vs. CATE: which framework for treatment effect heterogeneity?** TTE estimates the
marginal (population-average) treatment effect or the average treatment effect in the
"as-if-randomized" population. CATE estimation (Feuerriegel 2024; causal forests,
DR-learners) estimates individualized effects. The choice depends on the question:
- "Does lenalidomide maintenance improve OS overall?" → TTE / marginal structural model.
- "Which patients benefit most from lenalidomide maintenance?" → CATE / causal forest.
Both require the same core identification assumptions (unconfoundedness, positivity,
consistency); TTE is more principled about the design phase; CATE methods are more
flexible in the estimation phase. In practice, starting with TTE and then using a
doubly-robust estimator to explore CATE is a natural pipeline.

---

## Key References

[Hernan2016AJE] Hernán M.A., Robins J.M. "Using Big Data to Emulate a Target Trial When
a Randomized Trial Is Not Available." *American Journal of Epidemiology* 183(8):758–764,
2016. PMC4832051. The foundational paper: defines the TTE framework and the seven
protocol components.

[Hernan2016JCE] Hernán M.A., Sauer B.C., Hernández-Díaz S., Platt R., Shrier I.
"Specifying a target trial prevents immortal time bias and other self-inflicted injuries
in observational analyses." *Journal of Clinical Epidemiology* 79:70–75, 2016.
PMC5124536. The canonical bias-prevention paper.

[HernanRobins2020] Hernán M.A., Robins J.M. *Causal Inference: What If.* Chapman &
Hall/CRC, 2020 (2025 revision). Free online at https://miguelhernan.org/whatifbook.
Chapters 22–24 cover target-trial emulation and g-methods in depth.

[Dickerman2019] Dickerman B.A., García-Albéniz X., Logan R.W., Denaxas S., Hernán M.A.
"Avoidable flaws in observational analyses: an application to statins and cancer." *Nature
Medicine* 25:1601–1606, 2019. PMC7076561. High-profile demonstration that TTE corrects
statin-cancer discrepancies.

[Kwee2023] Kwee S.A. et al. "Target Trial Emulation: A Design Tool for Cancer Clinical
Trials." *JCO Clinical Cancer Informatics* 7:e2200140, 2023. PMC10166475.
Cancer-specific TTE review; 54 treatment-application studies identified.

[Hubbard2024] Hubbard R.A., Gatsonis C.A., Hogan J.W., Hunter D.J., Normand S.T.,
Troxel A.B. "Target Trial Emulation for Observational Studies — Potential and Pitfalls."
*New England Journal of Medicine* 391(21):1975–1977, 2024. PMID 39588897.
Balanced critique; emphasizes TTE does not solve unmeasured confounding.

[TargetStatement2025] Pham M.T. et al. (TARGET Guideline Group). "Transparent Reporting
of Observational Studies Emulating a Target Trial — The TARGET Statement." *JAMA*,
2025. PMID 40899949. The consensus 21-item reporting checklist; adopted by JAMA and
PLOS Medicine as reporting requirement.
