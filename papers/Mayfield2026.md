---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Mayfield2026
type: paper
title: Gene coordination patterns across 8,314 tumors reveal a spectral point of no return in cancer progression
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Mayfield2026
tags: []
datasets:
- dataset:mlomics
- dataset:tcga
ontology_terms:
- Hamiltonian eigendecomposition
- gene-gene coordination
- immune polarization
- metabolic dedifferentiation
- monopolar coordination
- pan-cancer transcriptomics
- phase transition
- spectral analysis
- survival prediction
- tissue-identity dissolution
---
## Key Findings

### Monopolar pan-cancer architecture
- Dominant eigenvalue λ₁ = 1,844.8 is 12.6-fold larger than λ₂ = 146.9.
- Spectral concentration c = 0.71: 71% of all gene–gene coordination across 8,314 tumors is captured by a single coordination program.
- Spectral gap Δλ = 1,697.8; critical temperature T* = 1/Δλ identifies the phase boundary.
- In statistical-mechanics terms, the pan-cancer transcriptome is deep in its ordered phase — the ground state (dominant mode) absorbs nearly all Boltzmann weight at T < T*.
- The dominant mode (mode 1) recovers tissue-of-origin identity (C-index ≈ tissue classifier performance); it is biologically interpretable as the global tissue-identity program that cancer globally preserves but partially erodes.

### Three survival-associated secondary modes
Modes 3, 15, and 20 had C-index > 0.58 in the pan-cancer screen (top 30 modes evaluated):

**Mode 3 — Metabolic dedifferentiation** (λ = 53.0, C-index = 0.630):
- Positive pole (better survival): estrogen response (NES = +2.19, FDR < 0.001), tight junctions (NES = +1.98, FDR = 0.038), adipogenesis (NES = +1.74, FDR = 0.023); top genes CLDN3, C2orf40, TMC4.
- Negative pole (worse survival): cytochrome P450 drug metabolism (NES = −2.21), xenobiotic metabolism (NES = −2.21), steroid hormone biosynthesis (NES = −2.19), cholesterol metabolism (NES = −2.01); top genes KIF18B, KIF14, AURKB (mitotic kinases).
- Captures the differentiation ↔ metabolic-reprogramming axis; recapitulates ClearCode34 (KIRC) and proneural–mesenchymal (GBM) axes.

**Mode 15 — Immune polarization** (λ = 9.4, C-index = 0.595):
- Negative pole (better survival): IFN-γ response (NES = −2.02, FDR = 0.002), allograft rejection (NES = −2.37, FDR < 0.001); genes CXCL9, CD8B, CD79A, ADAMDEC1. Adaptive/cytotoxic immunity.
- Positive pole (worse survival): IL-17 signaling (NES = +2.02, FDR = 0.012), TNF-α/NF-κB (NES = +1.91), EMT (NES = +1.97, FDR = 0.003); genes FOSL1, EREG, TREM1. Innate inflammatory programs.
- Directly separates checkpoint-blockade candidates (adaptive pole) from innate-inflammation-enriched tumors.

**Mode 20 — Tissue-identity dissolution** (λ = 6.3, C-index = 0.580):
- Positive pole: complement (NES = +1.73), inflammatory response (NES = +1.59), IL-6/JAK/STAT3 (NES = +1.51); genes SLC4A1, ATP6V0A4, CLCNKB, CYP11A1, KLK1 (renal proximal tubule transporters/enzymes).
- Captures whether the tumor retains or has dissolved its tissue-specific functional program; strongest in KIRC (C-index = 0.649) where coordinated loss of proximal-tubule-identity genes drives outcome.

### Spectral malignancy coordinate η predicts survival
- Pan-cancer: Q1 vs. Q5 quintile log-rank p = 6.9 × 10⁻³² (n = 8,262; 2,278 events).
- Significant in 11 of 30 evaluable cancer types (p < 0.05):

