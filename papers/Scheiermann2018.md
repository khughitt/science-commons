---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Scheiermann2018
type: paper
title: Clocking in to immunity
version: "1.0.0"
created: "2026-05-30"
updated: "2026-05-30"
bibkey: Scheiermann2018
tags: []
datasets: []
ontology_terms:
- adaptive-immunity
- chrono-immunotherapy
- circadian-rhythm
- clock-genes
- innate-immunity
---
## Key Findings

### Core clockwork in innate immunity

- Multiple innate immune cell types (monocytes, macrophages, mast cells, neutrophils, NK cells, dendritic cells, ILC2s) possess intrinsic molecular clocks that temporally gate their activity — phagocytic capacity, cytokine release, histamine release, and cytotoxicity are all time-of-day dependent.
- REV-ERBα (encoded by *NR1D1*) suppresses inflammatory functions: it represses *Il6*, *Ccl2*, and *Mmp9* in macrophages. Clock disruption removes this repression, shifting macrophages towards a pro-inflammatory state.
- PER1 is required for efficient function of splenic NK cells; in *Per1*-null mice cytotoxic factor rhythmicity is lost and can be suppressed by chronic jet lag.
- TLR9 expression in macrophages, DCs, and B cells oscillates under clock control (via *Per2*); mice treated with CpG at peak TLR9 expression showed stronger adaptive immune responses weeks later.

### Circadian control of innate immune cell trafficking

- Leukocyte egress from bone marrow to blood and from blood to tissues is circadian-gated through rhythmic expression of ICAM1/CCL2 on endothelium (β-adrenergic drive) and CXCL12/CXCL2 in the periphery.
- Ly6C^hi inflammatory monocytes traffic from blood to bone marrow and back under circadian control; *Bmal1*-null mice lose diurnal variation in monocyte numbers, show increased weight gain, adiposity, insulin resistance, and higher inflammatory cytokine production.
- Neutrophil recruitment to inflamed lung is circadian-gated through rhythmic CXCL5 secretion by bronchiolar Club cells; *Bmal1* deletion in Club cells eliminates nocturnal glucocorticoid-mediated suppression, resulting in constitutively elevated CXCL5 and enhanced neutrophilia.
- Neutrophils age in circulation across the day, increasing CXCR4 expression and bone-marrow homing at rest-phase end, driving rhythmic haematopoietic progenitor mobilisation. Ablating aged neutrophils (via microbiota depletion or LPS) alleviates sickle-cell and endotoxin-induced septic shock pathology.

### Clock control of adaptive immunity

- T and B cell numbers in blood and lymph nodes oscillate strongly: lymphocyte numbers peak at active-phase onset (night in humans), driven by CCR7 and CCL21 co-oscillations that peak at night and S1P1 that mediates daytime egress.
- Lymph node dwell time is longer for cells that entered at night (β₂-adrenergic-receptor-dependent retention), amplifying adaptive immune responses initiated then.
- Vaccination timing matters: in a randomised trial of >275 elderly individuals vaccinated against influenza, morning vaccination produced higher antibody titres 1 month later than afternoon vaccination.
- Th17 cell development is circadian-gated: NFIL3 (itself clock-regulated by REV-ERBα) suppresses RORγt and Th17 differentiation at night; day-isolated T cells are more prone to Th17 commitment. Melatonin reinforces Th17 suppression via the NFIL3–RORγt pathway.
- DEC1 and DEC2 (BMAL1–CLOCK targets) are required for CD4+ T cell effector function and B-1a cell BCR repertoire respectively; B cell development per se is more dependent on the bone-marrow microenvironmental clock than the B-cell-intrinsic clock.

### Microbial regulation of circadian immunity

- Gut microbiota shows diurnal compositional oscillations; antibiotic ablation disrupts epithelial TLR1–TLR5/TLR9 rhythmicity and induces a pre-diabetic syndrome reversible by LPS administration.
- RORα/REV-ERBα anti-phasically bind TLR gene promoters in intestinal epithelial cells, driving rhythmic NF-κB activity at ZT20–ZT4 (active phase onset in mice).
- NFIL3 links IEC clock, microbiota, and host metabolism: intestinal NFIL3 regulates lipid uptake and export; IEC-specific *Nfil3*-null mice are obesity-resistant on high-fat diet.
- Rhythmic microbial metabolites act as distal epigenetic regulators in the liver, and LPS from microbiota drives the neutrophil ageing cycle.

### Therapeutic implications

- **Chronotherapy (timed delivery):** Slow-release prednisone taken at bedtime (release 4 h later) reduces morning joint stiffness duration in rheumatoid arthritis (CAPRA-1 trial, n = 288, ref 108 in paper). Timed chemotherapy increases therapeutic index in animal models.
- **Targeting the clock:** REV-ERBα agonist SR9009 is lethal to cancer cells via autophagic/lipogenic blockade; SR9009 also reduces atherosclerotic burden in mice. CRY-stabilising compound KL001 shows anti-inflammatory effects in fibroblast-like synoviocytes in vitro.
- **REV-ERBα antagonist SR82778** has detrimental effects in viral encephalitis mouse model — indicating that clock manipulation can cut both ways.
- Morning vaccination superiority vs afternoon in elderly (>65) influenza trial is the strongest human clinical example cited.
- Seasonal variation in 23% of circulating immune cell genes suggests seasonal immune programming relevant to disease exacerbation (asthma, COPD, multiple sclerosis, cardiovascular events).
- Shift work increases risk of inflammatory bowel syndrome, psoriasis, type 2 diabetes, metabolic disorders, cardiovascular and cerebrovascular disease in human epidemiological studies.

### Why immune rhythmicity evolved (authors' hypothesis)

- Time-partitioning allows metabolic flux and detrimental redox processes in immune cells to be confined to specific phases — minimising collateral immunopathology.
- A refractory phase between active immune windows may prevent runaway inflammation.
- Heightened immune sensitivity at times of likely environmental challenge (activity phase = peak pathogen exposure) is adaptive.

## Limitations

- Primarily mouse model-centric; many key findings use constitutive whole-body clock knockouts (*Bmal1*−/−, *Clock*Δ19/Δ19) or inducible Cre-lox mosaics that do not cleanly isolate cell-autonomous vs. systemic effects.
- The only substantial human clinical evidence cited is the influenza vaccination timing trial (n > 275, elderly only), the CAPRA-1 prednisone trial, and shift-work epidemiology — all of which have confounders (light, sleep, meals, activity) that the review does not fully address.
- Human lymphocyte trafficking rhythms are inverted relative to mice (peak at night in humans = rest phase), meaning mouse active-phase findings cannot be directly translated without phase-realignment — the review acknowledges this but the implications for dosing windows are underspecified.
- Microbiota–clock interaction section relies heavily on antibiotic-ablation models, which have broad effects beyond microbiome composition.
- The review does not address sex differences in immune clock outputs — a significant gap given the sex-specificity of many autoimmune conditions and the H03 relevance.
- Cell-type specificity of clock effects is sometimes unclear: myeloid-specific Bmal1 loss and T-cell-specific Bmal1 loss produce opposing EAE phenotypes (worse vs. better), but the mechanistic resolution is acknowledged as unresolved.
- Citation coverage stops at early 2018; significant literature on sex-hormone–circadian crosstalk and scRNA-seq characterisation of immune clock states has accumulated since.
