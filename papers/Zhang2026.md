---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Zhang2026
kind: paper
title: A newly developed circadian imbalance index (CII) and risk of cardiovascular-kidney-metabolic
  disease in the UK biobank
version: 1.0.0
created: '2026-05-30'
updated: '2026-05-30'
bibkey: Zhang2026
tags: []
ontology_terms: []
---
## Key Findings

**Primary association (European ancestry, N=166,194, 16,907 incident CKM cases):**

| CII | Model 2 HR (95% CI) | P-trend |
|---|---|---|
| 0–1 (ref) | 1.00 | <0.001 |
| 2 | 1.26 (1.21–1.31) | |
| 3 | 1.42 (1.36–1.49) | |
| 4 | 1.65 (1.55–1.76) | |
| 5 | 1.95 (1.70–2.23) | |

BMI adjustment (Model 4) attenuated but did not eliminate these associations: HR for CII=5 became 1.42 (1.24–1.63), consistent with partial mediation via BMI.

**Asian ancestry (N=3,481):** Significant dose-response in Models 1–3 (Model 2 HR for highest CII: 2.03, 1.07–3.86; P-trend=0.002); attenuated at Model 4 (1.82, 0.95–3.48; P-trend=0.024).

**African ancestry (N=2,583):** No statistically significant association (HR 1.43, 0.67–3.06; P-trend=0.35), likely underpowered (small N).

**Night shift work interaction (European, N=166,194):**
- Day workers, high CII (4–5): HR 1.64 (Model 3), 1.36 (Model 4)
- Shift workers, high CII: HR 2.34 (Model 3), 1.88 (Model 4)
- Night shift workers, high CII: HR 1.65 (Model 3), 1.29 (Model 4)

Specifically for the highest combined exposure (night shift + high CII), Model 2 HR = 2.22 (95% CI: 1.95–2.53).

Significant additive interaction for night shift workers with middle CII (RERI = 0.249, 95% CI: 0.079–0.419; AP = 0.148, 95% CI: 0.052–0.243) and high CII (RERI = 0.456, 95% CI: 0.138–0.775; AP = 0.205, 95% CI: 0.083–0.327). Multiplicative interaction was not statistically significant (P-interaction=0.238).

**Extended night shift metrics (N=47,843 European subset):** Additive interactions were particularly pronounced among those who had worked night shifts for ≥20 years or at high intensity (≥8 nights/month).

**Component-level analyses:** Each individual CII component was independently associated with elevated CKM risk; the CII was also significantly associated with the risk of each individual CKM component disease (T2D, CVD, CKD) separately.

**Sex:** Association appeared stronger among European women than men, but interaction by sex was not statistically significant (P-interaction=0.666).

## Limitations

1. **Self-reported exposures:** All CII components except vitamin D are self-reported, introducing misclassification that is likely non-differential with respect to CKM outcome — biasing estimates toward the null. True CII–CKM associations may be stronger than observed.
2. **Single time-point baseline:** CII components measured only at enrollment; trajectory changes over 13.5 years of follow-up cannot be captured.
3. **Caffeinated coffee measurement scope:** Daily timing of coffee consumption not available; tea consumption not included; the absence-or-excess categorization may inadequately capture habitual caffeine's circadian effects.
4. **CII incomplete coverage:** Light exposure and meal timing — both directly relevant to circadian entrainment — are not included in the CII, partly because they were unavailable in UK Biobank at baseline. The authors note chronotype partially proxies for these.
5. **Ancestry imbalance:** 87% European ancestry; African ancestry group (N=2,583) was underpowered (HR 1.43, 95% CI: 0.67–3.06). Findings generalize most strongly to European-ancestry populations. Asian findings require replication in independent Asian cohorts.
6. **Healthy worker / volunteer bias:** Participants were employed at baseline and are a healthier, higher-SES subset than the general population; UK Biobank is known to under-represent lower-SES, older, and sicker individuals.
7. **Unmeasured confounding:** Residual confounding from occupation type, dietary patterns, and psychosocial stressors cannot be excluded despite the extensive covariate adjustment.
8. **Mediation vs. confounding of BMI:** BMI was treated as a potential mediator (modeled separately in Model 4) but could also be a confounder. The partial attenuation in Model 4 is interpretable either way.
9. **Index weighting:** Equal weighting of the five components was chosen for interpretability and generalizability; weighted versions (coefficients from CKM-outcome regression) gave similar results in sensitivity analyses, but optimal weighting for other outcomes is untested.
10. **Multiplicative vs. additive interaction:** Only additive (public health relevant) interaction was significant; multiplicative was not (P=0.238). The authors frame additive interaction as the more policy-relevant scale, which is appropriate, but the biological synergy question remains open.
