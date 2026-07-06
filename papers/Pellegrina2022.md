---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Pellegrina2022
kind: paper
title: Discovering significant evolutionary trajectories in cancer phylogenies
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Pellegrina2022
tags: []
ontology_terms:
- cancer evolution
- clonal exclusivity
- conserved evolutionary trajectories
- frequent itemset mining
- phylogenetic tree analysis
- statistical significance testing
- tumor heterogeneity
dataset_usage:
- ref: dataset:luo2023-aml-sc
  role: analyzed
  overlap: unknown
- ref: dataset:tracerx
  role: analyzed
  overlap: unknown
---
## Key Findings

### Simulated data

- Empirical FWER consistently ≤ α across all configurations; estimates remain close to the nominal bound, confirming WY does not over-correct.
- MASTRO robustly recovers implanted trajectories even when they appear in relatively few tumors or when tree inference introduces ordering noise.
- CONETT on the same null-resampled datasets produces large trees with systematically low P-values (many < 10⁻²), demonstrating that its statistical test is driven by alteration co-occurrence rather than ordering conservation.

### AML results

MASTRO identifies 138 maximal trajectories with ≥ 2 alterations observed in ≥ 2 tumors; the 40 most significant have estimated FDR ≈ 0.2. Four summary trajectory types emerge:

1. **DNMT3A → NPM1 → {FLT3 | NRAS | KRAS}** (clonally exclusive signaling genes; rank 1, support 17, p = 8 × 10⁻⁸): canonical epigenetic-initiator pathway confirmed.
2. **IDH1/IDH2 → NPM1 → FLT3** (rank 4, support 4, p = 10⁻⁵): second major epigenetic-initiator pattern.
3. **TET2 → {DNMT3A, NRAS}** (rank 22, support 3, p = 2 × 10⁻⁴): TET2 as initiating event consistent with Miles et al. 2020.
4. **NPM1 → {FLT3 | PTPN11 | NRAS | KRAS}** (clonally exclusive signaling; rank 7, support 5, p = 2 × 10⁻⁵): a previously unreported alternative progression where NPM1 is the *first* alteration (no epigenetic initiator precedes it), potentially characterizing a distinct AML evolutionary subtype.

The most *frequent* trajectories are not the most *significant* (only 23 of the 40 most frequent overlap the 40 most significant), underscoring the value of conditional statistical testing. MASTRO identifies multi-branch trajectories (e.g., three mutually exclusive subclonal alterations in a single trajectory) that pair-based methods like GeneAccord cannot capture.

### NSCLC results

The 15 most significant trajectories have estimated FDR ≈ 0.3. All trajectories are topologically simple (2–3 nodes), reflecting the coarser resolution of bulk multi-region WES compared to single-cell data. Notable findings:

- Groups of co-clonal alterations (TP53, PIK3CA, CDKN2A, FGFR1, PTEN, CCND1, SOX2) occur more frequently together and at higher nodes than expected by chance.
- Some alterations are more subclonal than expected, indicating preferentially late acquisition.
- The most frequent CONETT edge (TP53 → SOX2 amplification, 12 occurrences) is spurious: in all 12 trees, both alterations reside in the same node (unknown ordering), yet CONETT treats this as a directed ancestor–descendant relationship — an artifact of not enforcing induced subgraph semantics.

### Runtime

MASTRO is fast: all trajectories and P-values computed in ≤ 5 s (null models 1–2) or ≤ 30 s (null model 3). Permutation correction (10⁴ resamples, 64 cores multithreaded): < 2 h. CONETT requires 15 s on AML and ~4.5 h on NSCLC.

## Limitations

- **Ordering resolution depends on input phylogenies:** MASTRO consumes pre-inferred tumor trees; errors in phylogenetic reconstruction propagate directly into trajectory discovery. NSCLC bulk WES trees have few nodes with many co-labeled alterations, severely limiting ordering inference. Single-cell data (AML) provides far richer tree structure.
- **NP-hard worst case:** The FMT problem is provably NP-hard, and MASTRO's practical efficiency depends on the sparsity of frequent itemsets; dense alteration co-occurrence could make it intractable in principle.
- **σ = 2 threshold is liberal:** All experiments use a minimum support of 2 tumors. With 99–123-patient cohorts, this could surface trajectories present in <2% of patients, raising clinical interpretability concerns even if statistically controlled.
- **Conditional null model fixes tree topology:** The null does not permute the tree topology itself (null models 1–2), which means tree-topology biases inherited from phylogenetic inference algorithms are not accounted for. Null model 3 relaxes this but is computationally costlier.
- **Linear vs. branched trajectory discovery:** While MASTRO supports branched trajectories in principle, the NSCLC results show that bulk multi-region data rarely provides enough ordering constraints to support complex topologies. The method's full power is realized only with single-cell–resolution trees.
- **No integration with clonal frequencies or selection coefficients:** MASTRO treats alteration ordering as binary (observed or not) without weighting by clone size, VAF, or estimated fitness advantage. Strong selection could be indistinguishable from weak selection with high frequency.
- **Single cancer type per analysis:** Cohort-level application is within a cancer type. Cross-cancer generalization requires separate runs and a framework for comparing significance across different alteration universes.
