---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Hughitt2025MIPE
kind: paper
title: Large-scale human myeloma cell line small molecule compound screen dataset
version: "1.0.0"
created: "2026-05-29"
updated: "2026-05-29"
bibkey: Hughitt2025MIPE
tags: []
authors:
- V. Keith Hughitt et al.
doi: 10.1038/s41597-025-04989-8
ontology_terms:
- cell viability
- dose-response curve
- high-throughput drug screening
- multiple myeloma
pmid: '[UNVERIFIED]'
venue: Scientific Data
year: 2025
---
## One-Sentence Summary

A Data Descriptor releasing the full NCATS MIPE 4.0 pharmacological screen of 1,912 small-molecule compounds tested at 11 doses across 47 human myeloma cell lines (HMCLs), with raw and processed data, spatial-bias correction, dose-response curve fits, and a reproducible Snakemake pipeline.

## Key Findings

1. 1,912 MIPE 4.0 compounds were screened at 11 doses (3-fold serial dilution series; absolute concentration range [UNVERIFIED] — not stated in the published Data Descriptor) in 47 HMCLs using a 1,536-well CellTiter-Glo viability format; 43 out of 47 cell lines passed QC and are included in processed outputs (4 outlier lines — KMS11, KMS28BM, KMS21BM, Karpas417 — excluded from downstream processing due to control-well failures or edge effects, but raw data are retained).
2. A background plate correction for spatial bias was applied on top of standard positive/negative control normalization (bortezomib vs. DMSO wells); all data are released at multiple processing stages (raw, filtered, normalised, background-adjusted).
3. 36 drugs showed AC-50 < 100 nM in ≥ 80% of cell lines; 660 drugs had AC-50 > 1,000 nM in ≥ 80% of lines, illustrating a wide dynamic range of compound potency; dose-response curves were fit per cell line × drug pair using the four-parameter log-logistic `drc` R package.
4. Rich metadata accompany the screen: cell line sex, ancestry, heavy/light chain isotype, canonical IgH translocations, and mutation status for KRAS, NRAS, TP53, and TRAF3 (sourced from the Keats Lab HMCL Characterization Project and CCLE) for all 47 lines; predicted whole-exome mutations are provided for 46/47 lines.
5. The full processing pipeline is distributed as a Snakemake workflow at https://github.com/khughitt/hmcl-drug-screen-pipeline; data are packaged in Frictionless Data Package format with checksums and field-level metadata at Zenodo (DOI: 10.5281/zenodo.14902712).

## Methods

This Data Descriptor reports a pharmacological screen of the NCATS MIPE 4.0 library (1,912 small-molecule compounds) against 47 human multiple myeloma cell lines (HMCLs) obtained from the Keats Lab, from the same passage previously used for whole-exome sequencing. Cells were seeded in 1,536-well solid-bottom white plates (Multidrop Combi dispenser, ~10^3 cells/well in 5 µl) and dosed via a Kalypsys pintool (23 nl) with 11 doses of a 3-fold serial dilution series, each in a single replicate, alongside bortezomib (positive) and DMSO (negative) control columns. Viability was measured after 48 h by CellTiter-Glo luminescence on a ViewLux (10 s exposure). Raw values were clipped (negatives set to 0; ceiling at the 99.5% quantile) and converted to percent viability using the positive/negative control medians. A "background" plate (mean well intensity across all plates, per-concentration mean subtracted) was then subtracted from each raw plate and rescaled to [0,100] to correct spatial bias. Four-parameter log-logistic dose-response curves were fit per cell line × drug pair using the `drc` R package, yielding AC-50 and lac50 (non-convergent fits set to NA). Four cell lines (KMS11, KMS28BM — control-well issues; KMS21BM, Karpas417 — edge effects) were excluded from background-plate construction and all downstream processing, based on a per-plate QC score (median Pearson correlation of viability curves to an idealized sigmoid); raw data for these lines are retained. Cell-line metadata (sex, ancestry, isotype, translocations, KRAS/NRAS/TP53/TRAF3 status) came from the Keats Lab HMCL Characterization Project and CCLE. Whole-exome-derived predicted mutations (Agilent SureSelect V4+UTR capture, Illumina HiSeq 2000, GRCh37 via BWA/GATK/SAMTOOLS, germline-filtered against 1000 Genomes/ExAC r0.3/NHLBI ESP6500, COSMIC v74/snpEFF-annotated) are provided for 46/47 lines. The full pipeline (Snakemake, R, ggplot2 with ggpubfigs palettes) is public; outputs are released as a Frictionless Data Package.

## Limitations

- **Single-replicate compound testing:** each cell line × drug × dose combination was measured in a single replicate; only the control wells (bortezomib/DMSO) were replicated within a plate, limiting direct estimation of per-measurement technical noise for tested compounds.
- **Excluded cell lines reduce genotype coverage:** four HMCLs (KMS11, KMS28BM, KMS21BM, Karpas417) were dropped from background-plate construction and all downstream processing/figures due to control-well failures or edge effects; this removes specific translocation genotypes from the processed dataset (e.g., KMS11 carries t(4;14)/t(8;14)/t(14;16)), though raw data remain available.
- **Residual, unflagged batch effects possible:** plates from one experimental date for two further lines (MM1S_ATCC, U266_ATCC) were flagged rather than excluded; users must apply the plate-metadata QC fields themselves, and other undetected plate/date batch effects cannot be ruled out.
- **Simple spatial-bias model:** the background correction is a single mean-intensity plate subtracted per concentration — a first-order adjustment, not a full statistical plate-effect model; its residual adequacy is assessed only by qualitative plate-image inspection.
- **Compound annotation versioning:** drug metadata was compiled for the MIPE 4.0 library screened, then updated with newer MIPE 6.0 metadata — the annotated library is not identical to the exact lot screened, so mechanism-of-action/target annotations should be treated as approximate.
- **Descriptive, not inferential:** as a Data Descriptor, the paper performs no hypothesis testing or multiple-comparison-corrected inference; the AC-50 potency tallies are descriptive, and curve-fit p-values are per-fit, not screen-wide corrected.
- **Cell-line-only system:** HMCLs are immortalized, culture-adapted lines assayed without tumor microenvironment, stroma, or immune components; AC-50 potency rankings may not translate to patient-level drug response.
- **Divergent public dataset versions:** an earlier PubChem release (BioAssay 1918926) lacks the spatial-bias correction described here; the two public versions can disagree numerically and should not be mixed.
