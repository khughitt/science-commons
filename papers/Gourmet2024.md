---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Gourmet2024
kind: paper
title: The temporal evolution of cancer hallmarks
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Gourmet2024
tags: []
ontology_terms:
- GTEx
- TCGA
- cancer hallmarks
- dN/dS
- genomic instability
- immune evasion
- pan-cancer evolution
- patient stratification
- temporal ordering
- variant allele frequency
dataset_usage:
- ref: dataset:gtex
  role: analyzed
  overlap: unknown
- ref: dataset:tcga
  role: analyzed
  overlap: unknown
---
## Key Findings

### Pan-cancer hallmark ordering

The canonical temporal sequence, by decreasing mean VAF (earlier to later), is:

1. **Genome instability** (VAF = 0.3272 ± 0.001; dN/dS = 1.340 [1.295–1.387]) — first
2. **Replicative immortality** (VAF = 0.3196 ± 0.001; dN/dS = 1.361 [1.327–1.396])
3. **Metabolism** (VAF = 0.3123 ± 0.0008)
4. **Evading growth suppressors** (VAF = 0.3081 ± 0.0007)
5. **Angiogenesis** (VAF = 0.3080 ± 0.0008)
6. **Resisting cell death** (VAF = 0.2967 ± 0.0005)
7. **Metastasis** (VAF = 0.2964 ± 0.0004)
8. **Sustained proliferative signalling** (VAF = 0.2961 ± 0.0004)
9. **Tumour-promoting inflammation** (VAF = 0.2888 ± 0.0007)
10. **Immune evasion** (VAF = 0.2883 ± 0.0007) — last

In healthy (GTEx) tissues, hallmark VAFs show no consistent order (6 of 10 hallmarks have overlapping VAF estimates), and all hallmarks show dN/dS < 1 (pervasive negative selection). The contrast establishes that the ordering is cancer-specific and driven by positive selection.

### dN/dS confirms positive selection in cancer, negative in normal tissues

All 10 hallmarks show dN/dS > 1 in TCGA tumors. The strongest positive selection is on genomic instability (1.340) and immortality (1.361). In GTEx: immortality dN/dS = 0.287 [0.275–0.300]; genomic instability dN/dS = 0.456 [0.442–0.471]. The hallmark ordering by dN/dS is correlated with the VAF-based ordering pan-cancer (Spearman r = 0.806, p = 0.008) but not per-cancer-type (r varies; less consistent).

### TP53 drives early genomic instability

Removing TP53 from all hallmark gene sets shifts genomic instability to the last position while leaving most other hallmarks largely unaffected. This indicates that early acquisition of genomic instability is predominantly driven by TP53 mutations. TP53 is represented in 8 of 10 hallmark gene sets (it is the most broadly shared gene). The genomic instability hallmark has the fewest shared genes with other hallmarks (41%; 87/211 genes).

### Cross-cancer robustness and environmental exceptions

Hallmark ordering is conserved across 27/32 cancer types by Spearman rank correlation (strict multiple-testing threshold reduces this to 23 types with shared trajectory). Exceptions: **uveal melanoma, skin cutaneous melanoma, thymoma, thyroid carcinoma, pheochromocytoma, and paraganglioma** deviate from the common trajectory. UV light exposure (melanomas) and unknown environmental stressors in other outlier types are hypothesized to disrupt the default evolutionary path. The ASCETIC algorithm for trajectory inference from gene-group data yields consistent results with the VAF-based ordering.

### Environmental modulation: smoking and lung cancer

LUAD current smokers show significantly higher overall VAF across all hallmarks except genomic instability — consistent with a clonal sweep driven by modification of metabolism, growth, and angiogenesis (top 3 in smokers). Inflammation and immune evasion remain last in all LUAD and LUSC groups except LUAD non-smokers, suggesting smoking is less strongly associated with immune evasion than previously proposed.

### Patient-level clustering and prognosis

At the individual patient level, hallmark ranks show a bimodal distribution for genomic instability (GI tends to be ranked either 1st or 10th, driven by TP53 mutation status). PCA on all 10 hallmark ranks separates two clusters distinguished primarily by GI, immune evasion, and inflammation rank positions:

- **Cluster 1 (early GI):** Genomic instability acquired early — associated with **poorer OS, PFS, and DFS** (OS p = 0.00096; PFS and DFS p < 0.0001).
- **Cluster 2 (late GI):** Genomic instability acquired late — better prognosis.

Cluster membership is distributed across most cancer types, though breast (BRCA), head-and-neck squamous (HNSC), lung squamous (LUSC), and ovarian (OV) cancers show unequal distribution. ASCETIC-based clustering with k=6 also reveals prognostic differences.

### Gene-level details

- Genes under significant positive selection for genomic instability: ATM, CASP8, TP53, PTEN.
- Genes under significant positive selection for immune evasion: PIK3R1, HLA genes.
- Most known cancer driver genes (42%; 152/365) are not associated with any single specific hallmark by the gene list used.
- AKT, Ras, PIK3, MAPK gene families appear in 9 of 10 hallmarks; BRAF in 7/10; TP53 in 8/10.

## Limitations

- **VAF as a timing proxy is imperfect.** VAF reflects the clonal fraction at the time of sampling, not a direct timestamp of when a mutation arose. A high-VAF hallmark mutation could reflect early occurrence *or* strong selective sweeping. The authors partially address this with dN/dS cross-validation, and by showing consistency in diploid tumours and with CCF-corrected analyses, but interpretational ambiguity remains — especially for copy-number-altered regions.
- **Point mutations only.** The analysis covers only somatic nonsynonymous point mutations, not copy number alterations (CNAs), structural variants, or epigenetic changes. Many hallmark-relevant events (e.g., MYC amplification for growth, CDKN2A deletion for growth suppression, chromatin remodelling for immune evasion) would not be captured. The authors explicitly acknowledge this.
- **Cross-sectional design.** All timing inferences are made from single-timepoint bulk sequencing. True longitudinal ordering within a single patient is not directly observed; the reconstruction is statistical, based on population-level clonal fractions.
- **Gene list quality.** The hallmark gene sets depend on the Zhang et al. (CHG) database classification. Many driver genes span multiple hallmarks (TP53: 8/10); 58% of known driver genes are not assigned to any hallmark. Hallmark boundaries are fuzzy biological constructs, not discrete molecular programs.
- **TP53 dominance.** The early positioning of genomic instability is largely attributable to TP53, which is the most commonly mutated gene in cancer and is clonal in most tumours. Removing TP53 changes the entire hallmark ordering. This raises the question of whether the sequence reflects biology or gene-list composition.
- **Cancer-type exceptions.** 5–9 of 32 cancer types (depending on statistical threshold) do not share the common trajectory, limiting the universality of the model. The mechanisms underlying outlier types are not fully explored.
- **No therapy-treated samples.** TCGA is restricted to untreated primary tumors; the hallmark sequence under therapeutic pressure (relevant to h006's therapy-constraint component) cannot be assessed.
- **Preprint status.** Not yet peer reviewed as of the bioRxiv posting (January 2024).
