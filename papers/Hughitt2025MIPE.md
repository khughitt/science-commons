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

1. 1,912 MIPE 4.0 compounds were screened at 11 doses (3-fold serial dilution, ~0.8 nM to 46 µM) in 47 HMCLs using a 1,536-well CellTiter-Glo viability format; 43 out of 47 cell lines passed QC and are included in processed outputs (4 outlier lines — KMS11, KMS28BM, KMS21BM, Karpas417 — excluded from downstream processing due to control-well failures or edge effects, but raw data are retained).
2. A background plate correction for spatial bias was applied on top of standard positive/negative control normalization (bortezomib vs. DMSO wells); all data are released at multiple processing stages (raw, filtered, normalised, background-adjusted).
3. 36 drugs showed AC-50 < 100 nM in ≥ 80% of cell lines; 660 drugs had AC-50 > 1,000 nM in ≥ 80% of lines, illustrating a wide dynamic range of compound potency; dose-response curves were fit per cell line × drug pair using the four-parameter log-logistic `drc` R package.
4. Rich metadata accompany the screen: cell line sex, ancestry, heavy/light chain isotype, canonical IgH translocations, and mutation status for KRAS, NRAS, TP53, and TRAF3 (sourced from the Keats Lab HMCL Characterization Project and CCLE) for all 47 lines; predicted whole-exome mutations are provided for 46/47 lines.
5. The full processing pipeline is distributed as a Snakemake workflow at https://github.com/khughitt/hmcl-drug-screen-pipeline; data are packaged in Frictionless Data Package format with checksums and field-level metadata at Zenodo (DOI: 10.5281/zenodo.14902712).
