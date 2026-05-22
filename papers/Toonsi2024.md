---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Toonsi2024
type: paper
title: Causal relationships between diseases mined from the literature improve the use of polygenic risk scores
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Toonsi2024
tags: []
authors:
- Toonsi et al.
datasets:
- dataset:nhgri-gwas-catalog
- dataset:pgs-catalog
- dataset:pubmed-medline
- dataset:uk-biobank
doi: 10.1093/bioinformatics/btae639
ontology_terms:
- causal-disease-relation
- directed-acyclic-graph
- pleiotropy
- polygenic-risk-score
venue: Bioinformatics
year: 2024
---
## Key Findings

1. **Scale.** 8,191 unique directed disease-disease causal relations mined from PubMed; 2,969 supported by more than one sentence; 1,860 unique ICD-10-CM codes involved.

2. **Validation signal is real but modest.** Mined pairs have φ substantially higher than random (Cohen's d = 0.86); 84% expert-estimated accuracy; most pairs satisfy temporality (cause diagnosed ≤ outcome). GPT-4 confirmed fewer than half (3,687/8,191), raising a caution that language-model confirmation is conservative and/or inconsistent.

3. **DAG topology.** Infectious/parasitic and metabolic disease chapters are the largest sources of outgoing causal links, consistent with their role as systemic precursors to multiorgan complications (e.g., type 2 diabetes → retinopathy, atherosclerosis → angina/MI chains are among the top-scored edges and all five top-scoring relations are independently well-documented in the literature).

4. **PRS improvement.** In all three illustrative examples, adding causal-parent PRSs improves patient classification:
   - Heart failure (causes: hypertension, CHD, MI): AUC 0.580 → 0.678 (+0.098)
   - Myocardial infarction (causes: hypertension, CHD): AUC 0.659 → 0.779 (+0.120)
   - Angina pectoris (cause: CHD): AUC 0.655 → 0.784 (+0.129)
   Large-scale analysis (149 diseases, 111 modified PRSs): mean +0.73%, statistically significant.

5. **Derived PRS.** For diseases lacking any PRS in PGS Catalog (cardiomegaly, pulmonary edema), a useful proxy PRS can be synthesized purely from parent-disease PRSs.

6. **Pleiotropy decomposition.** 30/43 (70%) of shared CHD/angina GWAS variants are conditionally independent of angina given CHD — meaning their angina signal is mediated entirely through CHD. APOE and PCSK9 are among the explained variants, internally consistent with the DAG edge familial hypercholesterolemia → CHD → angina.

7. **Eight expert-curated relations** absent from direct text extraction were recoverable as directed paths through the DAG, demonstrating that the network captures transitively implied causal chains beyond direct lexical mentions.

## Limitations

1. **Publication bias.** PubMed abstracts over-represent well-studied disease pairs. Diseases with little literature will have few mined causal edges, not because they lack causal structure but because that structure is not described in accessible text. This is the directed analog of the publication-gravity problem the pan-disease project has characterized on the undirected gene axis.

2. **Lexical pattern limitations.** False positives arise from complex sentence structure (negations, hypotheticals, conditional language); false negatives arise from causal language not covered by the pattern set. The 84% expert accuracy estimate was obtained from a curated sample and may not be representative of tail distributions (rare diseases, cross-chapter pairs).

3. **GPT-4 instability.** The paper notes that GPT-4 gave conflicting answers on repeated queries for the same relation (hypertension → acute kidney failure example). The LLM-confirmation score is therefore noisy and potentially not monotone with true causal confidence.

4. **Cycle-breaking introduces ambiguity.** The greedy score-based cycle removal is arbitrary — another scoring scheme would produce a different DAG. 602 removed edges could include real causal relations in biological feedback loops (e.g., depression ↔ chronic pain are genuinely bidirectional). The resulting DAG should be treated as one plausible acyclic projection of a cyclic truth, not as authoritative causal structure.

5. **Equal weighting of five measures.** The combined score weights φ, dependence, temporality, annotation count, and GPT-4 confirmation equally. There is no principled justification for this; a weighted combination could perform differently. In particular, φ is a global co-occurrence measure from UKB, which has its own ascertainment biases (40–69 year-old UK volunteers, predominantly white British).

6. **ICD-10-CM scope.** ICD-10-CM is clinically oriented and excludes many molecular or sub-clinical disease entities relevant to the gene-axis. Crosswalking to MeSH or Disease Ontology will be lossy; some MeSH diseases will have no ICD-10-CM analog and vice versa.

7. **PRS results are proof-of-concept scale.** The illustrative cardiovascular PRS examples (three diseases) demonstrate the principle but are not a systematic benchmark. The 0.73% mean large-scale AUC gain, while statistically significant, is practically small and heterogeneous — some diseases may benefit substantially, others not at all.

8. **Restricted to binary disease outcomes.** The framework cannot handle quantitative traits or disease severity gradations, limiting its applicability to threshold-coded ICD diagnoses.
