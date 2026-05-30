---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Sheehan2025
type: paper
title: A glial circadian gene expression atlas reveals cell-type and disease-specific reprogramming in response to amyloid pathology or aging
version: "1.0.0"
created: "2026-05-30"
updated: "2026-05-30"
bibkey: Sheehan2025
tags: []
datasets: []
ontology_terms:
- alzheimers-disease
- circadian-rhythm
- glial-biology
- neurodegeneration
- transcriptomics
---
## Key Findings

### Glial circadian translatomes are highly cell-type-specific

In wild-type (WT) young mice, astrocytes and microglia each have large, distinct rhythmic transcriptomes. These overlap minimally with bulk cortex circadian profiles, confirming that bulk-tissue approaches miss most cell-type-specific circadian biology.

### Amyloid pathology causes bidirectional circadian reprogramming

**Bulk cortex.** In APP/PS1 versus WT cortex, 2,563 transcripts rhythmic in WT lost rhythmicity; 591 gained rhythmicity. Core clock genes (*Per2*, *Arntl/Bmal1*, *Ciart*) remained robustly rhythmic. Genes losing rhythmicity included the cellular senescence marker *Cdkn1a* and glutathione-S-transferase *Gstt2*. Genes gaining rhythmicity included inflammatory mediators *Nfkbia* and *Ccl4*. Lysosome and autophagy pathway rhythms were enriched in WT but not APP cortex; NF-kB and hormone synthesis pathways were enriched in APP cortex. Seven rhythmic genes changed phase in APP/PS1.

**Astrocytes.** Core clock preserved in APP astrocytes. In WT astrocytes 999 transcripts were rhythmic; 980 transcripts gained rhythmicity in APP astrocytes (roughly equal gain and loss, unlike the net loss in bulk cortex and microglia). Metabolic and insulin-signaling pathway rhythms lost in APP astrocytes; FoxO, Notch, PI3K-Akt, TNF signaling pathways gained rhythmicity. Several AD GWAS genes (*Clu*, *Picalm*, *Chi3l1*) gained rhythmic expression in APP astrocytes; *Srebf1* (lipid synthesis regulator) lost rhythmicity.

**Microglia.** The largest effect: 5,132 rhythmic transcripts in WT microglia fell to 2,267 in APP/PS1 microglia (only 1,008 overlapping). AD- and neurodegeneration-related KEGG pathways (Huntington, Parkinson, AD, prion disease, ALS), along with OXPHOS, lysosome, and proteasome pathways, were enriched for rhythmicity specifically in WT microglia but not APP microglia. PI3K-Akt signaling and ferroptosis pathways gained rhythmicity in APP microglia. The canonical homeostatic microglial markers *Tmem119*, *P2ry12*, and *Csf1r* gained rhythmic expression in APP/PS1. Disease-associated microglia (DAM) genes oscillated in WT but dampened in APP. Microglial *Iba1*-encoding gene *Aif1* was rhythmic in WT but not APP microglia.

**GWAS gene rhythmicity.** Nearly half of 85 AD GWAS genes were rhythmic in WT microglia; many lost rhythmicity in APP microglia.

**OXPHOS rhythms conserved in mice and humans.** The OXPHOS pathway was enriched for cycling genes in WT microglia (BH.q = 5.6 × 10^−6). In the ROSMAP human snRNA-seq dataset, the OXPHOS pathway was strongly enriched for rhythmic transcripts in control microglia (*P* < 2.3 × 10^−5) but not AD microglia (*P* = 0.345), confirming cross-species conservation and disease disruption.

### Microglial circadian ROS production and phagocytosis show functional rhythms

Primary microglia synchronized with forskolin showed significantly higher ROS (CellROX fluorescence) at CT24 versus CT12 (*P* < 0.0001, two-tailed *t*-test). In vivo, microglia phagocytosed more amyloid plaque material in the evening (ZT12) than the morning (ZT0) in 5-month-old APP^swe/PS1^dE9 mice (methoxy-X04+ microglia: ~4% vs ~2%; *P* = 0.0262, one-tailed *t*-test). The TAM phagocytosis receptor *Mertk* was highly rhythmic in both WT and APP microglia, and lysosomal transcripts (*Lamp1*, *Ctsl*, *Cd68*) peak in the evening, suggesting temporal regulation of microglial proteostasis and amyloid clearance.

