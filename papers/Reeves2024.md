---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Reeves2024
type: paper
title: 'Mutations, Bottlenecks, and Clonal Sweeps: How Environmental Carcinogens and Genomic Changes Shape Clonal Evolution during Tumor Progression'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Reeves2024
tags: []
datasets:
- dataset:reeves2024-gemm
ontology_terms:
- DMBA/TPA
- benign-to-malignant transition
- bottleneck
- clonal evolution
- clonal sweep
- environmental carcinogen
- field cancerization
- genomic instability
- immunoediting
- mouse model
- polyclonal metastasis
---
## Key Findings

### Initiating mutations are not sufficient for cancer

- Tissues in apparently histologically normal adults are riddled with driver mutations: up to 20% of normal skin cells and ~80% of esophageal epithelial cells carry NOTCH1 mutations; TP53, NOTCH2/3, and FAT1 are common in normal esophagus. Most of ~75% of melanocytic nevi carry BRAF V600E yet fewer than 1 in 33,000 progress to melanoma.
- A single initiating oncogenic mutation (BRAF, Hras Q61L) is insufficient; progression requires additional genomic hits (CDKN2A loss, TP53 mutation) or sustained exposure to promoters/tissue damage.
- Field cancerization: chronic inflammatory conditions (IBD, endometriosis) accelerate clonal evolution in colon and endometrium by expanding cells that carry initiating mutations, without directly mutating them — illustrating a non-mutagenic niche-as-mutagen effect.

### Genomic evolution during progression: mutation burden increases with stage

- In DMBA/TPA, malignant carcinomas have ~65% more SNVs than benign papillomas and significantly more whole-chromosome CNAs.
- In 4NQO oral carcinoma, invasive carcinomas have >3× more mutations than hyperplasia/dysplasia. In urethane lung, fully malignant adenocarcinomas have higher SNV burden than benign adenomas.
- Important caveat: outlier tumors with low mutational burden can be fully malignant (DMBA carcinomas), demonstrating there is **no fixed mutation number or threshold required for malignancy**.
- CNAs increase substantially during the benign growth phase: "late" papillomas (~1 yr) have dramatically more CNAs than "early" papillomas (~3 months); specific chromosomal gains (chr 7, 6, 1) are among the earliest CNA changes, with chr 1 gain nearly absent in papillomas but common in carcinomas — implicating it specifically in progression.

### Carcinogen type shapes evolutionary mode

- **Mutagenic carcinogens (DMBA, urethane, 4NQO):** Generate high SNV burdens with carcinogen-specific signature profiles (e.g., DMBA A>T; Hras Q61L amplification during progression — copy number of the activating Q61L allele increases as tumors advance). These create substrate diversity for Darwinian selection.
- **Non-mutagenic promoters (TPA, air pollutants, chronic wounding/inflammation):** Drive tumor promotion without direct mutagenesis. TPA stimulates outgrowth of cells carrying spontaneously arising driver mutations. Air pollutants (Hill et al. 2023) promote lung cancer through non-mutagenic effects on the tumor microenvironment, not through new mutations in target cells. Chronic wounding and inflammation act similarly.
- **Implication:** Carcinogen type determines which evolutionary mode dominates — mutagenic carcinogens expand phenotypic/genotypic variation on which selection acts; non-mutagenic promoters select from existing variants without broadening the mutation spectrum, functioning as niche expanders for pre-mutated clones.

### Clonal dynamics in benign vs. malignant tumors differ fundamentally

- Benign tumor growth in DMBA/TPA is driven by a **small number of stem cells** (Lgr6+ in papillomas), with structured boundaries between neighboring clones (patchwork of regionalized clones; Reeves et al. 2018).
- Malignant tumor growth is driven by a **larger proportion of cells**, with adjacent clones intermixing — losing clean spatial boundaries, suggesting increased migratory phenotypes.
- This transition mirrors human colorectal tumors: carcinomas show physical intermixing of genetically distinct clones; adenomas retain spatially segregated subclones.
- In KP GEMM with CRISPR lineage tracing (Yang et al. 2022): tumors progress through highly plastic states — a fit clone rapidly expands, then the tumor stabilizes; most tumors had undergone one or two "expansions" in which a single subclone came to dominate (consistent with punctuated clonal sweeps).

### A strong bottleneck at the benign-to-malignant transition

- Multicolor lineage tracing in DMBA/TPA: clones within benign papillomas form a patchwork of colors; after progression to malignancy, **all carcinomas were comprised of only a single color** — corresponding to the single clone that drove malignancy (Reeves et al. 2018).
- In 4NQO oral carcinoma: earliest-stage lesions have more tumor subclones and more low-VAF mutations; invasive carcinomas have more clonal mutations — consistent with a sweep of the fittest clone.
- In pre-malignant lung lesions (human; Hu et al. 2019): frequency of subclonal mutations highest at AAH (premalignant) stage; adenocarcinoma stages show increasing clonal mutation frequency — progressive sweep.
- **Specific genomic combinations drive the bottleneck:** Malignant carcinomas in DMBA/TPA frequently harbor losses of CDKN2A/B or Trp53 (never found in benign papillomas); Hras Q61L + CDKN2A loss or Trp53 loss strongly potentiate full malignancy; chromosome 1 gain is seen in few papilloma cells but is common in carcinomas. These combinations are "incompatible with the tumor staying benign."
- **No single required mutation or threshold:** The occasional fully malignant DMBA carcinoma with very low mutational burden confirms that specific combination — not cumulative count — governs the benign-to-malignant bottleneck.

