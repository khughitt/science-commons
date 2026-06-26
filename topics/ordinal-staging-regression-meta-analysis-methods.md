---
schema_profile: science-entity-base/1.0+topic/2.0
id: topic:ordinal-staging-regression-meta-analysis-methods
type: topic
title: 'Statistical Modeling of Multi-Stage Disease Progression in Genomics: Ordinal Regression, Piecewise Contrasts, and Cross-Cohort Meta-Analysis'
version: "1.0.0"
created: "2026-05-18"
updated: "2026-05-18"
tags: []
datasets: []
ontology_terms: []
related:
- decision:D1
- decision:D2
- question:11-genomic-vs-clinical-staging-expression
- question:continuous-disease-model
- question:disease-stage-transition-signatures
- topic:disease-stage-progression-methods
- topic:meta-analysis
source_refs:
- Archer2015penalized
- Bergsagel2012
- Brant1990
- Macnair2022psupertime
- Peterson1990partialPO
- Whitehead2001
---
## Summary

MM30 integrates 30 transcriptomic datasets spanning the MGUS → SMM → MM → RRMM
continuum alongside ISS-I/II/III and Durie-Salmon staging schemas. This topic
synthesizes the statistical literature on how to model ordered disease stages in
high-dimensional genomic data and how to combine ordinal evidence across heterogeneous
cohorts in meta-analysis. The core architectural tension is: (a) ordinal regression as
primary (single coefficient per gene capturing monotone gradient across all stages), (b)
piecewise binary contrasts (independent logistic fits per transition, MM30's current
approach), (c) continuous latent-state models (pseudotime/trajectory), or (d) mixture /
change-point models (qualitative shifts between stages). The choice has direct
implications for interpretability, meta-analysis compatibility, and the validity of
cross-dataset aggregation given that staging schemas differ across cohorts.

---

## Key Concepts

**Proportional Odds Model (POM) / Cumulative Link Model (CLM):** The canonical ordinal
regression family (McCullagh, 1980). For an ordered outcome Y ∈ {1, 2, ..., K}, models
log[P(Y ≤ k) / P(Y > k)] = α_k − β·x. Single coefficient β for each predictor; K−1
threshold parameters (intercepts). The proportional odds assumption states β is constant
across all K−1 cut-points — that is, the predictor shifts the entire cumulative
probability curve by the same amount at every threshold. In R: `MASS::polr()`,
`ordinal::clm()`, `rms::lrm()`.

**Continuation Ratio (CR) Model:** Conditions on reaching stage k before modeling the
probability of transitioning to k+1: log[P(Y = k | Y ≥ k) / P(Y > k | Y ≥ k)] = α_k −
β·x. Mechanistically appropriate when progression through lower levels is a
*prerequisite* for higher levels (MGUS must precede SMM). Can be fit as K−1 independent
logistic regressions, making it decomposable into piecewise components while still
admitting a single shared β under the parallel-slopes constraint. R: `VGAM::vglm(...,
cratio())`, `ordinal::clm(link = "cloglog")` (approximately).

**Partial Proportional Odds (PPO) Model (Peterson & Harrell, 1990):** Relaxes the PO
assumption for a designated subset of predictors while imposing it for others. Allows
one predictor to have threshold-specific slopes while preserving parsimony. Useful when
the Brant test (Brant, 1990) flags specific variables as violating PO.

**Brant Test:** Wald-type test comparing slope coefficients estimated at each binary
dichotomization implied by the ordered model. Per-variable p-values identify which
predictors drive PO violations. Implementation: R `brant` package; `car::Anova()` on
`polr` objects with the `brant` option.

**Continuation Ratio vs. PO in Cancer Staging:** In cancer, where stage transitions are
irreversible and sequential (cannot skip from I to III without II), the CR model is the
more principled theoretical choice. PO models treat the K categories symmetrically,
which is less natural when categories represent a one-way progression funnel. However,
in practice coefficient estimates rarely differ substantially between CR and PO when the
PO assumption holds (McCullagh & Nelder, 1989). The distinction matters most when
cell counts are unequal across stages (typical in MM: many MM, few MGUS) and when
transition-specific effects are hypothesized to differ.

**psupertime (Macnair & Yau, 2022):** Supervised pseudotime via penalized ordinal
regression. Uses sequential ordinal labels (Healthy < MGUS < SMM < MM) to fit a latent
continuous progression axis across cells or bulk samples. Identifies genes that change
monotonically along the axis. Designed for both single-cell and bulk expression data.
Directly applicable to MM30's continuum datasets. PMID: 35758781.

