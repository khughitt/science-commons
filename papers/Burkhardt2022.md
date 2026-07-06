---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Burkhardt2022
kind: paper
title: Mapping Phenotypic Plasticity upon the Cancer Cell State Landscape Using Manifold
  Learning
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Burkhardt2022
tags: []
ontology_terms:
- EMT
- RNA velocity
- attractor states
- cancer heterogeneity
- cell state landscape
- diffusion maps
- manifold learning
- non-genetic adaptation
- optimal transport
- phenotypic plasticity
- pseudotime
- single-cell omics
- state-gating therapy
- trajectory inference
---
## Key Findings

This is a review; findings are framed as the authors' synthesis of the literature rather than new empirical results.

### Conceptual framework claims

- **(C1) Cancer cells occupy a continuous phenotypic state space, not discrete clusters.** The landscape metaphor — from Waddington, revisited by Huang — provides a thermodynamic/informational description in which high-density regions of phenotypic state space are "attractor states" (stable cell states) and low-density regions between them are "transition channels" (canalising features enabling plastic transitions). Cell-state heterogeneity arises from the stochastic traversal of this landscape.

- **(C2) Phenotypic plasticity is a non-genetic, dynamic, reversible process that amplifies heterogeneity faster than clonal selection can.** The review explicitly distinguishes plasticity (epigenetic / transcriptional / translational program switching, operating on timescales of hours to days) from genetic mutation and clonal expansion (timescales of weeks to months). Regulation by specific molecular programs (e.g., ZEB1 bivalent chromatin configuration, SNAI1/polycomb/HDAC2 chromatin-silencing axis for CDH1) makes plasticity tractable to therapeutic targeting.

- **(C3) The EMT axis and its hysteretic dynamics are the best-characterised plasticity program.** EMT at the primary site increases metastatic potential; partial MET at the metastatic site enables colonization — meaning both forward (E→M) and reverse (M→E) plasticity are required for the full metastatic cascade. The miR200–ZEB1 bistable feedback loop demonstrates hysteresis: a 5-minute TGFβ pulse can lock ZEB1 activation for days, raising metastatic potential in a time-irreversible way. Three types of state transition are distinguished: bidirectional (A↔B), reversible single-cell (A→B→A), and asymmetrical (path-dependent trajectories).

- **(C4) Plasticity programs extend well beyond EMT** to include metabolic plasticity (fatty acid synthesis upregulated in brain mets; pyruvate carboxylase dependence in lung mets), immune-evasion plasticity (dormancy-associated immune-cloaking via upregulated immune genes; PD-L1 upregulation via ZEB1 in EMT), dormancy/senescence escape (slow-cycling cells reenter via CDK reactivation, stemness markers, ECM niche changes), and drug-resistance plasticity (chemotherapy actively induces EMT and resistant states, not merely selects pre-existing resistant clones).

- **(C5) Manifold learning can recover landscape topology from scRNA-seq data.** The intrinsic dimensionality of the phenotypic manifold is far lower than the ~20,000-dimensional measurement space due to gene coregulation and informational redundancy. Diffusion geometry, optimal transport, and VAE-based methods each recover complementary aspects of this topology: global trajectory geometry (diffusion maps, TrajectoryNet), local velocity (RNA velocity), continuous phenotypic spectra (archetypal analysis), and denoised state representations (VAEs). Together they enable clustering, pseudotime ordering, trajectory inference, and archetypal decomposition of cell state heterogeneity (Fig. 1E).

- **(C6) The landscape topology is itself mutable — this motivates "state-gating" therapy.** Chemotherapy actively remodels the landscape (Fig. 3B), activating E→E/M transition channels and inhibiting E/M→E reversal, increasing the hybrid/mesenchymal population. State-gating strategies could counteract this by: (i) activating E/M→E reversal to restore chemosensitive states (Fig. 3C); (ii) blocking E→E/M transition (Fig. 3D); or (iii) inhibiting E/M self-renewal (Fig. 3E). The Krishnaswamy group has a pending patent on methods of treating cancer based on these principles (PCT/AU2020/051146), and a phase I/II clinical trial (4CAST) is anticipated.

- **(C7) Stochastic noise level is itself an evolvable meta-property.** The level of stochastic jittering (effectively cellular information-processing noise) influences how readily cells traverse landscape topologies with multiple local minima. Stress-induced chromosomal instability raises mutation rates and therefore increases transcriptional heterogeneity — suggesting that the *noise parameter* of the landscape is itself under evolutionary control, linking genetic instability to non-genetic plasticity.

### Limitations acknowledged in the paper

- Clinical implementation of cell-state assays is currently limited to IHC panels of 1–3 proteins; defining phenotypic states clinically in a sufficiently systematic way to guide state-gating therapy is not yet possible.
- Manifold learning is limited in settings with very small or disconnected datasets; bulk sequencing data (~20 samples) cannot support manifold inference and requires classical statistical testing instead.
- Current optimal transport and RNA velocity models (TrajectoryNet, Waddington OT) are deterministic — two cells with identical transcriptional profiles produce identical predicted futures, missing posttranscriptional regulatory divergence. Stochastic differential equation extensions are proposed as improvements.
- Temporal and spatial dimensions of plasticity (e.g., how a transient EMT signal at the primary site maintains a stable metastatic phenotype after transit) are only beginning to be resolved; the review calls for integrated spatial-temporal single-cell experimental designs.

## Limitations

### As a review (methodological)

- No primary data; all empirical claims are drawn from cited literature. The review curates a perspective on what is emerging, but the mechanistic claims require verification against the primary experimental papers cited (many of which are in breast cancer / melanoma model systems).
- Cancer-type breadth is uneven: EMT-plasticity coverage is dense (breast, prostate, colon, NSCLC, melanoma, esophageal carcinoma referenced), but hematologic malignancies and pediatric cancers are largely absent.
- The "state-gating therapy" concept is framed as a future vision, not yet validated in clinical trials. The 4CAST trial (phase I/II) was anticipated at time of publication but results are not reported here.

### Conceptual gaps the paper itself acknowledges

- The review does not address how plasticity-derived non-genetic variation couples to genetic mutation acquisition — the critical juncture for H004 and H005. The question of whether plastic states are more or less mutagenic is noted as open.
- Spatial resolution: current technologies cannot yet fully resolve how spatial position within a tumor modulates landscape topology at single-cell resolution simultaneously with rich molecular profiling.
- The review does not address cross-cancer-type generalizability of the specific landscape topologies described (EMT-centric in breast / carcinoma contexts; metabolic plasticity scope may differ in hematologic contexts).
