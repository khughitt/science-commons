---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Boyle2023
kind: paper
title: Multiomic Mapping of Acquired Chromosome 1 Copy-Number and Structural Variants to Identify Therapeutic Vulnerabilities in Multiple Myeloma
version: "1.1.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: Boyle2023
authors:
- Boyle, Eileen M.
- Blaney, Patrick
- Stoeckle, James H.
- Davies, Faith E.
- Morgan, Gareth J.
year: 2023
venue: Clinical Cancer Research
doi: 10.1158/1078-0432.CCR-22-3209
tags: []
ontology_terms:
- chromosome 1p deletion
- chromosome 1q gain
- chromothripsis
- copy number variation
- structural variant
---
## Key Findings

1. **Focal vs. whole-arm gain(1q) are clinically distinct subtypes.** Of 302 patients with gain(1q), 219 (73%) have whole-arm gains (regions G2-G9) with adverse prognosis (PFS HR 1.3, p=0.04; OS HR 1.6, p=0.004) and 83 (27%) have focal gains associated with neutral outcome. Co-occurrence strength varies sharply, and only one association is strong: whole-arm gains co-occur with **del(13q) (corr=0.23, BF=1.19e5)**, whereas t(4;14) (corr=0.10, **BF=1.06**), del(16p):CYLD (BF=2.3), del(4p) (BF=1.89) and shorter telomeres (BF=1.2) sit at or barely above the no-evidence line — do **not** cite these as strong links. Focal gains are enriched for templated-insertion events (corr=0.34, BF=6e14), MYC translocation (corr=0.24, BF=3.0e6), and hyperdiploidy. (The Results report whole-arm as 73% of gain(1q); the Discussion says 60% — the paper is internally inconsistent.)

2. **Fine mapping identifies 9 gain, 7 deletion, 2 templated-insertion (TI), and 3 chromothripsis (CT) regions on chr1.** Key gain-region drivers: MCL1 (G3), BGLAP (G4), SLAMF1/SLAMF7 (G5), POU2F1 (G6), ABL2 (G7), BTG2 (G8), NLRP3 (G9). Key deletion-region tumor suppressors: CDKN2C/FAF1 (D3), FUBP1 (D5), RPL5/EVI5 (D6), TENT5C (D7). The paper places these named TSGs in **A**-compartments (active chromatin) — CDKN2C is "in an A-compartment in all samples," and FUBP1 sits in small A-compartments within an otherwise-inactive D5.