**Individual Patient Data (IPD) Meta-Analysis:** The gold standard for combining
ordinal outcomes across studies. All raw data are pooled and a single hierarchical model
with study-level random effects estimates the shared effect. The two-stage alternative
(fit per study, then pool effect estimates) is computationally lighter and robust to
missing studies, at the cost of some efficiency (Riley et al., 2020; Whitehead et al.,
2001). For ordinal outcomes, the one-stage approach fits a mixed-effects proportional
odds model; the two-stage approach pools log-odds ratios from per-study PO models using
standard random-effects meta-analysis.

---

## Current State of Knowledge

### A. Best Practices in Cancer Transcriptomics for Staged Progression

There is no single universally endorsed method; practice varies by field. Three
approaches dominate in recent cancer transcriptomics literature:

**1. Piecewise binary contrasts** remain the most common approach in genomic
association studies, including MM (Bustoros/Shen 2021, Blood; Kurowska 2024, Blood)
and hematologic oncology broadly. The logic is pragmatic: each transition may have
biologically distinct drivers, standard DESeq2/limma infrastructure handles binary
contrasts natively, and sample sizes are usually too small at the rare-stage ends
(MGUS, n ~ 10-20 per dataset) to reliably estimate multiple thresholds jointly. The
cost is statistical: piecewise contrasts discard monotonicity information, multiply
testing burden, and produce inconsistent summaries when effects are genuinely gradient.

**2. Ordinal regression as primary** is the methodologically preferred approach when:
(a) effects are expected to be monotonic (gene expression increases or decreases
progressively across all stages); (b) sample sizes are sufficient to estimate K−1
thresholds; (c) a single interpretable summary per gene is desired for meta-analysis.
Archer et al. (2015, Cancer Informatics; PMID: 26052223) demonstrated penalized
ordinal regression (PO and CR) for cancer-stage prediction in high-dimensional genomic
settings (p >> n), using L1 GMIFS penalization. The `ordinalgmifs` R package implements
this. Critically, ordinal regression with K stages uses K−1 thresholds but still one
β per gene — the same number of primary statistics as a single binary contrast, making
it *more* efficient per parameter than K−1 piecewise tests.

**3. Continuous / pseudotime approaches** are increasingly used when the goal is to
identify progression-associated genes rather than stage-specific drivers. psupertime
(Macnair & Yau, 2022, Bioinformatics; PMID: 35758781) fits a supervised penalized
ordinal regression to assign each sample a continuous position along the progression
axis, then tests which genes change monotonically. This is directly applicable to bulk
expression data with ordinal stage labels. Its key advantage for MM30: it naturally
handles the heterogeneous stage coverage across datasets (some have only MGUS/SMM/MM,
others have all five stages) by placing samples on a common latent axis rather than
requiring all pairwise transitions to be represented.

For MM30's specific architecture — 30 datasets with heterogeneous staging, n ~ 5-40 per
stage per dataset — the following hierarchy emerges from the literature:

- **Single-cohort within-dataset analysis**: ordinal regression (PO or CR) is
  preferred over K−1 binary contrasts when ≥ 3 stages are present and monotonicity is
  plausible. For datasets with only 2 stages (e.g., MM vs RRMM), binary logistic is
  equivalent.
- **Cross-dataset meta-analysis**: ordinal regression produces one β per gene per
  dataset — directly poolable with standard SumZ or metafor random-effects frameworks
  (consistent with D1). Piecewise contrasts produce K−1 statistics per gene per dataset,
  requiring parallel meta-analyses that are harder to summarize.

### B. Proportional Odds Assumption: When It Fails and What to Do

The PO assumption — that β is constant across all cut-points — is regularly violated in
practice. Violation means that a predictor has stronger effects on some transitions than
others (e.g., a gene strongly separates MGUS from SMM but not MM from RRMM, or vice
versa). This is biologically expected in MM: the Kurowska 2024 study shows that the
MGUS→SMM transition is the primary epigenetic inflection point, while MM30 finds that
the H→MGUS transition dominates transcriptomically. A single β will be a compromise
that may dilute true transition-specific effects.

**Formal testing:** The Brant test (Brant, 1990; PMID: 2085632) is the standard check.
Applied gene-by-gene, it will identify which genes have transition-specific effects.
For a genome-wide analysis, most genes will show *some* violation at conventional α =
0.05 simply due to multiple testing, so the test should be used diagnostically (to
understand the proportion of genes violating PO) rather than prescriptively (as a
go/no-go gate for every gene).

