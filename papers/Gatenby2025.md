---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Gatenby2025
type: paper
title: Parallel and convergent dynamics in the evolution of primary breast and lung adenocarcinomas
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Gatenby2025
tags: []
datasets:
- dataset:tcga
ontology_terms:
- TCGA
- carcinogenesis
- convergent evolution
- evolutionary triage
- niche construction
- parallel evolution
- phenotypic plasticity
---
## Key Findings

### Baseline differences (parallel but divergent early adaptations)

- LUAD has far more mutations (avg. 273/tumour) than BRCA (avg. 34/tumour).
- Only 2 genes mutated in >10% of BRCA (TP53, PIK3CA) vs. 166 in LUAD.
- LUAD has significantly more evolution-selected mutations (343 vs. 93) and more conserved genes (260 vs. 130); only HTT conserved in both.
- BRCA has more genes with ≥4-fold increased expression (963 vs. 558) and only slightly fewer with ≥75% decreased expression (822 vs. 914).
- Genes expressed in cancer but not in normal tissue: 273 (BRCA) vs. 111 (LUAD); "unlocked restricted genomic regions."

### Convergence signal — 150 most highly expressed genes

- In normal breast vs. normal lung: 75/150 top-expressed genes are shared (baseline similarity).
- In BRCA vs. LUAD: 100/150 top-expressed genes are shared (χ² = 8.57, df = 1, p < 0.005). Cancer transcriptomes are more similar to each other than the normal tissues they arose from.

### Parallel evolution — tissue-specific losses

- BRCA turns off 108 genes highly expressed in normal breast; LUAD turns off 32 expressed in normal lung. Only 7 in common — loss of tissue-specific differentiated function is parallel (same class, different genes).
- BRCA and LUAD downregulate tissue-specific signalling: BRCA loses 44 developmental genes (steroid metabolism, androgen/estrogen biosynthesis, adipogenesis); LUAD loses 43 (cilia, complement, surfactant, O2 exchange). Zero overlap between the two sets.

### Convergent evolution — shared gains

**Cell cycle and proliferation machinery (Table 2):** Both cancers upregulate the same 67 cell cycle genes (p = 8.9e-42), 58 mitotic genes (p = 1.9e-36), 39 checkpoint genes, 23 sister-chromatid-separation genes, 17 DNA repair genes, 15 meiosis-associated genes, 17 DNA repair genes. Highly significant shared upregulation of PLK1, Aurora A/B, FOXM1, E2F, RNA Pol II networks.

**Alternative signalling:** 51 shared signal transduction genes; MAPK/EGFR/RAS pathway convergence (R² normal: 0.33 → R² cancer: 0.84 for EGFR pathway). G protein-coupled receptors converge (R² 0.60 → 0.81). Both upregulate 10 C-MYC targets, 7 p53 pathway genes, 12 FOXM1 members, 7 p73 members.

**Niche construction — ECM and angiogenesis:** 19 (BRCA) and 12 (LUAD) ECM-related genes among the 150 most highly expressed; 8 collagen genes shared in BRCA, 6 in LUAD, 5 in common. Collagen and ADAM gene family expression converges strongly in cancers (ADAM R² 0.66 → 0.82). Both upregulate VEGFA (10–20% increased), decrease ANGPT1/2/4 and TEK; converge on angiogenic niche strategy.

**Ion channels:** Both cancers demonstrate strong genetic/epigenetic selection on voltage-gated ion channels. Na⁺ voltage-gated channels: R² near 0 in normal tissues → 0.79 in cancers. Potassium calcium-activated: R² 0.68 → 0.90. Potassium voltage-gated interacting: R² 0.02 → 0.89. Convergence interpreted as reduction of transmembrane potential to promote proliferation and pluripotency signals while decreasing differentiation function.

**Phenotypic plasticity — accessing restricted genomic regions:** Both BRCA and LUAD activate genes not expressed in normal tissue (273 and 111 respectively; 27 in common including TERT, LIN28B, CDH18, CSAG1, 10 MAGE family members). Framed as "unlocking" of normally epigenetically silenced genomic regions. 7 of the 27 shared genes are associated with pluripotency (TP53, AKT1, KRAS, TBX3, PIK3CA, PIK3R1, GATA3); 4 of these show ≥ 8-fold increased expression in BRCA.

**Tumour-to-host signalling:** Both cancers increase NMU expression but decrease NMUR1 — a co-option strategy to manipulate host cells. Both upregulate CA9 (32–64-fold) to buffer acidic niche conditions (convergent acid-adaptation strategy).

### Level of convergence — multi-level summary

| Level | Evidence for convergence | Strength |
|---|---|---|
| Driver mutation / specific gene | Minimal — only HTT conserved in both; TP53/PIK3CA are most-mutated in BRCA but not LUAD | Weak |
| Pathway / functional category | Strong — same GO pathways upregulated: cell cycle, MAPK, ECM, ion channels, pluripotency | Strong |
| Transcriptional state (expression level) | Strong — top-150 expressed gene overlap increases from 75 to 100; regression R² improves across gene families in cancers vs. normal tissues | Strong |
| Specific gene within shared pathway | Moderate — within VEGF, Cadherin, ADAM, Claudin families, same members upregulated; within MAPK, same EGF/EGFR/KRAS/RRAS members converge | Moderate–strong |

**Conclusion: convergence is primarily at pathway and transcriptional-state levels, not at the individual-driver-mutation level.** This is an important distinction for downstream inference — the paper does not claim that the same driver mutations recur in both cancers (the opposite: specific drivers diverge). It claims that the same functional outcomes (signalling independence, proliferation, niche construction, plasticity) are achieved through tissue-specific molecular routes that then converge on a common transcriptional phenotype.

## Limitations

1. **Bulk cohort-average analysis:** All expression and mutation signals are cohort averages, not single-cell or even individual-patient trajectories. Convergence at the cohort average level does not imply individual tumours converge — within-tumour heterogeneity and divergent subclonal trajectories are invisible here.

2. **LUAD cohort restriction:** Excluding EGFR, KRAS, BRAF driver mutations was intentional (to select the high-mutation, smoking-associated LUAD subtype) but means the findings do not generalise to the ~40% of LUAD with these drivers. The "convergence" claim therefore applies to a specific LUAD subtype with an unusually high mutation burden, not LUAD as a whole.

3. **Temporal/stage confound:** TCGA primary tumours represent a snapshot at diagnosis, which conflates early and late evolutionary stages within the same cohort. The paper's proposed two-phase model (parallel then convergent) is cross-sectional inference about a temporal process, not a longitudinal demonstration.

4. **No single-mutation-level driver convergence:** The paper acknowledges that specific driver mutations do not converge — only HTT is conserved in both. The "convergence" finding is pathway/transcriptional-state level. This is important because it means genomic convergence (e.g., TP53 mutation rate) does not predict the specific transcriptional convergence observed.

5. **Negative Storage Model IP restriction:** The core mutation analysis tool is under patent protection at Moffitt (a competing interest is declared). Independent reproduction of the mutation scoring is not straightforwardly possible from the paper alone.

6. **No validation cohort:** All findings are from TCGA; no independent cohort validation of the convergence signal is presented.

7. **Circular phenotypic plasticity framing:** The evidence that plasticity is a "selected trait" (activation of TERT, LIN28B, MAGE genes) is derived from the same expression data used to show convergence — the inference that these expression changes reflect selection for plasticity capacity (rather than selection for specific fitness consequences) is interpretive, not independently validated.
