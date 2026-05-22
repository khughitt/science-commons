---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:vanZeventer2023
type: paper
title: Evolutionary landscape of clonal hematopoiesis in 3,359 individuals from the general population
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: vanZeventer2023
tags: []
datasets: []
ontology_terms:
- clonal fitness
- clonal hematopoiesis
- longitudinal sequencing
- population-scale evolution
- selection coefficient
- variant allele frequency
---
## Key Findings

### Cohort and prevalence
- CH prevalence 39% at baseline (1,930 clonal mutations in 1,320 individuals). Prevalence increased 3.8% over the follow-up period (p < 0.001).
- Most frequent drivers: DNMT3A (1,309 mutations) >> TET2 (687) >> ASXL1 (138) >> TP53 (90) >> JAK2 (50) >> SF3B1 (48) >> SRSF2 (36).
- Median VAF across all detected mutations 2.3% (range 1%–82%).
- Anemia associated with CH (OR 1.37, 95% CI 1.12–1.68); thrombocytosis with OR 2.41 (95% CI 1.63–3.55). No significant association for thrombocytopenia, neutropenia, erythrocytosis, or leukocytosis in general.

### Gene-specific fitness (proportional VAF growth rates per year)
Core estimates from the linear mixed model (mean ± SD):

| Gene | Growth rate (% VAF/yr) | 95% CI | q-value |
|------|------------------------|--------|---------|
| SRSF2 | 17.9% | 6.8%–30.1% | q < 0.01 |
| U2AF1 | 14.3% | −0.4%–30.2% | — |
| SF3B1 | 10.9% | 1.1%–21.7% | q < 0.1 |
| JAK2 | 9.8% | 1.2%–19.0% | — |
| TET2 | 7.1% | 4.7%–9.6% | q < 0.001 |
| EZH2 | 0.32 ± 2.19 (mean ± SD) | — | — |
| ASXL1 | 3.9% | −1.6%–9.8% | — |
| TP53 | — (no significant proportional increase) | — | p = 0.284 |
| DNMT3A | 1.9% | 0.3%–3.5% | q < 0.1 |

Overall estimated mean proportional increase across all mutations: 4.1% per year (95% CI 2.9%–5.4%; p < 0.001).

The top-ranked spliceosome genes showed the highest estimated absolute growth in any individual clone: SRSF2 mean absolute change 4.44 ± 6.42% VAF; U2AF1 6.46 ± 7.77%.

### Heterogeneous dynamics and non-genetic modulation
- For 997/1,642 (61%) mutations VAF increased; 92 (6%) were stable; 553 (34%) decreased.
- Both increasing and decreasing clones were observed for all common gene mutations, including JAK2 and spliceosome, indicating large individual-level variability in clonal behavior beyond inherent genetic fitness.
- Opposite dynamics (one clone growing, another shrinking) seen within the same individual in 150 participants, indicating concurrent intra-individual clonal competition or independent evolution.
- **Classical cancer risk factors (smoking, alcohol, BMI, age, sex) did not significantly affect clonal expansion rates** — none reached significance as interaction terms in the mixed model (Table 1). Age increased the odds of acquiring *new* mutations (OR 1.04 per year, 95% CI 1.03–1.06) but did not accelerate expansion of existing clones.

### Sequential mutation acquisition
- 488 participants acquired at least one new detectable mutation during follow-up.
- Existing TET2 clones were the strongest predisposing background for new mutation emergence: new TET2 mutations most commonly arose on a TET2 background (OR 3.05, 95% CI 2.12–4.38) or SRSF2 on TET2 (OR 3.81, 95% CI 1.31–11.13).
- DNMT3A, TP53, JAK2, and spliceosome new mutations appeared independently of pre-existing CH background.
- NRAS, RUNX1, IDH1/2, SETBP1 emerged exclusively in the background of other CH mutations — consistent with a late-event role in progression.

### Risk of myeloid malignancy
- 74/3,324 evaluable participants developed a hematological malignancy over median 7.7-year follow-up; 47 carried CH at study inclusion.
- CH at baseline: hazard ratio (HR) 2.88 for incident hematological malignancy (95% CI 1.79–4.65; p < 0.001); cumulative 5-year incidence 2.5% (95% CI 1.6%–3.3%) for CH+ vs. background.
- Gene-specific hazard ratios for myeloid malignancy:
  - JAK2: HR 74.4 (95% CI 36.0–153.7) — highest risk
  - U2AF1 spliceosome: HR 75.1 (95% CI 25.7–106.7)
  - SF3B1: HR 10.7 (95% CI 3.2–35.5)
  - SRSF2: HR 10.1 (95% CI 2.4–42.3)
  - KRAS/NRAS: HR 24.7 (95% CI 4.2–95.4)
  - TP53: HR 6.4 (95% CI 2.9–52.4)
  - DNMT3A: HR 0.8 (95% CI 0.4–1.8) — not significant (absent myeloid risk)
- Myeloid malignancy risk highest for JAK2, spliceosome, TP53; absent for DNMT3A.
- 33/35 individuals with incident myeloid malignancy had preceding cytosis or cytopenia detectable before overt disease.
- Increased clonal expansion rates preceded newly diagnosed myeloid malignancies (p = 0.010), but not lymphoid malignancies (p = 0.290).

### Neutral vs. selected dynamics — relationship to Williams/Graham 1/f test
The authors do not apply the Williams/Graham 1/f VAF distribution test explicitly. Their design (targeted panel, VAF ≥ 1% floor, per-gene rather than pan-VAF analysis) does not permit neutral-model benchmarking at the whole-spectrum level. Instead, they use the Watson/Blundell framework: directly fitting empirical per-clone VAF trajectories with a mixed-effects growth model to extract gene-specific fitness coefficients. The finding of strongly gene-specific growth rates — with DNMT3A near-zero and spliceosome genes at ~11–18% per year — is inconsistent with a uniform neutral-drift expectation across genes; it is consistent with gene-specific positive selection, though the large inter-individual variance within each gene class indicates that non-mutation factors (host physiology, HSPC niche, stochastic drift) also modulate clone size substantially. No formal neutral-model statistical test is reported.

## Limitations

- VAF ≥ 1% detection floor means small clones and early neutral dynamics below threshold are invisible; cannot apply 1/f neutral test.
- Targeted panel of 27 genes: many potential CH drivers not covered; no structural variants, CNVs, or epigenomic measurements.
- Single-clone-level VAF from bulk sequencing cannot resolve whether co-occurring mutations are in the same cell or independent clones.
- Age range ≥ 60 restricts generalizability to younger individuals and to early CH initiation dynamics.
- Lifelines cohort lacks bone marrow examination — undiagnosed myeloid disorder possible in some participants.
- Study period (median 3.6 years, max 9.4 years) may be insufficient to observe late-onset DNMT3A transformation events; long latency hypothesis remains open.
- Classical cancer risk factor analysis was underpowered for gene-specific tests — cannot rule out gene-specific modulation by, e.g., smoking on ASXL1.
- No formal test of neutral evolution (Williams/Graham 1/f); fitness estimates depend on the linear mixed-model assumption of proportional growth.
