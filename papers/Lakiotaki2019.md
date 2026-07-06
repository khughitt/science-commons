---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Lakiotaki2019
kind: paper
title: A data driven approach reveals disease similarity on a molecular level
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Lakiotaki2019
tags: []
authors:
- Lakiotaki et al.
doi: 10.1038/s41540-019-0117-0
ontology_terms:
- co-expression-structure
- disease-similarity
- distributional-distance
venue: npj Systems Biology and Applications
year: 2019
dataset_usage:
- ref: dataset:omics-compendia-geo
  role: analyzed
  overlap: unknown
---
## Key Findings

1. **Strongest cross-disease pair (human transcriptomics): breast cancer and lung cancer** (edge weight = 34 — found in 34 independent dataset pairs). The paper attributes this partly to estrogen receptor alpha expression in non-small-cell lung carcinoma and shared cell-proliferation/metastasis pathway signatures.

2. **Further strong edges (weight >= 5):** Alzheimer's disease and schizophrenia (weight = 8; six of the ten explaining KEGG pathways are nervous-system pathways); psoriasis and asthma (weight = 6; both chronic immune-mediated inflammatory diseases); AML and viral infectious disease (weight = 7); asthma and hepatitis C (weight = 6); systemic lupus erythematosus and viral infectious disease (weight = 6); breast cancer and thyroid cancer (weight = 7); melanoma and breast cancer (weight = 5); asthma and malaria (weight = 5).

3. **Mouse transcriptomics strongest edge:** obesity and liver cancer (weight = 6), consistent with epidemiological evidence.

4. **Breast cancer pathway explanation (clique of 10 datasets, 1000 probe-sets):** Top enriched KEGG pathways are predominantly immune-related — B-cell receptor signaling, NF-kB, T-cell receptor, Th1/Th2/Th17 differentiation, hematopoietic cell lineage, allograft rejection — consistent with known tumor-immune infiltration biology.

5. **Alzheimer's-schizophrenia pathway explanation (8 dataset pairs):** Top pathways include oxidative phosphorylation, proteasome, phagosome, mTOR signaling, ErbB signaling, and thermogenesis — pointing to mitochondrial/proteostatic mechanisms as a shared substrate.

6. **Cross-platform consistency:** AML clique from microarray (GPL570, 5 datasets) vs. RNA-seq (GPL11154, 5 datasets) yields a Jaccard index of 0.62 on the explaining gene sets when ~15,000-20,000 probe sets are selected — far above random expectation — confirming that the identified mechanisms are robust to measuring technology.

7. **Community structure in GPL570 full network (1562 significant edges):** Manually annotated communities map onto disease or tissue categories (brain diseases, glioma, lymphoma, HPV-related cancers, breast cancer / cell line vs. human tissue, etc.), providing sanity-check evidence that the c-SKL metric recovers biologically coherent structure.

8. **Tissue is not the sole driver of similarity:** Cross-tissue similarities appear (e.g., anterior orbit/lacrimal gland and blood), and not all same-tissue datasets connect, showing the method captures molecular covariance structure beyond tissue-of-origin.

## Limitations

1. **Same-platform requirement.** The c-SKL can only compare datasets measuring the same variable set; no cross-platform (e.g., microarray vs. methylome) disease comparison is possible without additional methodology. This substantially fragments the network (6 separate networks, of which methylomics has only 11 disease nodes).

2. **Cannot distinguish sources of similarity.** The method cannot determine whether a detected similarity arises from shared disease biology, shared tissue, shared experimental protocol/batch effect, or other technical factors. Tissue removal via PCA is proposed but not implemented in the paper.

3. **Confounders from cell lines vs. patient tissue.** The breast cancer community splits into two disconnected components (cell-line studies vs. patient studies), indicating that experimental context is a major driver of covariance structure, potentially masking true biological similarities or producing false ones.

4. **No control for study-level co-annotation or dataset reuse.** While datasets sharing individual molecular profiles are excluded, datasets from the same laboratory or protocol cluster may share batch-specific covariance structure unrelated to biology.

5. **Binary disease labels.** The disease annotation is derived by automated text analysis of GEO metadata; heterogeneous studies covering multiple phenotypes will be labeled by whichever phenotype the automated annotator identifies, potentially misassigning dataset-level disease labels.

6. **Scale asymmetry.** The methylomics network has only 11 nodes (117 datasets), limiting its utility for pan-disease inference compared to the transcriptomics networks.

7. **Static snapshot.** Results are from GEO as of 2019. The rapidly growing omics repository will change the network structure; no versioning or reproducibility protocol is described for future replication.

8. **Code availability is request-based** (not deposited in a public repository at time of publication), limiting reproducibility. The interactive browser (datascope.csd.uoc.gr) provides exploration access but not computational reuse.