**Remedies:**
1. **Partial PO (PPO) model (Peterson & Harrell, 1990):** Allows some predictors to have
   threshold-specific slopes. Implemented in `VGAM::vglm()` with `parallel = FALSE` for
   selected covariates. Most appropriate for a small number of key predictors.
2. **Unconstrained continuation ratio model:** Fits K−1 separate logistic regressions but
   is interpretable as transition-specific odds ratios rather than global stage
   differences. Natural decomposition: each CR term is a conditional probability of
   advancing to the next stage given you are at the current stage. This is the closest
   ordinal framework to MM30's current piecewise approach — but with a clear theoretical
   motivation.
3. **Generalized ordered logit (gologit2):** Full non-proportional model with separate
   coefficients at each cut-point. Maximum flexibility; minimal parsimony. Only warranted
   when transition-specific biology is a primary hypothesis.
4. **Hybrid: test PO first, fall back to piecewise if violation is severe.** This is the
   most practical approach for genome-wide association: use PO as primary (one β per
   gene), flag genes where Brant-test p < 0.01 as having transition-specific effects,
   and report those separately as piecewise contrasts. This matches the spirit of
   MM30's existing approach while adding an ordinal primary track.

**Key empirical observation for MM30:** MM30's own data show that H→MGUS is the dominant
transcriptomic transition (665 FDR < 0.05 genes) while MGUS→SMM is weak. This is
prima facie evidence of PO violation for a large fraction of the genome — the effect of
stage on expression is *not* monotonically distributed across all transitions. This is
not a reason to abandon ordinal regression, but it is a reason to treat the ordinal β as
a summary of *net gradient* rather than as evidence of equally-spaced effects.

### C. Multi-Cohort Meta-Analysis with Heterogeneous Staging Schemas

This is the most underserved methodological question in the literature. Key practices
from multi-cohort hematologic oncology studies:

**Schema harmonization before analysis.** The dominant approach in TCGA/ICGC multi-cohort
analyses (e.g., the GDC harmonization pipeline; Shi et al., 2016, Cell) is to map each
dataset's staging schema to a common ontology before pooling. For MM30, this means:
- Map ISS-I/II/III, Durie-Salmon I/II/III, and MGUS/SMM/MM/RRMM to a common ordered
  integer scale.
- Treat datasets with only 2 represented levels as left- or right-censored ordinal
  observations, not as excluded data.
- Document which datasets contribute to which stage comparisons.

**Consequence for D2 (treatment_response).** The same problem that invalidated
`treatment_response` for SumZ pooling (D2) applies to staging: if ISS-I/II/III in one
dataset maps to a biologically different ordinal scale than MGUS/SMM/MM/RRMM in
another, pooling their β coefficients assumes commensurability that may not exist. The
correct approach is to either (a) meta-analyze within schema class (ISS only vs.
MGUS/SMM/MM/RRMM only), (b) use random-effects meta-analysis that allows schema-level
heterogeneity to appear as τ², or (c) treat schema type as a moderator in meta-regression.

**Whitehead et al. (2001; PMID: 11468762), Statistics in Medicine.** The foundational
reference for IPD meta-analysis of ordinal outcomes. Proposes the PO model as the basis:
(i) one-stage — fit a mixed-effects PO model across all studies with study-level random
intercepts; (ii) two-stage — fit per-study log-odds ratios from PO models, pool with
random-effects metafor. The log-odds ratio from a PO model is directly poolable with
standard random-effects meta-analysis, analogous to how MM30 already pools log-HRs from
Cox models (survival-meta-analysis-methodology.md). This means that replacing binary
logistic with ordinal PO in fassoc would require *no changes* to the meta stage — the
output is still a single coefficient and SE per gene per dataset, compatible with
both SumZ (convert to Z-score) and metafor REML.

**Consistency check with D1.** Under D1, MM30 z-scores gene expression within each
dataset before association testing. Z-scored expression feeds into the ordinal link
function as a continuous predictor. The ordinal β is then a log-odds ratio per SD of
expression across stages. This is directly poolable across datasets with metafor, and
the z-scoring ensures scale-comparability of the predictor — the same argument that
justified D1 for Cox models applies here.

### D. Meta-Analysis Frameworks for Ordinal Outcomes

