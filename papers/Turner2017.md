---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Turner2017
type: paper
title: Extrachromosomal oncogene amplification drives tumour evolution and genetic heterogeneity
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Turner2017
tags: []
ontology_terms:
- ecDNA
- extrachromosomal DNA
- glioblastoma
- intratumour heterogeneity
- non-Mendelian inheritance
- oncogene amplification
- pan-cancer prevalence
- random segregation
---
## Key Findings

### Data-derived findings (D)

- **(D) ecDNA prevalence: nearly half of cancers, essentially absent from normal tissue.** Using the conservative criterion (≥2 ECDNAs in ≥10% of metaphases), ecDNA was detected in approximately 40% of tumor cell lines and approximately 90% of patient-derived brain tumor models (PDX/neurospheres), but in 0% of 8 normal tissue cultures and rarely in immortalized cells (Fig. 2c–d). The abstract states ecDNA was "found in nearly half of human cancers varying by tumor type." The prior "~40% pan-cancer" figure is therefore an understatement for PDX/primary models and an overstatement if read as applying uniformly across all sample types; the correct characterization is that prevalence varied substantially by sample type and cancer type, with GBM and PDX at the high end.

- **(D) Approximately 30% of detected ECDNAs are paired double minutes.** Among the ecDNA-positive samples, approximately 30% of individual ECDNA objects were paired double minute chromosomes (Source Data Table S2).

- **(D) ecDNA carries confirmed driver oncogenes.** WGS-detected amplicons overlapped significantly with TCGA pan-cancer amplicons (p ≤ 10⁻⁶ by permutation). FISH validation confirmed the following oncogenes on ecDNA in specific samples: MYC (e.g., PC3 prostate, MB411FH breast, HL-60 AML), EGFR/EGFRvIII (GBM39, GBM6), ERBB2, CCND1 (SF295 glioma), CCND3, CCNE1, MDM4, ATM (Fig. 3b). From WGS, 14 oncogenes were identified in ≥2 samples, overlapping 7 of the top 10 TCGA pan-cancer oncogenes (hypergeometric p = 3.07 × 10⁻¹⁰). Oncogenes annotated at chromosomal loci in Fig. 3a include ARNT, MDM4, EGFR, CCND3, WHSC1L1, FGFR1, MYC, RECQL4, CCND1, KRAS, CCND2, CDK4, DDIT3, NKX2-1, ERBB2, CDK12, CCNE1, AKT2, GNAS, SS18L1 — all detected as amplified; their distribution across ecDNA vs. HSR is shown per-sample in Fig. 3b.

- **(D) All tested amplified oncogenes were found solely on ecDNA or concurrently on ecDNA and HSRs; none were found exclusively on HSRs when ecDNA was absent.** (p.3: "All of the amplified oncogenes tested were found solely on ECDNA, or concurrently on ECDNA and chromosomal homogenous staining regions (HSRs).")

- **(D) ecDNA-amplified oncogenes have higher copy numbers than chromosomally amplified counterparts.** FISH probes for EGFR, MYC, CCND1, ERBB2 in four cell lines (GBM39, MB411FH, PC3, SF295): the oncogene known to be on ecDNA in each line showed significantly higher copy number and higher Shannon entropy (copy-number diversity) than the same gene on chromosomal loci in the same cells (Fig. E7, Extended Data). qPCR confirmed that mRNA levels of EGFRvIII and c-MYC were significantly higher when amplified on ecDNA vs. chromosomally (p < 0.001, Mann-Whitney, n = 17; Fig. 3d).

- **(D) Random ecDNA segregation generates higher ITH than chromosomal amplification across all tested model parameters.** Galton-Watson model: ecDNA copy number rises faster and reaches higher levels than HSR copy number (Fig. 4b), and Shannon entropy (ITH) rises more rapidly and is maintained at higher levels under the EC model vs. HSR model across p_d values of 0.01–0.1 (Fig. 4d). Predicted Shannon entropy vs. copy number correlation (Fig. 4e) was recapitulated by experimental FISH data from tumor samples (Fig. 4f).

- **(D) EGFRvIII ecDNA reversibly shifts to HSR under EGFR inhibitor treatment and re-emerges as ecDNA after drug withdrawal.** In GBM39 cells: naive cultures carry ~110–150 EGFRvIII copies on ecDNA; erlotinib-treated cultures carry ~5.4 copies on HSRs (ecDNA lost); erlotinib-withdrawn cultures return to ~100–105 copies on ecDNA. WGS showed conserved fine structure between ecDNA and HSR amplicons, consistent with HSR formation by reintegration of ecDNA-derived sequences (AmpliconArchitect, Fig. E8–E9).

