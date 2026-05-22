---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Islam2024b
type: paper
title: Temporal recording of mammalian development and precancer
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Islam2024b
tags: []
datasets:
- dataset:gse235119
- dataset:htan-vanderbilt-colon
- dataset:tennessee-colorectal-polyp-study
ontology_terms:
- CRISPR molecular clock
- adenoma
- clonal analysis
- colorectal precancer
- lineage tracing
- polyclonal initiation
- serrated polyp
- single-cell multiomics
---
## Key Findings

**Polyclonal initiation in human precancers (15–30%):**
- ~20% of polyps in the Tennessee Colorectal Polyp Study showed ≥3 unique APC mutations → ≥3 founder clones.
- WES of VUMC polyps: ~15% showed potential polyclonal initiation.
- scRNA-seq VAF analysis: ~29% of polyps classified as polyclonally initiated.
- XCI mosaicism in female polyps corroborated polyclonal assignments.
- The true frequency is likely an underestimate due to sequencing depth limitations and the possibility of monoclonal conversion erasing early polyclonal history.

**Clonal selection signature distinguishes polyp subsets:**
- ~60% of all polyps overall showed signatures of clonal selection.
- Monoclonally assigned polyps had higher clonal selection signatures than polyclonally assigned polyps.
- Adenoma-specific cells from monoclonal polyps had higher expression of cell-cycle, nucleic-acid synthesis, and protein-translation signatures compared to polyclonal polyps.
- T cell exhaustion was lowest in polyclonal polyps, intermediate in monoclonal polyps, and highest in cancer — consistent with a transitional tumour microenvironment (TME) process starting at the premalignant stage.
- A subset of polyclonally initiated tumours showed clonal selection pressure, suggesting polyclonal polyps may be transitioning toward monoclonal composition en route to malignancy.

**Polyclonality as a potential progression biomarker:**
- The Discussion explicitly raises the possibility that clonality may serve as a predictive biomarker for precancers that will advance to malignancy (polyclonal polyps maintaining polyclonality may remain indolent; loss of polyclonality under clonal sweep may mark progression).
- Advanced CRC multiregional WES in 23 samples showed only one specimen with potential polyclonal initiation — consistent with clonal sweeps erasing polyclonal history during malignant progression.

**Persister intestinal stem cells (pISCs):**
- NSC-seq identified a developmentally distinct population of Tob2+ cells at the base of adult small-intestinal crypts; these pISCs derive from earlier embryonic cell generations than CBC (crypt-base columnar) stem cells, have larger clone sizes, and may act as stem/progenitor-like reservoir cells. [Relevant to precancer via stem-cell-of-origin question, though primarily a developmental finding.]

**Mouse development findings (context):**
- Tissue-specific cell proliferation rates vary markedly across organ types during gastrulation; cell division distributions narrow and shift after E7.75, indicating diversification initiation.
- Identified a previously unknown somite-derived erythroid progenitor (EryPro1) with similarity to zebrafish equivalents.
- Visceral endoderm cells intermix into the hindgut during gastrulation, confirmed by XCI and lineage analysis.

## Limitations

- **Polyclonality frequency is likely underestimated:** Sequencing depth limits detection of minor clones; monoclonal conversion during tumour growth erases early polyclonal signals; serrated polyps may have APC-independent polyclonal initiation mechanisms not captured by APC mutation counting.
- **Causal directionality unresolved:** It is not established whether polyclonality causes indolence or whether indolent lesions simply persist long enough to accumulate additional founder clones. The cross-sectional design cannot prove that polyps with monoclonal composition necessarily started monoclonal.
- **NSC-seq barcoding limited to constitutive Cas9 mouse models:** Direct barcoding not applicable to human tissue; human arm relies on endogenous somatic mutations (APC counts, mtVars, XCI, somatic SNVs) which provide coarser temporal resolution and are susceptible to artifacts from sequencing depth and contamination.
- **Mouse Apc^Min/+ model:** Tumorigenesis is driven by random inactivation of the second Apc allele — slightly different from sporadic human CRC where somatic APC mutations must be acquired independently, potentially inflating apparent polyclonality in the mouse arm.
- **Cohort composition:** Polyps were collected from three different patient cohorts with varying racial backgrounds, ages, and ascertainment strategies, which may introduce heterogeneity in clonality estimates.
- **WES was not available for all polyps:** Only 96/116 VUMC polyps had matching WES; the targeted sequencing dataset (Tennessee) lacks single-cell resolution.
- **Clonality as biomarker not yet validated prospectively:** The proposal that clonality predicts progression is speculative at this stage; no longitudinal follow-up data are presented.