**Two-stage (per-study PO β, then metafor pooling).** The practical default for MM30:
- In fassoc: replace `glm(family="binomial")` with `MASS::polr()` or `ordinal::clm()` for
  datasets with ≥ 3 represented stages.
- Extract coefficient, SE (from Fisher information or bootstrap).
- Pool in meta stage with existing SumZ / REML framework.
- Interpretability: pooled β is a log-odds ratio for a 1-SD increase in expression
  predicting higher disease stage, averaged across all stage transitions.

**One-stage (pooled mixed-effects PO).** More efficient when all IPD is available (which
it is in MM30 — all 30 datasets are held locally). Adds study random effects. More
complex to implement but the theoretically optimal approach (Riley et al., 2020, SiM;
PMID: 31671215). For MM30's scale (30 studies, potentially thousands of genes), this
is computationally intensive but feasible via `ordinal::clmm()` per gene.

**Harrell's recommendation.** Frank Harrell (Regression Modeling Strategies, 2015;
Statistical Thinking blog) consistently recommends the proportional odds model over
dichotomization of ordinal outcomes, citing the efficiency argument: a K-category ordinal
analysis with n total samples has roughly the same power as a binary analysis with n·[1 −
Σp_k²] equivalent binary observations, where p_k are stage proportions. With 5 stages and
unequal sizes (common in MM continuum datasets), ordinal regression captures 30-60% more
statistical information than a single binary contrast.

### E. Continuous vs. Discontinuous Disease Transitions

**Evidence for continuity:** psupertime analyses of hematologic malignancies consistently
find that most transcriptomic changes are gradual along a continuous axis, with the
ordinal stage labels providing noisy discretizations of an underlying continuous latent
variable (Macnair & Yau, 2022). The Ledergor 2018 scRNA-seq data show intertumoral
heterogeneity within clinical stages that blurs boundaries. MM30's own finding that the
H→MGUS transition has 665 significant genes while MGUS→SMM has very few is consistent
with a continuous model where *most* transcriptomic change occurs early and then plateaus,
rather than with discrete mechanistic shifts at each clinical boundary.

**Evidence for discontinuity:** Kurowska 2024 (Blood, ASH abstract) finds a major
epigenetic inflection point specifically at the MGUS→SMM boundary (12,166 differentially
accessible chromatin regions), even though the transcriptomic signal is weak. This
dissociation between epigenomic and transcriptomic progression suggests that different
molecular layers have different "phase transition" structures. The Maura 2026 (Blood,
DOI: 10.1182/blood.2024026313) three-group model — indolent MGUS, standard-risk SMM,
high-risk SMM — is incompatible with a purely continuous model; it implies qualitative
population mixtures within clinical stages.

**Synthesis for MM30:** The evidence points to a mixture model at the *population* level:
within each clinical stage label, there is a mixture of genomically distinct subpopulations
(Maura 2026 "genomic MM" vs. "genomic MGUS"), but within any pure subpopulation, changes
are likely continuous. This has a direct implication for MM30's stage variable: the weak
MGUS→SMM signal is likely not a biological discontinuity but a *contamination* artifact
(q11: genomic vs. clinical staging). An ordinal model that includes ISS stages (I/II/III)
within MM patients will capture a more continuous signal because ISS is a severity index,
not a boundary between mechanistically distinct populations.

**Recommendation:** Use ordinal regression for *within-mechanism* axes (ISS-I/II/III,
MGUS/SMM/MM for the genomic-MM subpopulation) where monotonicity is expected, and use
piecewise contrasts for *between-mechanism* boundaries (H→MGUS as entry into malignant
transformation) where a qualitative population shift is expected.

### F. MM-Specific Landmark Papers

**Bergsagel & Kuehl (2012), JCI (PMID: 22996694).** The foundational review of MM
molecular pathogenesis. Defines the two-pathway model (hyperdiploid vs. non-hyperdiploid
IGH-translocation). Does not use ordinal regression explicitly, but motivates the
biological argument for *subtype-stratified* progression modeling: the ordinal staging
gradient looks different in HD vs. non-HD patients, which is consistent with MM30's
gain(1q) and HD stratification findings (D5).

**Walker et al. (2012), Leukemia (PMID: 22722715; EMC-92/SKY92 signature).** 92-gene
high-risk expression signature for MM. Derived from HOVON65/GMMG-HD4 (n=290, newly
diagnosed). Validated in APEX (relapsed). The derivation approach uses binary high-risk
vs. standard-risk classification — a single threshold on a continuous risk score. This
is functionally equivalent to ordinal regression with K=2, and the validation across
newly diagnosed and relapsed cohorts implicitly assumes a common ordinal structure (the
same genes that separate risk groups in NDMM continue to separate them in RRMM). This
is evidence *for* the proportional-odds assumption holding for the bulk of prognostic
genes in MM.

