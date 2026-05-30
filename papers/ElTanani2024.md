---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:ElTanani2024
type: paper
title: 'Circadian rhythms and cancer: implications for timing in therapy'
version: "1.0.0"
created: "2026-05-30"
updated: "2026-05-30"
bibkey: ElTanani2024
tags: []
datasets: []
ontology_terms:
- cancer
- chronomedicine
- chronotherapy
- circadian-rhythm
- clock-genes
- pharmacokinetics
---
## Key Findings

### Molecular clock and tumorigenesis

- The core transcription-translation feedback loop (CLOCK:BMAL1 → PER/CRY → repression → reset, ~24 h) controls expression of clock-controlled genes governing cell proliferation, DNA repair, apoptosis, and metabolism.
- BMAL1 activates pro-cancer pathways (c-Myc, Wnt/β-catenin, Akt/mTOR) and can suppress p53. When dysregulated, these drive uncontrolled proliferation and apoptosis resistance.
- Rev-ERBα/β antagonise BMAL1 and act as tumour suppressors by suppressing the same pro-cancer pathways — creating a therapeutic target for pharmacological REV-ERB agonism.
- The Unfolded Protein Response (UPR) is circadianly gated via BMAL1; cancer cells exploit this to survive hypoxia/nutrient deprivation.
- Circadian disruption impairs DNA repair: the nucleotide excision repair pathway (including XPA) oscillates, and disruption allows mutation accumulation. DNA repair capacity peaks during the rest phase (night in humans), with trough activity during the day.

### Epidemiology of circadian disruption and cancer risk

- Night shift work is associated with higher incidence of breast, prostate, and colorectal cancers, attributed partly to melatonin suppression (loss of oncostatic melatonin secretion) and partly to shifted PER/CRY expression and impaired cell-cycle checkpoint control.
- Irregular meal timing and physical inactivity exacerbate peripheral clock desynchrony and are linked to metabolic disorders that increase cancer risk.

### Pharmacokinetics and chronotherapy

- CYP450 enzyme activity, ABC transporter expression, and drug-metabolising enzyme levels all oscillate with circadian phase, directly modulating ADME (absorption, distribution, metabolism, excretion) for chemotherapy agents.
- Dihydropyrimidine dehydrogenase (DPD), the rate-limiting enzyme for 5-fluorouracil (5-FU) catabolism, peaks during the rest phase. Administering 5-FU during the early rest phase (corresponding to ~4–8 a.m. in rodents) reduces toxicity while maintaining or enhancing antitumour activity.
- Glutathione (GSH) levels fluctuate daily: trough GSH during rest phase reduces oxidative-stress tolerance, relevant to timing oxaliplatin and cisplatin.
- Doxorubicin shows improved efficacy and reduced cardiotoxicity when administered in the morning.
- Cell-cycle-targeting drugs align to circadian cell-cycle phase: seliciclib (G1), palbociclib (G1-S transition), 5-FU (S phase), docetaxel (M phase).
- Imatinib (BCR-ABL inhibitor) efficacy varies by timing of administration in alignment with circadian expression of its target.

### Clinical evidence

- The European Cancer Chronotherapy Group's trials in metastatic colorectal cancer showed that chronomodulated infusion of oxaliplatin and 5-FU delivered during early night (when DNA repair in normal cells peaks, ~4 p.m.–8 p.m.) improved response rates and reduced gastrointestinal and haematological toxicity compared to conventional flat infusion.
- Patients with metastatic colorectal cancer receiving irinotecan chronotherapy experienced fewer severe side effects and better overall survival than those on standard chemotherapy.
- Actigraphy-guided scheduling in breast cancer chemotherapy patients: wearable data identified circadian disruption (irregular sleep-wake patterns) and allowed personalised treatment timing, reducing nausea and fatigue.

### Chronoimmunotherapy

- NK cells, T cells, and macrophages exhibit circadian variation in trafficking, activity, and cytokine production (IL-6, TNF-α).
- PD-1 (on T cells) and PD-L1 (on tumour cells) expression oscillates with circadian phase; administering ICIs (anti-PD-1, anti-PD-L1, anti-CTLA-4) when PD-1/PD-L1 interactions are minimal may enhance T cell-mediated anti-tumour responses.
- Preclinical: anti-PD-1 therapy efficacy in a melanoma mouse model was significantly enhanced when administered during the early active phase versus the rest phase (Loo et al., cited as ref 98), associated with increased T cell infiltration and cytokine production.
- Circadian regulation of Treg recruitment and immunosuppressive factor production within the TME can resist ICI therapy; timing administration to avoid peak Treg activity may be relevant.
- Ongoing clinical trial is testing circadian timing of anti-PD-1 in advanced melanoma patients.

### Lifestyle and adjuvant interventions

- Sleep hygiene (consistent schedule, reduced blue light at night) protects melatonin secretion and maintains PER/CRY expression.
- Time-restricted feeding (TRF; meals within a 10–12 h daytime window) synchronises peripheral clocks, improves glucose metabolism, reduces inflammation, and may enhance chemotherapy efficacy.
- Morning exercise advances circadian phase; timing exercise to morning/early afternoon is recommended.
- Morning bright-light therapy improves circadian alignment in cancer patients disrupted by hospital environments.
- Melatonin supplementation has oncostatic properties and may improve chemotherapy/radiotherapy tolerability by reducing side effects and synchronising rhythms.

### Future directions

- Wearable devices (Fitbit, Oura Ring, Apple Watch) combined with computational models enable real-time monitoring of individual circadian phase and prospective treatment-schedule adjustment.
- Multi-omics (transcriptomics, proteomics, metabolomics) of circadian gene expression in tumours and PBMCs are being used to identify novel biomarkers for treatment timing.
- Personalised chronotherapy protocols based on individual circadian profiles (melatonin levels, clock gene expression in PBMCs, rest-activity actigraphy) are the stated translational goal.

## Limitations

- Narrative review with no systematic search or quality assessment of included studies. Many claims rest on a single preclinical study without independent replication noted.
- Most strong chronotherapy clinical trial evidence is from colorectal cancer (European Chronotherapy Group); the review extrapolates broadly to breast, lung, and other cancers where evidence is thinner or only preclinical.
- Sex differences in circadian phase and chronotherapy response are not discussed, despite pharmacokinetic evidence that females and males differ in drug metabolism and toxicity timing.
- The review does not address tumour-cell-autonomous circadian clocks vs. host clock as separate biological actors; most cancer cells have disrupted clocks, which complicates the "align with circadian phase" argument if tumour cells have no functional clock to align to.
- Interindividual variability in circadian phase (chronotype), the dominant challenge for clinical implementation, is noted but not quantified or modelled.
- Review authors declare no funding and no competing interests, but the broad scope and narrative style reduce the evidential weight of specific claims. Several "clinical trial" examples are cited via single-reference pairs without trial registration numbers or effect-size reporting.
- The specific timing windows cited (e.g., "5-FU most effective at 4–8 a.m. in rodents") are primarily rodent data and require careful human phase-translation.
