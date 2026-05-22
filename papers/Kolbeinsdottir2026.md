---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Kolbeinsdottir2026
type: paper
title: Principles of subclonal gene dosage across human cancer
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Kolbeinsdottir2026
tags: []
datasets: []
ontology_terms:
- copy number variation
- gene dosage
- intratumor heterogeneity
- subclonal evolution
- transcriptional regulation
- transient clonality
- whole genome doubling
---
## Key Findings

**1. Dosage additivity is the default, but partial compensation is the rule.**
Mean regression slope across all expressed genes = 0.65 (between 0 = full compensation and 1 = perfect additivity). Neither extreme dominates pan-cancer; partial additivity is the consensus baseline.

**2. Four dosage-effect categories.**
- *Fully compensated* (12% of genes): never dosage-sensitive in any cancer type or patient.
- *Never compensated* (14%): always dosage-sensitive.
- *Cancer-type-specific* (62%): sensitive in some cancer types but not others — the dominant category, implicating tissue-specific regulatory networks.
- *Patient-specific* (12%): compensation varies between patients within a cancer type (examples: *MYC*, *CCND1*).

**3. CNV class determines transcriptional impact.**
- *Arm-level CNVs*: weakest transcriptional constraints; on average ~5 differentially expressed genes (DEGs) per clone pair; most DEGs map to non-affected (trans) regions.
- *Sub-arm and high-level focal amplifications*: intermediate-to-strong constraint; ~43 DEGs per clone pair; cis effects (genes in the altered region) contribute >50% of DEGs.
- *Highly amplified megabase-size focal segments (FOHAS)*: lowest regression slopes of all segment types (strongest dosage compensation), but with both strong cis and trans effects on transcription. FOHAS copy number was poorly predicted by expression (random forest), suggesting active transcriptional buffering, possibly via transcription factor oversubscription or tight feedback regulation.
- *WGD-separating clone pairs*: among the most transcriptionally distinct, even though relative copy-number differences between loci are modest; cell state is strongly constrained by ploidy change.

**4. Core promoter architecture predicts dosage sensitivity.**
Genes with a TATA box plus Initiator (Inr) element: mean slope 0.45. TATA alone: 0.54. Both significantly lower than genes lacking these elements (slope ~0.68, p<0.005 and p<0.05). Interpreted as: high-burst-rate promoters are under stricter feedback control. No significant effect of GC-box or CCAAT-box elements.

**5. HLA loci show dosage compensation pan-cancer.**
Chr 6 had the lowest median dosage slope; driven by HLA loci, consistent with immune evasion via epigenetic silencing and dosage buffering of antigen-presentation genes across cancer types.

**6. ARGOS genes show partial compensation in FOHAS.**
"Amplification-Related Gain of Sensitivity" genes (previously identified as expressed below expected level in amplified regions) had on average lower slopes than non-ARGOS genes, confirming partial compensation. Behaviour was gene- and sample-specific within a FOHAS (e.g., *RMB14* compensated, *CTSF* not, in same BC26 FOHAS).

**7. Genetically distant subclones are never transcriptionally similar; genetic similarity does not guarantee transcriptional similarity.**
Pairwise analysis: large genomic distance guarantees large transcriptomic distance; but two subclones can be transcriptionally highly distinct despite modest genetic distance.

**8. Transient clonality: a novel evolutionary category common in OC and SRC.**
Ten of 57 patients (6 SRC, 3 OC, 1 triple-negative BC) exhibited "transient clonality": every cell has a unique large-scale CNV profile; no detectable stable clonal hierarchy; chromosome-arm-sized regions (>50 Mb) differ between nearest-neighbour cells; high average ploidy; extensive LOH (often majority of chromosomes). Proposed mechanism: continuous missegregation of chromatin fragments at mitosis, driven by WGD followed by large-scale LOH. TP53 mutation found in 5/6 sarcoma transient cases (2 by WGS, 3 inferred from mRNA) but not an absolute prerequisite. Dosage effects in transient tumours are comparable in magnitude to stable subclone dosage effects — functionally non-silent. Hallmark interferon gamma response is downregulated in transient vs. clonal tumours, consistent with immunosuppressive phenotype of WGD.

**9. Non-cancer stromal cells show rare, cell-type-specific CNVs.**
Chr X loss is the most common somatic CNV in non-cancer cells (7% of T cells); chr 7, 12, 18 gains in fibroblasts. Dosage effects in non-cancer cells are similar to cancer cells except chr X (inactivation buffers dosage). Patient-specific gains in endothelial cells and fibroblasts suggest clonal selection.

## Limitations

- Preprint (not peer-reviewed at time of reading; March 2026).
- 57 patients; cancer-type-specific analyses are underpowered for rare events (e.g., AML n=5, MEL n=6).
- Ultra-low coverage scWGS: may miss sub-megabase focal CNVs; small structural variants and SNVs within subclones are not reliably detected, leaving some transcriptional variability unexplained (acknowledged by authors).
- Transient clonality: causal mechanism (WGD + LOH → ongoing missegregation) is proposed but not directly demonstrated; TP53 mutation consistent with but not sufficient for the phenotype.
- No explicit modelling of selection pressure on dosage; the paper describes dosage effects but does not estimate fitness consequences of specific CNV classes.
- FOHAS/ecDNA distinction is not addressed; whether any FOHAS are circular extrachromosomal DNA is not tested.
- Compensated gene categories are defined categorically; quantitative thresholds for "compensated" vs. "sensitive" are not described in the main text sections read.
- Non-cancer cell analysis is exploratory; larger targeted studies needed (authors acknowledge).
