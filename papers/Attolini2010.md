---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Attolini2010
kind: paper
title: A mathematical framework to determine the temporal sequence of somatic genetic
  events in cancer
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Attolini2010
tags: []
ontology_terms:
- Moran process
- RESIC
- cancer evolutionary trajectory
- cross-sectional genomics
- driver mutation sequence
- fixation probability
- mutation order inference
- population genetics model
dataset_usage:
- ref: dataset:attolini2010-cohorts
  role: analyzed
  overlap: unknown
- ref: dataset:cosmic
  role: analyzed
  overlap: unknown
- ref: dataset:tcga
  role: analyzed
  overlap: unknown
---
## Key Findings

### Colorectal cancer (validation)

- APC biallelic inactivation precedes any KRAS alteration (APC^{−/−} first: ~77.8% of flux for first-allele ordering).
- APC biallelic inactivation precedes TP53 biallelic inactivation (APC^{−/−} first: ~61.5%).
- At least one KRAS allele mutates before TP53 inactivation (KRAS^{+/−} first: ~57.6%; KRAS^{−/−} before TP53^{−/−}: ~69.6%).
- Combined: APC → KRAS → TP53, reproducing the classical Fearon–Vogelstein multistep model (ref. 10).

### Primary GBM (TP53 vs. NF1)

- TP53 mutation precedes NF1 loss in ~62.3% of all 91 samples and ~62.5% of 72 treatment-naive samples.
- Consistent with mouse-model experimental data (ref. 14: TP53 must be inactivated before or simultaneously with NF1 for high-grade glioma formation).
- Suggests TP53 inactivation is an early event in TP53-mutant primary GBM, not just secondary GBM.

### Secondary AML (JAK2 vs. TET2)

- JAK2 mutations precede TET2 mutations (~60.4% of flux for JAK2 first).
- Contradicts some earlier small-cohort reports suggesting TET2 precedes JAK2; consistent with concurrent longitudinal analysis of matched MPN/AML pairs from 14 patients (TET2 mutations present in AML but not preceding MPN sample in 5/14 concomitant JAK2/TET2 patients).

### Primary GBM large-scale (EGFR / PTEN / p16)

- With copy number data only (n = 552): no clear order between EGFR low-level amplification and PTEN homozygous loss (near-equal frequencies for the two dominant initiating paths).
- With combined copy number + sequence data: EGFR biallelic alterations likely precede PTEN loss.
- Three-way EGFR/PTEN/p16 network (n = 570): p16 deletion and EGFR low-level amplification are the most common initiating events (~35–39% each); high-level EGFR amplification is the most frequent final event (~56.4%).
- Interpretation: glial progenitor cells may tolerate full EGFR activation only after p16 or PTEN inactivation, consistent with mouse data showing EGFR overexpression alone is insufficient for GBM (refs. 27–28).

### Robustness

Results are robust to: sampling stochasticity, population size (tested over several orders of magnitude), mutation rate, influx rate, and subsampling. ~100 samples estimated as sufficient for networks of several loci.

## Limitations

- **Cross-sectional only:** RESIC infers order from population frequencies, not individual trajectories. It cannot validate that any single tumor followed the inferred sequence.
- **Pairwise/small-network scope:** Because RESIC requires significantly co-occurring mutations as input, it can only order events that co-occur frequently enough. Rare drivers or mutually exclusive subtypes require separate analyses. Even the n = 594 TCGA GBM set yielded only a handful of significantly correlated locus pairs (Fig. 4D).
- **No subclonal resolution:** RESIC does not model intra-tumor heterogeneity or subclonal dynamics. It treats each patient's tumor as a single genotypic state (the dominant clone). Subclonal mutations in minor clones are invisible to the framework.
- **Steady-state assumption:** The patient-population model assumes a steady-state distribution of disease states (constant influx/outflux). This may not hold for rare cancers, rapidly changing incidence rates, or datasets biased toward late-stage samples.
- **Uniform diagnosis likelihood:** Assumes all genotypic states are equally likely to be diagnosed. Aggressive genotypes that progress rapidly to death before diagnosis, or indolent genotypes that are never diagnosed, would bias the observed frequency distribution.
- **No microenvironment or immune modeling:** Tumor–microenvironment and immune interactions are excluded; they are acknowledged as modulations of effective fitness and mutation rates but not incorporated.
- **Fitness parameter identifiability:** The optimization fits fitness values r_i from genotype frequencies; with many states and limited samples, parameter identifiability may be low. The paper tests robustness to structural parameters (N, u, influx) but does not discuss identifiability of the fitness landscape itself in detail.
- **Requires pre-specified gene sets:** RESIC does not discover which genes are relevant — it orders a user-specified set. Discovery of the set requires GISTIC or equivalent; the temporal ordering is downstream.
