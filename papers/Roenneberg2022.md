---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Roenneberg2022
type: paper
title: 'The circadian system, sleep, and the health/disease balance: a conceptual review'
version: "1.0.0"
created: "2026-05-30"
updated: "2026-05-30"
bibkey: Roenneberg2022
tags: []
datasets: []
ontology_terms:
- chronomedicine
- circadian-medicine
- circadian-rhythm
- entrainment
- health-disease-balance
- sleep
- social-jetlag
---
## Key Findings

### Framework definitions

- **Circadian health** requires (a) stable entrainment to external zeitgebers at an appropriate phase for the species' temporal niche, and (b) stable internal entrainment — appropriate phase relationships among peripheral tissue and organ clocks. Both conditions must hold; internal desynchrony (e.g., peripheral clocks drifting from the SCN pacemaker) is sufficient to compromise circadian health even if external phase is correct.
- The dominant zeitgeber is the light–dark cycle. Industrialised societies have weakened the natural light–dark cycle dramatically (humans spend most waking hours indoors under low-lux artificial light, and rarely experience full darkness except when asleep), producing the wide chronotype distribution seen today — a ~12-hour spread from "extreme larks" to "extreme owls." This variance is not adaptive; it is a pathological expansion of the natural distribution driven by weak zeitgebers and fixed social schedules.
- **Social jetlag (SJL)**, the discrepancy between biological time and social clock time, is a canonical form of sleep and circadian rhythm disruption (SCRD) and is almost always accompanied by sleep loss. SCRD is epidemiologically associated with increased prevalence of virtually all diseases reviewed.

### Conditional process model (Figure 2, Figure 3)

- Light, activity-rest, and sleep-wake can each function as exposure (E), mediator (Me), or moderator (Mo) depending on the question. The framework requires explicit role assignment before causal inference.
- The circadian system most commonly acts as **moderator (Mo)**: it does not directly cause strokes or cancers, but it changes the probability of onset (aetiology), determines the severity of tissue damage (disease), and governs the efficacy and side-effects of therapy (recovery).
- Sleep is simultaneously a *state within* the circadian process (Ferris-wheel analogy: cabins = sleep stages; wheel = circadian system) and an outcome modulated by circadian phase. Functions occurring during sleep depend on where the cabin sits in the circadian wheel — an important distinction for interpreting sleep deprivation studies.
- Specific circadian functions may be **biologically restricted** to sleep (e.g., brain metabolite clearance, synaptic maintenance); others are merely segregated to the biological night for efficiency.
- Most feedback loops are bidirectional: disease affects sleep and circadian timing (e.g., illness triggers rest behaviour, reduces outdoor light exposure); circadian timing affects disease (e.g., viral replication is rhythmic, immune defence is gated). These loops make causal inference from cross-sectional data inadequate.

### Six clinical domains

| Domain | Key circadian claim | Framework role |
|---|---|---|
| **Fertility** | Circadian clocks time GnRH, LH, FSH, and oestrogen/progesterone release across the menstrual cycle; internal entrainment within the HPG axis is required for ovulation. SCRD (shift-work, jetlag) reduces fertility, extends cycle length, and disrupts reproductive hormones. | Mo (aetiology) |
| **Cancer** | SCRD is a likely aetiological contributor; WHO classifies shift-work as probable carcinogen. Within-timezone cancer risk gradient (east vs west edge of time zone) implicates SJL rather than LAN per se. Chrono-pharmacology improves progression-free survival and reduces toxicity. | Mo (aetiology + recovery) |
| **Immune system** | Circadian rhythms gate innate and adaptive immunity: T-cell balance, cytokine profiles, and vaccine antibody response all vary by time-of-day and sleep state. Viral replication is itself rhythmic; BMAL1 restricts SARS-CoV-2 replication in lung epithelium. Vaccination and aspirin in the morning vs evening produce measurably different outcomes. | Mo and Me (all three balance components) |
| **Psychiatric disorders** | Sleep loss is a known trigger for mood episodes in bipolar disorder; late chronotype and SJL are associated with higher rates of depression and substance use disorder. Circadian variation in negative affect is documented. Insomnia treatment reduces relapse risk of major depressive disorder. | Mo (aetiology) + E/O feedback |
| **Cardiovascular disease** | Ischaemic and haemorrhagic strokes, TIAs, and myocardial infarctions all peak 06:00–12:00. Morning cardiovascular activation (platelet aggregation, cortisol, heart rate rise) is circadian-driven. Antihypertensives and aspirin show substantially better outcomes when taken at bedtime rather than in the morning. SCRD elevates CVD risk via metabolic and inflammatory pathways. | Mo (aetiology + recovery) |
| **Metabolic syndrome** | SCN lesioning abolishes daily glucose rhythm in rodents. Liver clock synchrony is required for co-ordinated glucose output; peripheral desynchrony from the SCN leads to obesity and insulin resistance in clock-mutant mice. Eating during the biological night (common in night-shift workers) blunts circadian amplitude and promotes dysmetabolism. Time-restricted feeding (TRF) improves metabolic outcomes, possibly by restoring tissue clock synchrony. Sleep restriction decreases leptin, increases ghrelin, promotes overeating. | Mo (aetiology) |

### Circadian health and general health

- In mutant animals without circadian clocks, exposures (bacteria, diet, toxins) can still cause disease, and therapies can still aid recovery. This formally separates circadian health from general health — they overlap extensively but are not identical.
- The hypothesis that "a healthy circadian system will be more effective in keeping a positive health/disease balance than a challenged circadian system" is the paper's operative claim, demonstrated by four examples (UV-skin protection, metabolic tolerance of mis-timed eating, obstructive sleep apnoea severity, chrono-pharmacology response).

### Limitations identified by the authors

- Evidence base is heavily skewed toward aetiology and disease components; recovery component (how circadian system modulates treatment response) is least studied and most actionable.
- Most reviewed relationships are still observational/correlational; the framework is designed precisely to motivate causal experiments, but those remain sparse.
- Circadian system and sleep cannot be experimentally separated in observational designs because humans overwhelmingly sleep during their biological night.
- Rodent-based models differ in sleep-phase relative to circadian phase from humans, which partly explains translational failures.

## Limitations

- Conceptual review only — no primary data, no effect sizes. All specific quantitative claims come from cited studies; this paper provides the framework and pointers, not the numbers.
- The framework is intentionally abstract and not formally validated as a predictive model; it is a taxonomy and hypothesis-generating scaffold.
- The six clinical domains were chosen to illustrate scope; they are explicitly non-exhaustive.
- Confounding between sleep loss and circadian misalignment is acknowledged but not resolved — the paper uses SCRD as an umbrella term that blurs this distinction.
- Nocturnal rodent models used in many cited mechanistic studies may not translate to diurnal humans, as the authors note explicitly.
- Authors declare competing interests (Klerman: consulting for Circadian Therapeutics and National Sleep Foundation; Foster: co-founder of Circadian Therapeutics).
