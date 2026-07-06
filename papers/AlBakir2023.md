---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:AlBakir2023
kind: paper
title: The evolution of non-small cell lung cancer metastases in TRACERx
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: AlBakir2023
tags: []
ontology_terms:
- NSCLC
- TRACERx
- clonal dissemination
- metastatic divergence timing
- metastatic evolution
- polyclonal seeding
- selection in metastasis
dataset_usage:
- ref: dataset:tracerx
  role: analyzed
  overlap: unknown
---
## Key Findings

### Cohort and overview
- 30.2% (127/421) of TRACERx patients developed lymph node (LN) metastases at primary surgical resection (N1/N2 disease).
- 33.7% (142/421) of all patients developed recurrent disease (median time to recurrence = 353.5 days).
- Metastasis-unique driver mutations were identified in 33.3% of cases (42/126); median metastasis-unique drivers per case = 0 (IQR 0–1).
- 68.6% of driver mutations were shared between primary and paired metastases (median shared drivers = 5, IQR 3–7).

### Timing of metastatic divergence
- **74.6% (94/126) exhibited late divergence**; 25.4% (32/126) exhibited early divergence.
- Early divergence was associated with smoking status at time of primary resection (independent predictor; logistic regression, ANOVA χ², P = 0.016).
- Simulations indicate early divergence is more likely when the primary tumour diameter is less than 8 mm (the solid nodule management threshold). At tumour diameter of 2.5 × 10⁸ cells (~12–13 mm at 37% purity), 86% of simulations classified as late; at <1 mm, 78% classified as early.
- Single-region primary tumour sampling misclassified 83.3% (75/90) of late divergence cases as early — demonstrating that inadequate sampling creates false signals of early divergence.
- Clonal primary WGD preceded metastatic divergence in 64/79 (81.0%) of WGD-positive cases, confirming late molecular evolutionary timing in the majority.
- Platinum chemotherapy signature detected in recurrence/progression metastases (9/11 treated; 81.8%): in two brain metastases from patient CRUK0590, divergence from common ancestor occurred 6–8 months before recurrence — timing consistent with platinum mutagenesis before surgical resection.

### Modes of dissemination
- **Monoclonal dissemination: 68.3% (86/126)**; polyclonal: 31.7% (40/126).
- Of 40 polyclonal cases: 21 monophyletic (single branch), 16 polyphyletic (multiple branches), 3 ambiguous.
- Polyclonal dissemination was enriched at the **sample level** in primary LN/satellite lesions vs. recurrence/progression samples (Fisher's exact, P = 0.03).
- Polyclonal dissemination at the **case level** was associated with **extrathoracic recurrence** (Fisher's exact, P = 0.0056; linear modelling adjusting for metastases sampled, P = 0.006).
- Polyclonal dissemination cases had significantly more metastatic samples sequenced (median 2 vs. 1; Wilcoxon rank-sum, P = 0.00078), suggesting underestimation of polyclonal dissemination with limited sampling.
- In 11 cases: individual metastatic sites appeared monoclonal, but at the case level multiple distinct seeding clones were identified (polyclonal inference elevated by case-level analysis).
- Primary LN metastases contributed to metastatic relapse in fewer than 20% of cases — indicating LN disease is a **hallmark of metastatic potential, not a gateway** to subsequent recurrence.

### Selection in metastases
- 196 seeding clusters identified across 126 cases; 50 (25.5%) were truncal.
- **Maximum cancer cell fraction (CCF) was significantly higher in seeding vs. non-seeding subclonal clusters** (Wilcoxon rank-sum, P = 6.4 × 10⁻⁵); seeding clusters were more spatially dispersed across primary tumour regions (Wilcoxon, P = 1.6 × 10⁻⁸).
- dNdScv analysis: in both LUAD and LUSC, seeding cluster mutations showed **significant positive selection** (LUAD dN/dS = 1.97, 95% CI 1.14–3.38; LUSC dN/dS = 2.03, 95% CI 1.16–3.57).
- In LUAD, subclonal mutations in non-metastasizing primaries also showed positive selection (dN/dS = 1.97), but non-metastasizing LUSC primaries did not (dN/dS = 0.89, 95% CI 0.53–1.49) — LUSC metastatic seeding involves distinct selection.
- Gene-level: **NRAS, RBM5, and TPS3** showed significantly higher dN/dS in seeding vs. non-seeding cluster mutations after BH correction (q = 0.019, 0.019, and 5.92 × 10⁻⁶ respectively).
- TPS3 mutations almost always truncal/maintained in metastases; KRAS and KEAP1 also significantly maintained.
- Paired driver mutation analysis: TPS3 mutations in LUAD and LUSC were significantly "maintained" in metastases (multinomial test; LUAD q = 0.0009; LUSC q = 8.4 × 10⁻⁵), reflecting persistent positive selection across primary and seeding clones.
- **SCNA selection:** HIST1H3B amplification (11q13.3; also MDM2 12q15) in LUAD and CCND1/NFF2L2 in LUSC were recurrently amplified in metastases with higher G-scores vs. non-metastasizing primaries. PPP2R1A losses recurrent in both LUAD and LUSC metastases. LUAD parallel gains (CARD11, MACC1, RAC1, UNCX; 7p22.3–22.1 and 8q22.1–8q24.1) in metastasizing primaries suggest convergent selection on specific loci.

## Limitations

- Multi-region primary tumour sampling is more extensive than most studies, yet polyclonal dissemination remains likely underestimated (as the paper itself acknowledges): with limited metastatic sampling (median ~1–2 regions per metastatic site), some monoclonal dissemination calls will be false.
- Single time-point surgical resection for most primary tumours; evolutionary dynamics between resection and recurrence are inferred rather than observed.
- The study is restricted to operable early-stage NSCLC (stages I–III); findings may not generalize to advanced/metastatic-at-diagnosis NSCLC where the primary tumour has a longer evolutionary history.
- Metastasis-unique mutations were absent or unsampled in many cases (median 0 per case), limiting the ability to characterize evolution *after* seeding for most patients.
- The paper does not directly address cellular-level mechanisms of invasion (e.g., EMT, cell motility, intravasation) — the selection is identified at the subclonal level but the phenotypic mediator remains uncharacterized.
- LUSC interpretation is complicated by the non-significant positive selection in non-metastasizing LUSC subclonal clusters, which the authors attribute to neutral evolution in the remainder — but this could also reflect power limitations in smaller cohort sizes.