**Bustoros / Shen et al. (2021), Blood (PMID: 33598681).** Progression signature
(28 master regulators) derived from pairwise comparisons of primary vs. distant-site MM.
Uses binary DE, not ordinal regression. This is the canonical MM piecewise approach —
the study found biologically important genes (HMGA1, PA2G4) using piecewise contrasts.
It does NOT argue against ordinal regression; rather, it shows that piecewise contrasts
can identify mechanistically important transition-specific drivers that would be diluted
by an ordinal global summary.

**MM30 internal evidence.** The t166 Bayesian meta-analysis (4 continuum datasets) found
β = +0.524 log-odds per SD for PHF19 at the SMM→MM transition, with HDI [+0.032,
+1.097]. This was derived from binary logistic (one transition at a time). Under an
ordinal model, PHF19 would contribute a single pooled β across all transitions,
potentially diluting the SMM→MM signal with the H→MGUS transition where PHF19 is likely
not differential. This is the primary *concrete* argument for retaining the piecewise
approach for hypothesis-specific gene analyses — ordinal regression is a better exploratory
tool, but piecewise is more sensitive for testing a specific transition.

### G. Causal Inference and the Transition Framing

**When is the "transition" framing valid?** The cross-sectional transition framing (compare
MGUS samples to SMM samples) is a *cross-sectional surrogate for longitudinal change*. It
is valid as a descriptive comparison but has three important limitations:

1. **Berkson bias / prevalent-case sampling.** Patients biopsied at MGUS represent
   individuals who reached MGUS *and* were sampled at that stage. MGUS patients with
   aggressive biology may have already progressed to SMM before biopsy and therefore
   are not captured in the "MGUS" cross-section. This creates a systematic bias toward
   indolent-MGUS transcriptomes at the MGUS stage, deflating the apparent H→MGUS and
   MGUS→SMM gene expression changes. Correction requires incident-case sampling (biopsy
   at first diagnosis, not at current stage) or longitudinal data.

2. **Survivorship bias in advanced-stage cohorts.** RRMM cohorts over-represent patients
   who survived prior lines of therapy. The biology of these samples reflects both disease
   biology and selective survival under treatment. Comparing MM to RRMM transcriptomes
   without accounting for treatment history conflates true progression biology with
   treatment-selected biology — the same problem that invalidates the `treatment_response`
   SumZ category (D2). MM30's MM→RRMM contrast should be treated with this caveat, as the
   87 paired MMRF baseline/relapse samples (t055) are *less* subject to this bias than
   cross-sectional RRMM cohorts.

3. **Length-time bias.** Slower-progressing patients spend more time in each stage and
   are therefore over-represented in cross-sectional stage cohorts relative to faster-
   progressing patients. This means cross-sectional MGUS samples are enriched for stable
   MGUS, not for the pre-transition MGUS biology. For estimating progression-associated
   transcriptomes, cross-sectional designs are inherently biased toward the *stable-stage*
   phenotype.

**When the transition framing is NOT legitimate.** The "H→MGUS transition" defined by
comparing healthy plasma cell samples (from BM donors) to MGUS samples is a
*between-patient*, not a *within-patient* comparison. It is a group difference that
conflates (i) true transformation biology, (ii) patient-level confounders (age,
immune status, BM niche), and (iii) the sampling biases above. Causal inference requires
either longitudinal within-patient data (not available in MM30 except for the 87 MMRF
pairs) or a valid instrumental variable / natural experiment. The 87 paired MMRF
baseline/relapse samples are the most legitimate progression data available to MM30 but
are limited to the MM→RRMM transition.

**Practical implication.** For the H→MGUS and MGUS→SMM transitions in MM30, ordinal
regression and piecewise contrasts both face the same fundamental cross-sectional bias.
Ordinal regression is not more causal — it is simply more efficient at capturing the
average monotone gradient while sharing the same confounding structure as piecewise.
The 87 paired samples should be analyzed separately with paired (within-patient) methods
and their results treated as the more causally interpretable anchor.

### H. Treatment Response as an Ordinal Outcome

The multinomial treatment response scale (PD < SD < MR < PR < VGPR < CR < sCR) is
theoretically the ideal candidate for ordinal regression:

