---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Schmidt2024
kind: paper
title: Polyploid cancer cells reveal signatures of chemotherapy resistance
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Schmidt2024
tags: []
ontology_terms:
- EMT
- PI3K-AKT-mTOR signaling
- cell state change
- chemotherapy resistance
- circulating tumor cells
- non-genetic adaptation
- polyploidy
- transcriptional convergence
- whole-genome doubling
dataset_usage:
- ref: dataset:gse270567
  role: analyzed
  overlap: unknown
- ref: dataset:gse270568
  role: analyzed
  overlap: unknown
- ref: dataset:nct01505868
  role: analyzed
  overlap: unknown
---
## Key Findings

### CTC-IGC in patients
- CTC-IGC found in 9.7% of peripheral blood but **80.6% of matched bone marrow samples**; presence of ≥1 CTC-IGC in bone marrow associated with significantly worse PFS (p = 0.0095, Fig. 1C).
- Copy number concordance confirms CTC-IGC are tumor-derived (clonal origins with typical CTCs); copy number ratios are indistinguishable from normal-ploidy CTCs, consistent with complete WGD rather than focal amplifications.

### Chemotherapy-induced polyploidy is a cell-state shift, not a genomic event
- Surviving polyploid PC3 and MDA-MB-231 cells at 10 DPT show **no statistically significant copy number ratio differences** vs. DMSO controls — WGD without new focal alterations (Figs. 3A–C, S4B, S7, Table S3).
- FISH for centromeres of Chr1 (ploidy = 3) and Chr10 (ploidy = 1) in PC3 showed no significant differences between DMSO controls and progeny-1, arguing against ploidy reduction scarring.
- ~50% of surviving polyploid cells remain non-proliferative (endocycling/cytokinesis failure, protected from therapeutic stressors); this non-proliferative state is associated with ZNF697 and NPAS2 upregulation.

### Convergent transcriptional survival signature
- 1,591 genes upregulated in MDA-MB-231 at 10 DPT, 1,178 in PC3 at 10 DPT (LFC > 1.5, FDR < 0.01 vs. DMSO); intersection across both cell lines and both drug classes yields **309 shared survivor genes** (77% protein-coding, 17% lncRNA).
- Top enriched hallmark pathways in the 309-gene set: **EMT, KRAS Up, Coagulation, TNFα via NFkB, Hypoxia** (Fig. 4G); PI3K-AKT-mTOR and cholesterol homeostasis also enriched at single-cell level (Fig. 4H).
- Two significantly enriched transcription factors in survivors: **ZNF697 and NPAS2** — both previously linked to senescence exit and re-entry into a proliferative state.

### Novel protein survival markers: HOMER1, TNFRSF9, LRP1
- All three upregulated at RNA and protein level in survivors across both cell lines/drugs; retained in docetaxel-treated PC3 progeny-1.
- Mechanism sketched: TNFRSF9 and LRP1 act as surface receptors enhancing PI3K activity → AKT → pro-survival; HOMER1 functions in mTOR signaling and apoptosis protection.
- Patient validation: HOMER1, TNFRSF9, and LRP1 protein-positive CTCs detectable in bone marrow aspirates of 5 late-stage prostate patients (Fig. 6A–B); Patient 5 (shortest PFS = 1.4 months) had the highest percentage of TNFRSF9-positive CTCs.
- Public RNA data: high TNFRSF9 expression → shorter PFS in prostate (p = 4.3e-02) and worse RFS in breast (p = 3.88e-03); high LRP1 → shorter BCR-free survival in prostate (p = 3.68e-04) and worse RFS in breast (p = 7.09e-04); HOMER1 significant in breast (p = 7.16e-04) but not prostate (p = 0.183).

### Progeny viability and phenotype
- Of 480 single-cell-seeded PC3 polyploid cells (docetaxel), **only 1/480 gave rise to a proliferative clone** (progeny-1) after ~3 months; a second progeny clone (progeny-2) arose from cisplatin at 2.5 months but failed after first passage.
- Progeny-1 transcriptome closely resembles the large polyploid cells rather than the parental population; progeny-1 cells show higher nuclear/cellular diameter than parental PC3 and are sensitive to both cisplatin and docetaxel re-challenge.
- Progeny-2 displayed the most aberrant copy number profile (6p and 4p gains) and clustered separately — hinting at genomic evolution possible in long-lived polyploid descendants.

## Limitations

- In vitro model cannot recapitulate the in vivo tumor microenvironment; CTC-IGC interaction with neighboring stroma and immune cells is untested.
- Patient cohort (n = 44 bone marrow samples; n = 6 for marker staining) is small and biased toward late-stage, previously-treated patients — enriching for the very phenotype under study and limiting generalizability to early treatment contexts.
- The 309 shared survivor genes were identified from two cell lines (PC3, MDA-MB-231); cross-cancer-type validation of the convergent signature is absent.
- Extremely low progeny-formation rate (1/480) was studied in a single clone; conclusions about polyploid progeny biology rest on n = 1 proliferating clone plus one failed clone.
- Genomic evolution in progeny is noted (3p gain in progeny-1, 6p/4p gains in progeny-2) but not systematically characterized; whether polyploid persistence eventually channels into mutational adaptation is unresolved.
- Survival analysis for HOMER1 was not significant in prostate cancer (p = 0.183), limiting its generalizability as a pan-cancer marker.
