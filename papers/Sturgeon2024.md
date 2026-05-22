---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Sturgeon2024
type: paper
title: The Crossroads of Clonal Evolution, Differentiation Hierarchy, and Ontogeny in Leukemia Development
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Sturgeon2024
tags: []
datasets: []
ontology_terms:
- AML
- MDS
- cell-of-origin
- clonal evolution
- clonal hematopoiesis
- hematopoietic hierarchy
- iPSC models
- leukemia stem cells
- mutational order
- ontogeny
- single-cell multiomics
---
## Key Findings

### 1. Mutational order shapes leukemia identity

Driver genes in myeloid malignancies cluster into three temporal classes by cross-stage VAF analysis:

- **Early/truncal (CH and DTA genes):** DNMT3A, TET2, ASXL1 — epigenetic regulators that initiate clonal hematopoiesis (CH) and are retained across disease stages; serve as the preleukemic "trunk."
- **Intermediate (MDS-characteristic, SF and cohesin genes):** SRSF2, U2AF1, SF3B1, RUNX1, NPM1, STAG2, SMC3 — found in MDS and retained in sAML but not typical of de novo AML; mark MDS-stage commitment.
- **Late/signaling (AML-characteristic):** NRAS, KRAS, PTPN11, FLT3 — high frequency in sAML (MDS→AML progression); define the final transformation event.

The TET2→JAK2 vs. JAK2→TET2 paradigm (from MPN studies) demonstrates experimentally that mutation order — not just mutation co-occurrence — sets the clonal adaptation trajectory and the epigenetic "landscape" available to the second hit. Early DNMT3A/TET2/ASXL1 mutations may act as epigenetic landscapers that precondition the HSPC for subsequent transforming events ("epigenetic preconditioning").

Mutual exclusivity among SF genes and among cohesin complex genes, and near-mutual exclusivity of IDH1/IDH2, suggest functional redundancy constrains co-mutation — the architecture of the mutational landscape is shaped by cooperative and antagonistic gene interactions.

### 2. The LSC is not one cell: deep vs. shallow hierarchy, GMP-type LSCs, and clonal LSC diversity

The "LSC" is heterogeneous at multiple levels:

- **Deep vs. shallow hierarchies:** Leukemias vary in LSC frequency. High-LSC-frequency AMLs have pronounced differentiation block and shallow hierarchies (mostly LSC-like cells); low-LSC-frequency AMLs maintain deeper hierarchies resembling normal hematopoiesis but with distortion.
- **Not only HSCs/MPPs:** Experimental evidence (Krivtsov, Ye, Sango and colleagues) establishes that committed myeloid progenitors — CMP and GMP — can serve as transformation targets for specific oncogenes (e.g., MLL-AF9 requires the GMP compartment for efficient leukemogenesis; RAS mutations can transform GMPs into GMP-type monocyte-primed LSCs).
- **RAS-mutant GMP-type LSCs:** NRAS/KRAS mutations (which arise late in AML) can generate a GMP-type LSC that is phenotypically and metabolically distinct from the ancestral RAS-WT HSC/MPP-derived LSC coexisting in the same patient. RAS-WT LSCs are VEN-sensitive; RAS-mutant GMP-type LSCs are VEN-resistant (mediated by altered pro/antiapoptotic gene expression). This explains why RAS mutations drive clinical resistance to venetoclax, and why LSC populations from different genetic subclones co-exist within a single LSC compartment.
- **Mutational path selects LSC type:** Specific mutation pairs or sequences predetermine which HSPC type is permissive for transformation, so the resulting LSC type is not random but a structured outcome of genotype × cell-type interaction.
- **DNMT3A/TET2 mutations skew differentiation:** DNMT3A-mutant CH exhibits mutant-specific transcriptional profiles driving proliferation and differentiation biases (from GoT data), consistent with early mutations shaping the downstream cellular environment.

### 3. Ontogeny establishes a developmental window and sets the cellular context for transformation

Multiple hematopoietic waves arise sequentially from distinct embryonic sites:

- **Yolk sac (YS) primitive program:** Transient; confined to the first 3 weeks of gestation; produces primitive erythroid, macrophage, and megakaryocyte lineages with unique features. Not HSC-dependent.
- **YS erythro-myeloid progenitors (EMPs):** Broader lineage capacity; give rise to tissue-resident macrophages (e.g., microglia) that persist lifelong.
- **LMPP-like progenitors (YS?):** Possibly give rise to B-1 B cells and γδ T cells.
- **AGM-derived embryonic MPPs (eMPPs):** Emerge at day 32 of human gestation; may contribute multiple lineages into early adult life via the fetal liver (FL).
- **HSC-dependent definitive hematopoiesis:** Initiates from AGM-HSCs; colonizes BM; provides all lineages lifelong.

Key ontogeny-driven insights for leukemia:

