---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Pelissier2023
type: paper
title: Convergent evolution and B-cell recirculation in germinal centers in a human lymph node
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Pelissier2023
tags: []
datasets:
- dataset:pelissier2023-vdj
ontology_terms:
- B-cell recirculation
- BCR repertoire
- antibody affinity maturation
- clonal selection
- convergent evolution
- germinal center
- somatic hypermutation
---
## Key Findings

### GC diversity and independence
- Each GC is a distinct evolutionary environment: inter-GC Sorensen-Dice similarity <0.1 (very low sequence overlap), in contrast to high within-GC replicate concordance.
- Clonal dominance (proportion of most abundant clone) ranges from ~5% (GC9) to ~30% (GC10) across the 10 GCs — substantial heterogeneity in competitive dynamics.
- Diversity metrics (dominance, richness, evenness, Shannon entropy) vary substantially across GCs and are not explainable by sample size differences.
- Three V genes — IGHV1-18, IGHV1-2, IGHV2-5 — are enriched in the top 15 dominant clones relative to public LN and bone marrow databases, consistent with positive antigen-driven selection during the ongoing GC reaction.

### Non-functional BCR alleles and SHM crippling mutations
- ~90% of sequences are functional; 78% of non-functional sequences result from V(D)J frameshift; the remainder are approximately equally split between SHM-induced stop codons and V(D)J recombination-derived stop codons.
- Non-functional clone proportion ranges 10-25% across GCs.
- SHM mutational spectrum is **selection-independent** (stochastic): no significant difference in mutation position or nature between functional and non-functional clones, though expanded functional dominant clones show elevated R/S ratio in CDRs versus singleton sequences — confirming ongoing affinity-maturation selection.
- On average **3.6 mutations** accumulated in functional alleles before a crippling SHM mutation occurred (inferred from phylogenetic trees) — roughly one mutation per two cell divisions.
- SHM-induced crippling mutations cluster on V genes known to be involved in stereotypic rearrangements in B-cell malignancies (IGHV1-8, IGHV1-2, IGHV3-23, IGHV4-34, IGHV2-5), suggesting the same V genes that are susceptible to autoimmune and oncogenic recombination are sites of elevated SHM-induced crippling in the GC.
- The Y59* crippling mutation occurred independently in **five** clones using the IGHV3 gene — a concrete multi-hit example of convergent deleterious mutation.

### B-cell recirculation across GCs
- **10.8%** of functional clones (396/3,650) are shared in at least two GCs (identified in both NGS replicates for robustness).
- Distribution of clones across numbers of GCs fits a **Poisson process** (mu = 0.25): the reactivation of a B cell in a different GC is a memoryless stochastic event where the evolutionary history of the cell plays no role.
- From the Poisson fit: the probability that a given clone seeds at least one other GC during the whole GC reaction is P(N>=1) = 1 - e^(-0.25) ≈ **22%**.
- Using a 20-day GC lifetime (NP-CGG immunization model) as reference, the estimated reactivation rate is **lambda = 0.25/20 = 0.0125 seeding events per clone per day**. This is an upper limit — GC lifetimes of 100-200+ days in chronic/viral settings would reduce this substantially.
- Only 5% of shared clones achieve dominance >0.1% in more than one GC — recirculating clones typically face a disadvantage in new GCs where established dominant clones are already competing.
- CDR3 sequences are shared between GCs at only **2%** (38/1,885) — much lower than full clone sharing (10.8%) — confirming that CDR3 continues to mutate after B-cell recirculation in the new GC environment.
- Phylogenetic analysis of shared clone IGHV1-2_63_IGHJ6 (expanded with dominance >1% in both GC8 and GC1): GC8 sequences are closer to the unmutated germline root, GC1 sequences are more mutated, consistent with GC8 seeding GC1 and the clone undergoing further affinity maturation after transfer — direct evidence of evolutionary divergence post-recirculation.

### Convergent epitope reactivity across GCs
- Using the combined CDR similarity + Paratype + Ab-Ligity scoring: a minority of dominant clones across GCs are predicted to bind common epitopes, increasing with the number of dominant clones considered (approaches ~1,000 predicted pairs when top 300 clones per GC are included).
- The paratope distance distribution is **very similar within and across GCs**, with only a slightly lower average paratope distance within GCs — suggesting evolutionary convergence forces are comparable in magnitude whether operating within a single GC or across the whole LN.
- Estimated number of epitopes in the LN reaction: ~5,000 total, with each GC specializing on ~1,000 epitopes on average (statistical model). Approximately 500-5,000 epitopes are estimated to be shared across GCs.
- Four illustrative convergent clone pairs across distinct GCs (Figure 5A) show: CDR3 similarity 0.63-0.74, CDR1/2 nearly identical, paratype scores 0.76-0.92, despite arising from different V and/or J genes — convergent antibody structure driven by shared antigen.

### No quantitative selection-coefficient estimates
The paper does **not** provide direct selection coefficient (s) estimates. Selection pressure is inferred qualitatively via the R/S ratio (replacement/silent mutation ratio in CDR regions) — elevated R/S in expanded functional dominant clones vs. singletons confirms positive selection is acting, but no numerical s is derived. The Poisson-based reactivation rate (lambda = 0.0125/clone/day at 20d GC lifetime) is the closest quantitative evolutionary parameter, but it describes a dispersal rate, not selection strength per se.

## Limitations

- **Single patient, single LN.** All 10 GCs are from one individual; all quantitative parameters (clone sharing rate, diversity, convergence frequency) are from a single snapshot with unknown antigens. Replication in additional patients and tissues (tonsil, Peyer's patches) is needed.
- **No scRNA-seq or scATAC-seq.** The study is BCR-sequence-only from gDNA. Transcriptional states, differentiation stages, and cell-surface phenotypes of individual B cells are entirely absent. The GC/centroblast/centrocyte distinction, the memory vs. plasma cell fate decision, and any transcriptional plasticity are not characterized.
- **No direct antigen identification.** The LN reacts to unknown natural antigens. Convergent paratopes are inferred computationally (Parapred + Ab-Ligity); actual epitope identity is not established. Epitope count estimates (500-5,000) are statistical model outputs with acknowledged high uncertainty.
- **No selection coefficient quantification.** The paper demonstrates selection via R/S ratio enrichment but does not derive numerical selection coefficients. The Poisson reactivation rate (lambda = 0.0125/clone/day) is an upper bound derived from a 20-day GC lifetime assumption that may be very wrong for chronically activated human LN.
- **GC lifetime is unknown for this patient.** The LN is from a patient with chronic sialadenitis; GC reaction duration may be months to years, making the 20-day-based rate estimate a substantial overestimate.
- **gDNA-based clone frequencies.** gDNA gives one V(D)J rearrangement per B cell (one count = one cell), which is more accurate than mRNA for frequency estimation, but LCM efficiency may vary across GC sections.
- **Cancer analogy is by homology, not mechanism.** GC convergent evolution arises from shared antigenic selection on antibody structure. Cancer convergent evolution arises from shared fitness landscapes acting on somatic mutations. The mechanistic substrate (SHM vs. random somatic mutation; antigen vs. microenvironment vs. therapy selection) differs; quantitative parameters may not transfer directly.
- **No longitudinal data.** Cross-sectional snapshot of a single ongoing GC reaction; the temporal dynamics of clonal succession, recirculation timing, and convergence emergence cannot be resolved.
