---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Fortin2024
kind: paper
title: Circadian Control of Tumor Immunosuppression Affects Efficacy of Immune Checkpoint
  Blockade
version: 1.0.0
created: '2026-05-30'
updated: '2026-05-30'
bibkey: Fortin2024
tags: []
ontology_terms:
- chronomedicine
- circadian-clock
- colorectal-cancer
- immune-checkpoint-blockade
- myeloid-derived-suppressor-cells
- tumor-immunosuppression
---
## Key Findings

### 1. Clock disruption remodels the intestinal immune landscape

scRNA-seq at ZT 4 identified distinct myeloid and lymphoid populations. Relative to WT, *Bmal1−/−*, *Apc+/−*, and *Apc+/−;Bmal1−/−* mice all showed increased proportions of neutrophils and decreased proportions of CD8+ T cells. The most striking effect was a ~5-fold increase in intestinal neutrophils in clock-disrupted mice versus respective controls — seen in both tumor-bearing and non-tumor-bearing settings. Environmental shift disruption replicated the genetic finding: neutrophil proportions rose significantly after only 3 weeks of shift exposure, preceding the CD8+ T cell decline (which required 5 weeks), suggesting neutrophils are the primary cell type initially altered.

### 2. Clock disruption accumulates immunosuppressive MDSCs

A scRNA-seq cluster of myeloid cells highly expressing *Iftm1*, *Wfdc17*, *S100a8*, *S100a9*, *Irg1*, and *Arg2* was identified as an MDSC signature, enriched by both clock disruption and cancer. Flow cytometry confirmed that Gr1+ (CD11b+Gr1+) cells were significantly increased in *Bmal1−/−* and *Apc+/−;Bmal1−/−* intestines and spleens. These cells:
- Produced elevated ROS (H2DCFDA assay).
- Had a higher proportion of PD-L1+ cells.
- Expressed elevated immunosuppressive genes (*S100a8*, *S100a9*, *Wfdc17*).
- Functionally suppressed T cell proliferation in co-culture.

### 3. Epithelial clock disruption drives MDSC development via Wnt/c-Myc/cytokine axis

*Bmal1−/−* intestinal monolayers and organoids treated with Wnt3a showed hyperactivation of the Wnt-target genes *c-Myc* and *Survivin* versus WT. *Cxcl5* was strongly upregulated in a Wnt-dependent, clock-dependent manner (over 100-fold induction in MEF model). A 32-plex cytokine array identified:
- **Clock-dependent only:** IL-5, CCL5, IL-17, CXCL9 — upregulated in *Bmal1−/−* monolayers regardless of Wnt.
- **Wnt-dependent only:** CXCL1, M-CSF, G-CSF, GM-CSF, CCL2, IL-2, VEGF, TNFα, IFNγ.
- **Both clock and Wnt:** CXCL5, CXCL6, CXCL2.

Conditioned medium from *Bmal1−/−* monolayers (not WT) drove naïve bone-marrow-derived neutrophils to upregulate MDSC-signature genes (*s100a8*, *s100a9*, *Wfdc17*, *Arg2*) and significantly increased neutrophil migration in a transwell assay. MYC knockdown in WT monolayers downregulated *Cxcl5*, implicating MYC as a transcriptional mediator.

### 4. PD-L1+ MDSCs peak rhythmically at ZT 16 (early active phase)

In WT mice (intact circadian clock everywhere), Gr1+ and Gr1+PD-L1+ cells were significantly more abundant in the intestine at ZT 16 vs. ZT 4. This rhythmicity was **lost** in the intestine of *Apc+/−;Bmal1−/−* mice (epithelial clock disrupted) but **retained** in the spleen (where the clock remains intact). In the spleen, both WT and *Apc+/−;Bmal1−/−* showed the ZT 16 peak, confirming the intestinal epithelial clock as the local driver of rhythmic MDSC gating. PD-L1 was highly expressed by myeloid/neutrophil clusters in both the mouse scRNA-seq data and in reanalysis of 36 human CRC patient samples, where PD-L1+ myeloid cells were highly abundant in tumor vs. normal colon.

### 5. ZT 16 anti-PD-L1 dosing outperforms ZT 4 in three cancer models

In *Apc+/−;Bmal1−/−* GEMM mice:
- ZT 16 anti-PD-L1 significantly reduced intestinal Gr1+ MDSCs and increased CD8+ T cells vs. ZT 4.
- ZT 16 treatment (but not ZT 4) increased spleen weight, indicating inflammatory anti-tumor response.
- Polyp size was significantly reduced by ZT 16 treatment; polyp count was not significantly changed after 3 weeks.

In subcutaneous syngeneic models treated 4 times:
- **MC38 (CRC):** ZT 16 CR rate 30% (4/14) vs. ZT 4 CR rate 8% (1/12); ZT 4 PD rate 50% (6/12) vs. ZT 16 PD rate 29% (4/14).
- **CMT167 (lung):** ZT 16 (but not ZT 4) significantly reduced tumor volume.
- **D4M-S (melanoma):** ZT 16 more effective than ZT 4 at reducing tumor growth.

## Limitations

- All mechanistic work is in mouse models (C57BL/6, 9–10 months, both sexes). The temporal architecture of MDSC cycling in humans (active/rest phase equivalents, ZT mapping) is not established.
- The ICI timing experiments use the *Bmal1−/−* epithelial clock-disruption GEMM, which is a non-physiological model (permanent clock loss). Whether intact-clock tumor-bearing mice show the same ZT 16 advantage is implied by the rhythmic MDSC data in WT mice but not tested with ICI treatment.
- Statistical analyses were not blinded; normality was assumed but not formally tested.
- The scRNA-seq was performed only at ZT 4 — the time-course of immune landscape changes across the full circadian cycle is not captured.
- Mouse Zeitgeber time does not directly translate to human clock time; the ZT 16 "early active phase" in nocturnal mice corresponds roughly to early morning in diurnal humans, but the human-equivalent optimal ICI dosing window is not determined.
- Sample sizes in the subcutaneous ICI experiments are small (n = 12–14/group); the CR/PD rates should be interpreted cautiously.
- The 32-plex cytokine data are from in vitro monolayer and organoid cultures, which may not fully recapitulate the in vivo epithelial secretome.
- Sex as a variable is noted (both sexes used) but no sex-stratified analysis is reported.
