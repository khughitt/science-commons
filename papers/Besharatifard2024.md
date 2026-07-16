---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Besharatifard2024
kind: paper
title: A review on graph neural networks for predicting synergistic drug combinations
version: "1.0.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: Besharatifard2024
tags: []
dataset_usage: []
ontology_terms: []
paper_kind: review
---
## Key Findings

**GNN architecture taxonomy.** The 25 models are grouped predominantly into three architecture families (24 of 25), plus one study (Lv et al. 2022) built on graph regularization rather than these three:
- GCN (graph convolutional network): most common; used for molecular graph feature extraction and biological network embedding.
- GAT (graph attention network): second most common; assigns learned attention weights to neighbor nodes, enabling selective aggregation; used in both drug-structure graphs and knowledge graphs.
- GAE (graph autoencoder): encodes drug-drug synergy networks into latent space and reconstructs the adjacency matrix to infer novel synergistic relationships.

**Feature landscape.** Two orthogonal axes structure how models represent drugs and cell lines: (a) representation type — molecular graph (2D/3D structure via SMILES) vs. fingerprint vs. knowledge graph node, and (b) entity scope — drug only vs. drug + cell line vs. drug + cell line + biological network (PPI, pathway, gene expression).
Models incorporating richer, multi-modal heterogeneous features consistently outperform single-feature baselines; e.g., the Hu et al. (2023) model's use of drug + protein + disease heterogeneous graph with pre-trained embeddings outperformed DeepDDS which used drug structure only (AUC 0.84 vs. 0.66 on AstraZeneca) [@Besharatifard2024].

**Benchmark fragmentation.** No shared benchmark exists.
Studies differ in: dataset (Merck/O'Neil, DrugComb, AstraZeneca, ALMANAC, CLOUD, FORCINA), synergy metric (Loewe, Bliss, ZIP, HSA), thresholding strategy (arbitrary fixed cutoffs, quartile splits, averaging of multiple metrics), and cross-validation scheme (3-, 5-, or 10-fold; hold-out; leave-one-drug-out; leave-one-cell-line-out).
The authors conclude that direct performance comparison across models is unreliable, and call for a benchmarking study with controlled confounders [@Besharatifard2024].

**Class imbalance and metric choice.** Synergistic combinations are rare relative to non-synergistic ones; AUC-ROC is insensitive to this imbalance.
AUPR (area under the precision-recall curve) is the recommended metric for drug synergy classification tasks.

**GNN limitations.** Four recurring failure modes: (1) high computational cost + data hunger given a sparse experimental landscape; (2) overfitting risk under limited labeled pairs; (3) interpretability gaps — predictions cannot be mechanistically explained; (4) expressivity limits of standard GCNs on heterophilic graphs (nodes of different types connected by diverse edge semantics).

## Methods

This is a narrative literature review, not an original experimental study. The authors searched PubMed, Google Scholar, and Web of Science through July 2023 using the keywords "graph," "drug combination," and "synergy," screening retrieved articles for relevance to GNN-based drug-synergy prediction in cancer. This identified 25 GNN-based models published between February 2020 and July 2023. For comparison, the authors separately compiled non-GNN machine-learning studies on drug-synergy prediction from 2010–2023 (Supplementary Table 1) to contextualize adoption trends.

Table 1 catalogs the benchmark datasets used across the 25 studies: in vitro screening sets (Merck/O'Neil, Oncology Screen, NCI-ALMANAC, AstraZeneca, CLOUD, FLOBAK, YOHE, FORCINA, DrugComb) and four clinical-trial-derived datasets (US FDA-approved combinations, two literature-curated clinical sets, EHR data, DrugBank). Table 2 tabulates, per study: prediction task (classification vs. regression), dataset(s), GNN architecture, input features, strengths, limitations, and code availability. Of the 25 studies, 16 use classification (5 of which also report a regression variant); the remaining 11 classification-only studies are grouped by architecture family — GCN, GAT, and GAE — with one additional study (Lv et al. 2022) using graph regularization. Five studies use clinical data.

Table 3 compiles reported performance (AUC, ACC, AUPR, F1, RMSE/MSE) stratified by validation scheme (3-, 5-, or 10-fold CV; hold-out; leave-one-drug-out; leave-one-cell-line-out), synergy metric (Loewe, Bliss, ZIP, HSA), and thresholding approach. No new models, code, or experiments were produced; this is a secondary literature synthesis and performance-comparison exercise.

## Limitations

The review does not compare GNNs against the strongest non-GNN baselines (e.g., MatchMaker, DeepSynergy, DTF) in a controlled head-to-head study; this gap is acknowledged but deferred to future work.
Performance comparisons across the reviewed models are confounded by dataset selection, synergy metric, and threshold choices — the authors acknowledge this but do not resolve it.
The review ends at July 2023; GNN-based drug-synergy methods published after that date are not covered. (Transformer-based methods are not a gap here — several of the 25 included studies already use transformers, e.g. DTSyn and TranSynergy; the paper does not discuss large language models at all.)
For science/meta purposes, the drug biology claims (which cell-line features matter, which synergy metric is most predictive) are domain-specific and should not be imported into toolkit design reasoning without a domain-transfer justification.
