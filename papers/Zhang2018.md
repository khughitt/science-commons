---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Zhang2018
type: paper
title: Systematic identification of latent disease-gene associations from PubMed articles
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Zhang2018
tags: []
authors:
- Zhang et al.
datasets:
- dataset:human-disease-network-goh
- dataset:omim
- dataset:semmeddb
doi: 10.1371/journal.pone.0191568
ontology_terms:
- disease-gene-association
- disease-topic
- latent-dirichlet-allocation
- network-motif
pmid: '29373605'
venue: PLOS ONE
year: 2018
---
## One-Sentence Summary

An integrative LDA + network analysis framework applied to 146,245 disease-gene associations from SemMedDB groups 7,039 diseases into 160 latent disease topics and then reconstructs disease-specific association networks whose scale-free topology and statistically enriched network motifs point to novel disease mechanisms.

## Key Findings

1. **160 optimal disease topics from 7,039 diseases.** LDA over the SemMedDB disease-gene matrix converged at K = 160 topics (highest log-likelihood across K = 1–250, confirmed by convergence after 1,000 iterations). Topics range from 71–472 diseases and 76–441 genes per topic. The number of genes per topic is not strongly correlated with disease count, indicating many diseases share common gene pools.

2. **LDA topics align with known disease categories.** 19 of 22 Goh et al. human disease network categories map to the 160 LDA topics (Developmental, Ear-Nose-Throat, and Respiratory categories were absent, presumably due to sparse SemMedDB coverage). Cancer shows the highest overlap (73 LDA topics); Metabolic overlaps 49, Hematological 46, Neurological 39. SNOMED-CT annotation AUC across 160 topics averages ~0.8, confirming LDA groupings are consistent with independent disease ontology knowledge.

3. **Validation against OMIM: average 17.8% disease-gene association coverage.** 159 of 160 topics have OMIM-annotated gene-disease associations. Mean overlap is 17.8% across topics; Topic 123 reaches 32.3%. This is interpreted as a floor, not a ceiling: SemMedDB captures literature associations beyond curated databases (e.g., AD case study: 544 AD-associated genes in SemMedDB vs. only 46 in OMIM within the same topics). LDA can therefore surface associations not yet curated in OMIM.

4. **Topic-topic similarity is higher at disease level than gene level.** Pairwise cosine similarity of topics averaged 0.26 at disease level vs. 0.146 at gene level, confirming that LDA generates distinct groups: phenotypically similar diseases may belong to different topics depending on which gene clusters drive them. The authors interpret this as evidence that gene-based grouping is more discriminative than phenotypic grouping — a direct analogue of this project's gene-axis vs. symptom-axis divergence.

5. **Disease-specific association networks are scale-free.** For each of the 10 focal disease topics (e.g., Topics 115, 24, 94, 103, 136, 50, 112, 124, 43, 53), bipartite disease-gene association networks were constructed. Node counts range from 231–608; edge counts from 799–10,895; network diameter 5–8; characteristic path length 2.55–3.03 (Table 3). All exhibit power-law degree distributions — a few diseases and genes act as hubs.

6. **Network motif analysis recovers biologically meaningful substructures.** Three statistically enriched three-node motifs were identified in the AD network (p ≤ 0.05 vs. 1,000 random networks via FANMOD), with z-scores indicating these are topologically distinct from random networks. Motif enrichment was consistent across the AD, lung cancer, and asthma-lymphoma topics.

7. **Alzheimer's case study: known and novel associations recovered.** Topic 61 (the most representative AD topic, with AD as a non-zero proportion in 55 topics) contains hub diseases including Parkinson's disease, neurodegenerative disorders, and ALS. Gene set enrichment via Ingenuity Pathway Analysis on Topic 61 genes recovers Huntington's Disease Signaling (–log p = 8.95), G-Protein Coupled Receptor Signaling (6.5), Parkinson's Signaling (5.21), and Mitochondrial Dysfunction (4.74). Novel finding: *tardive dyskinesia* is a highly connected disease not previously well associated with AD, identified as a potential future research direction. Four enriched APP-involving pathways were also identified (Mitochondrial Dysfunction, WReelin Signaling in Neurons, Neuroprotective Role of THOP1, and Amyloid Processing).

8. **Asthma-lymphoma case study: immune cross-disease mechanisms.** Topic 94 contains 180 diseases and 279 genes linked through 10,895 associations. Hub diseases are asthma, lymphoma large-cell diffuse, and chronic lymphocytic leukemia. Enriched gene pathways include Th1/Th2 activation, crosstalk between Dendritic Cells and Natural Killer Cells, and Altered T and B Cell Signaling — consistent with the known immune imbalance hypothesis for the asthma-lymphoma co-association.

## Limitations

1. **Co-occurrence basis.** SemMedDB predications are co-occurrence-derived (sentence-level), not curated causal associations. The paper acknowledges that ~77% prediction accuracy of SemMedDB may lead to false positives in the disease-gene associations feeding LDA. This is the same upstream-noise concern as PubTator3 gene mentions in this project.

2. **LDA fixed K = 160 is heuristic.** K was chosen by log-likelihood, but log-likelihood is a poor model-selection criterion for LDA because it monotonically increases with K given enough data. The claim that "160 is optimal" should be treated as "160 is where the log-likelihood curve starts flattening" — not a principled model selection.

3. **Validation is within the literature ecosystem.** OMIM, SNOMED-CT, DO, and HPO all derive substantially from published literature. Cross-validation against independent (non-literature) molecular axes — transcriptomics, proteomics, GWAS — is absent. This is the key gap that `hypothesis:h03-multi-axis-validation` is designed to fill.

4. **Publication gravity not addressed.** The paper does not account for the fact that well-studied diseases and genes will dominate LDA topics (Topic 115 hub: carcinoma, non-small-cell lung; top genes are *egfr*, *tp53* etc.). The resulting topics over-represent research-intensive diseases; rare diseases with sparse literature will be absorbed into large topics or remain peripheral. This project has now empirically characterized this bias (tasks t027/t028) and implemented a normalization knob (t029); Zhang et al. have no analogous correction.

5. **Single NLP layer.** Disease and gene extraction uses SemMedDB's pre-built predications. Errors in SemRep NLP or UMLS concept normalization propagate directly into the topic model with no sensitivity analysis.

6. **No disease-disease similarity matrix.** The paper derives disease groupings (topics) but does not construct or report a pairwise disease-disease similarity matrix. It therefore cannot directly characterize which specific disease pairs are most and least similar under the gene axis — the primary output of this project's pipeline.

7. **Case studies cherry-picked.** Three case studies (AD, lung cancer, asthma-lymphoma) were chosen because they represent well-studied, data-rich diseases. Generalizability to rare diseases, poorly understood conditions, or cross-category associations is not demonstrated.
