---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Evans2023
type: paper
title: Clonal Hematopoiesis, Somatic Mosaicism, and Age-Associated Disease
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Evans2023
tags: []
datasets: []
ontology_terms:
- CHIP
- age-associated disease
- cardiovascular disease
- clonal hematopoiesis
- drift
- fitness coefficient
- inflammaging
- mosaic chromosomal alterations
- selection
- somatic mosaicism
---
## Key Findings

### Prevalence and drivers

Clonal hematopoiesis prevalence is strongly sequencing-method-dependent:

| Study | Cohort | Method | Detection limit | ~Prevalence at 70+ |
|---|---|---|---|---|
| Jaiswal et al. 2014 | 17,182 | WES, 160 driver genes | ~3% VAF | ~10% |
| Genovese et al. 2014 | 12,380 | Non-biased WES | ~3% VAF | ~10% |
| Zink et al. 2017 | 11,262 Icelanders | Barcoded whole-genome | ~7% VAF | ~50% |
| McKerrell et al. 2015 | 4,219 aged 60–98 | Ultra-deep hotspot | ~0.8% VAF | ~40%–74% by age 90 |
| Young et al. 2016 | 20 (NHS) | Error-corrected sequencing | ~0.03% VAF | DNMT3A/TET2 in 95% at 50–70 y |
| Fabre et al. 2022 | 385, 55–93 y | Longitudinal targeted | <0.1% VAF | Near-ubiquitous by midlife |

Principal CHIP driver genes by frequency: *DNMT3A* (most frequent, particularly R882H missense hotspot with dominant-negative effect on methyltransferase activity), *TET2* (second most frequent, loss-of-function indels/nonsense), *ASXL1*, *JAK2* (V617F gain-of-function), *TP53* (missense at codons 248/273 with gain-of-function), *PPM1D* (gain-of-function exon 6 truncations), *SF3B1*, *CBL*, *SRSF2*, *EZH2*, *SETBP1*, and others.

Non-coding/chromosomal subtypes: mosaic loss of Y chromosome (mLOY; most common somatic mutation in human leukocytes — 8.2% of men by 70 years, rising to ~40% >85 years), mosaic autosomal chromosomal alterations (mCAs; ~2% <45 y rising to ~5% >65 y in UK Biobank), mosaic loss of X (mLOX in women). Unknown driver mechanisms account for ~40% of all detectable clonal events.

Clonal dynamics (Fabre et al. 2022 longitudinal data): most clones expand at a stable exponential rate dependent on driver identity; many *DNMT3A* mutation clones were acquired before the age of 10, with growth rates decelerating in old age; splicing-factor-mutant clones show accelerated expansion; diversity of clones peaks in midlife then declines as a subset expands to dominate, possibly providing a fertile ground for clone outgrowth.

### Selection vs. drift — fitness landscape

**Key quantitative source: Watson et al. 2020 (Science 367:1449–1454; ref 40 in this review).** That paper used longitudinal VAF dynamics and evolutionary modelling to estimate per-gene fitness coefficients for CH mutations. Evans & Walsh do not reproduce the coefficient values directly, but the review's biological framing is consistent with the following gradient:

| Mutation class | Fitness context | Evidence for selection |
|---|---|---|
| *TET2* loss-of-function | Constitutive; augmented under inflammatory stress (TNFα/IL-6) | Clear: *Tet2*-deficient HSCs expand progressively in competitive BMT under homeostatic conditions; clonal expansion in mice mirrors human CH kinetics |
| *DNMT3A* R882H | Context-dependent; strong in aged/inflamed niche, minimal in young transplant recipients | Partial: *Dnmt3a*-mutant HSCs do not expand appreciably in 4-month competitive BMT studies; expand after serial transplants or in aged mice; strongly promoted by IFN-γ/chronic infection (Liao et al.) |
| *JAK2* V617F | Constitutive gain-of-function; myeloid expansion | Strong: constitutive kinase activation; expands exclusively in myeloid lineage; enriched in pulmonary hypertension patients |
| *PPM1D* gain-of-function | Context-specific: selectively advantaged under DNA-damage-activating chemotherapy (cisplatin, etoposide, doxorubicin, carboplatin, radiation); selective disadvantage in serial transplantation | Therapy-conditional: pre-existing small clones expand 15–20% among cancer patients on platinum-based or radiation therapy |
| *TP53* missense gain-of-function | Therapy-conditional (radiation, taxanes, platinum); provides HSC resistance to apoptosis | Strong therapy-selection: enriched in ~30% of lymphoma patients post-autologous SCT and in 25% of non-hematologic cancer patients post-chemotherapy |
| *ASXL1* truncating | Natively slow; advantaged under inflammation and HIV infection | Weak in homeostasis; mTOR-dependent accumulation via Akt signalling; competitive disadvantage in transplantation; ASXL1 most common mutated driver in HIV-positive individuals |
| mLOY | Uncertain clonal vs. random somatic event; possibly a marker of genomic instability | Partially clonal: longitudinal increase in fraction in some individuals; unclear whether growth advantage or tolerance |

