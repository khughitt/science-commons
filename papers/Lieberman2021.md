---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Lieberman2021
type: paper
title: Oncogenic Viruses as Entropic Drivers of Cancer Evolution
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Lieberman2021
tags: []
datasets: []
ontology_terms:
- entropy
- epigenetic reprogramming
- gene regulatory network
- phenotypic plasticity
- tumor heterogeneity
- viral oncogenesis
---
## Key Findings

**Entropy operationalization:** The authors define "genetic entropy" informally as the ability to reconfigure the genome and its programmed processes. They decline to give a rigorous biological definition but anchor the concept in two frameworks: (a) statistical mechanics — entropy as the count of accessible microstates; (b) Shannon information theory — viral genomes as signal noise that expands output diversity of GRNs. The claim is explicitly a heuristic, not a quantitative thermodynamic argument.

**Viruses amplify, rather than replace, endogenous variation:** The paper consistently frames viral infection as working *in addition to and in synergy with* cellular mutation processes. Viral heterogeneity (copy number variation, latency type switching, abortive lytic reactivation) layers additional variation on top of somatic mutation. EBV-NPC fishplot data (Figure 3) illustrate early viral gene expression changes (EBNA2/3, LMP1/2) that precede cellular mutations (3p/9p loss, PI3K/MAPK), suggesting that viral contributions front-load phenotypic variation at early tumor stages while cellular mutations accumulate later — an *amplification/front-loading* model, not a replacement model.

**Viral mechanisms that generate variation:**
- *Integration mutagenesis:* HPV integrates at TERT and ERBB2/PTPN13 loci; HBV at TERT and KMT2B/MLL4; HTLV-1 integration as part of normal life cycle is constitutively mutagenic. Integration can disrupt tumor suppressors, dysregulate viral oncogenes (HPV E6/E7 upregulated on loss of E2 repressor), and introduce structural variants.
- *Episomal maintenance and copy number variation:* EBV, KSHV, HPV, MCPyV persist as episomes; genome copy number per cell (1 to ~100 for EBV) varies and drives heterogeneous viral gene expression. Episomal tethering to host chromatin can be dynamic, providing epigenetic plasticity.
- *Oncoprotein expression heterogeneity:* Variable expression of LMP1 (100-fold range across single NPC cells), EBNA2, abortive lytic cycle genes — these are inherently stochastic and provide a source of non-genetic phenotypic variation independent of host mutation.
- *Epigenomic reprogramming:* Viral infection alters DNA methylation (host hypermethylation in HPV/EBV carcinomas), histone modifications, and chromosome conformation (EBV tethering reinforcing H3K9me3 or switching H3K9me3 → H3K4me3 zones). This creates heritable epigenetic variation.
- *GRN destabilization:* Viral oncoproteins perturb major hubs in GRNs (EBNA2 cooperativity with RBPJ, EBF1, RUNX1; LANA binding to core histones H2A/H2B; EBNA2 super-enhancer formation at cMyc). Destabilizing GRN hubs increases signal noise and enables transitions between attractor states.
- *Immune evasion as selection enabler:* PD-L1/PD-L2 upregulation (HPV, EBV), HLA downregulation (HPV E5), and recruitment of regulatory T-cells (EBV LMP2, KSHV) reshape the selective microenvironment so that viral-infected cells with higher plasticity are preferentially retained.

**Viruses vs. cellular oncogene interchangeability:** The authors argue that viral oncogenic activities may be replaced by cellular mutations at later tumor stages (Figure 2, EBV-NPC model). Early stages rely on viral gene expression; later stages accumulate cellular mutations (Myc translocations, NF-kB, PI3K activation) that can substitute for viral functions. This implies viruses provide "lower cost pathways to cellular oncogenesis" — kinetically fast, heterogeneous, and reversible routes to the oncogenic attractor that are eventually superseded by genetically fixed cellular drivers.

**Waddington landscape model (Figure 4):** Normal developmental landscape has one primary attractor (differentiated state) and non-viable saddle points. Viral tumor landscape features multiple stable attractors (M1, M2) with favorable thermodynamic properties and increased Darwinian fitness. Viral-borne adaptability is described as the "entropic driver" that opens these new attractor regions.

**Therapeutic implication — amplifying entropy to lethal levels:** Since excessive genetic variability can be incompatible with life, the paper speculates that amplifying viral-induced plasticity through epigenetic modifier drugs could provoke chaotic and lethal gene expression patterns selectively in cancer cells. This is the flip side of q010 (optimal instability): push variance past the upper tolerance threshold.

## Limitations

- The "entropy" framing is explicitly acknowledged by the authors as informal and heuristic — they do not provide a formal biological definition, a quantitative measure, or an empirical test of the entropy claim. The concept risks being unfalsifiable as stated.
- The paper does not quantitatively compare the magnitude of viral-generated variation against endogenous mutation processes. The claim that viruses *amplify* (rather than replace or operate orthogonally to) somatic mutation is supported by the EBV-NPC temporal model, but this is one cancer type and the relationship may not generalize.
- The Waddington attractor-state model (Figure 4) is illustrative rather than parameterized; no dynamical systems evidence (e.g., bifurcation analysis of EBV-infected GRNs) is presented to support the claim that viral infection creates genuinely new attractor states vs. merely widening existing basins.
- The seven oncoviruses covered are heterogeneous in mechanism (DNA vs. RNA viruses, integrating vs. episomal), and the paper acknowledges that the "entropy" framing applies differently across them. HCV, for example, does not infect the cancer cell directly — its entropic contribution is through inflammation rather than direct GRN perturbation.
- No causal inference framework is applied to distinguish viral-driven variation from selection of pre-existing host variants. The temporal ordering in Figure 2 (viral early, cellular late) is a hypothesis, not measured in individual tumors.
- Therapeutic speculation (lethal entropy amplification via epigenetic modifiers) is not supported by in vivo experiments in this paper; it is a logical extrapolation.
