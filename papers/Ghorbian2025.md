---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Ghorbian2025
type: paper
title: 'Cancer cell plasticity and therapeutic resistance: mechanisms, crosstalk, and translational perspectives'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Ghorbian2025
tags: []
datasets: []
ontology_terms:
- cancer cell plasticity
- cancer stem cells
- drug-tolerant persisters
- epigenetic reprogramming
- epithelial-mesenchymal transition
- lineage plasticity
- metabolic reprogramming
- non-coding RNA
- therapeutic resistance
- tumor microenvironment
---
## Key Findings

### Plasticity mechanism taxonomy (the five arms)

The paper organizes cancer cell plasticity into a set of interacting programs:

1. **EMT/MET.** EMT drives invasion and metastasis via cytoskeletal remodeling, loss of epithelial polarity, and gain of mesenchymal traits. The reverse (MET) enables colonization at distant sites. EMT is not a binary switch but a spectrum of partial (meta-stable) states. Key transcription factors: Snail/SNAI1-3, Slug/SNAI2, Twist1/2, ZEB1/ZEB2. Key upstream pathways: TGF-β (Smad-dependent and non-Smad), Wnt/β-catenin, Notch, RTKs, PI3K/AKT/mTOR. miR-200 family and miR-34A suppress EMT and form feedback loops with ZEB1/2.

2. **Dedifferentiation / Lineage plasticity.** Encompasses neuroendocrine differentiation (NED) from adenocarcinoma (prostate NEPC, NSCLC→SCLC), melanocyte-to-neural-crest stem cell (NCSC) transitions, and lineage switching. Key drivers: loss of TP53 + RB1 (necessary but not sufficient for NED), SOX2 (neuroendocrine axis), SOX10 (neural crest axis), EZH2/PRC2 overexpression (epigenetic reprogramming hub), REST silencing (neuroendocrine de-repression). MITF/AXL axis controls melanoma proliferative vs. invasive state switching.

3. **Cancer stem cells (CSCs).** CSCs are a dynamic, plastic subpopulation (not a fixed hierarchy) capable of self-renewal, inter-conversion with non-CSC states, and population reconstruction. Key markers and pathways: Notch-IGF-II/IGF1R-c-Met/FRA1/HEY1-FAK axis regulated by MSCs, CAFs, immune cells, and exosomes. EMT activation generates CSC traits (mammosphere formation, stemness markers). Non-CSCs can spontaneously convert to CSC states, with frequency shaped by ZEB1, hypoxia, and TAM-derived signals.

4. **Epigenetic reprogramming.** Widespread CpG hypermethylation of tumor suppressor promoters (e.g., RB, VHL) and global hypomethylation enabling oncogenes. EZH2/PRC2 is a master hub: catalyzes H3K27me3 repression of differentiation programs, essential for NEPC aggressiveness, and upregulated downstream of REST silencing. Histone modifications (H3K9me3 establishing heterochromatin in DTPs, KDM6A/KDM5A/B demethylase activity modulating DTP survival), chromatin remodeling by SWI/SNF, and DNA methylation by DNMTs cooperate. Bivalent chromatin (simultaneous active + repressive marks near key genes) in CSCs enables rapid state switching.

5. **Non-coding RNA regulation.** miR-200 family (miR-200A/B/C, miR-141, miR-429): suppresses EMT by targeting ZEB1/2; forms a feedback loop with TGF-β-driven ZEB1 expression. miR-34A: suppresses HOTAIR and reduces MMP production. Oncogenic miRNAs: miR-21, miR-31 (promote EMT via TIAM1 targeting; induced by TGF-β-1). lncRNAs: HOTAIR (promotes EMT, maintains CSC populations, acts via HOXD10/miR-34A axis); MALAT1 (alternative splicing, chromatin remodeling, EMT induction); the 11p15 imprinted lncRNA (TGF-β pathway modulation, MMP production, Wnt/β-catenin for CSC self-renewal); UCA1 (EMT, chemoresistance via P-glycoprotein, Wnt/β-catenin); TUG1 (MDR gene upregulation via PRC2/ZEB1/Snail, engages miRNA sponge activity); MEG3 (tumor suppressor, reduces miR-155/miR-21 to suppress EMT); NEAT1 (PI3K/AKT/Wnt/MAPK axes, cancer progression via chromatin/splicing effects).

