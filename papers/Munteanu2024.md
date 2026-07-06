---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Munteanu2024
kind: paper
title: The Relationship between Circadian Rhythm and Cancer Disease
version: 1.0.0
created: '2026-05-30'
updated: '2026-05-30'
bibkey: Munteanu2024
tags: []
ontology_terms:
- DNA-damage-response
- cancer
- cell-cycle
- chronotherapy
- circadian-rhythm
- clock-genes
- melatonin
- tumor-microenvironment
---
## Key Findings

### Molecular clock and cancer — mechanisms

- The core transcription–translation feedback loop (TTFL) drives ~24 h periodicity via CLOCK:BMAL1 heterodimers activating PER1–3 and CRY1–2 through E-box elements; PER/CRY complexes translocate to the nucleus and suppress CLOCK:BMAL1, closing the loop. A secondary loop (REV-ERBα/β and RORα/β) regulates BMAL1 transcription.
- Clock-controlled genes (CCGs) include ~50–80% of the mammalian genome, encompassing key oncogenes (c-Myc) and tumor suppressors (p53, TP53, RB).
- **Cell cycle:** Circadian clock gates G1/S and G2/M checkpoints. PER2 limits growth by modulating CCNB1 (Cyclin B1), CCND1 (Cyclin D1), and TP53 transcription. BMAL1 and CLOCK regulate cyclins and CDKs. GSK3β, a circadian-regulated kinase, suppresses p53 and RB, promoting tumor cell survival across pancreatic, lung, renal, and CLL contexts.
- **DNA repair:** NER, BER, and DSB repair components exhibit circadian rhythmicity peaking at distinct times; clock gene disruption (shift work, jet lag) impairs these processes, causing mutation accumulation. CHK2 and ATM exhibit circadian oscillations. CRY2 has a unique role in DNA damage repair and genomic stability maintenance.
- **Apoptosis:** CRY1/2 affect the intrinsic apoptotic pathway (TNF-α-dependent) and extrinsic pathway; PER1 operates via both. p53-/-/CRY1/2-/- mice lived 1.5× longer than p53-/- mice with lower cancer incidence, suggesting CRY loss restores apoptotic sensitivity against a p53-null background.
- **Immune system:** Circadian clock regulates biphasic Th1/Th2 cytokine balance (IL-2, IFNγ, IL-12 in early sleep; IL-4, IL-10 in late sleep). Disruption → chronic inflammation, immunosuppressive tumor microenvironment. BMAL1/CLOCK/PER/CRY are expressed in dendritic cells, NK cells, T cells; circadian clock enriches PD-L1, PD-1, TCR, and TNF signaling pathways. IFN-β showed stronger anticancer effect during early light vs. dark phase in mice.
- **Melatonin:** Pineal melatonin peaks nocturnally, suppresses tumor cell lines and acts as a tumorigenesis initiation suppressor; reduced by artificial light at night (ALAN). Melatonin binds MT1/MT2 receptors, blocks NF-κB and HIF-1α nuclear translocation, excludes androgen receptors, inhibits VEGF-A, and suppresses GLUT1 to impair cancer cell glucose uptake.
- **Metabolic reprogramming:** Oncogenic MYC hijacks E-box binding (same sites as CLOCK:BMAL1), driving metabolic dysrhythmia. HIF-1α (activated by clock disruption-induced hypoxia) upregulates GLUTs and glycolytic enzymes (Warburg effect). miR-143, miR-200 family, and miR-378a regulate glycolysis and are interconnected with circadian control. OVEREXPRESSION of CLOCK enhances VEGF and HIF-1α expression.
- **Epigenetics:** Histone modifications, miRNA production, and DNA methylation are under circadian control; methylation of PER1/CRY1 promoters silences these genes in breast cancer cells. Aberrant methylation of circadian gene promoters and dysregulated miRNA production alter 24 h oscillation tempo.

### Cancer-type specificity