- **(D) ecDNA is abundant in cancer and shows high cell-to-cell variation in copy number within a single culture.** Shannon index of ecDNA count per metaphase varies greatly within samples, particularly in PDX/brain tumor models, confirming high intra-sample copy-number heterogeneity (Fig. 2e–f).

### Author interpretations (L)

- **(L) Random ecDNA segregation is a mechanistic engine for rapid tumour evolution.** The authors argue that because ecDNA copies partition by binomial random segregation (no centromere tethering), every cell division regenerates a new distribution of oncogene copy numbers among daughters — continuously producing high-amplitude heritable variation without requiring new mutations. This is framed as enabling faster evolutionary adaptation than chromosomal mutation accumulation.

- **(L) ecDNA-driven copy-number heterogeneity pre-adapts tumours to selection pressures, including therapy.** The GBM39 erlotinib experiment is interpreted as showing that ecDNA's high copy-number variance pre-positions tumours to rapidly adapt: under inhibitor pressure the ecDNA copies are lost (consistent with selection against high-copy cells or preferential loss), while upon withdrawal ecDNA re-emerges (possibly from a residual subpopulation or reintegration-then-re-excision). The authors frame this as a reversible resistance mechanism mechanistically distinct from acquired mutation.

- **(L) ecDNA prevalence has been substantially underestimated.** The authors argue that bulk WGS and array-CGH without metaphase cytogenetics cannot distinguish ecDNA from chromosomally integrated amplicons, and that prior prevalence estimates (e.g., 1.4% for double minutes in Mitelman database) dramatically undercount ecDNA because cytogenetic analysis was not applied systematically.

- **(L) ecDNA represents a qualitatively distinct mode of oncogene amplification relative to HSRs.** The authors interpret their combined data as showing that the *inheritance mechanism* (random vs. mitotic-recombination-based segregation), not merely copy number, is the biologically consequential variable: ecDNA generates higher per-cell copy numbers, greater ITH, and higher mRNA output than equal-copy-number chromosomal amplicons — constituting a distinct evolutionary regime.

- **(L) The elevated mRNA output of ecDNA-carried oncogenes may reflect a more permissive chromatin environment.** The qPCR data show higher mRNA for ecDNA-amplified EGFR/MYC than chromosomally amplified counterparts. The authors suggest this may reflect "transcript level" elevation on ecDNA. However, this paper does not perform ATAC-seq or other chromatin accessibility assays — the mechanistic characterisation of ecDNA chromatin architecture (super-enhancer enrichment, hub formation) is the contribution of subsequent papers (Wu et al. 2019).

## Limitations

- **FISH-based prevalence is cytogenetic, not single-cell sequencing.** *ECdetect* counts DAPI-stained objects; structural characterisation and oncogene identity require WGS. Copy number quantification per cell is probe-count limited.
- **Low WGS coverage (median 1.19×).** Structural inference by AmpliconArchitect at this depth may miss complex rearrangements or undercount amplicon heterogeneity.
- **Moderate sample sizes per cancer type.** Fig. 1a shows N ranging from ~5 to ~25 per cancer type. Per-type confidence intervals are wide; the paper does not report per-type N in text.
- **Cell-line and PDX models dominate.** The ecDNA characterisation is predominantly in cultured cancer cell lines and PDX neurospheres. In vivo tumour metaphases are a minority of the cohort (35 cancer tissue biopsies). Whether in-culture ecDNA dynamics are quantitatively representative of primary tumours is not directly tested.
- **Drug-response experiment is cell-culture only.** The GBM39 erlotinib/withdrawal experiment is in a single cell line. The paper does not present paired patient tumour biopsies pre/post-treatment. The reversal observation is consistent with selection plus re-excision but does not distinguish these mechanisms.
- **No ATAC-seq or chromatin accessibility assay.** The elevated mRNA per ecDNA copy is measured by qPCR but the chromatin-level mechanism is not characterised here. Attribution to a "permissive chromatin environment" on ecDNA is an inference in this paper; the direct chromatin measurement is made in Wu 2019.
- **No formal phylogenetic model.** The evolutionary-regime claims rest on the branching-process simulation and FISH data, not on phylogenetic reconstruction of ecDNA-carrying tumours.