- The scale is ordered (deeper response = better).
- A PO model produces a single log-odds ratio for a 1-SD expression increase predicting
  deeper response — directly interpretable.
- An ordinal β is commensurable across datasets even if different datasets define
  response slightly differently (e.g., some lack sCR), because the PO model accomodates
  differing numbers of categories via differing numbers of threshold parameters while
  keeping β fixed.

**However, D2 identifies a deeper problem.** The invalidity of `treatment_response` for
SumZ pooling in MM30 is not about the ordinal vs. binary coding of response — it is
about *what is being measured*: MMRF's `fresp` encodes depth of response (in patients
who all respond), while GEO datasets encode treatment sensitivity (PR vs. PD/SD). These
are biologically different quantities. No statistical model — ordinal, binary, or
otherwise — can make these commensurable. Replacing binary logistic with ordinal
regression in fassoc for treatment response would improve within-dataset efficiency but
would NOT resolve the cross-dataset incommensurability that D2 identified.

**Correct architecture for treatment response.** The ordinal framework is appropriate for:
- Within-MMRF analysis of `fresp` (ordinal depth of response, single-dataset).
- Within-GEO analyses where responder/non-responder is the natural binary.
- Schema-matched meta-analysis: pool MMRF-type datasets (all depth-of-response) separately
  from GEO-type datasets (responder/non-responder), then report as separate meta-analyses.
Do NOT pool across these schema types even with ordinal regression.

---

## Key References

*Full entries should be added to `papers/references.bib`.*

- **Whitehead, A. et al. (2001).** "Meta-analysis of ordinal outcomes using individual
  patient data." *Statistics in Medicine* 20(15):2243-60. PMID: 11468762. Foundational
  reference for IPD meta-analysis of proportional-odds outcomes; two-stage and one-stage
  frameworks; directly applicable to MM30 meta infrastructure.

- **Archer, K.J. et al. (2015).** "Penalized Ordinal Regression Methods for Predicting
  Stage of Cancer in High-Dimensional Covariate Spaces." *Cancer Informatics* 14(S2):
  1-8. DOI: 10.4137/CIN.S17277. PMID: 26052223. L1-penalized PO and CR models for p>>n
  genomic settings; breast cancer methylation example; `ordinalgmifs` R package.

- **Macnair, W. & Yau, C. (2022).** "psupertime: supervised pseudotime analysis for
  time-series single-cell RNA-seq data." *Bioinformatics* 38(Suppl 1):i290-i298.
  DOI: 10.1093/bioinformatics/btac227. PMID: 35758781. Penalized ordinal regression for
  supervised pseudotime from labeled sequential stages; applicable to MM30 bulk + continuum
  datasets.

- **Peterson, B. & Harrell, F.E. (1990).** "Partial proportional odds models for ordinal
  response variables." *Applied Statistics* 39(2):205-217. DOI: 10.2307/2347760.
  PMID: not available (methodological paper). Foundational partial-PO reference;
  VGAM implementation.

- **Brant, R. (1990).** "Assessing proportionality in the proportional odds model for
  ordinal logistic regression." *Biometrics* 46(4):1171-1178. DOI: 10.2307/2532457.
  PMID: 2085632. Standard test for PO assumption; implemented in R `brant` package.

- **Bergsagel, P.L. & Kuehl, W.M. (2012).** "Molecular pathogenesis of multiple myeloma
  and its premalignant precursor." *JCI* 122(10):3456-63. DOI: 10.1172/JCI61188.
  PMID: 22996694. Canonical MM staging biology review; two-pathway model motivating
  subtype-stratified ordinal analysis.

- **Riley, R.D. et al. (2020).** "One-stage individual participant data meta-analysis
  models for continuous and binary outcomes: Comparison of treatment coding options and
  estimation methods." *Statistics in Medicine* 39(19):2536-2555.
  DOI: 10.1002/sim.8555. PMID: 31671215. One-stage vs. two-stage IPD meta-analysis;
  mixed-effects models; basis for clmm() one-stage ordinal implementation.

- **Bustoros, M. / Shen, Y-J. et al. (2021).** "Progression signature underlies clonal
  evolution and dissemination of multiple myeloma." *Blood* 137(17):2360-2372.
  DOI: 10.1182/blood.2020007160. PMID: 33598681. MM piecewise transition contrast using
  binary DE; demonstrates biological value of transition-specific approach even when
  ordinal is methodologically preferable.

---
