---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Kumar2022secDrug
kind: paper
title: 'secDrug: a pipeline to discover novel drug combinations to kill drug-resistant multiple myeloma cells using a greedy set cover algorithm and single-cell multi-omics'
version: "1.0.0"
created: "2026-05-29"
updated: "2026-05-29"
bibkey: Kumar2022secDrug
tags: []
ontology_terms:
- computational-pipeline
- drug-combination-discovery
- drug-resistance
- multiple-myeloma
- pharmacogenomics
- secondary-drug-prediction
- single-cell-omics
---
## Key Findings

**Algorithm predictions:**
- 94 B-cell cancer lines passed filtering criteria; PI-only (Bortezomib) killed 33% of these lines.
- Top predicted PI+2 secDrug combinations (with coverage) include: PI + FK866 + 17AAG (72.2%), PI + XAV939 + 17AAG (71.1%), PI + PF.4708671 + Bleomycin (76.3%), PI + Bleomycin + SB505124 (75.3%), PI + PLX4720 + Navitoclax (75.3%).
- 28 distinct PI+2 combinations are reported in Table 1 (coverage 71.1–76.3%); adding a third secDrug (PI+3 regimens) reaches 80.4–87.6% coverage.
- Proof-of-principle secDrug: 17-AAG (HSP90 inhibitor) + FK866 (NAMPT inhibitor) combined with PI backbone.

**Single-cell transcriptomic validation:**
- scRNA-seq confirmed that target genes of the top two proof-of-principle secDrugs — HSP90AA1, HSP90AB1 (17-AAG targets) and NAMPT (FK866 target) — are highly expressed in the majority of single-cell subpopulations in both drug-sensitive and drug-resistant myeloma HMCLs, supporting broad subclonal coverage of the predicted combinations.

**In vitro synergy validation:**
- 17-AAG showed high single-agent cytotoxicity against the HMCL panel, including innate and acquired PI-resistant and IMiD-resistant lines.
- 17-AAG + Ixazomib: CI < 1 across sensitive (FLAM76, KAS6/1, MM1S), innate-resistant (JIM3, LP-1), and acquired PI-resistant clonal pairs (U266P/VR, RPMI8226P/VR); CI values range 0.037–0.590; DRI values 5.22–9.26 (large reduction in effective Ixazomib dose required). (Figs. 3A tests these 9 lines; JJN3-P/VR and MM1S/LenR are not in this panel.)
- 17-AAG + FK866: synergistic (CI < 1) across FLAM-76, LP-1, RPMI-P/VR, and U266-P/VR pairs (JJN3-P/VR tested but no CI/DRI value reported); CI 0.136–0.571, DRI 4.20–9.18.
- 17-AAG + Lenalidomide: CI 0.428–0.735 in MM1S-Len sensitive and resistant lines; DRI 8.33–16.59.

**CyTOF (patient PMCs):**
- In n=6 patient primary samples, 17-AAG induced elevated cleaved caspase-3 (CC3) in a distinct cell cluster (apoptosis confirmed by FlowSOM/UMAP analysis) at concentrations of 0.2–5 µM.
- Downregulation of myeloma survival markers (IRF4, pSTAT3, CD138, pRB, CD27) in PMCs post-17-AAG treatment.

**Mechanism — ROS and mitochondrial pathway:**
- 17-AAG induced elevated cellular superoxide anions and intracellular ROS (DHE fluorescence assay) and mitochondrial membrane depolarization (JC-1 assay) in sensitive and resistant HMCLs, consistent with mitochondria-mediated apoptosis.
- CRISPR-mediated HSP90AA1 knockout in RPMI8226 confirmed on-target cell death comparable to pharmacological 17-AAG treatment.

**Gene expression profiling:**
- Bulk RNAseq of HMCLs (sensitive vs. resistant to 17-AAG): 421 genes differentially expressed; top 50 upregulated/downregulated reported in Supplementary Table S2. IPA: B Cell Receptor Signaling (p=1.90E-03), RhoGDI Signaling (p=1.22E-03), and IL-10 Signaling (p=1.43E-03) as top canonical pathways.
- Single-agent 17-AAG kinetic DEG analysis across all HMCLs: 422 genes common to all treated vs. untreated signatures; IPA top pathways: cell cycle control of chromosomal replication (z=-4.243), EIF2 signaling (z=2.496), aryl hydrocarbon receptor signaling (z=-3.464), protein ubiquitination pathway (p=7.90E-08; no z-score reported for this pathway). Upstream regulator analysis: CEBPB (z=-6.670), ERBB2 (z=-5.358), CSF2 (z=-4.750), CCND1 (z=-3.707) downregulated; microRNA let-7 upregulated (z=5.501).
- 17-AAG + Ixazomib combination (vs. untreated): 3,974 genes significantly changed; IPA top canonical pathway: PUP (p=3.89E-23); upstream inhibition of CEBPB (z=-8.871), MYC (z=-6.732), VEGF (z=-6.805), HGF (z=-7.139), CSF2 (z=-6.770).