### Aging uniquely and distinctly reprograms glial circadian biology

**Aged astrocytes (22 months).** Core clock maintained. Rhythmic pathways in aged astrocytes differed substantially from both WT and APP astrocytes; endocytosis, autophagy, and mTOR pathways gained rhythmicity uniquely in aged astrocytes. Autophagy genes *Atg10*, *Pdpk1*, *Ulk1*, and *Mtor* were rhythmic only in aged astrocytes, suggesting clock-regulated induction of autophagy as an aging response.

**Aged microglia (22 months).** Dramatic blunting of core clock amplitude: *Arntl*, *Nr1d1*, *Per2*, and *Ciart* had markedly dampened amplitude (but *Ciart* remained statistically rhythmic). The metabolic pathway that was prominent in WT and APP microglia was absent from rhythmic transcripts in aged microglia (possibly replaced by TCA cycle / AMPK compensation). Endosomal trafficking gene *Rab5c* and proteasome subunit *Psmd11* gained rhythmicity in aged microglia. Lipid metabolism genes *Ldlr* and *Mafg* lost rhythmicity. Apoptosis and TCA cycle pathways were significantly enriched in aged microglia rhythmic transcripts.

**Context-dependence of reprogramming.** Aged astrocyte rhythmic transcripts had little overlap with APP/PS1 astrocyte rhythmic transcripts, and aged microglia rhythmic transcripts differed from both WT and APP/PS1 microglia patterns — establishing that aging and amyloid produce mechanistically distinct circadian reprogramming.

### Time-of-day strongly confounds AD differential gene expression

In APP/PS1 versus WT microglia, 506 DEGs were identified in AM tissue and 627 DEGs in PM tissue; only ~20% overlap between the two time windows. More than 25% of identified DEGs were significant only at one time of day. Key genes — including *Ldlr*, *Aim2*, *Cd209a*, *Cx3cr1*, *Spi1*, *Ighm*, *Ccl9*, *Ly96*, and GWAS genes *Spi1* and *Ighm* — were only differentially expressed in one time window. Similar pattern in astrocytes: 406 DEGs in AM, 438 in PM; >25% unique to one time bin. This finding directly implies that combining transcriptomic data collected at different circadian phases will introduce substantial noise or obscure true disease signals.

## Limitations

1. **Mouse model only for primary data.** APP/PS1 is an amyloid overexpression model; it does not capture tau pathology or late-stage neurodegeneration. Whether findings translate to human AD is only partially tested (ROSMAP OXPHOS replication is a single pathway, and CYCLOPS phase inference introduces noise).

2. **4-h resolution for aged mice.** Aging experiments used every-4-h sampling (vs every-2-h for young mice); authors note this may reduce sensitivity to detect rhythmic transcripts. Comparison of gain/loss statistics across age groups should be interpreted cautiously.

3. **Two biological replicates per time point (young mice).** While in silico validation demonstrates 89% sensitivity, this remains a low-replicate design; false-negative rate for low-amplitude oscillators is non-trivial.

4. **Ribosome-associated (translating) mRNA, not steady-state transcriptome.** Data more closely approximate the translatome (actively translated mRNA) than the pure transcriptome; correlation with the proteome may be imperfect.

5. **Relative cell-type abundance shifts with pathology.** Changes in relative DAM/homeostatic microglia subcluster proportions over the circadian cycle could mimic or obscure rhythmicity detection — authors acknowledge this limitation.

6. **Single sex per time point (one male, one female).** Designed to avoid sex-specific circadian confounds but limits power to detect sex differences in circadian reprogramming.

7. **Mouse circadian conventions.** Results are in circadian time (CT) under constant dark; direct translation to Zeitgeber time (ZT) or human clock time requires care.