- **Infant leukemias (especially KMT2A/MLL-rearranged):** Driver mutations acquired in utero, in fetal progenitors (FL HSPCs or HSC-independent waves). Experimental induction of MLL-AF9 in FL HSPCs vs. adult BM HSPCs produces more aggressive disease from FL. Explains infant AML's exceptionally low mutational burden, distinct clinical features, and mixed myeloid-lymphoid phenotype (lineage plasticity in fetal progenitors).
- **Down syndrome leukemia:** Trisomy 21 creates a 20–150× elevated AML risk; GATA1 truncation mutations arise in fetal blood cells and generate transient abnormal myelopoiesis (TAM) exclusively in infants. TAM is restricted to the fetal developmental window — a narrow "susceptibility window" governed by the fetal progenitor context, not by the mutation alone.
- **Adult AML with prenatal CH mutations:** Phylogenetic tree analyses show that some adult myeloid malignancies carry initiating CH mutations acquired before birth, raising the possibility of a small subset of adult AML with prenatal origins.
- **Developmental wave identity vs. HSC identity:** The composition of the HSPC compartment changes across developmental stages — FL HSPCs differ from cord blood (CB) HSPCs differ from adult BM/mobilized peripheral blood (mPB) HSPCs — and these differences affect transformation potential and the resulting LSC hierarchy.

### 4. Genetic, differentiation, and developmental hierarchies interact

The central synthesis (Fig. 4) is that distinct LSCs at different disease stages (preleukemic LSC → MDS-SC → AML LSC → relapsed AML LSC) are the products of specific mutation sets acting on specific HSPC types. Each successive genetic clone may "select" a new HSC type as the dominant LSC, producing a shift in the hierarchy structure. Therapeutic resistance emerges from this: RAS-WT and RAS-mutant subclones sustain phenotypically distinct LSC compartments with opposite VEN sensitivities, coexisting in the same patient.

"Epigenetic landscaping" by early mutations (DNMT3A, TET2, ASXL1) may explain non-random cooperative mutation patterns: the first mutation alters the differentiation or chromatin accessibility landscape of HSPCs, biasing which cell types are available as targets for the second hit and which second hits will be selectively advantageous. This is consistent with co-mutation patterns (e.g., DTA genes co-occur preferentially with chromatin remodeling partners) being driven by epigenetic-level selection rather than purely mutational chance.

### 5. New model systems enable interrogation of the three-dimensional framework

- **Synthetic leukemogenesis (primary HSPCs + lentiviral/CRISPR editing):** Prospective isolation of defined HSPC populations → oncogene induction → xenotransplantation enables controlled cell-of-origin experiments; identifies which progenitor types are permissive for which oncogenes.
- **Patient-derived iPSC lines:** Capture distinct genetic clones along the CH→MDS→AML axis from individual patients; enable directed differentiation to specific HSPC or mature cell types; allow isolation of the effects of mutation from developmental stage (iPSC-derived HSPCs from different ontogenetic waves can be generated in vitro via distinct directed differentiation protocols). Key limitation: iPSC-derived non-leukemic hematopoiesis is not engraftable.
- **Single-cell multiomics with genotyping:** GoT, TARGET-seq, and Genotyping of Transcriptomes (GoT) enable simultaneous capture of somatic mutations + transcriptome + chromatin accessibility from the same cell. Applied to DNMT3A-mutant CH (GoT): mutation-specific transcriptional and differentiation biases detected within the clonal population. Applied to JAK2V617F MPN (GOCA): chromatin accessibility + genotype profiles linked within a single assay.
- **Cellular barcoding and phylogenetic reconstruction:** Mitochondrial DNA variants, single-nucleotide variants from scWGS, and DNA methylation "epimutations" used as natural barcodes for retrospective lineage tracing without genetic engineering; reconstruct clonal dynamics during disease progression and treatment response in primary human cells.

## Limitations

- The three-dimension synthesis is conceptual/programmatic rather than empirically demonstrated in a unified experiment: no single study yet jointly controls mutation identity, HSPC type, and ontogenetic origin in a comprehensive factorial design across all AML subtypes.
- The cell-of-origin experimental evidence is mostly from murine leukemogenesis models or human xenotransplantation; the assumption that transformation permissiveness hierarchies seen in mouse/xenograft models fully translate to human in vivo leukemogenesis remains unvalidated.
- The paper focuses almost exclusively on myeloid malignancies (AML, MDS, MPN); the extent to which the three-dimensional framework applies to lymphoid malignancies or solid tumors is not systematically addressed.
- Epigenetic landscaping (the first mutation biasing the HSPC epigenome for the second mutation) is supported by correlational co-mutation patterns and some experimental MPN data (TET2→JAK2 order effects) but is mechanistically incomplete — it is not clear how generalizable the ordering effect is across all DTA combinations in AML.
- The developmental ontogeny section is based heavily on mouse models; human embryonic hematopoiesis is less well-characterized, and the persistence and transformation potential of distinct human embryonic progenitor waves is inferred rather than directly demonstrated.
- iPSC-derived models have a critical unresolved limitation: iPSC-derived non-leukemic HSPCs are not engraftable in current protocols, preventing direct comparison of normal vs. preleukemic HSPC function and preventing use of iPSC-derived cells to model the CH stage of the clonal hierarchy in vivo.
- The review does not address the role of the bone marrow microenvironment / niche in shaping LSC fate or evolutionary dynamics — a potentially important fourth dimension not integrated into the framework.
