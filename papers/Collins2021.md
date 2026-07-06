---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Collins2021
kind: paper
title: Post-transcriptional circadian regulation in macrophages organizes temporally
  distinct immunometabolic states
version: 1.0.0
created: '2026-05-30'
updated: '2026-05-30'
bibkey: Collins2021
tags: []
ontology_terms: []
---
## Key Findings

### 1. Extensive circadian regulation with low mRNA–protein overlap

- 5,790 transcripts (15.8% of the macrophage transcriptome) and 1,778 proteins (29% of detected proteome) classified as circadian by ECHO.
- Only 68% of circadian transcripts yielded any circadian protein; only 14% of circadian proteins derived from a circadian transcript — confirming post-transcriptional regulation dominates.
- Two temporal protein waves: "early wave" peaking CT3–15 (n = 807 circadian proteins) and "late wave" peaking CT15–3 (n = 947 circadian proteins).

### 2. Translation machinery and ubiquitin-mediated proteolysis drive the late wave

- Late-wave (CT15–3) circadian proteins are enriched for translation (tRNA aminoacylation, eukaryotic initiation factors, RNA Pol II transcription, processing of capped intron-containing pre-mRNA).
- tRNA-synthesizing enzymes peak at CT20; eukaryotic initiation factors average peak at CT16.
- Ubiquitin-proteasome pathway proteins (21 circadian subunits) peak at CT20, suggesting timed protein degradation underlies protein-level oscillations for transcripts that lack circadian RNA.
- E3 ubiquitin ligase CBLB oscillates antiphase to its PTK-substrate VAV2, providing a mechanistic example of degradation-driven circadian protein control.

### 3. Early-phase immunometabolic priming: oxidative phosphorylation and anti-inflammatory state

- Early-wave proteins are enriched for citric acid cycle, respiratory electron transport, metabolism of vitamins and cofactors, and receptor tyrosine kinase signaling (innate immune system and adaptive immune system pathways shared between waves).
- TCA cycle: 11 of 11 identified circadian protein subunits peak in the early phase (CT8 average); enzymes catalyzing irreversible reactions (entry of glycolysis-derived metabolites) are included, predicted to drive the forward, NADH-producing direction.
- Electron transport chain: 24 subunits across four complexes oscillate; average peak in early phase.
- Glycolysis/PPP: 14 circadian proteins; glycolytic phosphofructokinases (PFKL, PFKM, PFKP, rate-limiting enzymes) peak in the late phase; PPP proteins peak in the late wave antiphase to glycolysis proteins (consistent with Hurley et al. 2018 *Neurospora* findings).

### 4. Circadian ATP production and mitochondrial morphology are post-transcriptionally regulated

- Only 4 of the identified circadian metabolic proteins had a corresponding circadian mRNA (one in glycolysis, one in PPP, two in ETC), confirming majority post-transcriptional origin.
- Seahorse assay: basal OCR and ATP-linked OCR are significantly higher at CT4 (early phase) vs CT16 (late phase; p < 0.0001).
- Mitochondrial fission factor (MFF) protein oscillates circadianly (its mRNA does not); mitochondria are most fragmented (fissioned, ~35% fragmented) at CT0 coinciding with peak MFF; most elongated (fused, ~75% elongated) at CT6 coinciding with highest OCR/ATP production.
- Maximal and spare respiratory capacity decrease monotonically over the time course (not oscillatory), indicating the circadian clock gates basal and ATP-linked but not maximal respiration.

### 5. Circadian metabolic gating shapes phagocytic immune response

- Zymosan phagocytosis peaks at the end of the active phase (CT0), 11.4% higher than trough (CT12), fitting a circadian pattern confirmed by ECHO and JTK analysis.
- Adding oligomycin (ATP synthase inhibitor) at each circadian time point eliminated the oscillation in phagocytosis, indicating that metabolic competence is required for the timed phagocytic response.
- *Per1/Per2* double-knockout BMDMs showed no oscillation in phagocytosis, confirming clock dependence.
- NF-κB signaling proteins (12 circadian proteins) peak at CT22 in the late/active phase, providing a concurrent pro-inflammatory signaling peak that aligns with peak phagocytosis.

### 6. Macrophage post-transcriptional regulation is cell-intrinsic, not systemic

- The extensive post-transcriptional oscillations observed in vitro contradict the prevailing view that post-transcriptional circadian regulation in mammals derives primarily from systemic cues (hormones, nutrients, nerve signals).
- Results establish that the endogenous macrophage clock alone drives these oscillations independently of the systemic environment.

## Limitations

- In vitro BMDM model: macrophages are serum-shock synchronized and maintained in culture, removing in vivo tissue-context signals (cytokines, neighboring cells, nutrient flux). Whether in vivo tissue-resident macrophages show the same post-transcriptional dominance is unresolved.
- Male mice only: sex-specific effects on macrophage circadian regulation (potentially relevant to estrogen modulation of macrophage rhythms) are not addressed.
- Static proteomics cannot distinguish synthesis-rate oscillations from degradation-rate oscillations; ribosome and degradation profiling would be needed to decompose the post-transcriptional mechanisms definitively.
- Dense sampling in vitro across 48 h gives high temporal resolution, but in vivo translation of CT timing requires phase reference to light–dark cycle (done via Per2 mRNA comparison to Keller et al. 2009 ex vivo data — a single-gene approximation).
- Functional metabolic measurements (Seahorse, mitochondrial morphology, phagocytosis) are validated at only 2–3 time points per cycle; fine-grained temporal resolution of functional output is not established.
- Per1/Per2 double-knockout is a severe perturbation (arrhythmic in all tissues); milder or tissue-conditional clock disruptions may show different functional phenotypes.
