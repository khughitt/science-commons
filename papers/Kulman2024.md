---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Kulman2024
type: paper
title: 'Orchard: Building large cancer phylogenies using stochastic combinatorial search'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Kulman2024
tags: []
datasets: []
ontology_terms:
- Gumbel-Max trick
- cancer phylogenetics
- clonal evolution
- mixed sample perfect phylogeny
- mutation tree
- subclonal reconstruction
- tumor heterogeneity
- variant allele frequency
---
## Key Findings

**Scalability.** Orchard successfully reconstructs trees with up to 1,000 mutations in approximately 26 hours wall clock time (k=10, supplementary). CALDER fails entirely on problems with >100 mutations. Pairtree degrades severely with increasing mutation count.

**Accuracy on simulations.** For small problems (10–30 mutations), Orchard matches Pairtree and CALDER on reconstruction quality while being 5–10x faster. For ≥50 mutations, Orchard consistently outperforms both competitors on log perplexity ratio and relationship reconstruction loss across all problem sizes tested. Orchard (k=1) wins on perplexity in 4–10/15 datasets per size class; Orchard (k=10) wins on relationship reconstruction loss in 7–14/15 datasets at larger sizes (Table 1).

**B-ALL real data.** Orchard outperforms Pairtree on 10/14 B-ALL datasets on log perplexity ratio (average improvement: −2.17e-5 bits). A key finding: Pairtree's reconstruction quality degrades as more samples are included (log perplexity ratio increases with sample count for B-ALL case SJBALL022611), while Orchard's remains stable or improves. This suggests Pairtree's MCMC sampler is overwhelmed by the constraint landscape of large multi-sample datasets.

**Subclonal recovery.** On SJBALL022611 (84 mutations, 29 samples), Orchard's phylogeny-aware clustering recovers subclones with an Adjusted Rand Index (ARI) of 0.96 versus expert-defined subclones; Pairtree's clustering achieves ARI of 0.82. The phylogeny-aware approach matches or exceeds state-of-the-art VAF-based clustering on 12/14 B-ALL datasets.

**Mutation ordering effects.** Pre-clustering mutations before tree inference (the traditional approach) is shown to cause information loss and error propagation, particularly for partial mutation ordering relevant to hematological malignancies. Orchard's mutation-level reconstruction avoids this failure mode.

## Limitations

- **ISA required:** Orchard assumes the infinite sites assumption; mutations in regions with complex copy number alterations must be excluded or require reliable allele-specific CNA estimates. This is a significant constraint for CNA-heavy cancer types (e.g., HGSC, breast cancer) where the ISA is frequently violated.
- **Runtime scaling.** Wall clock time grows at least quadratically in the number of mutations (quadratic in clonal proportion estimation alone) and linearly in k and f. Reconstructing 1,000-mutation trees takes ~26 hours; routine use on large datasets will require parallelism or algorithmic improvements to the projection step.
- **Star-tree exponential blowup.** When the partially built tree is a star (all mutations children of root), Orchard evaluates 2^ℓ + ℓ possible placements — exponential in the current tree size. The authors note this is rare in practice under the ISA but it remains a theoretical scaling concern.
- **Mutation ordering sensitivity.** The factored approximation Q^π depends on the mutation order π, and accuracy of the approximation depends on whether data for yet-unplaced mutations is truly conditionally independent of placed mutations given the partial tree. The authors derive conditions for this (Eq 7) but acknowledge counterexamples exist (discussed in S1 Appendix A2.1).
- **Single-cell data not supported.** Orchard's noise model (binomial read count, bulk VAF) is not applicable to single-cell sequencing data without modification. Extension to scDNA-seq would require updating both the noise model and the sampling routine.
- **Clone tree is a post-hoc derived product.** The phylogeny-aware clustering is non-probabilistic (Ward's method + GIC selection); the authors anticipate a fully probabilistic merging step would further improve clone tree inference but have not implemented it here.
- **Benchmark limited to B-ALL.** Real-data validation used only B-ALL — a hematological malignancy with relatively low somatic mutation burden and well-structured clonal hierarchies. Performance on solid tumors with higher mutational burden, more complex copy number landscapes, and less structured subclone architectures is not directly evaluated.