**Where drift likely dominates:** The large clonal pool of small-VAF clones detected only at extremely deep sequencing (0.03% VAF) and accounting for ~40% of all clonal events shows growth kinetics that are consistent with neutral drift or very small selection coefficients (s < 0.01 per year). The "unknown driver" events — by definition not in known cancer driver genes — likely represent a mixture of true neutral clones hitchhiking on linked driver mutations (Poon et al., ref 46) and genuine alternative driver mechanisms. Mitchell et al. 2022 (ref 47) phylogenetic analysis of *DNMT3A* clades found 2 of 13 expanded clades acquired their mutations before age 20, with the remaining acquired before age 40 and expanding over decades — a pattern consistent with modest selection coefficients (estimated ~1% selective advantage per cell division in the Watson 2020 modelling, [UNVERIFIED for the specific coefficient value from Evans & Walsh, which cites Watson 2020 as the primary source but does not reproduce the table]).

**Key evolutionary insight:** Once clones exceed ~2% VAF they are more likely to continue growing than those below this threshold (ref 114), suggesting a threshold-dependent competitive dynamic rather than a purely linear selection model.

### Disease associations: catalogue and evidence quality

The review distinguishes correlation, predisposition risk, and experimental causal demonstration. The table below summarises findings across the major conditions:

#### Cardiovascular disease (most extensively studied)

| Condition | CH type | Evidence type | Key numbers | Mechanism (experimental) |
|---|---|---|---|---|
| Coronary heart disease / ischemic stroke | CHIP (DNMT3A, TET2, ASXL1, JAK2) | **Epidemiological correlation + predisposition** | HR 2.0 (CHD), 2.6 (stroke) after adjusting for traditional CVD risk factors (Jaiswal 2014); JAK2 mutation carriers HR 12.0 for CHD | IL-1β/NLRP3 inflammasome upregulation in TET2-deficient macrophages (causal in mice) |
| Heart failure (CHF, STEMI, TAVI) | CHIP (DNMT3A, TET2, PPM1D) | **Predisposition + causal in mice** | VAF ≥1–2% associated with worse prognosis; dose-dependent relationship; TET2-VAF inversely correlated with telomere length | TET2 and DNMT3A promote adverse cardiac remodelling via IL-1β/IL-6; NLRP3 inhibition (MCC950) rescues in LAD/TAC models |
| Atherosclerosis | CHIP (TET2, JAK2^V617F^, TP53) | **Causal in mice** | ~40% larger atherosclerotic lesions in *Tet2*-deficient chimeric mice vs. controls | TET2: NLRP3→IL-1β in macrophages → endothelial activation → monocyte recruitment; JAK2: AIM2 inflammasome; TP53: macrophage hyperproliferation |
| Peripheral artery disease | CHIP | **Correlation** | CHIP associated with incident PAD in 50,122 individuals from 2 biobanks | — |
| mLOY-cardiovascular | mLOY (Y chromosome loss) | **Correlation** | Men with >40% mLOY cells had 30% higher risk of dying from circulatory diseases (HR: hypertensive disease 3.48, heart failure 1.76, aortic aneurysms 2.76) | TGF-β1 signalling-driven profibrotic macrophage phenotype (causal in mouse TAC model using CRISPR mLOY) |
| Stroke | CHIP | **Correlation** | CHIP associated with increased hemorrhagic and small-vessel ischemic stroke (TET2 strongest for ischemic; DNMT3A for hemorrhagic) | — |
| Thrombosis | JAK2^V617F^ CHIP | **Correlation + mechanistic** | 25% of JAK2^V617F^ CHIP carriers experienced thrombotic event vs. 2% non-CHIP; even 2% VAF clones confer risk | JAK2^V617F^ neutrophils form extracellular traps (NETs) via PAD4; β1/β2 integrin activation |