**NRas-mutant sensitivity:**
- ANBL6 NRas-mutant cell lines showed 20-fold greater 17-AAG sensitivity (lower IC₅₀) compared to ANBL6P or VR parental/resistant lines, identifying NRas-mutant myeloma as a potential precision niche for 17-AAG.

**R software package:**
- secDrug R package publicly released; generalized to accept any cancer type and any standard-of-care drug as input; outputs ranked list of top secondary drug combinations with confidence scores and biological pathway visualizations.

## Methods

**In silico prediction (secDrug algorithm).** Inputs came from the GDSC1000 database (>250 drugs across >1,000 human cancer cell lines; 1,091 total lines). Filtering for B-cell/haematopoietic lineage, tissue, histology, site, and data completeness yielded 94 computable cell lines, categorized by IC₅₀ as PI-sensitive (S), PI-resistant (R), or intermediate (N) to Bortezomib (the primary test PI). A modified greedy set-cover, regularization-based optimization sequentially selected secondary drugs maximizing additional resistant-line killing, ranking PI+2 and PI+3 regimens by percent coverage (Table 1). Top proof-of-principle secDrug: 17-AAG (HSP90 inhibitor) + FK866 (NAMPT inhibitor).

**scRNAseq screening.** ~1,500 tumor cells/sample captured via 10x Genomics Chromium; sequenced on Illumina HiSeq 2500 (2×125 bp, >50M reads/sample). Seurat + Partek Flow for processing; t-SNE for cluster visualization; used to confirm HSP90AA1/HSP90AB1 and NAMPT expression across single-cell subpopulations.

**In vitro validation.** >70 HMCLs spanning sensitive, innate-resistant, and clonally derived (dose-escalation) acquired PI/IMiD-resistant pairs; Ixazomib as representative PI, Lenalidomide as representative IMiD. Viability by CellTiter-Glo (48 h); IC₅₀ via GraphPad Prism nonlinear regression; CI and DRI via Chou–Talalay method using Calcusyn/isobologram software (Biosoft). CRISPR-Cas9 HSP90AA1 knockout in RPMI8226 (Synthego sgRNA + spCas9 RNP; confirmed by Synthego ICE + Sanger). Additional assays: Caspase-3/7 (Promega), DHE superoxide, JC-1 mitochondrial membrane potential.

**Ex vivo/multi-omic validation.** CyTOF (37-antibody panel, Fluidigm; Cytobank; t-SNE/viSNE/FlowSOM) on n=6 Mayo Clinic patient CD138+ PMCs treated with 17-AAG (Methods states 0.2/1/5 µM; Fig. 4's legend instead reads 2/5/10 µM — an internal inconsistency in the source [UNVERIFIED which is correct]). Bulk RNA-seq (HMCLs, 4×10⁵ cells/mL, 17-AAG ± 15 nM Ixazomib, 24 h, Illumina NovaSeq 150 bp PE, >20M reads/sample): DESeq2/edgeR + Partek Flow, GSA/limma DEGs (|fold-change|>1, p<0.05), IPA (QIAGEN) for pathways/upstream regulators. Western blotting with ImageJ densitometry. Statistics: R and GraphPad Prism 9.0, two-sided tests, α=0.05.

## Limitations

- The GDSC1000 filtering retains only 94 B-cell cancer lines for the myeloma use case; this is a relatively small training set and may underrepresent the full diversity of PI-resistant myeloma biology.
- The in silico algorithm ranks combinations by predicted percent cell-line coverage, not by synergy score; coverage-optimal combinations are not guaranteed to be synergistic (CI < 1), and synergy confirmation requires separate in vitro follow-up, which here covered the 17-AAG + Ixazomib, + FK866, and + Lenalidomide combinations.
- The in vivo toxicity profile of PI + 17-AAG ± FK866 is not addressed; clinical translation of HSP90 inhibitors will require tolerability data this study does not provide. (Note: claims that 17-AAG/Tanespimycin has hepatotoxicity or limited single-agent activity are not sourced from this paper — which in fact reports strong single-agent 17-AAG cytotoxicity across the HMCL panel.)
- The CyTOF ex vivo data uses only n=6 patient PMC samples, limiting statistical power for patient-level generalizations.
- FK866 (NAMPT inhibitor) is validated as a secDrug primarily through the in silico prediction and cell-line synergy data; patient-derived or in vivo validation of the 17-AAG + FK866 combination is not presented.
- The secDrug algorithm does not model drug-drug pharmacokinetic interactions, tolerability, or clinical dose constraints — the coverage percentages reflect in vitro cell-line predictions only.
- The R package and datasets are stated to be available on reasonable request from the corresponding author (for raw/analysis data) and on GitHub (for code), but the GitHub URL provided (Ujjal-Mukherjee/secDrug) should be verified for current availability.
- No mouse xenograft or in vivo model data is presented; the pipeline stops at ex vivo (patient PMCs) and in vitro for experimental validation.