- **Breast cancer:** Clock genes NPAS2, CLOCK, RORA, RORB, and PER3 drive breast cancer. Lower PER1/2 expression in sporadic and familial breast tumors vs. normal tissue. Evening chronotype and prolonged (>15 yr) night-shift work linked to higher estradiol in postmenopausal women and higher breast cancer risk. CRY2 high expression correlates with better survival.
- **Prostate cancer (PCan):** ARNTL, CLOCK, BMAL1, CK1ε, CRY1, CRY2, NPAS2, PER1–3 implicated. PER1 suppresses androgen receptor transcriptional activity. Low PER3/CRY2 variants associated with PCan expression. Melatonin mediates androgen receptor nuclear exclusion, suppresses HPG-axis steroidogenesis, and inhibits GLUT1, VEGF-A, and HIF-1α in prostate.
- **AML/leukemia:** BMAL1/CLOCK are required for leukemia stem cell formation in AML; shRNA silencing or pharmacological suppression causes myeloid differentiation and impaired cell-cycle progression. In contrast, earlier data suggest core clock genes can behave as tumor suppressors in other leukemia contexts (downregulation in majority of genes detected).
- **Other cancers:** PER1 suppressed in glioma, breast, prostate; PER2 in leukemia, lung, stomach; PER3 in colorectal. CRY1 overexpression associated with tumor advancement in colorectal. CRY2 low in liver cancer (shorter survival) and thyroid carcinoma. CLOCK protein decreased in Wilms tumors.
- Rest/activity rhythm is an independent prognostic factor in metastatic colorectal cancer patients.

### Chronotherapy

The review organizes chronotherapeutic approaches into three categories (Figure 5):
1. **Training the clock:** melatonin supplementation, morning bright light, glucocorticoid timing, caloric restriction, time-restricted eating (TRE). TRE/early time-restricted feeding shown in mouse models to inhibit tumor development and attenuate metastasis in postmenopausal obesity-driven breast cancer.
2. **Drugging the clock:** small molecules targeting clock proteins directly — CK1δ/ε inhibitors (highly expressed in leukemia, breast, pancreas, ovarian), Fbxw7 regulators, CRY/REV-ERB agonists (prevent GSC growth), CLK8 (stabilizes TTFL negative arm), nobiletin (raises PER2, stabilizes TTFL). RORγ agonists in clinical trials (NCT0292862, NCT03396497) with pembrolizumab for solid cancers.
3. **Clocking the drug:** timing conventional chemotherapy to circadian phase. Oxaliplatin chronotherapy demonstrated safe and effective for metastatic colorectal cancer with "unprecedented long-term survival rates." Cisplatin DNA repair maps show time-of-day repair variation (maximum in evening for murine nocturnal; rodent-to-human translation requires diurnal correction). ADME processes (absorption, distribution, metabolism, excretion) show circadian rhythmicity, making pharmacokinetics time-dependent.

Notable claim: chronotherapeutic regimens using oxaliplatin have led to unprecedented long-term survival rates in metastatic colorectal cancer in clinical trials conducted across multiple centers.

Late meal timing correlated with breast and prostate cancer risk in a large French cohort (NutriNet-Santé); shorter interval between last meal and sleep linked to decreased prostate/breast cancer risk in a separate study.

## Limitations

- Narrative review without systematic selection or PRISMA protocol; no study-quality assessment; evidence levels not distinguished.
- Heavy reliance on animal (mostly murine, nocturnal) and cell-line data for mechanistic claims; rodent-to-human translation of optimal treatment timing requires diurnal correction that is inconsistently addressed.
- Authors note that "existing evidence does not substantiate the assertion that chronochemotherapy is universally advantageous for treating all types of cancer, and it is not a widely adopted practice" — the review's enthusiasm for chronotherapy somewhat outpaces this caveat in the framing.
- Cancer-type-specific clock gene findings are mixed (e.g., BMAL1 is pro-tumorigenic in AML but tumor-suppressive in leukemia contexts), and the review does not resolve this tension systematically.
- No explicit coverage of individual circadian phase variability (genotype, chronotype heterogeneity across patients) as a barrier to implementing chronotherapy at scale, despite citing this as a limitation in the conclusions.
- Institutional affiliation is Romanian veterinary/agricultural sciences — the review does not report primary experimental data and is not from a cancer-biology laboratory; standard for this venue but warrants noting.
- The claimed "unprecedented long-term survival rates" for oxaliplatin chronotherapy in colorectal cancer is not quantified in the review and should be traced to primary trial data (Lévi et al.) before citing this claim.
