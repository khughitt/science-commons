---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Edelman2025
type: paper
title: 'Trajectories matter: Discovery and validation of ordered EHR sequences that inform clinical risk predictions'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Edelman2025
tags: []
authors:
- Edelman et al.
datasets:
- dataset:all-of-us
doi: 10.1101/2025.09.14.25335720
ontology_terms:
- clinical-risk-prediction
- disease-trajectory
- multimorbidity
- temporal-ordering
pmcid: ''
pmid: ''
venue: medRxiv (preprint)
year: 2025
---
## One-Sentence Summary

Mining temporally ordered A→B→C clinical event sequences from 432,617 All of Us EHR participants and testing them with IPTW-adjusted competing-risk survival analysis reveals 39 validated disease trajectories — spanning MI, lung cancer, dementia, leukemia, breast cancer, and colorectal cancer — where the ordering of prior events carries clinically meaningful prognostic information that bag-of-codes representations miss.

## Key Findings

1. **Ordered sequences outperform unordered representations.** At the 5-year horizon, validated A→B→C trajectories had a median risk ratio (RR) of 2.18 (IQR 1.76–2.65; maximum 5.28) versus the primary comparator (B without prior A → C), and a median absolute risk difference (ΔCIF) of 2.3 percentage-points (IQR 1.4–3.7 pp; maximum 5.9 pp). These effect sizes were consistent across four comparators — primary (B without prior A), reverse order (B→A→C), tertiary (A without subsequent B), and a calendar-time baseline — ruling out single-reference-group artifacts.

2. **Scale of discovery and confirmation.** From 633,547 persons in the OMOP source, 432,617 met eligibility (≥365 observation days). Discovery yielded 340,687 frequent A→B pairs (≥500-support threshold), which combined with 9 curated adverse outcomes to create 3,066,183 candidate A→B→C trajectories. Compute constraints limited testing to 20,565 (0.67%). After discovery FDR (BH, α=0.05), 234 unique trajectories advanced; 39 validated under global FDR control in the confirmation set across at least one time horizon.

3. **Six outcome domains covered.** Validated signals spanned: myocardial infarction (19 sequences at 5 years), lung cancer (10), dementia (7), and single validated sequences for colorectal cancer, breast cancer, and leukemia.

4. **Reverse-order check supports directionality.** The reverse comparator (B→A→C) was feasible for 89.7% of hypotheses. The median A→B→C vs B→A→C RR was 1.21 (IQR 1.02–1.41); 64% of feasible reverse-order checks showed RR > 1.1 for the forward direction, indicating that temporal ordering — not merely co-occurrence — carries incremental risk information.

5. **Validated pathways are clinically coherent.** Four illustrative trajectories with literature anchoring:
   - *COPD → peripheral nervous system disorder → lung cancer* (5-year RR 2.89; ΔCIF 1.4 pp [0.7–2.4]): consistent with COPD-associated chronic airway inflammation and paraneoplastic PNS manifestations that often antedate small-cell lung cancer diagnosis.
   - *Chronic pain → duloxetine → MI* (5-year RR ~1.6; ΔCIF ~1.8 pp): sustained sympathetic overactivation from chronic pain plus SNRI noradrenergic amplification in already-primed patients.
   - *Acquired organ absence → obstructive sleep apnea → dementia* (5-year RR 1.83; ΔCIF 1.9 pp [0.5–3.6]): bilateral oophorectomy → hormonal/weight/airway changes elevating OSA risk → intermittent hypoxia accelerating amyloid deposition.
   - *Diabetes mellitus → visual disturbance → MI* (5-year RR 3.52; ΔCIF 5.2 pp at 5 years): diabetic retinopathy as a marker of diffuse microvascular disease preceding macrovascular events.

6. **Estimated untested space.** The authors extrapolate that approximately 5,500–6,000 additional trajectories remain discoverable if compute constraints were removed — the current results represent only 0.67% of the candidate space.

## Limitations

- **Observational design:** Residual confounding and phenotype misclassification remain possible despite IPTW. Indication confounding is especially plausible for drug-involving trajectories (e.g., duloxetine → MI could partly reflect underlying pain severity selecting for sicker patients).
- **Coded events only:** Under-ascertainment of symptoms and care-seeking behavior variation can shift apparent event ordering — the coded order may not reflect the biological sequence.
- **Only 0.67% of candidate space tested:** The 39 validated trajectories are almost certainly a small fraction of the true signal; the methodology is sound but the current results are heavily truncated by compute.
- **Ordered pairs only (A→B→C):** Some pathways likely require higher-order or time-gap-sensitive patterns (A→B→C→D) to fully characterize risk propagation.
- **AoU dissemination rules:** Cell suppression (<20 cases) and rounding to nearest 5 constrain fine-grained subgroup analysis.
- **Not pre-peer-reviewed:** medRxiv preprint as of September 2025; findings should be treated as preliminary.
- **No direct mapping to MeSH / ICD crosswalk:** Integrating these OMOP-coded trajectories with the pan-disease project's MeSH-based disease network requires a crosswalk (the pan-disease project's open gap noted in h03).