#### Leukemia and hematological malignancy

| Condition | Evidence | Key numbers |
|---|---|---|
| Risk of hematological malignancy | **Predisposition** — confirmed epidemiological | 10-fold increased risk in CHIP carriers vs. non-carriers; absolute risk low: most will never develop blood cancer (requires multiple driver mutations) |
| Therapy-related myeloid neoplasm (t-MN) | **Predisposition + causal** | 30% of lymphoma patients post-autologous SCT have CHIP (PPM1D and TP53 enriched); PPM1D mutations ~15–20% prevalent in therapy-related MDS vs. ~3% in de novo AML; pre-existing small clones below detection limit are selected and expanded by cytotoxic therapy |
| Risk is clone-size-dependent | **Predisposition** | VAF >10% associates with higher hematological cancer risk |

#### Infectious disease

| Condition | CH type | Evidence | Key numbers |
|---|---|---|---|
| Infection (sepsis, pneumonia, digestive/respiratory) | mCAs | **Correlation** | mCAs associated with hazard ratio 1.12 for incident infection; expanded autosomal mCAs HR 1.25; stronger association for those who subsequently develop cancer |
| Severe COVID-19 | mCAs + unknown driver CH | **Correlation** | Unknown-driver CH (odds ratio 2.01) and passenger mutations associated with severe COVID-19; no association with putative driver gene CH (CHIP) in same study |
| HIV | CHIP (ASXL1-enriched) | **Correlation + mechanistic hypothesis** | HIV-positive individuals have >2x the level of CHIP; ASXL1 most commonly mutated in HIV-positive cohort; HIV may provide selective advantage to ASXL1 mutant clones |
| C. difficile, Streptococcus/Enterococcus infection | CHIP | **Correlation** | CHIP associated with onset of both infection types in cancer patients (MSK-IMPACT cohort); C. difficile significant only for unknown-driver CH and VAF >5% |

#### Cytopenias and immune conditions

| Condition | Evidence | Notes |
|---|---|---|
| Anemia / cytopenia | **Correlation** | Reduced hematopoietic output from DNMT3A-mutant HSCs (impaired differentiation despite intact self-renewal); DNMT3A mutations in some aplastic anemia patients |
| Autoimmune conditions (ulcerative colitis, vasculitis) | **Correlation** | CHIP enriched in IBD (~30% of anti-neutrophil cytoplasmic antibody-associated vasculitis have CHIP vs. ~17% controls); inflammatory environment likely promotes CHIP expansion |
| Alzheimer's disease | **Complex/divergent** | CHIP associated with *lower* hazard ratio for incident Alzheimer's disease (protective?); mLOY associated with *higher* risk; divergent findings suggest different downstream effects of CHIP driver genes vs. chromosomal mutations on immune cells in brain |

#### Other conditions