| Cancer | n | C-index | AUC | p |
|---|---|---|---|---|
| Glioblastoma (GBM) | 76 | 0.845 | 0.906 | 1.8 × 10⁻⁶ |
| Prostate adenocarcinoma (PRAD) | 91 | 0.800 | 0.876 | 8.9 × 10⁻³ |
| Kidney clear cell (KIRC) | 505 | 0.649 | 0.700 | 7.4 × 10⁻⁵ |
| Uterine endometrial (UCEC) | 80 | 0.634 | 0.681 | 9.0 × 10⁻³ |
| Lung SCC (LUSC) | 86 | 0.618 | 0.655 | 2.3 × 10⁻² |
| Rectal adenocarcinoma (READ) | 250 | 0.606 | 0.607 | 1.5 × 10⁻² |
| Bladder urothelial (BLCA) | 291 | 0.581 | 0.570 | 2.9 × 10⁻² |
| Colon adenocarcinoma (COAD) | 505 | 0.570 | 0.588 | 2.0 × 10⁻² |
| Cutaneous melanoma (SKCM) | 361 | 0.550 | 0.576 | 4.8 × 10⁻² |
| Head & neck SCC (HNSC) | 267 | 0.543 | 0.506 | 2.6 × 10⁻² |
| AML (LAML) | 400 | 0.537 | 0.517 | 2.6 × 10⁻² |

Mean C-index across all 30 cancer types = 0.575. 19 of 30 types showed no significant η association.

### External validation
Eigenvectors and scaler frozen from discovery; projected onto 2,480 non-overlapping TCGA Pan-Cancer Atlas samples (2,801/3,000 genes matched). Pan-cancer: Q1 vs. Q5 log-rank p = 8.5 × 10⁻⁹ (maintained, no retraining). Per-cancer: 3 of 12 evaluable types reached significance — breast carcinoma (C-index = 0.579, p = 0.024, n = 456), glioblastoma (C-index = 0.560, p = 0.046, n = 165), lung SCC (C-index = 0.545, p = 0.047, n = 193). Per-cancer C-indices attenuated, consistent with cross-platform normalization differences and 199 unmatched genes.

### The coordination threshold as a molecular point of no return
The monopolar architecture (c = 0.71) combined with the survival-associated secondary modes yields a model: early tumors retain multi-program architecture (high-T regime — distributed phase, many independent coordination programs coexist); as cancer progresses, secondary programs become subordinated to the dominant mode (low-T regime — ordered phase, monopolar). The spectral coordinate η measures position along this trajectory. Below T* = 1/Δλ, the Boltzmann distribution over coordination modes concentrates overwhelmingly on the dominant program — coordination has "frozen" into a single mode. The authors argue this is a mathematical property of the eigenspectrum (not merely an analogy), making the phase transition testable: longitudinal biopsies of progressing tumors should show increasing c and decreasing secondary-mode amplitudes.

## Limitations

- **Bulk mRNA only:** The 3,000 × 3,000 Hamiltonian is computed from bulk expression, so coordination modes conflate cell-intrinsic gene regulation with cell-type compositional gradients. Single-cell resolution would distinguish whether coordination collapse is a within-cell regulatory event or a cell-composition shift (e.g., loss of differentiated epithelial cells). This is the most significant interpretive limitation.
- **Cross-sectional design:** The monopolar architecture is observed in bulk tumor snapshots; the progressive coordination-collapse model is a cross-sectional inference, not a longitudinal observation. The claim that η tracks progression trajectory requires serial-biopsy validation in progressing tumors — the paper acknowledges this as a testable prediction.
- **External validation attenuation:** Per-cancer C-indices were attenuated in the external TCGA cohort (3 of 12 evaluable types significant vs. 11 of 30 in discovery). Cross-platform normalization differences and 199 unmatched genes are the proposed explanation, but overfitting to the MLOmics discovery cohort (particularly for small-n cancer types) cannot be excluded.
- **19 of 30 cancer types non-significant:** The authors suggest these are cancers where non-transcriptomic features dominate prognosis, or where coordination axes are oriented differently from the pan-cancer modes. This is post-hoc and untested.
- **Temperature-framework weighting:** The Boltzmann-weighted version of η gave near-uniform weights across modes 3, 15, 20 (0.331, 0.335, 0.335), indicating the temperature formalism does not differentiate the survival modes at the individual level — the physics operates at the macro (monopolar structure, phase boundary) rather than individual-mode-weighting level.
- **Single-author preprint:** The paper has not yet undergone peer review. Statistical choices (mode selection by C-index, σ selection by median heuristic) and biological interpretations of the coordination modes should be treated as preliminary pending external review.
- **Variance-gene selection circularity:** The 3,000 genes were selected by highest variance across the full pan-cancer cohort, which may bias the coordination kernel toward tissue-of-origin differences (which dominate pan-cancer variance) rather than within-type progression signals.
