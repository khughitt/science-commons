---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Collins2022
kind: paper
title: A cross-disorder dosage sensitivity map of the human genome
version: "1.0.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: Collins2022
tags: []
dataset_usage: []
ontology_terms:
- copy-number-variation
- dosage-sensitivity
- haploinsufficiency
- pan-disease
- rare-variant-association
- triplosensitivity
paper_kind: ''
---
## Key Findings

**rCNV-disease associations.** The discovery meta-analysis identified 163 distinct large rCNV segments and 795 rCNV-phenotype associations. Combined with 15 additional literature-curated GDs meeting a targeted significance threshold (p ≤5.26×10⁻⁴), the consensus set is 178 disease-associated rCNV segments. Most phenotypes (43/54; 89.6%) showed significant GD rCNV associations; 39/54 (72.2%) showed significant constrained-gene rCNV contributions outside known GDs.

**Structural features of rCNV segments.** The 178 consensus segments are gene-dense (overlapping 44% more genes than expected by permutation; observed 12.7 vs expected 8.6 genes; p=0.003) and enriched for genes under strong mutational constraint (34% stronger depletion for PTVs; average minimum LOEUF per segment: 0.25 observed vs 0.37 expected; p=0.006). Highly penetrant segments (mean OR=444.0) show this signal more strongly than incompletely penetrant segments (mean OR=10.3). Pleiotropic segments (associated with multiple phenotypes) contain more genes and overlap more strongly constrained genes.

**Dosage-sensitive driver gene fine-mapping.** Fine-mapping reduced average candidate genes per locus by 48%, producing 115 credible sets averaging 4.2 genes (range 1–28). PIP ≥0.8 nominated 31 "highly confident" driver genes; PIP 0.2–0.8 nominated 90 "confident" genes. Fine-mapping prioritized driver genes in 55.2% (90/163) of significant rCNV segments. Of 70 NDD-associated GDs with sufficient DNM data, 26% (18/70) had mutational excess concentrated in 1–2 driver genes; many correspond to known developmental disorder genes.

**DNM convergence.** PTV DNMs are enriched in NDD deletion segments (p=0.028), while missense DNMs are enriched in NDD duplication segments (p=0.002), consistent with mechanism-specific convergence of rCNVs and point variants. Critically, after excluding 270 previously known NDD genes, PTV enrichment in deletion segments was ablated (p=0.203), but missense enrichment in duplication segments persisted (p<10⁻⁵), suggesting many TS driver genes are currently unrecognized.

**pHaplo and pTriplo scores.** 2,987 haploinsufficient (pHaplo ≥0.86) and 1,559 triplosensitive (pTriplo ≥0.94) genes were defined. pHaplo and pTriplo are moderately correlated (Pearson R²=0.30), with 648 genes uniquely triplosensitive. Both scores are externally validated by: (1) classifying independent gene sets with biological evidence for DS/DI; (2) stratifying ASD risk from de novo CNVs in 13,786 affected children; (3) inverse correlation with population CNV rates; (4) enrichment of damaging DNMs in NDD probands in the top decile; (5) correlation with point-mutation constraint metrics.

**HI vs TS gene properties.** Bidirectionally DS genes are distinguished above all by evolutionary constraint. Genes more sensitive to deletion (primarily HI) are larger, farther from other genes, and flanked by more poised cis-regulatory enhancers — hallmarks of developmentally critical, precisely regulated genes. Genes more sensitive to duplication (primarily TS) are generally shorter, G/C-rich, and located in gene-dense, broadly active regions.

## Limitations

**Microarray resolution.** All CNV data are microarray-derived; breakpoint precision is low, conservative filtering undoubtedly misses some disease-causing rCNVs, and the molecular consequences of duplications (more diverse than deletions) are more likely undercharacterized. Smaller (<100 kb) CNVs are entirely excluded.

**No protective rCNV analysis.** Non-uniform phenotyping across cohorts precluded searching for protective rCNVs — an important gap for understanding the full fitness landscape of dosage sensitivity.

**HPO phenotype mapping imprecision.** The 54 phenotypes were constructed by hierarchical clustering of HPO-mapped terms with fuzzy keyword matching. This introduces misclassification, especially for phenotypes with overlapping HPO subtrees. Integration with the project's MeSH-based disease space will require a careful HPO-to-MeSH crosswalk — not all 54 phenotypes will map cleanly.

**ML model training circularity.** The pHaplo/pTriplo models were trained partly on the same rCNV data used to derive the association statistics (calibration training sets). External validation is reassuring but not fully independent of the training data for all 145 features.

**Common-variant and somatic biology excluded.** The study focuses on rare (frequency <1%) CNVs and ignores common-variant dosage effects, somatic mosaic CNVs, and smaller structural variants — all of which may be disease-relevant.

**No direct quantification of cis-regulatory or epistatic effects.** Many rCNVs likely act partly or entirely through non-coding regulatory mechanisms or gene-gene interactions; the study's "single driver gene" model is acknowledged as an approximation.
