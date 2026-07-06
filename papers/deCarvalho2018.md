---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:deCarvalho2018
kind: paper
title: Discordant inheritance of chromosomal and extrachromosomal DNA elements contributes
  to dynamic disease evolution in glioblastoma
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: deCarvalho2018
tags: []
ontology_terms:
- clonal evolution
- discordant inheritance
- double minutes
- extrachromosomal DNA
- glioblastoma
- non-Mendelian segregation
- oncogene amplification
- tumor heterogeneity
---
## Key Findings

### Data-derived findings (D)

- **(D) ecDNA is prevalent and highly variable within samples.** Interphase FISH across 34 validated ecDNA amplification loci revealed a highly variable number of fluorescent signals per nucleus, ranging from 2 to 100, consistent with copy-number heterogeneity arising from random ecDNA segregation. This heterogeneity was absent for chromosomally amplified control loci.

- **(D) ecDNA and chromosomal sSNVs show discordant propagation across model systems.** 100% of homozygous deletions and sSNVs affecting GBM driver genes were faithfully propagated from tumor to neurospheres and xenografts. In contrast, ecDNA-encoded amplifications showed variable representation: e.g., MET ecDNA amplification was high-frequency in HF-3035 primary tumor (63.5%) and HF-3077 neurospheres (83%), but dramatically decreased in HF-3035 neurospheres (15.5%) and partially in some xenograft passages (HF-3077 PDX1: 64%), while *MYC* ecDNA emerged de novo at 100% in HF-3016 recurrence even though primary tumor showed only 2% frequency.

- **(D) FISH-validated ecDNA is present in 100% of neurosphere metaphase spreads for multiple oncogenes (CDK4, MET, PDGFRA, EGFR, MYC).** Metaphase FISH confirmed extrachromosomal status — amplified signals appeared as scattered double-minute-like foci rather than homogeneously staining chromosomal regions (HSRs).

- **(D) Longitudinal profiling of 66 tumors (38 patients) shows ecDNA persistence under treatment.** EGFR-harboring ecDNA was preserved in 11 of 13 patients across primary–recurrent pairs, including in patients treated with EGFR inhibitor dacomitinib. 23 of 25 preserved ecDNAs carried at least one cancer driver. MYC ecDNA emerged upon recurrence in one case (HF-3354) where it was absent in the primary. One patient (HF-2829) lost EGFR ecDNA and EGFRvIII mutation upon recurrence after standard chemoradiation.

- **(D) Clonal tracking reveals ecDNA-marked subclones evolving independently of sSNV-defined subclones.** PyClone analysis of HF-3035 and HF-3077 primary/recurrence pairs identified sSNV-based subclones (C1–C5) with stable trajectories across tumor and model systems, while MET and EGFR/CDK4 ecDNA amplification frequencies shifted substantially and non-concordantly with sSNV-cluster trajectories, including de novo expansion of MYC ecDNA independently of any detected chromosomal change.

- **(D) Shorter time to second surgery in ecDNA-positive patients.** Log-rank test showed significantly shorter time to second surgery (P = 0.018) for patients whose primary tumor carried at least one predicted ecDNA, relative to ecDNA-negative patients.

- **(D) Long-read sequencing (PacBio) confirms circular ecDNA structure.** De novo assembly of xenograft DNA identified assembled contigs with sequence fragments that could be connected in a circular configuration consistent with double-minute architecture. In HF-3035, 7 contigs aligned to MET–CAPZA2 region with complex nonlinear joining; in HF-3077, 2 contigs aligned to MET–CAPZA2 on chromosome 7. Short-read data detected 16 of 17 genomic amplifications as highly variable FISH signals (supporting ecDNA), while 26 non-amplified control regions were confirmed as such.

