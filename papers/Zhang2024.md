---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Zhang2024
type: paper
title: 'Tumor initiation and early tumorigenesis: molecular mechanisms and interventional targets'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Zhang2024
tags: []
datasets: []
ontology_terms:
- cancer prevention
- cell competition
- cell of origin
- chemoprevention
- clonal evolution
- dedifferentiation
- driver mutations
- epigenetic reprogramming
- field cancerization
- microenvironment
- tissue architecture
- tumor initiation
---
## Key Findings

### Taxonomy of initiation mechanisms

The review organises driver events into four overlapping classes, each of which can operate independently or synergistically:

**1. Genetic drivers**
- *SNVs and driver mutations:* >3,000 cancer driver genes identified; SBS1/SBS5 age-related signatures are the primary endogenous mutagenic forces in most tissues; exogenous signatures (SBS4 tobacco, SBS22 aristolochic acid) are contextually dominant. The liver shows the highest mutational burden across 9 normal organs from the same donors; pancreas the lowest. [UNVERIFIED: exact organ-comparison study from the authors' lab, single cited study]
- *CNAs and structural variants:* Chromosomal alterations occur early; TP53 biallelic loss is among the first events in esophageal LGIN; ecDNA detected early in Barrett's-to-EAC progression; CIN itself drives both immune activation (cGAS-STING, type I IFN) and paradoxical immune evasion via secretome-induced chronic inflammation.
- *WGD:* Whole-genome duplication facilitates CNA accumulation; TP53 loss often precedes WGD and enables propagation of CIN.

**2. Epigenetic drivers**
- Age-related CpG island methylation and global hypomethylation are parallel to malignant changes and can be detected in morphologically normal tissues (epimutations).
- DNA hypermethylation at promoters silences tumor suppressors (DNA repair, cell cycle, p53 pathways) in precancerous stages.
- Highly repressive marks (H3K4me3/H3K27me3 bivalent domains) at lineage-committed TF loci transform "poised" sequences into inactive states, promoting dedifferentiation.
- Epigenetic plasticity (overly permissive states) can stochastically activate pro-carcinogenic programs via enhancer hypomethylation and Polycomb repressor inactivation (e.g., KMT2D inactivation in early lung tumorigenesis).
- RNA m6A modification is an emerging epitranscriptomic layer; m6A in super-enhancer RNA activates H3K4me3 via YTHDC2/MLL1; RNA m6A can cause DNA demethylation via FXR1/TET1. Genetic mutations and epigenetic alterations promote each other's accumulation.
- Epigenetic priming can precede driver mutations: BRAF^V600E^-susceptible Wnt pathway sensitization by DNA methylation precedes Braf mutation in colon; chromatin states 48 hours post-pancreatic injury predate Kras co-optation.

**3. Environmental/extrinsic drivers** (Table 2 compendium)
The review catalogues gene–environment interactions across six environmental classes, each with specific tissue examples:
- *Inflammation:* The most convergent environmental driver. Kras mutation in acinar cells is insufficient for PDAC without injury/inflammation (ADM required); Trp53-mutant ISCs are context-dependent — in inflammatory conditions they replace wild-type ISCs via STAT3; Sox2 overexpression + inflammation transforms esophageal basal progenitors to SCC via Sox2/STAT3; TET2 mutation accelerates myeloid malignancy under NF-kB modulation; DNMT3A/TET2 CHIPs expand under inflammatory stimuli.
- *Chemical carcinogens and radiation:* Nicotine activates AKT-ERK-MYC-GATA6, suppressing acinar differentiation, priming Kras transformation. Cigarette smoke induces heritable epigenomic changes making bronchial epithelium susceptible to single Kras mutation. PM2.5 induces IL-1β/macrophage-mediated AT2 → progenitor-like reprogramming. UV promotes quiescent Braf^V600E^ melanocyte stem cells over differentiated cells.
- *Diet and metabolic factors:* High-fat diet disrupts cell competition (HFD impairs Ras^V12^ apical extrusion; HFD promotes CCL2/PPAR-δ/FGF21-dependent MDSC recruitment in Kras-mutant pancreas). Hyperglycemia activates NSUN2-TREX2 cGAS-STING via dsDNA accumulation. Calorie restriction enhances niche competition and apical extrusion of mutant cells.
- *Microbiome:* ETBF synergistically with Braf^V600E^ drives CpG island methylation and immune suppression in colon. S. anginosus → ANXA2 receptor → MAPK → gastric cancer. Fungi activate mannose-binding lectin/complement in pancreas to accelerate PDAC. Ruminococcus/Blautia family inhibit colon tumor by maintaining CD8 T cell surveillance.
- *Aging:* Aging-induced spontaneous CpG methylation activates Wnt/Braf^V600E^ colon tumorigenesis. Senescent stroma secretes SASP that reverses cell competition (senescent fibroblasts promote mutant cell EMT/invasion, suppress Ras^V12^ apical extrusion). Braf^V600E^/FAT1/TP53/NOTCH2/CDKN2A cooperate in age-driven esophageal SCC.

**4. Cell-autonomous cellular processes and tissue-architecture constraints**

The review describes three cell-autonomous routes to malignant transformation and four microenvironmental constraint mechanisms:

*Three cell-autonomous routes:*
- **Stem cell activation** — inherent self-renewal capacity and longevity; developmental chromatin programs (ATAD2-based) determine TF accessibility for oncogenic programs; WNT/MYC axes trap CSCs in proliferative phenoscapes.
- **Dedifferentiation** — lineage-committed cells acquire stem-like properties on oncogenic mutation or environmental stimulation. Melanoma from mature pigment-producing melanocytes (Braf^V600E^ + Pten loss, transcriptional reprogramming via SOX10/Crestin). Mammary luminal progenitors via PIK3CA or MYC. Pancreatic acinar ADM via Kras (requiring epigenetic priming by BRD4 chromatin reader at injury). FAT1 LOF triggers hybrid EMT state in SCC.
- **Trans-differentiation** — cells convert from one committed fate to another via an intermediate state, as exemplified by KRT8 intermediate cells (AT2→AT1 transition) in LUAD-adjacent normal lung; these intermediate cells are identified as key progenitors in LUAD initiation.

*Four microenvironmental constraints and their subversion:*
- **Cell competition:** "Epithelial defense against cancer." Supercompetitors (KRAS, APC, PIK3CA mutants) secrete NOTUM, BMP activators, to suppress neighboring ISC stemness while maintaining their own; Apc^Min/+^ ISCs secrete NOTUM to suppress wild-type ISCs. In stratified epithelium, winner determination is governed by cell fate decisions not microstructure. Inflammation undermines competition by promoting mutant survival (Trp53-mutant ESC niche advantage in colitis). Calorie restriction strengthens competition (apical extrusion of Ras^V12^ cells). HFD weakens competition.
- **Immune surveillance:** Early tumors harbor an "immune ignorance" phase when low neoantigen burden limits immune activation. Driver mutations shape immune landscape: Kras → stronger immune activation vs. EGFR → Treg promotion; TP53 mutations → NF-kB chronic inflammation and innate immune suppression. SOX17 downregulates IFNγ receptor/MHC-I/CXCL10 from precancerous stages to initiate immune evasion in ESCC. Mathematical model: TP53 mutations in non-cancerous tissues are primarily selected pro-oncogenically, not against immunogenicity.
- **Fibroblast/CAF co-evolution:** CAFs emerge from precancerous stage; pre-CAFs enrich in polyps. Fibroblasts secreting SASP and HGF suppress cell competition (suppress apical extrusion of Ras^V12^). BRCA1/NOTCH1 mutations in fibroblasts also contribute. Reciprocal mechanism identified in ESCC: epithelial cells downregulate ANXA1, fibroblasts lose KLF4, triggering TGF-β-mediated CAF transformation. JAG1-NOTCH2 signals on ductal/mammary CA fibroblasts.
- **ECM and tissue architecture:** ECM stiffness primes cells harboring RTK-Ras mutations for transformation via YAP/TAZ. Filamin (actin cross-linking protein) normally extrudes mutant cells; in stiff ECM, filamin relocates to perinuclei and fails. SmoM2-induced skin basal cell carcinomas arise in dense-collagen ears but not soft ears. Type 2 diabetes-induced ECM viscoelasticity activates integrin-β1-tensin-1-YAP. Tissue curvature, basal membrane assembly, and suprabasal stiffness shape early tumor morphology in stratified epithelia.

### Quantitative field-effect data

Table 1 provides a cross-tissue cross-stage driver gene compilation. Key quantitative field-effect observations:
- NOTCH1 mutations: more abundant in normal esophagus than in ESCC (echoing Ogawa2022). FAT1 mutations also more common in normal vs tumor tissues in esophagus.
- TP53 mutations: increase from precancerous state into ESCC; TP53 mutations detected before morphological dysplasia in Barrett's esophagus (TP53 mutation predicts progression even without dysplasia). Biallelic TP53 loss is an early LGIN event in ESCC.
- ERBB2/ERBB3 mutations: positively selected in Barrett's (EAC precursor) but not in EAC itself — a second instance of the Ogawa "selected-in-normal-≠-precursor" paradox.
- TERTp mutations: occur early in normal liver and are not detected in healthy or cirrhotic livers — appear specifically in early malignant evolution.
- CDKN2A/FAT1: more common in normal than in tumors in skin (squamous).
- APC mutations: present in precancerous colons and not detected in normal colons — enriched from precancerous state.
- PIK3CA mutations: found in both normal and proliferative lesions in breast, although less common in normal lobules.
- Endometrium: TERTp, TP53, CTNNB1, ARID1A mutations occur early in dysplastic nodules and not detected in healthy/cirrhotic livers (separate row); KRAS mutations promote regeneration after liver injury.
- [UNVERIFIED: exact cell counts and sample sizes for individual tissue entries in Table 1 — these are drawn from cited studies, not computed in this paper]

### Proposed interventional targets and strength of rationale

The review's "Cancer Risk Prediction and Intervention Strategies" section organises four translational directions:

**Risk prediction (Table 4):**
- Molecular risk-prediction biomarkers are tissue-specific and multi-modal (genetic mutations, CNA patterns, methylated DNA, metabolites, proteins, immune cell counts). Most validated in esophagus (BE progression: TP53 + 17p LOH; CNA panels with 50% high-risk group predicted 8 years before HGD/cancer), blood (CHIP gene panels + clinical features for AML/MDS/MPN risk), and colon (microbiome + metabolite panels).
- Rationale strength: **strong** for esophagus and blood (prospective cohort validation); **moderate** for lung, cervix, gastric; **weak/exploratory** for pancreas.

**Chemoprevention (Table 5):**
- Endocrine therapies (tamoxifen, raloxifene, aromatase inhibitors) for breast: FDA-approved / USPSTF-recommended. Tamoxifen reduces incidence by 31% in placebo-controlled trials. Strongest rationale in the review.
- 5α-reductase inhibitors (dutasteride, finasteride) for prostate: RCT evidence; high-grade prevention requires further confirmation.
- Aspirin (COX1/COX2): USPSTF-recommended for CRC; RCT for Barrett's. Rationale: convergent anti-inflammatory + Wnt-β-catenin inhibition.
- Metformin (mitochondrial complex I, MAPK, mTOR): first-line T2DM drug; observational + RCT (adenoma/polyp recurrence confirmed); ongoing RCTs for oral, lung, multiple myeloma. Rationale: metabolic competition reversal + insulin sensitivity. The review argues personalized regimens based on OXPHOS dependence may be needed.
- Statins (HMG-CoA reductase): associated with reduced overall cancer risk; mevalonate pathway disruption; ongoing RCT for colon.
- mTORC1 inhibitors: short-term mTORC1 inhibition curtailed BRCA2-linked tumorigenesis in preclinical ERBB3^lo^ mammary model — a specific mechanistic rationale for the mTORC1/BRCA2 cancer prevention hypothesis.
- Rationale strength varies sharply: **highest** (RCT-validated) for breast endocrine therapy and aspirin in CRC; **moderate** (observational + preclinical) for metformin and statins; **exploratory** (preclinical only) for mTORC1 inhibitors and JAK inhibitors.

**Immunoprevention:**
- HPV vaccine (FDA-approved): prototype; reduces cervical intraepithelial neoplasia.
- HBV vaccine: RCT evidence for primary liver cancer prevention.
- MUC1 vaccine: ongoing RCTs; randomized trial showed non-significant adenoma recurrence reduction; requires improvement.
- KRAS/EGFR mutation-targeted vaccines: ongoing RCTs (KRAS for pancreatic, EGFR for lung).
- PD-1 monoclonal antibodies (nivolumab, pembrolizumab): ongoing RCTs for precancerous lesions (oral leukoplakia, CIN, melanoma). Nivolumab showed >80% decrease in dysplasia in 36% of high-risk proliferative verrucous leukoplakia patients in preliminary trial. [UNVERIFIED: single small trial, n=12]
- Calcipotriol + 5-FU: RCT showing significant lesion reduction with CD4+ T cell mobilization for actinic keratoses (squamous cell precursor).
- Rationale strength: **highest** for viral vaccines; **moderate** for tumor-antigen vaccines (MUC1) with ongoing RCTs; **preliminary** for checkpoint blockade at precancerous stage.

**Lifestyle and dietary interventions:**
- Low-calorie / fasting regimens: activate nutrient-sensing pathways (AMPK/mTOR) and anti-tumor immune responses; confirmed in multiple animal models; clinical evidence limited.
- Dietary fiber / microbiome modulation: associated with reduced CRC risk; mechanisms include butyrate-HCAR2-WNT axis; BE GONE trial confirmed fiber-inulin modulates gut microbes, metabolism, inflammation. Direct intervention trial evidence still lacking.
- Nicotinamide (B3): Phase III RCT confirmed 20% reduction in non-melanoma skin cancers and actinic keratoses in high-risk populations (immunocompetent). Failed in transplant recipients due to DNA damage from immunosuppression. [UNVERIFIED: specific trial NCT]

## Limitations

- Narrative review with no new primary data; all claims are synthesised from highly heterogeneous studies with different designs, sample sizes, and tissue contexts.
- The four-class taxonomy (genetic/epigenetic/environmental/cell-autonomous) is organisationally useful but does not resolve the relative contribution of each class to any specific cancer type. The review does not attempt to quantify which class is rate-limiting.
- Table 1 driver gene dynamics are drawn from cited studies using different sequencing technologies, input sample sizes (N varies from 5 to 616), and analytical methods; cross-tissue comparisons require caution. Many N values are sample counts rather than patient counts.
- The cell competition section describes tumor-suppressive competition as "epithelial defense against cancer" but does not provide a systematic quantification of how frequently competition successfully suppresses vs. fails to suppress transformation.
- The interventional targets section (Table 5) catalogues clinical evidence but does not critically appraise trial quality, publication bias, or effect sizes. Many ongoing RCTs are listed without outcome data.
- Field-effect and epigenetic "tissue memory" concepts are described but not clearly distinguished from one another or from clonal field cancerization — potentially conflating different mechanisms under shared language.
- The review was led by the Lin and Wu groups at CAMS/Peking Union Medical College, and some cited studies are from the same groups; no declaration of a systematic search strategy is provided.
