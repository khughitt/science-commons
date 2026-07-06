---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Cermakian2022
kind: paper
title: Circadian rhythms in adaptive immunity and vaccination
version: 1.0.0
created: '2026-05-30'
updated: '2026-05-30'
bibkey: Cermakian2022
tags: []
ontology_terms:
- B-lymphocyte
- T-lymphocyte
- adaptive-immunity
- chronomedicine
- circadian-clock
- dendritic-cell
- vaccination
---
## Key Findings

### Clock gene expression in adaptive immune cells

- Clock genes (Per2, Rev-erba) show rhythmic expression in mouse lymph nodes, DCs, CD4 and CD8 T cells, and human PBMCs/CD4 T cells.
- ~6% of the CD8 T cell transcriptome is rhythmically expressed (796 transcripts), including mediators of TCR signaling (ZAP-70, AKT, mTOR); TCR-inhibitory pathways are predicted to peak at night.
- Bmal1 KO abolishes these rhythms; PER2::Luc explants of lymph nodes oscillate for several days ex vivo.
- Clock gene expression is absent in regulatory T cells (Tregs) except for Rev-erba.

### Lymphocyte trafficking

- Blood lymphocyte counts show robust 24 h rhythms: peak at night/rest phase in humans, peak in the light/rest phase in nocturnal rodents.
- Mechanism involves cortisol/corticosterone rhythmically regulating IL-7R and CXCR4 expression on T cells, driving nighttime migration to secondary lymphoid organs (LNs, spleen).
- Adrenergic signaling (noradrenaline/beta2-adrenergic receptor, b2AR) drives lymphocyte homing into LNs at night onset (ZT13 in mice).
- CCR7 (on T/B cells) and its ligand CCL21 (on HEVs) peak at night onset, controlling homing; S1PR1 peaks in the morning, controlling egress.
- T cell-specific Bmal1 KO blunts the Ccr7 and S1pr1 transcript rhythms and ablates rhythmic T cell counts in LNs.
- Several studies found no LN cell-count rhythms in mice (discrepancies attributed to differences in whether constant-darkness controls and Bmal1 KO were used).

### T cell activation and antigen presentation

- In a DC-based vaccination model (DC-OVA injection into mice), 2–3× more OVA-specific CD8 T cells accumulate in the spleen after daytime immunization (mid-day) than nighttime. The rhythm is abolished in CD8 T cell-specific Bmal1 KO mice and persists under constant darkness (endogenous clock, not light-driven).
- Glucocorticoids contribute non-cell-autonomously: Lm-OVA infection leads to more OVA-specific CD8 T cells at ZT16 (early night) vs ZT4; this day-night difference is lost in mice lacking the glucocorticoid receptor in T cells.
- Dendritic cell migration from skin to lymphatic vessels is enhanced in the day (ZT7 vs ZT19), controlled by clocks in both lymphatic endothelial cells and DCs (Bmal1 KO in either cell type abolishes the variation).
- The DC clock (Bmal1) also governs infection outcome timing: Trichuris muris worm expulsion is earlier after morning infection (ZT0) and is paralleled by a Th2/IgG1 bias; the morning-evening difference is lost in DC-specific Bmal1 KO.

### Th17/Treg balance and autoimmune disease

- In the EAE mouse model of multiple sclerosis, daytime immunization (ZT8) produces higher clinical scores and more demyelination than nighttime (ZT20), paralleled by more LN Th17 cells; this is abolished by T cell-specific Bmal1 KO.
- REV-ERBa links the clock to Th17 differentiation via two competing mechanisms: (a) REV-ERBa induces NFIL3, which represses the Rorgt promoter, reducing Th17; (b) at high REV-ERBa levels, direct REV-ERBa/RORgt competition at RORE elements promotes Th17. Studies disagree on net direction, possibly due to model-specific REV-ERBa expression levels.
- Melatonin blocks Th17 and promotes Treg differentiation (relevant to humans and seasonal MS patterns, but C57BL/6 mice used in most studies have negligible melatonin).
- In collagen-induced arthritis (CIA), Treg numbers in joints are higher at ZT18 vs ZT6; glucocorticoids induce CXCR4 in Tregs, explaining the rhythmic joint distribution; Treg depletion at ZT18 activates innate monocyte/macrophage inflammation.

### B cell development and humoral response

- Bmal1 KO mice have reduced blood and spleen B cell counts; the deficit maps to the bone marrow stroma (not to the B cells themselves), since Bmal1 KO bone marrow→WT recipient reconstitutes normally.
- Intradermal immunization in the night (ZT17) elicits higher IgM and IgG1 titers than daytime (ZT5) in mice; the effect requires b2AR (adrenergic rhythm of LN lymphocyte numbers).
- Cry1/Cry2 double KO mice show an auto-immune-like phenotype (high IgG, autoantibodies), driven by B cell hyperactivation and enhanced T cell-independent antigen responses.

### Human vaccination timing (Table 1 summary)

- **Influenza** (98 participants, ~45 y): retrospective time binning; higher antibody titers 11:00–13:00 for one of three antigens only.
- **Influenza** (707 participants, ~44 y): no time-of-day effect.
- **Influenza** (276 older adults, ~71 y, randomized): morning (9:00–11:00) group had higher antibody titers at 1 month than afternoon (15:00–17:00), independent of sex.
- **Influenza** (89 older adults, ~73 y): sex × time interaction; men vaccinated in the morning showed a stronger response; no difference in women.
- **Hepatitis A** (75 young adults, ~23 y): sex × time interaction; men showed better morning response; women showed a tendency for better afternoon response.
- **Hepatitis B** (63 young adults, ~20.5 y): no time-of-day effect.
- **BCG** (18 vs 36 participants, morning [8:00–9:00] vs evening [18:00] vaccination): morning BCG vaccination led to stronger cytokine responses (IL-1b, TNFa, IL-6, IFNg) 2 weeks and 3 months later, for both Mycobacterium tuberculosis-specific and trained immunity (S. aureus) responses. Effect was cell-intrinsic (replicated in monocytes cultured ex vivo) and associated with differential chromatin accessibility (mTOR pathway enriched in morning cells).
- **Sleep deprivation:** sleeping after hepatitis A/B vaccination enhanced antibody titers and T helper cell counts vs sleep deprivation; slow-wave sleep duration correlated with T cell response. Short sleep predicted lower hepatitis B antibody titers and reduced likelihood of a protective response (Prather et al. study).
- **Shift work:** night-shift workers vaccinated for meningitis had lower antigen-specific antibody responses and lower baseline CD4 T cells and DCs than day-shift controls.

## Limitations

- Most mechanistic evidence is from inbred mouse models (C57BL/6); translation to humans is assumed but rarely tested.
- Human vaccination studies reviewed had small and mostly Caucasian samples, short time-of-day windows (morning vs. afternoon only — finer granularity missing), and inconsistent outcomes across trials.
- Studies did not control for or record menstrual cycle phase, hormonal contraceptive use, or reproductive stage in female participants — the sex × time-of-day interaction may confound infradian variation with circadian effects.
- Sleep was rarely controlled or measured in vaccination timing studies; sleep and circadian effects are conflated in most designs.
- The Th17/REV-ERBa story has contradictory results across studies (direction depends on model REV-ERBa expression level); the net physiological effect is unresolved.
- Discrepancies in lymphocyte count rhythms across mouse studies (some studies find no LN rhythms) remain unexplained; the authors attribute this partly to the use of constant-darkness conditions (which is required to demonstrate true circadian vs. masking effects) in only a subset of studies.
- Molecular mechanisms downstream of the identified clock genes are largely unknown in adaptive immune cells.
