---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Ecochard2024
type: paper
title: Evidence that the woman's ovarian cycle is driven by an internal circamonthly timing system
version: "1.0.0"
created: "2026-05-30"
updated: "2026-05-30"
bibkey: Ecochard2024
tags: []
datasets: []
ontology_terms: []
---
## Key Findings

### 1. Three actogram phenotypes

Of 425 European women with ≥18 cycles, 1,846 oscillations of ≥4 cycles were observed (mean 4.3 per woman): 890 (48%) in a stable state, 906 (49%) after a phase jump, 50 (3%) with fluctuations. 890 stable-state oscillations were found in 338 women (80% of the European cohort). Of those, 150 (17%) had amplitude ≥3 days, observed in 115 women (27%). Phase-jump sequences — stable oscillation, sudden lengthening of one cycle, return to (same or different) stable oscillation — exactly mirror circadian relative-coordination and jump phenomenology described in the circadian literature.

### 2. Significant autocorrelation of successive cycle lengths (European dataset)

ACF and PACF for cycle durations showed highly significant 2nd-order autocorrelation (ACF p < 0.0001; PACF p = 0.0032, after Bonferroni) in the European cohort. Third and fourth-order autocorrelations also significant (ACF p = 0.0004, 0.0024; PACF p < 0.0001, 0.0010). This means the duration of a cycle depends on the duration of the preceding 2–4 cycles — not just the immediately preceding one — implying a system with multi-cycle memory extending up to ~3 months.

### 3. Partial autocorrelation implicates direct, not only carry-forward, dependence

The significant PACF at ranks 2–4 indicates a **direct** relationship between a cycle and those 2–4 cycles before it (net of the intermediate cycles), consistent with the ~90-day follicular-maturation timeline and with a clock that corrects accumulated phase error over several cycles.

### 4. Weak but significant lunar-phase association

In the European cohort (26,912 cycles), the first day of menstruation occurred most frequently at the **waxing crescent** (13.1% of cycles vs. 12.5% expected by chance). Chi-square (p = 0.0214) and Rayleigh test per cycle (p = 0.0056) were statistically significant; the Rayleigh test per woman was not (p = 0.0986). In the 28–30-day subset (9,385 cycles): Rayleigh test per cycle and per woman both p < 0.0001. In the North American dataset (3,137 cycles): most frequent onset at **full moon** (not waxing crescent as in Europe); Rayleigh per cycle p = 0.0226; per woman p = 0.0927. In the 28–30-day subset: Rayleigh per cycle and per woman both p < 0.0001. The difference in preferred lunar phase between continents is unexplained (possible lifestyle or data-collection era differences).

### 5. Effect sizes are small

The lunar-phase association, while statistically significant in large samples and the 28–30-day sub-cohort, is weak in absolute terms: the excess of menses at the preferred phase is ~1.4 percentage points above the expected 12.5%. This is explicitly interpreted as an influence, not synchronization.

## Limitations

- **Observational design with natural-family-planning cohorts:** Women in these cohorts were motivated to track cycles without contraceptives for family-planning purposes; this introduces selection bias toward regularity and may not be representative of the general population. The authors acknowledge this and call for confirmation in larger, unselected populations.
- **No direct clock-mechanism evidence:** The paper cannot identify the molecular or neural substrate of the proposed clock. The analogy to circadian clocks is phenomenological, not mechanistic.
- **Continental phase discrepancy unexplained:** European women menstruate most often at the waxing crescent, North American women at the full moon. The authors speculate about lifestyle, light environment, and data-collection era differences but have no test. This limits the strength of the lunar-synchronization interpretation.
- **Lunar effect is weak and per-woman statistics often non-significant:** The Rayleigh test per woman fails in the full-cohort analysis for both datasets. The effect is driven by population-level pooling, not robust individual-level phase-locking.
- **Artificial-light confound not modeled:** The paper acknowledges light can affect the menstrual cycle (ref. 16 review, ref. 49) but does not measure or adjust for light exposure, a potentially major confounder for any lunar-light pathway.
- **Datasets differ in collection era:** European data span 1960–1997; North American data were collected 2008–2013. Era-dependent lifestyle changes (artificial light, diet, stress) may explain continental differences, but cannot be disentangled post hoc.
- **Circular statistics tested at both cycle and person level:** Discrepant p-values between the two levels indicate that the signal is partially driven by clustering of cycles within high-compliance women rather than being uniform across individuals.