### Crosstalk taxonomy (which arms cross-couple and how)

The paper's most distinctive contribution is identifying shared signaling nodes that simultaneously activate multiple plasticity arms:

| Coupling | Mechanism |
|---|---|
| EMT ↔ CSC | EMT transcription factors (Snail, ZEB, Twist) activate CSC programs; partial EMT state confers peak stemness; CSC Wnt/Notch signaling reciprocally reinforces EMT |
| EMT ↔ Epigenetic reprogramming | EZH2/PRC2 represses epithelial genes; ZEB1 recruits PRC2 and DNMT3B to CDH1 locus; TUG1-PRC2 complex promotes mesenchymal gene activation; histone deacetylation stabilizes mesenchymal state |
| EMT ↔ ncRNA | miR-200/ZEB1/2 double-negative feedback loop (core EMT bistability circuit); TGF-β-1 drives miR-31 and miR-21 to promote EMT; HOTAIR/miR-34A crosstalk; UCA1 sponges miR-145/miR-204 to enhance EMT |
| CSC ↔ Metabolic reprogramming | Glycolytic (Warburg) phenotype generates biosynthetic precursors for stemness programs; fatty acid oxidation and glutamine metabolism support CSC survival under stress; HIF-1α (induced by VEGF/hypoxia) stabilizes both CSC and EMT programs |
| EMT ↔ TME | CAF-secreted HGF and TGF-β promote EMT; TAM-derived cytokines (TNF, IFN-γ) drive stromal plasticity; M2-polarized macrophages secrete TGF-β, IL-6, TNF-α, VEGF to enhance EMT and stemness; exosomes transfer EMT/stemness programs to recipient cells via PI3K/AKT and Wnt activation |
| EMT ↔ Immune evasion | IL-6-STAT3 maintains stemness/tolerance; ECM stiffness via FAK–SRC–YAP/TAZ creates a feed-forward EMT loop; EMT state increases PD-L1 on tumor cells via exosome delivery, suppressing local immune response |
| DTP survival ↔ Epigenetic + Metabolic | H3K9me3 heterochromatin silences drug-targeted pathway reactivation in DTPs; LINE-1 element suppression by H3K9me3 reduces IFN-triggered cytotoxicity; KDM6A/KDM5A/B regulate DTP viability; metabolic switching (glycolysis ↔ FAO ↔ glutaminolysis) provides redundant survival buffers preventing single-target eradication |
| Senescence ↔ Immune plasticity | SASP (IL-6, IL-8, MMPs, growth factors) creates pro-inflammatory and pro-tumorigenic milieu; SASP reprograms adjacent cells toward more plastic/stem-like states; tumor immune evasion is promoted via SASP-driven TME remodeling |
| Autophagy ↔ DTP | Autophagy enables metabolic adaptability during drug stress by recycling damaged organelles; autophagy suppression can enhance tumor sensitivity and interfere with DTP phenotype maintenance |

### Drug-tolerant persister (DTP) trajectory

The paper articulates a gradient model of resistance acquisition:
1. Drug exposure → reversible transcriptomic reconfiguration to slow-cycling phenotype (non-genetic, H3K9me3-mediated)
2. Recovery of proliferative capacity → evasion of epigenetic alterations
3. Sustained DTP culture → irreversible genetic changes (reactivating drug-targeted pathway)
4. Possible reversion to drug-sensitive state on drug withdrawal (phenotypic, not genetic stabilization)

All drug-tolerant morphologies share common resistance mechanisms transcending genetic modification. The epigenetic–metabolic network provides redundant survival pathways preventing single-agent DTP eradication.

### Signaling pathways enabling plasticity

The review identifies the following pathways as shared activators of multiple plasticity arms:

- **TGF-β / Smad:** Master EMT inducer; activates Smad2/3→Smad4 complex; also signals via Ras/ERK MAPK, PI3K/AKT, JNK/p38 (non-Smad routes). Interacts with Wnt (Smad+β-catenin/TCF/LEF), Notch (Smad+NICD/CSL), and Hippo (YAP/TAZ). Isoform-specific: TGF-1 is the primary EMT driver in most cancers; BMP5 inhibits TGF-β EMT; BMP7 supports epithelial phenotype. TGF-β-RII phosphorylates SMAD2/3; Smad complexes bind SNAI1 promoter to drive EMT.
- **Wnt/β-catenin:** LRP/Frizzled receptor activation → β-catenin nuclear entry → TCF/LEF → EMT, stemness (Snail/Snail2 stabilization, fibronectin), and MDR. Stabilized by PI3K/Akt signaling. Targeted by LGK-974 (clinical).
- **Notch:** TACE/γ-secretase release of NICD → CSL repressor complex activation → EMT gene induction and miRNA modulation; EndMT via Notch-driven vascular E-cadherin depletion; Notch1 inhibition reverses lung cancer EMT.
- **PI3K/AKT/mTOR:** Downstream of TGF-β, integrin activation (via ILK/AKT), and RTKs; activates SNAI1 via NF-κB; mTOR supports DTP biomass accumulation; concurrent YAP/PI3K activation marks early drug response.
- **RAS–ERK:** TGF-β-activated Ras/Raf/MEK/ERK cascade; integrin→FAK→Src→ERK; MAPK activity modulates stromal stiffness. CAFs reactivate ERK through HGF.

### Therapeutic strategies

- **Combination targeting:** Concurrent inhibition of YAP + PI3K at treatment initiation, plus MCL1/IGF1R/EGFR/MET/AXL inhibitors to reduce the DTP pool.
- **Phenotypic modulation:** HDAC inhibitors (trichostatin A, MS-275) reactivate LINE-1 elements and reduce DTP populations; KDM inhibitors modulate H3K9me3/H3K27me3 to destabilize DTP epigenome.
- **Restoring cellular identity:** TGF-β pathway inhibition to reverse EMT; thalidomide analogs to degrade SOX factors; chromatin-modifying enzyme targeting; BET inhibitors + metabolic inhibitors (LDHA/CPT1A blockers) as dual-function node targeting (e.g., EZH2/BRD4).
- **Cellular reprogramming / collateral vulnerability:** Direct reprogramming to non-resistant identity; SCLC lineage switch → transient EGFR-suppressed → platinum-etoposide sensitivity; enzalutamide-resistant prostate cancer → pembrolizumab sensitivity.
- **Autophagy suppression + DTP targeting.**
- **Intermittent dosing** to prevent DTP stabilization (but practically limited by multi-mechanism resistance emergence).

## Limitations

- Single-author review from a single lab (Islamic Azad University, Tabriz); no co-author with expertise in cancer evolution or evolutionary biology explicitly engaged. The framing is resistance-mechanisms-first, not evolution-first.
- The paper does not engage with Darwinian / Extended Evolutionary Synthesis frameworks, genetic accommodation, adaptive therapy, or clonal dynamics. It treats plasticity as a mechanisms catalogue without asking when each route predominates, or how to distinguish them in data.
- The crosstalk taxonomy is assembled from individual pairwise studies; most cross-mechanism claims are inferences from separate experiments, not from studies that simultaneously measured multiple plasticity axes. Direct crosstalk evidence (e.g., simultaneous EMT + CSC + metabolic reprogramming readouts in the same cells under therapy) is sparse.
- DTP trajectory claims are mostly from in vitro cell-line studies; the paper itself flags this limitation ("most studies were performed in laboratory environments"). In vivo and clinical DTP evidence is limited.
- No formal quantitative model of the DTP epigenetic–metabolic network. The claim that "the epigenetic–metabolic network offers several redundant pathways for survival" is a qualitative inference from separate pathway studies.
- Limited cancer-type specificity in the crosstalk section: most signaling pathway descriptions are presented as broadly applicable, but the cited evidence is often cancer-type-specific (prostate, NSCLC, melanoma).
- The immune plasticity arm (immune evasion, checkpoint, SASP) is described mechanistically but not integrated into a quantitative resistance model.
- No data on prevalence of each plasticity arm across cancer types (quantitative epidemiology of DTP, NED, or partial-EMT incidence across tumor contexts is absent).