- **(D) MET ecDNA-positive PDXs respond to capmatinib; chromosomally amplified MET PDXs do not.** HF-3077 PDXs (MET ecDNA-positive) showed significantly improved survival with capmatinib (P = 0.013; HR 1.38 [0.61–3.74] is not significant — but survival curves separated); HF-3035 PDXs (MET ecDNA showed decreased frequency in neurospheres) did not show survival benefit. Capmatinib fully inhibited p-MET in treated HF-3035 tumors.

### Author interpretations (L)

- **(L) ecDNA elements allow rapid increase of genomic heterogeneity independently of chromosomal DNA alterations.** The authors interpret the variable, discordant copy-number patterns across cells and model systems as evidence that ecDNA "allow rapid increase of genomic heterogeneity during GBM evolution, independently of chromosomal DNA alterations" (abstract). This is a mechanistic inference; the observed heterogeneity is consistent with random segregation but the study does not directly measure segregation rates per cell division.

- **(L) ecDNA is unevenly inherited by offspring cells due to random mitotic segregation.** The authors invoke the binomial segregation model (citing Lundberg et al. 2008) to explain the wide cell-to-cell copy number variance observed by FISH. This is a theoretical attribution supported by the FISH data pattern but not directly demonstrated by live-cell tracking of individual mitoses in this study.

- **(L) ecDNA marks distinct tumor subclones with differential selection dynamics.** The disjoint propagation of chromosomal sSNVs and MET-carrying ecDNAs is interpreted as evidence for "alternative modes of tumor evolution" — i.e., ecDNA-defined subclones responding to different selective pressures than sSNV-defined ones. This is an interpretive claim; the data are consistent with but do not uniquely support this mechanistic picture.

- **(L) Oncogenic ecDNA can prevail following selective pressure imposed by anticancer therapy.** EGFR ecDNA retention in 11/13 primary–recurrent pairs, and MYC ecDNA emergence upon recurrence, are interpreted as evidence of positive selection for ecDNA-carrying cells during treatment. This is plausible but not experimentally demonstrated (no matched treated/untreated controls with serial FISH).

- **(L) ecDNA detection provides clinically relevant prognostic information.** The association of ecDNA presence in primary tumors with shorter time to second surgery (P = 0.018) is presented as suggesting clinical relevance, but the authors appropriately note this analysis was limited by cohort size and ecDNA detection sensitivity limitations.

- **(L) Targeting MET in GBM with MET ecDNA amplification has therapeutic potential.** The capmatinib experiment is interpreted as proof-of-principle that ecDNA-encoded amplifications can be therapeutically exploited, though the authors note that "further work is needed to establish the factors determining the sensitivity of MET-amplified tumors."

## Limitations

- **No direct single-cell ecDNA tracking across mitosis.** The discordant inheritance inference is based on population-level FISH signals and clonal frequency estimates, not live-cell observation of ecDNA segregation. Random-segregation mechanism is inferred, not observed.
- **AmpliconArchitect sensitivity and specificity.** The authors acknowledge incomplete overlap between copy-number-based and AmpliconArchitect ecDNA predictions; some predicted ecDNAs may be HSRs or other structures. Long-read validation was performed only for two xenografts.
- **Small longitudinal cohort for survival analysis.** The primary–recurrent longitudinal analysis covers 38 patients (66 tumors); the time-to-surgery association (P = 0.018) is based on a small sample with acknowledged detection limitations.
- **Model system selection pressure.** Neurosphere culture in EGF/bFGF medium and xenografting impose selective pressures that may not recapitulate in-patient dynamics (e.g., MET ecDNA loss in HF-3035 neurospheres). The authors discuss this as a finding, but it complicates interpretation of "natural" ecDNA evolution.
- **No functional ecDNA quantification at single-cell transcriptome level.** Expression consequences of copy-number variation are inferred from bulk RNA-seq; single-cell resolution of ecDNA-to-expression coupling is absent (addressed later by Lee2026, Wu2019).
- **IDH status confounding.** IDH-mutant tumors had fewer ecDNAs (medians 1 vs. 2 for IDH-wild-type), but the cohort was not powered to test ecDNA evolutionary dynamics separately by IDH status.
