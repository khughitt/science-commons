---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Graham2017
type: paper
title: Measuring cancer evolution from the genome
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Graham2017
tags: []
datasets: []
ontology_terms:
- 1/f VAF distribution
- Big Bang model
- chromothripsis
- clonal selection
- dN/dS
- gradualism
- intratumour heterogeneity
- neutral evolution
- punctuated evolution
- subclone reconstruction
---
## Key Findings

1. **Neutral evolution is common, not exceptional.** In the Williams et al. 2016 dataset (14 solid cancer types), ~30% of tumours showed VAF spectra consistent with neutral evolution (1/*f* distribution not rejected). Neutral drift of tumour cells is also observed in model systems (Driessens et al. 2012).

2. **Neutral evolution is the within-clone baseline.** Between selection sweeps, a clone grows neutrally. The frequent detection of neutral patterns is therefore expected and is not in tension with selection being the engine of cancer formation — selection events are episodic, not continuous.

3. **Selection signature requires a "caught in the act" window.** A selected clone is genomically detectable only while it is mid-expansion (above the detection floor of ~5% VAF but not yet fully clonal). Once it has swept to fixation, the tumour appears neutral again. Fitter clones sweep faster and thus offer shorter detection windows.

4. **The limited driver list suggests a low driver-accrual rate.** Pan-cancer cohort studies (e.g. 24 significantly mutated genes in 276 colorectal cancers) imply few potential drivers per cancer type, consistent with low rates of new driver-mutation acquisition and correspondingly frequent neutral intervals.

5. **"Mini-driver" small-effect mutations are undetectable at standard depth.** Mutations with selective advantages causing <~5% VAF changes are indistinguishable from neutral background at 100× exome coverage.

6. **Manifest ongoing selection is prognostically adverse.** Pan-cancer analysis (Andor et al. 2016; Morris et al. 2016) shows tumours with three or more large clones have worse survival; putative subclonal drivers associate with worse prognosis.

7. **Neutral tumours are not benign — they harbour a cryptic reservoir of variation.** Pre-existing, non-adaptive diversity in a neutrally evolving tumour can become adaptive when the microenvironment changes (e.g. therapy application). Neutrally evolving tumours may be especially prone to therapy resistance.

8. **Punctuated phenotype change is consistent with gradual genotype evolution.** Loss of a single gene (*APC* biallelic loss) can cause a gross normal-to-neoplastic phenotype switch despite only two mutational hits. Epistasis (requiring a full complement of interacting drivers before clonal expansion occurs) can produce apparent punctuated equilibrium even under gradual mutation accumulation.

9. **Saltatory genotype changes (hopeful monsters) are frequently observed.** Chromothripsis, chromoplexy, and whole-genome doubling confirm punctuated genotype evolution across many cancer types. Single-cell CNV data show no intermediate genomic forms between normal and grossly altered cells in breast cancer, implying saltatory origins.

10. **Predicting evolutionary trajectories requires the genotype–phenotype map.** Genetics identifies accessible phenotype space but cannot alone determine which phenotypes are selected and why; the microenvironmental context is essential.

11. **Treatment selects for rare or undetected pre-existing subclones.** Several studies (Diaz et al. 2012 EGFR blockade; Ding et al. 2012 AML relapse; Siravegna et al. 2015 liquid biopsy) document treatment-driven selection of subclones that were below detection limits pre-treatment.

## Limitations

- Review is conceptual; all quantitative claims derive from cited primary studies and are not independently validated here.
- The ~30% neutral-evolution figure (Williams et al. 2016) is based on solid tumour types only and uses moderate-depth exome sequencing; haematological malignancies and ultra-deep sequencing data are not discussed. Cross-cancer generalisation requires caution.
- The 1/*f* test assumes exponential tumour growth; it is formally inapplicable to constant-population-size dynamics (e.g. crypt niche competition) and may be confounded by sampling artefacts, tumour cellularity, and ploidy.
- dN/dS in individual tumours is acknowledged to be largely underpowered; the review does not offer a solution beyond large cohorts.
- The genotype–phenotype map is identified as the critical unknown but no framework for resolving it is offered — it is posed as a future challenge.
- Plasticity, epigenetic state changes, and non-genetic inheritance are not discussed; the review is framed entirely around somatic genetic evolution.
- The "Big Bang" model is presented as applying to colorectal cancer; whether it generalises is not evaluated.
- Treatment-driven selection is mentioned but the review does not address how to predict which subclones will be selected, or how resistance architectures differ across cancer types.
