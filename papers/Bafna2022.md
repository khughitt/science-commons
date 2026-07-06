---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Bafna2022
kind: paper
title: Extrachromosomal DNA in Cancer
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Bafna2022
tags: []
ontology_terms:
- chromothripsis
- copy-number heterogeneity
- ecDNA
- enhancer hijacking
- extrachromosomal DNA
- homogeneously staining regions
- non-Mendelian inheritance
- oncogene amplification
- random segregation
---
## Key Findings

### Data-derived findings (D, secondary)

These findings originate in primary papers cited by the review; Bafna & Mischel inherit them as secondary evidence.

- **ecDNA prevalence (D, secondary from Turner 2017):** Automated metaphase DAPI imaging across >2,500 cancer cell lines found ecDNA in "nearly 40% of all samples." [UNVERIFIED — exact figure not independently confirmed here; inherited from Turner2017]
- **ecDNA prevalence in tumours (D, secondary from Kim 2020):** Sequencing-based detection in 3,212 tumour samples identified ecDNA in 460 (14.3%) of tumours; no ecDNA detected in 1,810 normal samples. [UNVERIFIED — exact figure inherited from Kim2020]
- **Gene expression amplification (D, secondary from pan-cancer study):** In a pan-cancer cohort of >3,000 samples, ecDNA-resident oncogenes showed significantly higher expression than chromosomal copies even after correcting for copy-number differences — implying a transcriptional accessibility or structural advantage beyond copy number alone. [UNVERIFIED — source paper not specified in available text]
- **Chromatin accessibility (D, secondary from ATAC-seq studies):** ATAC-seq showed ecDNA contains among the most accessible chromatin in cancer cells, lacking higher-order compaction/heterochromatin structure typical of chromosomal regions.
- **Enhancer hijacking / neo-TAD formation (D, secondary from 4C-seq studies):** 4C-seq demonstrated ecDNA-resident oncogenes form new contacts outside their canonical topologically associating domains (TADs), recruiting enhancers and insulators from distal genomic regions into a "neo-TAD" configuration.
- **ecDNA hub formation (D, secondary from ChIA-PET studies):** ChIA-PET identified ecDNA hubs that co-localize via Brd4/BET protein interactions, functioning as mobile enhancer aggregates ("ecDNA party bus") that regulate both ecDNA-resident and chromosomal genes. Hubs disassemble in metaphase and reform in G1.
- **Reversible ecDNA–HSR interconversion (D, secondary from Nathanson et al.):** In a glioblastoma cell line carrying EGFR-vIII on ecDNA, Erlotinib treatment drove ecDNA reintegration into chromosomes as HSR; drug removal led to re-emergence of ecDNA with "essentially identical structures" to the naïve state.
- **Hydroxyurea-accelerated ecDNA loss (D, secondary from Snapka & Varshavsky):** Non-cytotoxic HU doses accelerated ecDNA loss such that 90% of cells lost ecDNA in 4–5 doublings, via micronuclei formation rather than inhibition of DNA synthesis; without selection pressure, natural ecDNA loss takes ~25–30 doublings.
- **HPV integration and ecDNA formation (D, secondary):** HPV integration generates hybrid ecDNA in nearly 50% of cervical cancer samples. [UNVERIFIED — source not specified in available text]
- **Deep-learning ecDNA detection (D, secondary):** U-net CNN applied to metaphase DAPI images achieved ~85% accuracy for automated ecDNA detection. [UNVERIFIED — exact accuracy figure inherited from cited study]

### Mathematical model predictions (D, model-derived)

The following are not empirical observations but outputs of the Bafna & Mischel population-genetics model — they are data-generated in the modelling sense, and subject to the model's assumptions:

- **Selection threshold:** Under the model's coupled ODEs (binomial segregation + selection coefficient s), if s ≤ 1 the proportion of ecDNA-negative cells increases to 1 (ecDNA is lost); if s > 1 the ecDNA-negative fraction rapidly diminishes. This predicts that ecDNA persistence requires ongoing positive selection.
- **Copy-number distribution shape:** The model predicts ecDNA copy-number distributions with tail probabilities satisfying e^(−λx²) ≤ Pr(copy fraction = x) ≤ e^(−λx) — wider than a Normal distribution but narrower than purely exponential decay. This is the formal basis for the prediction of "relatively high heterogeneity of ecDNA copy number."
- **High copy numbers under modest selection:** Simulations show that even with modest selection coefficients, typical ecDNA counts per cell can remain in the hundreds, sustaining high oncogene dosage.

## Limitations

- Being a review, it does not generate primary data; all D-findings are secondary. Quantitative figures on prevalence, expression excess, and clinical outcomes are inherited from cited studies without independent reanalysis.
- The mathematical model (Equations 1–2) is theoretical; its predictions (power-law tail, selection-threshold dynamics) have not been empirically validated in a controlled experimental setting within this paper.
- The "rare formation" claim is not quantified — the rate of ecDNA formation events per cell division in cancer vs. normal contexts is not estimated.
- The review covers through ~2021; subsequent developments (e.g., Lee2026 eicicle classifier, newer AmpliconArchitect versions, single-cell ecDNA profiling) are not included.
- Citation count in Europe PMC as of early 2026: 44 — substantially below the 500-citation threshold used for the well-known-classic exception. This paper is newer (2022) and citation accumulation is ongoing, but the relatively low count means some claims may not yet have independent replication in the community. [Note: this affects the weight to place on secondary claims, not on the review's conceptual framing.]
- Clinical translation claims (ecDNA as drug target, HU as ecDNA-eliminating agent) remain preclinical; the review does not discuss the gap between cell-line demonstrations and patient-level applicability.
