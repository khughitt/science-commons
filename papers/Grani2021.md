---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Grani2021
type: paper
title: A network-based analysis of disease modules from a taxonomic perspective
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Grani2021
tags: []
authors:
- Grani et al.
datasets:
- dataset:disease-ontology
- dataset:disgenet
- dataset:human-interactome-barabasi
doi: 10.48550/arXiv.2104.00386
ontology_terms:
- Lin-semantic-similarity
- disease-module
- interactome-taxonomy
- taxonomy-alignment
venue: arXiv (q-bio.MN) — preprint
year: 2021
---
## Key Findings

**1. Selected I-T vs. DO cosine similarities.** The four I-T variants all score significantly above random (random baseline ~29.84%): Induced+Average = 46.33%, LCC+Average = 39.94%, Induced+Complete = 43.59%, LCC+Complete = 39.84%. Induced+Average is the best-performing configuration and is used for all downstream analyses.

**2. Top-level DO category correspondence (Table II).** DO categories differ greatly in how well they map to the interactome-induced taxonomy:
   - "Disease of cellular proliferation" (255 diseases): label score 54.77%, p = 3.14×10⁻²⁰ — the strongest match; cancer/proliferative diseases are highly co-localized in the interactome.
   - "Disease of anatomical entity" (434 diseases): label score 50.05%, p = 0.08 — high similarity but NOT statistically significant. Diseases grouped by anatomical location are scattered across the network, not co-localized.
   - "Genetic disease" (12 diseases): label score 41.66%, p = 6.14×10⁻¹⁰ — strong match; genetic diseases form tight interactome neighborhoods.
   - "Disease by infectious agent" (10): 30.0%, p = 1.92×10⁻⁷.
   - "Physical disorder" (21): 26.09%, p = 1.51×10⁻⁹.
   - "Disease of mental health" (76): 21.51%, p = 1.06×10⁻¹³.
   - "Syndrome" (42): 21.27%, p = 8.69×10⁻¹¹.
   - "Disease of metabolism" (55): 16.36%, p = 4.66×10⁻¹¹.

**3. Anatomical classification is molecularly unsupported.** A systematic pairwise comparison of DO sub-categories within "disease of anatomical entity" confirms that anatomically grouped disease sub-categories "very rarely" have overlapping I-T clusters, with expected exceptions (nervous/respiratory systems, gastrointestinal/cardiovascular systems). Conclusion: the anatomical classification principle does not correspond to network-based disease proximity, at least given current disease-gene association knowledge.

**4. Unexplored structural molecular relationships between disease categories.** The I-T surfaces strong molecular neighborhoods for disease categories whose members appear distant in human-curated taxonomies. Clinical experts reviewing the I-T found cross-taxonomy connections including:
   - Glaucoma and pulmonary arterial hypertension (validated by Gupta et al. 2020: shared secondary open-angle glaucoma and serous macular detachment molecular mechanisms).
   - Cholestasis and COPD (validated by Tsechkovski et al. 1997: mediated by Alpha 1-antitrypsin).
   - Peroxisomal diseases and ciliopathy-related syndromes (validated by Miyamoto et al. Zaki et al. 2016: Pex6 in Joubert/Bardet-Biedl/Jeune syndromes).
   These cross-category molecular relationships are detectable in the I-T but absent from the DO.

**5. Nomenclature errors in DisGeNET detected.** By looking for "unconvincing" high-Jaccard matches between I-T and R-T categories — cases where disease modules are suspiciously similar yet the diseases have different names — clinical experts identified nomenclature errors in DisGeNET. Examples:
   - "Hyper-IgM immunodeficiency syndrome" types 1/3/5 are incorrectly linked to the same three gene associations (AICDA, CD40, UNG) in DisGeNET, when each type is defined by mutations in only one of those genes.
   - "Obstructive lung disease" shares 12 disease-gene associations with pulmonary emphysema sub-entities (focal, panacinar, centrilobular emphysema) — all traceable to a single publication about pulmonary emphysema in general.
   - "Bone remodeling disease" shares the same gene-disease associations for osteoporosis, age-related osteoporosis, post-traumatic osteoporosis, and senile osteoporosis.

**6. Coverage limit.** Only ~12% of DO diseases were covered in the induced taxonomy (948/10,012), because the current interactome's disease-gene knowledge is incomplete. This limits the mapping between the I-T and DO, and may explain some undetected molecular relationships.

## Limitations

- **Interactome incompleteness is the dominant constraint.** Only ~12% of DO diseases (948 of 10,012) could be included in the I-T because the human interactome's disease-gene association coverage is sparse. Undetected molecular relationships may exist for the 88% not covered.
- **Disease module definition sensitivity not fully resolved.** The paper tests 4 I-T variants (2 DM definitions × 2 linkage methods) but selects one configuration post-hoc based on similarity to the DO — introducing mild circularity if the DO similarity score is also used to interpret results.
- **GDA score threshold choice (≥ 0.3) is asserted but not sensitivity-tested.** Different score cutoffs could materially alter which genes are included in each disease module and therefore which diseases cluster together.
- **Gene-set size threshold (≥ 10 genes) excludes rare/understudied diseases.** Rare diseases often have highly specific gene-disease associations of greatest interest for taxonomy refinement.
- **Clinical validation of unexplored relationships is manual and selective.** The paper relies on clinical experts reviewing a visualized I-T and searching supporting literature for a small number of identified cross-category pairs. This is not a systematic evaluation.
- **Preprint status (arXiv).** The paper is a preprint (arXiv:2104.00386v1, April 2021); peer review status is unclear as of the paper date.
