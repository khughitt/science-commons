---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Tirosh2024
type: paper
title: 'Cancer cell states: Lessons from ten years of single-cell RNA-sequencing of human tumors'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Tirosh2024
tags: []
datasets: []
ontology_terms:
- EMT
- cancer cell states
- cell plasticity
- cycling cells
- deconvolution
- expression programs
- intra-tumor heterogeneity
- mesenchymal programs
- single-cell RNA-sequencing
- stress response
---
## Key Findings

### Recurring eITH programs across cancer types

Based on meta-analysis across hundreds of tumors (principally Gavish 2023 and Barkley 2022), the following programs are designated as recurrent (pan-cancer):

1. **Cell cycle (cycling / G1S and G2M).** The single most consistently observed eITH axis. Cycling fraction varies widely between tumors — from <1% in some low-proliferation tumors to the majority in rapidly proliferating tumors and cell lines. G1/S and G2/M programs are highly consistent across cancer and non-cancer cell types. Cycling cells exhibit additional state-associated variation even within the cycling fraction, so normalizing out cell cycle can mask biologically meaningful state heterogeneity.

2. **Stress / hypoxia programs.** The second most common eITH axis. A generic stress program (AP-1 family: JUN/FOS; ATF3; heat-shock proteins; DNA-damage genes; EGLN3; SLC2A1) is observed broadly across tumor types and is spatially organized — stress programs correlate with tumor region and oxygen/nutrient availability. Technically, this program can be artifactually elevated by tissue dissociation; however, it is also observed in spatial transcriptomics and snRNA-seq (no dissociation), confirming biological reality. Stress programs are linked to drug resistance and may be orchestrated by AP-1 family transcription factors.

3. **Mesenchymal (MES-like / EMT-like) programs.** Present across virtually all epithelial cancer types and also in non-epithelial tumors (melanoma, glioma, neuroblastoma, sarcoma — where EMT terminology is inapplicable). Cancer mesenchymal programs reflect *limited, partial* versions of the full developmental EMT: they co-express epithelial and mesenchymal markers simultaneously and usually lack canonical EMT transcription factors (Snail, Zeb) that were traditionally considered essential. Accordingly, calling these programs "EMT" is contested by multiple researchers. Linked to metastasis, drug resistance, and reduced survival in some contexts, though statistical power is limited in individual studies. In ovarian cancer, EMT-like transitions appear to facilitate adaptation to therapy and contribute to a resistance continuum.

4. **Immune-interaction programs: MHC-II and interferon-response.** MHC-II genes (not typically induced in eITH programs) and interferon-response genes (ISG15, IFIT3, STAT1, OAS1) are frequently co-expressed in cancer cells. MHC-II is expressed by multiple cell types beyond professional APCs, including cancer cells, fibroblasts, and endothelial cells in a TME-context-dependent manner. In glioma, mesenchymal programs correlate with increased immune activity mediated by MHC-I and MHC-II upregulation. Interferon-response and MHC-II expression are tightly coupled in most cancer types, consistent with T-cell and immune-cell secretion inducing coordinated expression in neighboring cancer cells.

5. **Developmental lineage-linked programs (cancer-type-specific).** Cancer cells frequently express programs reminiscent of developmental precursor cell types, but as distorted partial versions:
   - Glioma: neural progenitor cell (NPC-like), oligodendrocyte progenitor cell (OPC-like), astrocyte-like (AC-like), and mesenchymal-like (MES-like) programs — reminiscent of neurodevelopmental lineages but transcriptionally closer to one another than to their respective normal counterparts.
   - Melanoma: melanocyte-like, neural crest-like, MES-like programs.
   - Carcinomas: epithelial-to-mesenchymal (EMT-like), epithelial senescence (EpiSen), neuroendocrine, intestinal stem cell-like, lung alveolar (AT2-like) programs.
   - Colorectal cancer: colonic stem/transit-amplifying-like cells, neuroendocrine-like cells (the latter scarce in primary but prominent in liver metastases).
   - Neuroendocrine programs emerge in multiple post-treatment contexts: prostate cancer (after EGFR inhibition), lung (after androgen receptor inhibition), colorectal liver metastases.

