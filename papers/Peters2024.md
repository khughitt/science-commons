---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Peters2024
type: paper
title: Tissue-Predisposition to Cancer Driver Mutations
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Peters2024
tags: []
datasets: []
ontology_terms:
- cancer driver mutation
- chromatin organization
- developmental origins of cancer
- epigenetic landscape
- paralogue paradox
- replication timing
- synthetic lethality
- tissue-specific selection
- transposable elements
---
## Key Findings

### 1. Epigenetic landscape encodes tissue-specific mutation rate geography

Cell-type-specific chromatin states (H3K9me3-marked closed chromatin vs. H3K4me1/H3K27ac-marked open chromatin) impose non-uniform mutation rates genome-wide. H3K9me3-dense regions have elevated mutation rates; open, actively transcribed chromatin benefits from transcription-coupled DNA repair (TCR) and shows lower rates. Importantly, the epigenetic profile of the *cell of origin* (not the cancer cell) predicts the regional mutation rate in the cognate cancer — an algorithm built on this principle can predict the cancer cell of origin from the mutational landscape (Polak et al. 2015, referenced as ref. 17). Metaplastic cells (e.g., in Barrett's esophagus) are better predictors of esophageal cancer mutational patterns than non-metaplastic cells in the same tissue, suggesting that the premalignant epigenetic state locks in mutational geography.

### 2. Gene expression is a weak but pathway-level expression is a strong predictor

Individual gene expression in normal cells is a weak predictor of tissue-specific driver mutations; however, expression of entire pathways acting within the normal cell is a stronger predictor. The direction of the association is often *negative* — highly expressed genes accumulate fewer mutations because TCR protects them. This underscores that function in the cell of origin (which pathway is operative and depends on a given gene), not raw expression, guides which mutations are selectively propagated.

### 3. The "paralogue paradox" reveals locus-level regulatory determinism

KRAS and HRAS encode functionally redundant proteins; yet KRAS is the predominant RAS mutation in NSCLC while HRAS predominates in skin cancer. A knock-in experiment (To et al. 2008, ref. 45) replacing the KRAS locus with wild-type HRAS showed that HRAS codon-61 mutations occurred specifically when expressed from the KRAS locus, and never from the native HRAS locus. The tissue-specific bias between paralogues is therefore driven by gene-regulatory elements at the locus, not by inherent protein differences. This mechanism extends to mutual exclusivity patterns: KRAS and EGFR are mutually exclusive in lung adenocarcinoma, PTEN and PIK3CA in sarcoma, reflecting synthetic-lethal co-dependencies rather than redundancy per se.

### 4. Synthetic lethality as a tissue-specific selection filter

If tissue A highly expresses gene X, and mutation in gene Y is synthetic lethal with X, then Y mutations will be counter-selected in tissue A but propagated in tissue B (which lacks X expression). The BRCA1/GSTM5 axis illustrates this: ovarian and breast tissues express GSTM5 at high levels; liver and kidney do not. GSTM5 expression creates a synthetic-lethal relationship that *positively selects* BRCA1 mutations in tissues where GSTM5 is expressed — making synthetic lethality not merely a therapeutic concept but a mechanistic explanation for tissue-biased driver frequencies.

### 5. Tissue-specific senescence wiring shapes driver selection

Oncogene-induced senescence (OIS) is not uniform: the p53/p21 and p16/Rb pathways are major routes, but their downstream wiring is cell-type-specific. CK1α deletion in the intestine induces a senescence-associated inflammatory response (SIR) that is protumorigenic but distinct from the canonical senescence-associated secretory phenotype (SASP). BRCA1 haploinsufficiency in mammary epithelial cells triggers premature senescence via a Rb-acetylation/SIRT1 axis (independent of p53/p16), but not in mammary fibroblasts. Because senescence barriers vary by cell type, the specific tumor-suppressor deletions required to bypass them also vary — determining which TSG mutations are selected.

### 6. LINE-1 transposable elements as tissue-specific endogenous mutagens and OIS triggers

LINE-1 (L1) retrotransposons are expressed in a cell-type-specific manner (chromatin accessibility at TE loci predicts cell type; ref. 64). Re-expression of retrotransposition-competent LINE-1 in cancer is a common but variable feature across cancer types. Tissues that re-express LINE-1 face a DDR (DNA damage response) burden mediated through p53, creating selective pressure to inactivate TP53. ORF1p expression (a LINE-1 protein) correlates positively with TP53 mutation frequency across cancer types (Figure 4A), and TP53 inactivation is the most common event in esophageal cancer (approximately 65%), which also shows high ORF1p in Barrett's esophagus. In ovarian cancer, LINE-1-driven genomic instability may additionally select for BRCA1/2 mutations. Thus, LINE-1 acts as both an endogenous tissue-specific mutagen and a tissue-specific OIS enforcer — in tissues where it is expressed, mutations in its sentinels (TP53, BRCA1/2) are specifically selected.

### 7. Replication timing dynamics as a tissue-specific mutation-rate modulator

Late-replicating genomic regions accumulate more mutations (reduced nucleotide pool, single-stranded DNA susceptibility, less-effective MMR). Replication timing is cell-type-specific: the same genomic region may replicate early in one cell type and late in another, creating tissue-specific mutation rate topographies. Furthermore, the mutational *processes* active during late replication are also cell-type-specific: in CLL lines, late-replication mutations are dominated by Pol η defects; in CRC lines, by MMR defects. Crucially, this mutational-process bias is conserved between normal cells and their cancerous counterparts — establishing that early tissue-specific driver mutations can arise as a direct consequence of replication-timing dynamics inherited from the cell of origin.

### 8. Developmental pathway reactivation specifies context-dependent driver effects

Developmental pathways (Notch, Wnt/β-catenin, Hedgehog, BMP/TGF-β) are interpreted differently by different cell lineages. Notch suppresses differentiation in hematopoietic progenitors (leading to T-ALL when constitutively active) but promotes terminal differentiation in other contexts (acting as tumor suppressor). APC loss hijacks Wnt signaling specifically in colon stem cells, not in hematopoietic stem cells, because the intestinal stem-cell niche depends on paracrine Wnt ligand proximity (Paneth cell niche). The KRAS-driven EGFR/SOX9 axis is selectively reactivated in pancreatic acinar cells to drive PDAC; the same KRAS^G12D cannot induce biliary intraepithelial neoplasia (BiIIN) in bile duct — where PI3K^H1047R can. This illustrates that different oncogenic signals command entirely different tissue responses depending on which developmental state-space is accessible.

## Limitations

- As a review, the mechanistic axes are proposed as a framework; no single analysis establishes their relative contribution or whether all five operate simultaneously in any given cancer type.
- The review does not address how the five mechanisms interact or are ranked in importance — it treats them as a "network" but provides no quantitative integration.
- Mutation-frequency data shown (Figure 1) are drawn from cBioPortal without specifying dataset versions, sample sizes, or covariate adjustments — the frequency comparisons are illustrative rather than statistically rigorous.
- The LINE-1/TP53 correlation (Figure 4A) is correlative; causality (LINE-1 expression driving TP53 selection) vs. confounding by cancer type is not formally tested in the cited data.
- The review focuses on intrinsic tissue features; extrinsic factors (UV light for skin, H. pylori for gastric) are acknowledged only briefly and are not integrated into the mechanistic framework.
- The developmental-origins sections (Notch, Wnt) discuss specific cancer types in depth (PDAC, T-ALL, CRC) but the generalization to the full spectrum of cancer types is asserted rather than demonstrated.
- All claims in the "Key Findings" section are from the review's synthesis and may compress or simplify the original studies cited. Key primary findings (Polak 2015, To 2008, Falcomata 2021, Caballero 2023) should be consulted for quantitative details.