| Condition | CH type | Evidence | Notes |
|---|---|---|---|
| Chronic kidney disease | CHIP (TET2, JAK2, PPM1D, CBL) | **Correlation** | Myeloid-derived CH mutations negatively associated with eGFR-cys; CHIP → worse adverse outcomes 1.56-fold higher |
| Type 2 diabetes | CHIP, mCAs | **Modest correlation** | CHIP modestly associated with increased T2D risk; mCAs associated with T2D (chromosomes 10 and 17) but not autosomal mCAs overall |
| COPD | CHIP | **Correlation** | CHIP poses similar risk for severe COPD as ~20 pack-years cigarette exposure; strong smoking–CHIP confound |
| Osteoporosis | CHIP (DNMT3A, ASXL1) | **Correlation + causal in mice** | DNMT3A-mutant macrophages secrete IL-20 promoting osteoclastogenesis; alendronate rescues bone mineral density in *Dnmt3a*-deficient BMT mice |
| Gout | TET2 | **Causal in mice** | *Tet2*-deficient macrophages show enhanced IL-1β secretion after monosodium urate crystal stimulation; NLRP3 pathway |
| Accelerated biological aging | CHIP (DNMT3A, TET2) | **Correlation** | CHIP associated with accelerated epigenetic aging (Horvath clock); TET2/ASXL1/JAK2/PPM1D CHIP inversely correlated with telomere length |
| Premature menopause | CHIP (DNMT3A) | **Correlation** | CHIP associated with premature menopause in women; gene-specific analysis significant only for DNMT3A |
| Solid organ tumors | mLOY, CHIP | **Modest correlation** | mLOY associated with non-hematological cancers; unclear whether CHIP is a causal contributor or biomarker of genomic instability |

### Experimental mechanisms (summary of mouse model evidence)

**TET2 (causal evidence strongest):**
- TET2 deficiency in macrophages increases IL-1β transcription and NLRP3 inflammasome expression → excess active IL-1β secretion → endothelial activation and monocyte recruitment (causal for atherosclerosis).
- Validated by competitive BMT in *Ldlr*^-/-^ mice with 10% Tet2-deficient cells: accelerated atherosclerosis with ~40% larger plaque; myeloid-specific Tet2 deletion confirms myeloid cell primacy.
- NLRP3 inhibitor MCC950 reduces atherosclerotic lesion size specifically in Tet2-deficient chimeras.
- CANTOS trial sub-analysis: *TET2* CHIP carriers showed 62% reduction in MACE with Canakinumab (IL-1β neutralization) vs. 7% reduction in non-CHIP individuals — translational validation of the IL-1β causal mechanism.
- TET2 loss accelerates heart failure (LAD and TAC models); CRISPR approach confirmed.
- TET2 mediates metabolic syndrome: *Tet2*-deficient cells exacerbate insulin resistance in high-fat/high-sucrose diet model via NLRP3/IL-1β in epididymal white adipose tissue.
- TET2 deficiency promotes lung cancer growth in subcutaneous model via S100a8/S100a9 → VEGF-A/angiogenesis (also an opposing myeloid Tet2 result in melanoma — discrepant tumor-type findings).

**DNMT3A (causal evidence for inflammation; fitness mechanism distinct from TET2):**
- DNMT3A mutations: methylation erosion → IFN regulatory factor 3 (IRF3) → NF-κB → IL-20 → osteoclastogenesis (mechanism for osteoporosis).
- DNMT3A heart failure model shows augmented macrophage and T-cell accumulation in heart; augmented inflammatory cytokine profile (IL-6, CCL chemokines) that differs from TET2 (which uses IL-1β/NF-κB not Cxcl1/Cxcl2).
- DNMT3A mutant cells do not expand appreciably in short-term competitive BMT but do so in aged recipients and during chronic infection (IFN-γ pathway).
- DNMT3A R882H promotes HSPC self-renewal at expense of differentiation; resistance to necroptosis (downregulated RIPK1/RIPK2); provides competitive advantage in inflammatory aged bone marrow niche.

**JAK2^V617F^:**
- Gains of function → constitutively active kinase → myeloid expansion; STAT3 signalling; expansion accelerated post-myocardial infarction (clinical data: myocardial injury promotes JAK2^V617F^ expansion).
- Heart failure: 1–19% JAK2^V617F^ chimerism sufficient to increase right ventricular pressure and promote pulmonary hypertension in mice; mechanism via IL-6-JAK-STAT-ACVRL1 upregulation → Smad1/5/8 → arterial remodelling.
- Thrombosis: JAK2^V617F^ neutrophils have increased PAD4 → NET formation.
- Atherosclerosis: JAK2^V617F^ macrophages use AIM2 inflammasome (not NLRP3); IL-1β blockade improves plaque stability without reducing lesion size.