### Meta-conclusion: plasticity, selection, or both?

The paper does not definitively resolve the plasticity-vs-selection question but its empirical framing strongly favors plasticity as the dominant within-tumor mechanism for most eITH programs:

- Cancer eITH programs are described as **partial and bidirectional** versions of developmental transitions, not unidirectional clonal sweeps.
- The expression of multiple programs simultaneously within single cells (e.g., a cell can score high on both mesenchymal and cycling programs at once) is inconsistent with a model in which distinct subclones exclusively occupy distinct states.
- The pseudotime critique directly challenges models that read cancer state continua as unidirectional differentiation or selection trajectories.
- However, the paper explicitly acknowledges that the relative contributions of within-lineage plasticity vs. clonal selection of epigenetically distinct subpopulations have not been resolved empirically for most programs — this remains an open question requiring longitudinal lineage tracing.
- The inter-tumor variability in program frequencies (e.g., mesenchymal fraction, cycling fraction) is consistent with both genotype-driven differences between clonal compositions and stochastic/plastic state sampling, and the paper does not adjudicate between them.

### Timescale of state switching

No specific quantitative claim about timescale of state switching is made in this paper. The bidirectionality of cancer plasticity (states can move in multiple directions) is argued to be inherently faster and more reversible than clonal selection-based state shifts, but no concrete timescale figures (hours, days, cell generations) are provided in this review. The MAPK-inhibition melanoma reprogramming example (attributed to Vendramin2021 citation context) implies timescales incompatible with clonal selection but this is referenced rather than documented here.

### Distorted developmental programs — a key conceptual framing

A central argument of the paper is captured in Figure 2: cancer eITH programs are partial, bidirectional, distorted versions of normal developmental or physiological transitions (Figure 2A). In development, transitions from cell type X to Y are unidirectional, complete (full marker switch), and consistent across individuals. In cancer, analogous transitions are bidirectional, partial (cells co-express X and Y markers), and strongly patient-specific in their exact expression profile (Figure 2B). This patient-specificity arises from the unique genetics + transcriptome of each tumor, which modulates the program on top of shared inter-tumor patterns.

### Deconvolution and its limits

scRNA-seq-derived signatures of eITH programs enable deconvolution of bulk RNA-seq datasets (e.g., TCGA), but the authors issue substantive caveats:
- Most cell-state genes are not exclusive to that state; they are also expressed (at lower levels) by other cell types and states.
- Non-canonical expression of rare-cell-type markers by abundant cell types causes disproportionate estimation errors for rare states.
- Programs with low specificity (cell cycle, stress, MES) are especially prone to cross-cell-type contamination in deconvolution.
- An "accurate and nuanced analysis of cell states will therefore continue to require single cell measurements despite advances with bulk deconvolution."

## Limitations

- This is a perspective, not a primary research article — all claims are synthesis of cited literature, primarily from two large meta-analyses (Gavish 2023, Barkley 2022). No original data.
- The paper does not quantitatively adjudicate the relative contributions of clonal selection vs. within-lineage plasticity to any specific eITH program — this central question is acknowledged as open.
- No timescale data for state switching are provided; the plasticity argument rests on bidirectionality and continuum structure of state distributions, not on direct kinetic measurements.
- The stress program's biological vs. artifactual origin is unresolved for dissociation-based protocols; while spatial and snRNA-seq data support genuine biology, the magnitude of artifact contribution is uncertain.
- Annotation ambiguity for EMT/mesenchymal programs is discussed but not resolved; the extent to which programs labeled "mesenchymal" across studies represent the same biological entity is unclear.
- The patient-specificity observation (same programs realized differently across patients) means that cross-patient generalization of any single program's functional consequences is limited without knowing the genetic context.
- Clinical translation of eITH insights is briefly mentioned but not addressed in depth; the focus is mechanistic and methodological.
