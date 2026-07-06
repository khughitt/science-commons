---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Tuffaha2025
kind: paper
title: Nonhypermutator Cancers Access Driver Mutations Through Reversals in Germline
  Mutational Bias
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Tuffaha2025
tags: []
ontology_terms:
- APOBEC
- driver availability
- driver mutations
- germline mutation
- hypermutator cancers
- hypoxia
- mutation spectrum
- mutational bias
- mutational signatures
- nonhypermutator cancers
- positive selection
dataset_usage:
- ref: dataset:pcawg
  role: analyzed
  overlap: unknown
- ref: dataset:tuffaha2025-normal-tissue
  role: analyzed
  overlap: unknown
---
## Key Findings

### Germline bias is oversampling of transitions

- Germline de novo mutations have a transition RMR of 0.853 (germline overrepresents transitions relative to the uniform expectation of 1/6 per substitution class normalized by genomic opportunity).
- Normal somatic tissue spectra are not significantly different from the germline (t-test P = 0.074 for Ti RMR).

### NHM tumors show a systematic, tissue-conserved bias reversal

- NHM tumor Ti RMR is significantly reduced relative to germline (t-test P = 9.1 × 10⁻⁹), while HM tumor Ti RMR does not differ from germline (P = 0.57).
- At the 1-mer level, NHM samples show significantly reduced RMR for both transitions and significantly elevated RMR for 2 of 4 transversion classes (Bonferroni-corrected P < 0.05/18 = 0.0028); HM samples differ from germline only for C>G transversions, which are reinforced rather than reversed.
- The 3-mer NHM spectrum is highly correlated across the 20 PCAWG tissues (mean pairwise R = 0.86 ± 0.052 SD), far more conserved than HM spectra (mean R = 0.62 ± 0.16 SD; HM vs NHM difference P = 7.8 × 10⁻⁴). The overall NHM–HM 3-mer correlation is R = 0.54 (P = 1.89 × 10⁻⁸).
- Bias reversal measure is significantly positive for NHM passenger genes at all three spectral resolution levels (Ti:Tv, 1-mer, 3-mer; P < 2.8 × 10⁻⁹); normal tissues and HM tumors show no such pattern.

### Signature decomposition identifies the reversal mechanism

- Pooled NHM spectrum: ~52% SBS5 (clock-like; modest bias reversal), ~16.8% SBS2+SBS13 (APOBEC; strongly reverses germline transition bias by enriching C>G transversions), ~14.4% SBS40; essentially all composing signatures have positive bias reversal measures except SBS1/SBS2.
- SBS13 (APOBEC deamination) and SBS40 (correlated with hypoxia via Serrano Colomé et al. 2023) are identified as the primary reversal-driving signatures.
- Hypoxia-associated SBS40 is consistent with a known hypoxic-state reduction in DNA repair efficiency (Bhandari et al. 2020; Kaplan and Glazer 2020), suggesting that NHM tumors may exploit the hypoxic microenvironment as a mechanism for spectrum alteration.

### Positive selection in NHM is anticorrelated with the germline spectrum

- In NHM, the nonsynonymous excess measure distribution for CGC genes is significantly positive (mean distribution t-test P = 2.02 × 10⁻²¹), while HM nonsynonymous excess is marginally significant (P = 0.0065) but synonymous excess is not (P = 0.44), consistent with a weaker positive-selection signal in HM due to clonal interference and high deleterious load.
- 24 specific 3-mer mutation types in NHM show significant nonsynonymous excess (z > 3.47 after Bonferroni); none do in HM (Fig. 4b,c).
- In NHM, the 24 positively selected 3-mer types are anticorrelated with germline mutation frequency (R = −0.51; Fig. 4d): mutations that selection favors are precisely the ones underrepresented in the germline — confirming that spectrum reversal is directionally aligned with driver accessibility.
- No such anticorrelation is seen in HM (R = −0.08, P = 0.43; Fig. 4e), further distinguishing the two evolutionary strategies.

### Two strategies for driver access (Fig. 5)

- **HM cancers:** increased mutation rate → more copies of all mutation types including rare drivers, at the cost of high deleterious load and clonal interference.
- **NHM cancers:** spectrum reversal → directional shift toward undersampled (including driver-class) mutations without a rate increase; positive-selection signals are stronger because deleterious load and clonal interference are lower.

## Limitations

- The bias reversal mechanism is correlational: the paper demonstrates that NHM spectra reverse the germline bias and that positively selected 3-mers are anticorrelated with germline frequency, but it cannot directly show that a specific tumor reversed its spectrum to reach a specific driver mutation (would require single-cell longitudinal data).
- The PCAWG HM classification conflates multiple hypermutation etiologies (UV, MMR deficiency, POLE proofreading) with heterogeneous spectra; tissue composition confounds are addressed only for five tissues in the restricted analysis.
- The germline de novo reference is drawn from Rodriguez-Galindo et al. 2020, which itself aggregates heterogeneous family-based cohorts across continents; germline spectrum variation by ancestry is not modeled.
- SBS40 is linked to hypoxia through correlation (Serrano Colomé et al. 2023) not mechanistic proof in this paper; the temporal sequence (hypoxia-first vs. spectrum-shift-first vs. co-occurring) is acknowledged as unresolved.
- The 3-mer bootstrap analysis is limited to 92 of 96 mutation contexts (4 types lack synonymous mutations in the dataset), and CGC gene coverage per tissue is low for some NHM tissues (<200 synonymous mutations in 10/20 tissues).
- APOBEC (SBS13) contribution to bias reversal and carcinogenesis is acknowledged to be complex — mutagenic, causing genomic instability, yet potentially acting early in tumor formation rather than throughout.
