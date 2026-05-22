---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Pellegrini2025
type: paper
title: 'From EHRs to Patient Pathways: Scalable Modeling of Longitudinal Health Trajectories with LLMs'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Pellegrini2025
tags: []
arxiv: '2506.04831'
authors:
- Pellegrini et al.
datasets:
- dataset:mimic-iv
doi: 10.48550/arXiv.2506.04831
ontology_terms:
- electronic-health-record
- longitudinal-modeling
- patient-pathway
- trajectory-prediction
venue: arXiv preprint (cs.LG)
year: 2025
---
## One-Sentence Summary

EHR2Path is a transformer-LLM framework that converts heterogeneous EHR data into structured text, then simulates complete multi-step patient clinical trajectories (vitals, labs, medications, diagnoses) while compressing full patient history via a Masked Summarization Bottleneck, outperforming task-specific baselines on both next-step prediction and longitudinal simulation in MIMIC-IV.

## Key Findings

1. **End-to-end trajectory simulation, not only outcome prediction.** EHR2Path (EHR2Path-Summ+Text, E2P-S+T) iteratively predicts every clinical event at the next time-step, feeding predictions back to simulate full future trajectories — a shift from single-outcome classifiers. The model handles 22 structured tables and 20 ICU chart event categories spanning ED, hospital, and ICU.

2. **Masked Summarization Bottleneck (MSB) enables efficient long-context modeling.** A custom attention mask forces `m` summary tokens (`<SUM>`) to compress an unbounded patient history; output tokens can attend only to summary and preceding output tokens, creating an information bottleneck. Bottleneck size = 8 tokens per category section was selected as the best performance-per-compute tradeoff (Table 5: val loss 0.21 at 8 vs 0.18 at 32–64 tokens; avg/max context 86/728 vs 344/2912 input tokens). The MSB allows the model to handle average contexts of ~9,823 tokens (up to 86,621) while consuming only 220/1,494 avg/max input tokens.

3. **Next-time-step prediction results (Table 1).** E2P-S achieves the highest macro F1 (0.54) and best numerical prediction (MAE 0.65/0.71 macro/micro) among all models. E2P-T-24h is strongest on micro F1 (0.80), reflecting its advantage on frequent events. Both summary-based variants use 8–20× fewer input tokens than text-only variants while covering 8× more context on average in MIMIC-IV.

4. **Longitudinal simulation results (Table 2).** E2P-S+T consistently ranks first or second across nine simulation tasks. E2P-S excels in dense ICU contexts (ICU Vital Sign F1 0.75, ICU Input Development F1 0.85), while E2P-T+S is strongest on ED/Hospital Discharge Diagnosis (F1 0.50) and ICU Length-of-Stay (Acc. 0.69). ETHOS achieves ICU Imminent Mortality Acc. 0.61 (vs E2P-T 0.53, E2P-S 0.50, E2P-T+S 0.57).

5. **Fine-tuning transfers to outcome prediction.** Outcome-Oriented Fine-Tuning (FT-O) achieves best performance in three of four clinical outcome tasks (Table 3): ED Admission Acc. 0.74 (vs MEME 0.67), ED Discharge Diagnosis F1 0.45 (vs REMed n/a), ICU Imminent Mortality Acc. 0.83 (vs REMed 0.78). ICU Length-of-Stay FT-O (0.76) trails FT-P (0.82).

6. **Length-of-Stay Indicator improves trajectory convergence.** Appending a noised-countdown LOS signal to each clinical unit during training (50% of the time dropped entirely, so model learns to infer it from context) boosts Hospital Discharge Diagnosis F1 from 0.32 → 0.50 and convergence from 51% → 100%, and ICU LOS Acc. from 0.65 → 0.69 with convergence from 29.6% → 68.5% (Table 4).

## Limitations

- **Single-site generalizability.** MIMIC-IV is from one US academic center (BIDMC). Treatment patterns, coding practices, and demographic distributions may not generalize; the paper acknowledges differing demographics and site-specific treatment strategies as a limitation.
- **Short-term trajectories only.** Current evaluation covers acute care stays (ED, hospital, ICU). Long-term disease trajectories spanning years — relevant to chronic disease progression and the pan-disease project's interest in cumulative disease relationships — are outside the current scope.
- **LOS indicator is a privileged input.** The model gains from a noised ground-truth countdown signal during training; at inference this must be estimated from context. The boost in convergence (29.6% → 68.5% for ICU LOS) may not fully transfer when the ground-truth signal is absent.
- **Text representation is LLM-dependent.** The approach relies on a transformer LLM's pre-trained ability to interpret clinical text strings. Performance may degrade for rare disease codes or clinical units poorly represented in pre-training data.
- **No disease taxonomy / clustering output.** EHR2Path predicts patient-level trajectories; it does not produce a disease-disease similarity matrix or clustering directly. Mapping this output to a pan-disease comparator axis would require nontrivial aggregation across patients.
