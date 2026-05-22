---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Wang2024Pathway
type: paper
title: A Probabilistic Approach to Estimate the Temporal Order of Pathway Mutations Accounting for Intra-Tumor Heterogeneity
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Wang2024Pathway
tags: []
datasets:
- dataset:tcga
ontology_terms:
- cancer progression
- intra-tumor heterogeneity
- maximum likelihood
- mutation ordering
- pathway-level evolution
- probabilistic model
- tumor phylogenetics
---
## Key Findings

**Colon cancer (COAD).** Without ITH, the prior method (Wang et al. 2019) incorrectly placed p53 signaling before PI3K-Akt signaling — contradicting biological literature. With ITH via PATOPAI, the inferred order is Wnt → MAPK → Apoptosis → PI3K → p53 → TGF-beta, which correctly positions p53 as a late event (following pro-growth pathway mutations) and matches the canonical colorectal carcinogenesis model. The discrepancy arose because p53 pathway mutations are predominantly subclonal (late arising), so ignoring ITH systematically inflates their apparent ordering priority.

**Hepatocellular carcinoma (HCC).** Calcium signaling → MAPK → Wnt → p53 → TGF-beta → PI3K-Akt → Cell cycle. Calcium signaling and growth/proliferation pathways (MAPK, WNT) are early; p53 and downstream signaling are mid-to-late. Consistent with biological evidence for early calcium signaling alterations in HCC initiation and MAPK as the most critical HCC oncogenic pathway (~50% of cases).

**Glioblastoma multiforme (GBM).** Calcium signaling → MAPK → ErbB → p53 → Cell cycle → mTOR. Calcium signaling is again an early event, consistent with its known role in glioma progression and prior evidence that calcium-related alterations occur in normal glial development and low-grade gliomas. Cell cycle alterations (e.g., CDKN2A deletions) are positioned as late events, concordant with a recent study associating acquired CDKN2A deletions with GBM recurrence.

**Pancreatic adenocarcinoma (PAAD).** Apoptosis → ErbB → p53/MAPK (parallel) → PI3K-Akt → TGF-beta → Cell cycle → Jak-STAT → VEGF. MAPK is correctly recovered as an early event (consistent with >90% KRAS mutations in PanIN-1 lesions and prior literature). TGF-beta is a late event (consistent with TP53/SMAD4 mutations in PanIN-3). One discordance: cell cycle signaling was placed at a lower temporal order than expected from CDKN2A biology (active in PanIN-2), which the authors attribute to heterogeneity in cell cycle pathway mutation timing.

**Method comparison.** On COAD, OncoTree correctly recovered MAPK before PI3K/p53/TGF-beta but failed to position Wnt as the first event and could not order p53 vs. PI3K/TGF-beta. Youn & Simon placed MAPK first (correct) but Wnt fourth (incorrect) and produced incorrect PI3K/TGF-beta ordering. PATOPAI was the only method to recover the complete canonical colorectal ordering.

**Computational efficiency.** Pairwise analysis with tree merging and parameter stabilization reduced run time by approximately half compared to the naive approach (371 s vs. 732 s on PAAD MAPK/TGF-beta pair).

## Limitations

- **No subtype resolution.** All four cancer types are analyzed as monolithic cohorts; cancer subtypes (e.g., MSI vs. MSS colon cancer, IDH-mutant vs. IDH-wild-type GBM) likely differ in pathway ordering and are conflated. The authors explicitly flag this as future work.
- **Cross-sectional design.** All inferences are from single time-point surgical samples; the "temporal order" is inferred statistically across patients, not observed longitudinally within patients. The method assumes a shared progression trajectory across the cohort.
- **ITH input dependency.** Results depend on the accuracy of the upstream phylogenetic tree reconstruction (PhyloWGS here). Errors or poor resolution in tree structure propagate into ordering inferences. Single-cell sequencing inputs could improve ITH characterization but were not used (bulk WES only).
- **Non-overlapping pathway assumption.** When pathway gene sets overlap, the method requires reorganizing genes into mutually exclusive sets; this is handled per the prior Wang et al. 2019 method but introduces some sensitivity to pathway definitions and curation choices.
- **Computational cost.** Pairwise analysis of many pathways is still computationally intensive (up to 506 min per pair in extreme cases); scaling to large gene sets or finer pathway resolution may be prohibitive.
- **PAAD discordance.** Cell cycle pathway ordering in pancreatic cancer contradicts known CDKN2A early-lesion biology — a case where the model's inferences disagree with well-established literature, suggesting the method is not uniformly reliable across all cancer-pathway combinations.
- **Hypermutator exclusion.** Top 16% of hypermutated colon cancer samples are excluded; hypermutator biology (e.g., MSI-high) may follow a distinct mutation ordering regime that the method cannot currently address.