3. **Whole-arm gain(1q) drives substantially broader transcriptional rewiring than focal gain.** Whole-arm gains: 2409 DEGs (101 transcription factors, including upregulation of BACH2, NR5A1, MYBL1, GLMP, E2F2 and downregulation of PAX5, SMAD1, TBX21); focal gains: only 20 DEGs. Pathway enrichment (**g:Profiler over GO terms** — the paper's prose calls this "GSEA," but no formal gene-set-enrichment method was run) highlights metabolic and biosynthetic processes, apoptotic resistance, and MAPK signaling. **The 20-vs-2409 contrast is not power-matched**: focal (n=56) and whole-arm (n=173) are each compared against the same n=297 no-gain reference, so the ~100x DEG ratio partly reflects group size.

4. **TENT5C super-enhancer hijacking is a proposed mechanism for oncogene upregulation at receptor sites.** TI1 (1p13.1-1p11.2) rearranges the TENT5C super-enhancer to receptor loci; TI2 (1q32.1-1q32.2) contains super-enhancers linked to BTG2 and MDM4. The authors hedge this deliberately: the rearrangement "**likely** deregulates genes at its receptor site" and "**may** explain the frequency of events at this locus." The NOTCH2 super-enhancer was active in all 3 cell lines but in only **2 of 10** NDMM patients.

5. **Hypomethylation at 1q21.3-1q23.1 provides an additional CNV-independent mechanism for gene overexpression.** 378 of 383 differentially methylated probes on chr1 are hypomethylated; 62 genes in gain(1q) patients are both hypomethylated and overexpressed, falling predominantly outside GISTIC2-defined gain boundaries. DDR2 and NTRK1 identified as hypomethylated-overexpressed targets. Of the GEP70 genes and previously implicated chr1 drivers, **only** EVI5, SLAMF7 and PDZK1 were hypomethylated — i.e. most known drivers are *not*.

6. **CRISPR dependency analysis is largely a negative result.** Re-analysis of public DepMap data across 19 MM cell lines — of which **9 carry gain(1q) and 6 carry del(1p)**, not all 19 — identified **14 differentially dependent genes, 9 of them on 1q** (incl. ZNF281, ZBTB37, PIGN, CD1D, HAX1, UCHL5, POU2F1, LAMTOR2, CCDC190); three genes show increased dependency in del(1p) cells (ID3, GLMN, TRNP1). But **no delta-dependency exceeded 0.4**, cell lines did not cluster by copy-number profile, and the abstract itself concedes CRISPR found "only limited variants associated with acquired CNAs." The del(1p) comparison also returned 8 genes with *reduced* dependency (incl. NRAS, RPL11) that the authors say "would not constitute effective therapeutic targets." **PSMD4 and MDM4 are imported from prior literature** (refs 57 and 58 — the latter a 1999 glioma study), **not** results of this screen, and appear nowhere among the 14 genes. Every "therapeutic vulnerability" here is a computational candidate: the paper contains no functional validation and no drug-sensitivity data.

7. **Mutational landscape (from a separate 1,273-exome cohort, not the 752 WGS cases).** NRAS (17%) is the most frequently mutated gene on chr1. Bi-allelic tumor-suppressor inactivation is reported as a **percentage of *mutated* cases, not of the cohort**: CDKN2C (62% of mutated cases), FUBP1 (50%), TENT5C (26%). Because CDKN2C and FUBP1 are each mutated in only ~1% of cases, bi-allelic CDKN2C inactivation is roughly **0.6% of all patients** — a rare confirmatory second hit, not a common lesion. Critically, **of 63 known MM driver genes, 5 map to 1p and none to 1q**, so the 1q phenotype is dosage/epigenetically driven rather than mutation-driven. NRAS negatively correlates with CN cluster 3 (del(1p)/gain(1q)/del(13q)/del(16q)).

## Methods

- **Design:** Retrospective multiomic association study in newly diagnosed multiple myeloma (NDMM). No original data were generated — every layer re-analyzes an existing public dataset. **Four non-overlapping source cohorts are combined, and no cross-layer integration is within-patient.**
- **Primary cohort (CNA/SV + expression):** 752 NDMM patients from MMRF CoMMpass (NCT01454297, IA13) with long-insert **low-coverage** WGS; a 643-patient subset has matched RNA-seq. Observational registry; non-randomized; heterogeneous treatment.
- **Mutation cohort (separate):** the mutational landscape comes from an independent set of **1,273 NDMM exomes**.
- **Methylation cohort (separate):** GEO **GSE21304** — NDMM n=161, plus normal B cells n=6, normal plasma cells n=3, MGUS n=4, PCL n=7, and 9 myeloma cell lines. Different patients from CoMMpass.
- **Chromatin / enhancer data:** Hi-C from 4 normal B-cell states (EGAD00001006485) and **3 cell lines only** (U266, RPMI8226, KMS11; GSE87585 / EGAD00001003597) — **no patient Hi-C**. H3K27ac ChIP-seq for super-enhancer calling in **10 NDMM patients + those same 3 cell lines**.
- **Dependency data:** re-analysis of public **DepMap** CRISPR-Cas9 essentiality data (CERES scores) across **19 MM cell lines + 15 unrelated lines**, 1,701 chr1 genes. The authors ran no new screen.
- **CNA/SV calling:** GISTIC2.0 for copy-number peaks; the `hotspots` ("hotornot-mm") tool for recurrent regions; BEDtools v2.30.0; the **PCF algorithm** for breakpoint-clustered regions (templated insertion, chromoplexy); **chromothripsis called by manual inspection** to remove sequencing artifacts.
- **Expression:** STAR v2.5.1b → QoRTS → Salmon v0.7.2 → DESeq2 (GRCh38). The main gain(1q) contrast is defined by a **single-gene proxy — CKS1B copy number at 1q12** — giving 173 gain vs 376 no-gain (549 of the 643 RNA-seq cases). Differential expression was repeated *within* the t(4;14) and t(11;14) subgroups to strip translocation-subgroup confounding.
- **Methylation:** RnBeads; GENCODE v36; PCA over 2,498 chr1 probes.
- **Chromatin:** hic-bench, BWA, Juicer, ICE normalization, HOMER (A/B compartments at 100 kb), TopDom (TADs); ROSE2 on H3K27ac for super-enhancers; pyGenomeTracks for multiomic visualization.
- **Statistics:** co-occurrence tested with a pairwise **Phi correlation coefficient** (R, `sjstats::phicoef`); Bayes factors are reported alongside, but their computation is never described. Pathway analysis is **g:Profiler over GO terms**. Survival is reported as **bare hazard ratios — the paper specifies no survival model and reports no multivariable adjustment.**
- **Not performed:** no external validation cohort; no functional validation of any candidate driver; no drug-sensitivity or treatment-response data.
- **Code:** SV hotspot detection — https://github.com/evenrus/hotspots/tree/hotornot-mm

## Limitations

**Stated by the authors:**

- CRISPR added little: the abstract concedes it identified "only limited variants associated with acquired CNAs." **No differential dependency had a delta > 0.4**, which the authors read as evidence that the dependencies are "not just the resultant of the CNA on chromosome 1 but the resultant of many other factors such as cytogenetic background." The del(1p) comparison returned 8 genes with *reduced* dependency that "would not constitute effective therapeutic targets."
- del(1p) **was not associated with adverse outcome in this dataset**, and no patients with bi-allelic 1p32 loss were present, so the authors could not confirm Schavgoulidze 2022's ultra-high-risk bi-allelic del(1p32) entity. (The Discussion nonetheless states that 1p events "associate with a significant impact on prognosis" — the paper contradicts itself here.)
- The mechanism of the broad transcriptional deregulation under whole-arm gain "is currently uncertain"; the phenotype is attributed to many 1q drivers collectively rather than to any single gene.
- The key prognostic event on 1p "remains uncertain" because the deletion regions overlap heavily.
- The TENT5C super-enhancer-hijacking model is hedged by the authors themselves ("likely… may").

**Fair inferences from the reported design (not stated by the authors):**

- **Prognosis is unadjusted and confounded.** The whole-arm HRs (PFS 1.3, OS 1.6) come with no stated survival model and no multivariable adjustment, while the whole-arm group is *defined by the paper* as carrying del(13q), t(4;14), del(4p), shorter telomeres and higher age. Adverse outcome cannot be attributed to 1q gain per se on this evidence.
- **"Focal gain is prognostically neutral" is an underpowered null, not a demonstration of equivalence** (n=83 for outcome, n=56 for expression).
- **Nothing is integrated within-patient.** Methylation (n=161), mutations (1,273 exomes), Hi-C/compartments (3 cell lines) and dependencies (19 cell lines) are each a *different* sample set from the 752-patient WGS cohort. Every cross-layer claim — including the 62 hypomethylated-and-overexpressed genes — is a cross-cohort intersection.
- **The 62-gene hypomethylation/overexpression overlap was never formally tested for independence from copy-number dosage.** The only argument offered is that most probes fall outside the GISTIC2.0 gain boundaries — a spatial observation, not a statistical test.
- **All chromatin-state and super-enhancer conclusions rest on 3 cell lines** (plus 10 NDMM for H3K27ac only); tumour-specific compartment structure is unmeasured.
- **Candidate drivers are prioritized by association, never by function.** No knockdown, overexpression, or drug-sensitivity experiment appears anywhere in the paper.
- Chromothripsis calls involved a **manual inspection step**, and the WGS is low-coverage — limiting subclonal resolution and the gain-vs-amplification (>3 copies) distinction, which this study's main split does not use.
