---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Deota2025
type: paper
title: 'The Time is Now: Accounting for Time-of-day Effects to Improve Reproducibility and Translation of Metabolism Research'
version: "1.0.0"
created: "2026-05-30"
updated: "2026-05-30"
bibkey: Deota2025
tags: []
datasets: []
ontology_terms:
- chronobiology
- circadian-rhythm
- experimental-design
- metabolism
- reproducibility
- zeitgeber
---
## Key Findings

### Scale of the problem
- A survey of 1,000 research articles across multiple biomedical fields found that only **6% reported time-of-day information** about experimental procedures (ref 2: Nelson et al., BMC Biol 2022).
- ~85% of protein-coding genes have daily rhythms; 20–50% of metabolites across tissues show circadian variation; most metabolic enzymes peak at specific times of day.

### Biological factors affecting circadian rhythms in rodents
1. **Strain and genotype** — free-running period varies across inbred strains (e.g. BALB/cByJ 22.9 h, 129/J 23.93 h, C57BL/6J 23.77 h); C57BL/6J does not produce melatonin (mutations in *Aanat* and *Asmt*); disease-model genotypes (e.g. *db/db*) often carry circadian disruption as a secondary phenotype, confounding comparisons.
2. **Sex** — sex modulates SCN clock outputs; amplitude of locomotor and feeding rhythms peaks in proestrus; female C57BL/6J mice are protected from diet-induced obesity and retain feeding rhythms under short-term HFD, unlike males; female liver has more rhythmically expressed genes; the estrous cycle modulates clock outputs.
3. **Age** — daily rhythms of locomotor activity, sleep, feeding, and hormones dampen with age; aged mice have increased mortality under chronic jetlag; reduction in rhythmicity occurs for many metabolic pathways but only a modest reduction in core clock gene expression.

### Environmental factors
4. **Housing temperature** — standard housing (20–22°C) is ~30% above basal metabolic rate; recommended range 26–28°C (slightly below thermoneutrality); temperature affects feeding onset, corticosterone, cholesterol/triglycerides, and hepatic gene expression rhythms.
5. **Running wheel** — voluntary wheel running shifts clock phases in skeletal muscle and peripheral organs (not SCN); affects phases and amplitudes of glucose/lipid metabolism genes in liver; male HFD mice with wheel access partially retain feeding rhythms.
6. **Home cage environment** — group vs individual housing; social dominance alters sleep and corticosterone rhythms; environmental enrichment increases night-time activity and slow-wave sleep.
7. **Light** — ZT0 = lights-on by convention; dim light at night increases body weight and shifts food intake timing; light quality (spectrum, intensity in µW/cm²/s, not lux) matters for phase; photoperiod length modulates peripheral clocks and energy metabolism.

### Experimental factors
5. **Diet and feeding method** — 75–80% of caloric intake is nocturnal in lean mice; obesity shifts eating to daytime (30–35%); timing of caloric restriction (day vs night) determines the direction of gene-expression changes; ≥30% of hepatic rhythmic genes depend on rhythmic feeding.
6. **Gut microbiome** — diurnal composition rhythms require intact epithelial clock; collecting microbiome samples at the same ZT is critical for reproducibility; antibiotic-induced microbiome depletion (AIMD) alters GLP-1 rhythms and glucose metabolism.
7. **Treatments and interventions** — exercise, pharmacological agents, and sleep deprivation alter clock phases and amplitudes; pharmacokinetic/pharmacodynamic properties depend on circadian physiology; time of administration can shift efficacy and toxicity.

### Confounding effects of single-timepoint experiments
- **GLP-1 and OGTT example:** AUC for GLP-1 can differ **5-fold**, insulin **2-fold**, and glucose **1.8-fold** depending on ZT of the test.
- **Calorie restriction (*Fasn*, *Pck1* in liver):** at ZT4 (early light phase) CR-day mice show very low *Fasn* relative to ALF; but at ZT8 (mid light phase) CR-day mice show much higher *Fasn* than ALF or CR-night — sampling at a single ZT yields opposite conclusions.
- **HFD in ileum (*Hacd1*, *Agpat2*):** daytime sampling shows no change or upregulation; night-time sampling shows downregulation of both genes in HFD vs control.
- The paper illustrates six failure modes schematically (Fig. 4a–f): (a) random ZT inflation of variance/irreproducibility; (b) wide collection window inflates variance; (c) groups measured at different ZTs → false effect; (d) amplitude change → opposite conclusions at single ZT; (e) phase change → wrong ordering at single ZT; (f) circadian gating → stimulus detectable at ZT0 but not ZT12.

### Nocturnal/diurnal translation challenge
- Mice are nocturnal; most physiology is inverted relative to the light-dark cycle compared to diurnal humans but aligned with the rest-activity cycle. Glucose tolerance and GLP-1 secretion peak during the early active phase in both (early dark phase ZT14 in rodents; morning in humans).

### Recommendations
**Table 1 — Experimental design checklist:**

| Technical aspect | Recommended approach |
|---|---|
| Transgenic strains / disease models | Assess daily rhythms in feeding, locomotor activity, and sleep for secondary circadian effects |
| Sample collection | Perform all collections within ~2-hour window; use red/infrared light for dark-phase collections |
| Timing of sample collection | At minimum, sample at one fed/dark-phase and one fasted/light-phase timepoint |
| Overnight fasting | Restrict food access during the daytime natural fast, not overnight |
| Behavior and physiology assays | Perform in dark phase when mice are active and in fed state |

**Table 2 — Reporting checklist for rodent metabolic experiments** (three categories):
- *Biological:* strain, genotype, age, sex (pooled vs stratified)
- *Environmental:* housing type, enrichment, temperature/humidity range, light-dark cycle with ZT0 defined, light quality, wheel access, noise
- *Experimental:* diet composition and supplier, feeding method with ZT, intervention type/duration/ZT, treatment with ZT and frequency, microbiome status (SPF/germ-free/antibiotic-treated), pre-experiment fasting conditions, **time of sampling in ZT or CT**

## Limitations

- Focused exclusively on rodent in vivo metabolic research; recommendations in Tables 1–2 do not directly address human observational studies, clinical trials, or cell-culture systems (though the paper briefly notes its points apply broadly).
- The 6% reporting rate statistic (ref 2) is from a survey of 1,000 articles across fields — the breakdown by specific field (e.g. just metabolism journals) is not given in this paper.
- Narrative/expert-consensus format: no systematic meta-analytic estimate of variance inflation attributable to ZT omission; the GLP-1/OGTT magnitude figures are from specific assays, not generalizable averages.
- Sex effects on circadian rhythms are described mainly for female mice (estrous cycle, ovarian hormone protection from HFD); the review does not provide a symmetric treatment of male-specific rhythm biology or interactions between aging and sex.
- The diurnal/nocturnal translation section acknowledges that correspondence between mouse and human active-phase timing is complex; no consensus alignment table for commonly measured metabolites is provided.
- The review does not address infradian (e.g. seasonal, menstrual) rhythms — its scope is the 24-hour circadian/diurnal domain.
