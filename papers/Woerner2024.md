---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Woerner2024
kind: paper
title: Uncovering genetic associations in the human diseasome using an endophenotype-augmented
  disease network
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Woerner2024
tags: []
authors:
- Woerner et al.
doi: 10.1093/bioinformatics/btae126
ontology_terms:
- disease-disease-network
- endophenotype
- genetic-correlation
- pleiotropy
- shared-SNP
venue: Bioinformatics
year: 2024
dataset_usage:
- ref: dataset:uk-biobank
  role: analyzed
  overlap: unknown
---
## Key Findings

1. **242% edge increase from endophenotype augmentation.** ssDDN has 645 edges (estimated from context); ssDDN+ adds 1,561 indirect edges. The proportion of cross-category edges rises from 75% to 85%, showing that endophenotypes preferentially link diseases from different organ systems.

2. **24 previously isolated diseases gain connections.** Diseases with no shared genome-wide-significant SNPs with any other disease nonetheless have significant genetic correlations with biomarkers shared by other diseases, recovering them from isolation. GERD is highlighted as a specific example — zero connections in the ssDDN, one of the highest degree ranks in the ssDDN+ (despite ~31% heritability and known risk genes FOXF1, MHC, CCND1).

3. **Non-uniform augmentation across disease categories.** The musculoskeletal category gains the largest proportional increase in edges (relative doubling), consistent with known metabolic co-morbidities of musculoskeletal degradation. Neoplasms and sense organs gain relatively few edges. Hematopoietic, endocrine/metabolic, and circulatory categories gain a high proportion of new connections, reflecting the systemic nature of those disorders.

4. **HDL-C is the dominant endophenotype bridge.** Of 31 biomarkers, HDL-C contributes 996 new edges in the full ssDDN+ — the largest contribution by a wide margin — and 70 new edges in the cardiometabolic subnetwork alone. Triglycerides also add a substantial number. Some biomarkers (e.g., phosphates) contribute zero new edges. This differential contribution is a key result: not all biomarkers carry equal information for disease network structure.

5. **Cardiometabolic subnetwork is substantially enriched.** In the cardiometabolic subnetwork (endocrine/metabolic + circulatory system phenotypes), endophenotype augmentation adds 144 genetic correlations, increasing edge count from 116 to 200. Heart failure (phecode 428.2), with no connections at all in the ssDDN, gains 54 disease connections in the ssDDN+. Other newly connected diseases include obesity, type 1 diabetes, chest pain, and precordial pain — all conditions whose polygenic architecture is partially captured through shared biomarker correlations.

6. **Direct and indirect edges are complementary, not redundant.** Of the 1,561 new indirect edges, 116 overlap with pre-existing direct edges, suggesting some genome-wide significant shared SNPs do operate through biomarker-associated pathways. The majority (~93%) of indirect edges, however, are novel associations not recoverable from genome-wide SNP sharing alone. A density plot of direct vs. indirect edges in network space confirms they occupy substantially different regions.

7. **Degree rank shifts reveal biology.** Hyperlipidemia retains the top degree rank in both networks (driven by Mendelian effects of LDLR/APOB/PCSK9 and lipid biomarker associations). Skin cancer, a hub in the ssDDN due to neoplasm-shared SNPs, does not gain edges in the ssDDN+, consistent with the known poor utility of blood biomarkers for skin cancer prognosis. GERD rises sharply in the ssDDN+.

## Limitations

- **UK Biobank European ancestry only.** The entire analysis is limited to British European-ancestry individuals. All conclusions about disease network structure may not generalize across ancestries. The authors explicitly note that MVP and All of Us data could provide future validation.

- **Unweighted, undirected edges lose quantitative information.** The ssDDN+ adds a binary edge if any FDR-significant biomarker correlation links two diseases, regardless of the number of biomarkers linking them or the magnitude of correlations. This discards potentially useful graded signal and means the network topology cannot distinguish a disease pair linked by one borderline correlation from one linked by five strong correlations.

- **Endophenotype set limited to 31 biomarkers.** The choice of biomarkers was driven by data availability (Neale Lab UKBB summary statistics), not biological completeness. Many relevant intermediate phenotypes (inflammatory markers, proteomic traits, microbiome features) are absent. The paper itself notes that richer biomarker panels would likely yield additional edges.

- **FDR threshold applied separately from the shared-SNP threshold.** The two edge types (direct shared-SNP, indirect biomarker-correlation) use different evidence standards. A genome-wide significant SNP at 5 × 10⁻⁸ is a very strong signal; an FDR < 0.05 LDSC genetic correlation can be driven by small but consistent genome-wide signal. The two edge types are treated symmetrically in the final graph, which may conflate very different confidence levels.

- **No causal inference.** The ssDDN+ captures genetic correlation — a symmetric, undirected measure. It cannot distinguish whether Disease A causes Biomarker B which causes Disease C from a shared genetic architecture that simultaneously influences all three. The authors acknowledge that Mendelian randomization is needed and flag it as future work.

- **Phecode system imperfections.** Phecodes aggregate ICD-9 codes and can miscategorize or aggregate heterogeneous disease presentations. Edge conclusions inherit these classification artifacts.

- **Two separate PheWAS pipelines.** The binary and quantitative PheWASs differ in sample size (~400K vs ~361K) and SNP count (~28M vs ~13.7M), harmonized down to ~1.2M HapMap3 variants with pre-computed LD scores. The harmonization is valid but reduces power relative to what a jointly processed dataset would provide.

- **Categorically constrained biomarkers.** The choice to use only 31 UKBB blood/urine biomarkers with pre-computed LDSC summary statistics means disease categories without strong biomarker correlates (neoplasms, sense organs) are structurally disadvantaged — not because they lack multimorbidity, but because their biology is not well-captured by these particular biomarkers.