**TP53:**
- Missense gain-of-function (p53^R248W^, p53^R273H^): provides resistance to apoptosis after radiation/taxane/platinum; promotes doxorubicin-induced cardiomyopathy via neutrophil-mediated cytotoxic response.
- Accelerates atherosclerosis via macrophage hyperproliferation mechanism (TP53^-/-^ macrophages more proliferative, accumulate in plaques).

**PPM1D:**
- Gain-of-function (exon 6 truncations): reduces DNA-damage response → cells survive cytotoxic stress; selectively advantaged only under specific agents (cisplatin, etoposide, doxorubicin, carboplatin, radiation; NOT vincristine or 5-FU).
- Promotes non-ischemic heart failure via elevated ROS/IL-1β/IL-18 → NLRP3; rescued by MCC950 in mice.

**mLOY:**
- CRISPR-Cas9 mLOY mouse model (Walsh laboratory, Sano et al. 2022): LOY cells generate macrophages with profibrotic (TGF-β1) rather than proinflammatory (IL-1β) phenotype — mechanistically distinct from CHIP.
- mLOY macrophages promote cardiac fibrosis via TGF-β1/SMAD2 signalling; anti-TGF-β1 partially rescues.
- Anti-Gr1 antibody (myeloid depletion) reduces cardiac dysfunction in mLOY mice, confirming myeloid cell primacy.

### Factors promoting clonal expansion

The review identifies two classes of factors:

**HSC-intrinsic:**
- TET2 mutations → increased self-renewal and myeloid differentiation; clear competitive advantage even in homeostasis.
- DNMT3A mutations → increased self-renewal at expense of differentiation; requires aged/inflammatory context for expansion.
- TP53 and PPM1D mutations → extrinsic DNA damage resistance (chemotherapy/radiation).
- ASXL1 truncating mutations → Akt/mTOR-dependent cycling; competitive disadvantage in transplantation but can expand via accumulating DNA damage over long time horizons; rapamycin reverses expansion.

**HSC-extrinsic (niche and environment):**
- Aged bone marrow niche: aged HSCs exhibit diminished self-renewal, myeloid skewing, oxidative stress, epigenetic drift, telomere shortening — aged niche provides relative competitive advantage to mutant clones.
- Inflammation: TNF-α elevated in aged bone marrow; TET2 and DNMT3A mutant HSCs are relatively resistant to inflammatory-stress-induced cell death, outcompeting wild-type HSCs.
- Chronic infection (Mycobacterium avium → IFN-γ): promotes DNMT3A-mutant clone expansion by selectively impairing IFN-γ-driven terminal differentiation.
- Disease environment as selective pressure: HIV favors ASXL1 clones; smoking favors ASXL1; UC/IBD inflammatory environment selects DNMT3A/PPM1D; myocardial injury promotes JAK2^V617F^ expansion.

## Limitations

- The field is dominated by observations from the UK Biobank and TOPMed, which are predominantly of European ancestry; CHIP prevalence, driver-gene spectrum, and disease associations in diverse populations are incompletely characterised.
- Causality vs. correlation remains underdetermined for most non-cardiovascular associations (infection, T2D, CKD, COPD, Alzheimer's). The cardiovascular domain is the exception where mouse models have established causal links.
- The CHIP definition (VAF ≥2%) is acknowledged as a sequencing detection limit artifact, not a biologically principled threshold; clinically relevant effects likely begin at lower VAFs (data on 0.5–2% VAF from Dorsheimer et al. and Cremer et al. suggest prognostic effects below 2%).
- Mouse models are confounded by pre-conditioning irradiation in most BMT approaches (inflammation, niche disruption, depletion of tissue-resident macrophages); adoptive transfer and CRISPR approaches address some but not all of these artifacts.
- The mechanism by which mLOY promotes cardiac fibrosis (TGF-β1-profibrotic macrophage) was established only in one mouse model; clinical causal evidence for mLOY remains weaker than for CHIP.
- Directionality of the CHIP–aging relationship is bidirectional and not fully resolved: does CHIP drive accelerated aging, or does accelerated aging drive CHIP expansion, or both?
- Solid organ tumor associations with CHIP are confounded by therapy-related CHIP enrichment in cancer patients; the independent association with non-hematological cancers is uncertain.
