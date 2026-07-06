---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Luquette2025
kind: paper
title: A comprehensive view of somatic mosaicism by single-cell DNA analysis
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Luquette2025
tags: []
ontology_terms:
- clonal phylogenetics
- copy number alterations
- mutational signatures
- normal tissue evolution
- primary template-directed amplification
- single-cell whole-genome amplification
- somatic mosaicism
dataset_usage:
- ref: dataset:dbgap-phs004193
  role: analyzed
  overlap: unknown
---
## Key Findings

### Per-cell Mutation Burden

- Mean per-cell somatic SNVs (sensitivity-corrected): **1,385 SNVs per lung cell** and **863 SNVs per colon cell**. [Note: these are raw called counts; sensitivity-corrected burden would be higher given ~37% sensitivity for SNVs.]
- Mean per-cell indels: **76 indels per lung cell**, **45 per colon cell**.
- Mean per-cell DNVs: **17 per lung cell**, **7 per colon cell**.
- Mutational catalogs totaled 68,083 small mutation calls in lung and 37,563 in colon across all cells.

### Cell-to-cell Mutational Heterogeneity

Single cells clustered into at least 6 distinct SNV spectral groups (Figure 2F). Clusters 1 and 2 were tissue-mixed (lung and colon) and differentiated primarily by T>C rate. The remaining four clusters were tissue-enriched:
- **Cluster 3 (colon-only):** distinguished by high C>T at CpG (SBS1-like clock signature).
- **Clusters 4 and 6 (lung-enriched):** widespread C>A mutations; Cluster 6 contained the three highest-burden lung cells and is consistent with heavy tobacco exposure.
- **Cluster 5 (lung-enriched):** nearly entirely defined by C>T at TCN context (APOBEC-like, SBS2).

### Mutational Signatures

Six components extracted de novo:
1. **Component 1** (~COSMIC SBS5): clock-like, ubiquitous across all cells, most mutations attributed to this component.
2. **Component 2** (~COSMIC SBS5/SBS16): T>C mutations; higher in lung cells.
3. **Component 3** (tobacco): present primarily in lung cells; combination of C>A-rich SBS4 (SNV), 1-bp deletion ID3, and CC>AA DBS — all three consistent with a single tobacco mutagenic etiology. Two lung cells showed exceptionally high component 3, consistent with a history of smoking.
4. **Component 4** (~COSMIC SBS1): C>T at CpG clock-like; higher in colon cells.
5. **Component 5** (~COSMIC SBS2 / APOBEC): C>T APOBEC-induced damage in a handful of lung and colon cells. Notably, no kataegis was observed; instead, pairs of C>T mutations separated by <100 bp were scattered across the genome (*didyma* pattern) — consistent with a recently described APOBEC–tobacco interaction. One lung cell showed C>G APOBEC (APOBEC3A) without *didyma*, suggesting APOBEC3A vs. APOBEC3B differential activation can vary cell-to-cell.
6. **Component 6:** not explicitly named; minor component.

### Phylogenetic Structure

- Three primary clades branch from the root (zygote). Combined cell fractions across all three clades sum to ~100% in both lung and colon, confirming the root represents the zygote.
- The single-cell PTA phylogeny captured a crucial early branching event missed by bulk WGS (bulk WGS analysis of the same tissue by a companion SMaHT effort missed one of the earliest clades, omitting it from the tree topology).
- Clock-like SBS5 signature was present in all cells and correlated with no clade structure; tobacco and APOBEC signatures appeared in late branches only, confirming they are adult-acquired exposures.

### Copy Number Alterations and Structural Variants

- 98 cells analyzed for CNA (4 excluded for likely amplification dropout artifacts).
- **14 cells had whole-chromosome aneuploidies:** most common events were loss (6 cells) or gain (2 cells) of chromosome Y — the most common somatic aneuploidy in males. Each ChrY gain/loss event arose independently (different phylogenetic lineages), indicating these are recurrent somatic events.
- 6 of the 14 aneuploid cells showed multi-chromosome copy number changes.
- **31 cells had subchromosomal CNAs ≥10 Mb** (13 colon, 18 lung), including 3 copy-neutral LOH events, duplications, and deletions.
- One lung cell (Mayo-WashU Lu_S2) had complex chromosomal rearrangements consistent with multiple translocations forming non-canonical dicentric chromosomes — cancer-like genomic architecture in a normal somatic cell.
- **5 cells from lung tissue were identified as T lymphocytes** based on somatic V(D)J recombination signal: 22 deletions identified in these cells, 16 at T-cell receptor loci (TCRα, TCRβ, TCRγ), confirming bona fide VDJ recombination rather than artifact.

## Limitations

- **Single donor, single age point:** All data come from one 74-year-old male. No age-series, no sex comparison, no cancer samples. Quantitative per-cell mutation rates cannot be generalized without replication.
- **Low sensitivity:** SCAN2 SNV sensitivity ~37%, indel sensitivity ~25%. Correction for sensitivity is applied, but the correction assumes uniform calling efficiency across the genome, which may not hold at all loci or for all mutation types.
- **Small cell count (n = 87 retained):** Statistical power for formal selection/drift tests or clone frequency estimates is limited. Claims about "independently arising" ChrY events are phylogenetically motivated but not formally tested.
- **Non-neural, non-hematopoietic tissues only:** Prior PTA work focused on brain (postmitotic neurons) or blood; this is the first postmortem lung/colon application. Generalization to other tissue types awaits further SMaHT work.
- **Preprint status:** Not yet peer-reviewed as of the filing date (November 3, 2025).
- **Throughput and cost:** The authors explicitly acknowledge that throughput is a current limitation of PTA-based single-cell sequencing, preventing large-scale studies. Duplex sequencing is complementary and more scalable for population-level estimates.
- **Cell type identity not fully resolved:** Although T-cells were identified by V(D)J signatures, the remaining 82 cells are not assigned to specific cell types; the contribution of cell-type heterogeneity to observed mutational spectrum variation is not formally partitioned.