### A less restrictive bottleneck at metastasis; polyclonal seeding predominates

- In DMBA/TPA skin metastasis (Reeves et al. 2018) and Pdx1-Cre;Kras;p53 PDAC (Maddipati and Stanger 2015): metastases are frequently polyclonal, with contributions from multiple cells of the primary tumor. Circulating tumor cell clusters (polyclonal) isolated from PDAC-bearing mice had higher metastatic potential.
- In human cancers (prostate, colorectal, lung, breast; Gundem et al. 2015, Naxerova et al. 2017, Hu et al. 2020): polyclonal metastases confirmed. A pan-cancer study found 60% of lymph node metastases vs. 30% of distant metastases were polyclonal — LN metastases are nearly twice as likely to be polyclonal as distant metastases.
- KP GEMM CRISPR lineage tracing (Yang et al. 2022): metastases mapped to specific spatial regions of the primary tumor. Three liver metastases in the main case study mapped to one end of the primary; soft-tissue metastasis mapped to the other end — reflecting spatial origin.
- Polyclonal seeding is proposed to confer a selective advantage during transit (immune evasion; Lo et al. 2020 on NK-cell killing resistance of clusters).
- Key caveat: transplant models (Quinn et al. 2021, A549 cells) overestimate metastatic cell reseeding of the primary and obscure clonal dynamics; transplanting aggressively malignant cells bypasses the full evolutionary process. Spontaneous tumor models (e.g., DMBA/TPA, KP GEMM) better recapitulate the evolutionary bottleneck.

### Immunoediting shapes clonal evolution

- First demonstrated in a carcinogen (methylcholanthrene)-induced sarcoma: specific loss of immunogenic spectrin-β2 mutation permitted "escape" from immune control (Matsushita et al. 2012).
- Multi-region sequencing confirms ongoing immunoediting in human patients: epigenetically silenced immunogenic mutations and LOH of HLA alleles in early lung lesions (Rosenthal et al. 2019); pervasive subclonal LOH at HLA locus across 394 tumors/22 types (Watkins et al. 2020).
- Immune "cold" lung tumor clone (low T-cell abundance) was phylogenetically closely related across multiple tumor regions — a common "immune cold" clone underwent positive selection and came to dominate the tumor (Abduljabbar et al. 2020).
- Biological sex and age modulate the strength of immune selection: younger, female patients have fewer immunogenic mutations, suggesting their tumors have evolved to be more "immune-invisible" — offering a mechanistic explanation for why female patients respond less well to immunotherapy.

### Mouse model advantages and limitations

- Advantages: precise genetic and carcinogenic control; observation of tumors that have undergone the full evolutionary process from initiation; single treatment (mutagen alone, or mutagen + promoter) can recapitulate clonal diversity and selection processes.
- Limitation: genetic models (GEMMs) have very low point mutation burden and simultaneously induce identical mutations in many target cells, altering clonal dynamics. They are essential for lineage tracing and precise mechanism work but are less suited to studying selection acting on natural variation.
- Transplant xenograft models obscure evolutionary dynamics by beginning with an already-aggressively malignant pool — best avoided for evolutionary questions.

## Limitations

- No original primary data presented; synthesis is weighted heavily toward the Balmain laboratory's own DMBA/TPA mouse skin carcinogenesis model. Generalizability claims rest on comparison with published data from other systems.
- The framework is **descriptive cataloging**, not a quantitative regime-shift model. The paper does not provide testable predictions about when a given carcinogen or tumor context will favor one evolutionary mode over another, nor does it define thresholds, rates, or parameters that would allow regime classification in a new system.
- Smoking is implicated in the early/late metastatic divergence data from AlBakir2023 (cited by Reeves2024 indirectly via NSCLC context), but the paper does not itself analyze smoking-signature carcinogens (tobacco-specific nitrosamines, PAHs) in terms of regime-shifting. Tobacco is discussed as an environmental carcinogen class but without specific mutational signature data mapped to evolutionary regime.
- Asbestos and alcohol are not discussed as specific carcinogen classes. The carcinogen catalog reduces to: mutagenic chemical carcinogens (DMBA, urethane, 4NQO, methylcholanthrene), non-mutagenic chemical promoters (TPA), air pollutants/particulates, and chronic inflammation/wounding. No UV-driven or HPV-driven evolutionary comparison is included.
- Polyclonal metastasis claims are supported by multicolor lineage tracing and pan-cancer sequencing meta-analysis but rely on studies with limited metastatic sampling depth. The paper acknowledges the A549 xenograft transplant caveat (transplant models overestimate polyclonality from reseeding rather than co-seeding) without fully quantifying the bias.
- Immunoediting section is descriptive and draws primarily on published patient studies; the review does not integrate immunoediting quantitatively into the regime framework.
