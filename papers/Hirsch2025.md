---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Hirsch2025
type: paper
title: Stochastic modeling of single-cell gene expression adaptation reveals non-genomic contribution to evolution of tumor subclones
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Hirsch2025
tags: []
datasets:
- dataset:gse215963
- dataset:gse255484
ontology_terms:
- Ornstein-Uhlenbeck process
- Wnt signaling
- gene expression adaptation
- immunotherapy resistance
- melanoma
- non-genomic evolution
- plasticity
- stochastic modeling
- subclonal evolution
---
## Key Findings

**Quantitative claim on non-genomic contribution:** Among the 8,363 analyzed genes, EvoGeneX identified 812 genes (9.7%) with adaptive expression in HA-R (496 upregulated, 316 downregulated), 1,277 genes (15.3%) in SA-S (201 upregulated, 1,076 downregulated), and 616 genes (7.4%) in MA-S (288 upregulated, 328 downregulated). No constrained genes were found (consistent with simulation studies showing the method cannot distinguish constrained from neutral in this noise regime). The percentage of mutated genes with adaptive expression is approximately equal to the genome-wide adaptive percentage, confirming that mutational status does not predict adaptive expression — i.e., the adaptively evolving expression is largely non-genomic in character.

**Benchmarking vs. differential expression:** On simulated data, EvoGeneX correctly identified 42% of adaptively simulated genes across all parameter combinations (up to 95% under favorable parameters) with a false positive rate of 3.4% for neutrally evolving genes. Differential expression identified more adaptive genes (46% vs. 42%) but had a dramatically higher false positive rate (26.3% vs. 3.4%), demonstrating that OU modeling is substantially more specific than differential expression for detecting true selection.

**Pathway-level biology:** Genes with adaptive expression in HA-R (invasive, ICB-resistant phenotype) are enriched for Rap1 signaling and bacterial invasion of epithelial cells pathways — GPCR signaling components, cytoskeleton genes, and non-canonical Wnt pathway effectors (Gnaq, Gnas, Rac1, Prkca, Actr2/3). Genes with adaptive expression in SA-S (proliferative, ICB-sensitive phenotype) are enriched for ribosomal and mitochondrial processes (canonical Wnt / MITF pathway effectors). Histone modification enzyme genes (Kdm1a, Ezh1, Kdm5a, Smyd4, Kdm4b, Smyd2, Smyd3) are adaptively upregulated in HA-R and adaptively downregulated in SA-S, suggesting epigenetic switches as a mechanism for the expression divergence.

**Wnt signaling bifurcation:** The two phenotypes map onto the known melanoma canonical/non-canonical Wnt dichotomy: SA-S sublines (proliferative) show adaptive upregulation of canonical Wnt components (β-catenin/MITF axis, ribosomal/mitochondrial genes, cell cycle genes including Pcna, Tk1, Polr2j, Polr1d); HA-R sublines (invasive) show adaptive upregulation of non-canonical Wnt components (G protein → PDE/PKC/PKG → Ca²⁺/calcineurin/CDC42 → actin cytoskeleton).

**ICB validation:** Genes with adaptive upregulation in HA-R are significantly enriched among genes more highly expressed in post-CTLA4 treatment responder tumors compared to non-responder tumors (7.2% vs. 1.6% of DEGs; chi-squared p < 0.0001). Genes with adaptive downregulation in HA-R are enriched among genes more highly expressed in non-responder tumors (6.1% vs. 5.4%). The SA-S enrichment pattern is reversed: adaptively upregulated SA-S genes are enriched in non-responder DEGs (12.7% vs. 1.1%), and adaptively downregulated SA-S genes are enriched in responder DEGs. This cross-validates the subline-level adaptive calls against an independent in vivo treatment dataset.

**dN/dS comparison:** Genome-wide dN/dS across all sublines = 1.63 (weak positive selection signal); within individual regime groups (HA-R: 1.32, SA-S: 1.80, MA-S: 1.46), all indicating weak positive selection but with insufficient power for gene-level resolution. Expression-based analysis provides complementary resolution unreachable by sequence evolution alone.

## Limitations

- The OU model cannot distinguish whether adaptive expression arises from epigenetic inheritance (heritable variation subject to Darwinian selection) versus regulated plastic response to microenvironmental cues (EES substrate). The model detects the signature of directional selection without resolving its molecular mechanism.
- Only 23 sublines (8 cells each) — very small sample, low statistical power, especially for detecting constrained evolution. The authors acknowledge that adding more sublines would improve performance.
- Mouse melanoma cell-line system (B2905): all sublines evolved in vitro and in syngeneic inbred mice. Tumor microenvironment diversity is limited; generalizability to human primary tumors is untested.
- The method requires a mutation-based phylogenetic tree as input backbone, which ties the approach to datasets with matched genetic and expression data from the same clonal lineage. This is rarely available in human clinical data.
- EvoGeneX cannot reliably distinguish constrained from neutral evolution in this noise regime (shown in simulations), limiting detection to adaptive signals only.
- Bulk whole-exome for phylogeny combined with sparse single-cell expression (8 cells/subline) means within-subline expression heterogeneity is estimated with high noise; the negative binomial correction partially addresses but does not eliminate this.
- The validation uses a different experimental context (parental B2905 line, not isolated sublines), so the enrichment of adaptive genes in responder/non-responder DEGs is suggestive rather than mechanistically confirmatory.
