---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Aiello2026
kind: paper
title: Circadian Disruption Drives Extracellular Matrix Remodeling to Facilitate Pulmonary
  Metastatic Colonization
version: 1.0.0
created: '2026-05-30'
updated: '2026-05-30'
bibkey: Aiello2026
tags: []
ontology_terms:
- cancer
- circadian-rhythm
- epithelial-to-mesenchymal-transition
- extracellular-matrix
- hippo-pathway
- metastasis
---
## Key Findings

**1. Circadian desynchronization eliminates temporal migration gating in lung fibroblasts.**
Under synchronized conditions, MLg cell migration responses to EGF, FGF2, and TGF-β were temporally restricted to a 12–24 h post-synchronization window; desynchronized cells showed constitutive migration responses at all timepoints. TNF-α bypassed the temporal gate regardless of synchronization status. GSK2945 (REV-ERB antagonist) elevated basal migration independent of cytokine stimulation; KL001 and PF670462 selectively amplified TGF-β-induced migration without affecting basal motility. BMAL1 knockdown dramatically enhanced TGF-β-induced migration, while PER2KO completely abrogated it — establishing that positive (BMAL1) and negative (PER2) clock components have functionally distinct roles.

**2. Circadian synchronization gates MMP expression to discrete temporal windows; desynchronization produces constitutive MMP elevation.**
Under synchronized conditions, Mmp9 showed robust circadian rhythmicity with TGF-β-induced peak expression at 9–15 h post-synchronization, coinciding with the migration window. In unsynchronized cells, all three MMPs (Mmp2, Mmp3, Mmp9) were constitutively elevated throughout the 24 h period. Notably, circadian state inverted TGF-β responsiveness for Mmp3: TGF-β further reduced Mmp3 expression in synchronized cells while markedly suppressing it across all timepoints in unsynchronized cells. GSK2945 recapitulated the unsynchronized MMP pattern.

**3. Chronic jet lag generates nocturnal TNF-α surges that drive sustained in vivo MMP expression and inflammatory programs.**
CJL lungs displayed dramatic nocturnal Tnf-α elevation (ZT12–21; approximately 4-fold amplitude increase relative to daytime nadirs) that was essentially absent under LD control. Concordantly, Mmp2 showed pronounced nocturnal elevation at ZT15–21 specifically under CJL; Mmp9 displayed sustained elevation throughout the circadian cycle under CJL compared to a daytime peak (ZT6) under LD. The temporal co-occurrence of peak TNF-α and peak MMP expression under CJL is mechanistically coherent with in vitro evidence that TNF-α is the most potent inducer of all three MMPs in fibroblasts.

**4. YAP/TEAD is the obligate, non-redundant convergence node for cytokine-driven migration, independent of circadian state.**
Verteporfin (YAP/TEAD inhibitor) completely abolished TGF-β- and TNF-α-induced migration in both synchronized and unsynchronized cells regardless of when inhibitor was added (0, 6, or 12 h post-stimulation). There were no compensatory pathways capable of rescuing migration when YAP/TEAD was disrupted. This invariance to circadian state and inhibitor timing positions YAP/TEAD as the downstream integration point where clock-regulated ECM signals and cytokine programs converge.

**5. CJL reorganizes Hippo pathway temporal dynamics in lung tissue, inverting the permissive window for YAP transcriptional activity.**
Under LD, phospho-YAP (inactive form) peaked at ZT12, with total YAP elevated at the night-to-day transition (ZT18–ZT3), creating a nighttime YAP activity window. CJL inverted this: phospho-YAP peaked at ZT6 and was sustained through day (ZT15–18), while total YAP was elevated primarily during the day (ZT3–12), shifting the permissive window for YAP transcriptional output to daytime hours. This reorganization temporally converges with CJL-induced daytime TGF-β signaling capacity (elevated SMAD4/SMAD7 ratios at ZT9–15 under CJL vs. ZT9 under LD).

**6. CJL activates EMT programs in lung tissue through convergent YAP/TGF-β co-activation.**
CJL induced pronounced nocturnal Zeb1 elevation (ZT12–21) — directly overlapping with the TNF-α surge and following the daytime YAP/TGF-β convergence. At the protein level, CJL produced dramatic and sustained VIMENTIN elevation throughout the 24 h cycle while reducing E-CADHERIN amplitude, representing constitutive rather than gated mesenchymal marker expression.

**7. Chronic jet lag doubles pulmonary metastatic colonization incidence in the B16F10 model.**
Approximately 90% of CJL-exposed mice developed detectable lung metastases compared to approximately 40% of LD controls (chi-square p = 0.045; n = 9–10 per group). CJL significantly increased both the number and size of metastatic foci (two-way ANOVA p = 0.0093) and the percentage of total metastatic lung area (unpaired t-test p = 0.0309).

**8. CJL eliminates temporal organization of pulmonary macrophage populations, favoring constitutively low M1/M2 ratios.**
Under LD, M1 macrophages maintained sustained levels throughout the day while M2 macrophages showed a modest elevation at ZT21, generating time-of-day-varying M1/M2 ratios. CJL abolished this temporal pattern: M1 macrophages dropped dramatically at ZT21, M2 macrophages remained constitutively elevated, and the M1/M2 ratio was constitutively low throughout the day. Single-cell RNA-seq data identified a Cd86+/Mrc1+ double-positive macrophage population expressing elevated clock genes (Clock, Nr1d1, Per2, Per3), high MMP expression (Mmp13, Mmp19), and strong EMT-associated gene patterns — a hybrid pro-metastatic cell type whose temporal oscillations were lost under CJL.

**9. Established metastases amplify CJL-induced pathway reorganization through self-reinforcing cycles.**
In tumor-bearing lungs, CJL created maximal TGF-β expression (ZT15–21), constitutive YAP activity (extended permissive windows through both day and night), sustained Mmp9 elevation, and maximal VIMENTIN levels. The SMAD4/SMAD7 ratio was amplified beyond non-tumor-bearing CJL levels. This demonstrates that established tumors exploit and amplify the pro-metastatic microenvironment created by circadian disruption, transforming CJL from a facilitator of initial colonization into a driver of progressive metastatic burden.

**10. Pathway convergence architecture is conserved in TCGA-SKCM human metastatic melanoma.**
Clock-disrupted tumors (n = 289) showed significantly elevated Clock Correlation Distance (CCD = 4.703) compared to functioning-clock tumors (n = 78; CCD = 3.925; ΔCCD = 0.778, p = 0.002). Among 28 pairwise pathway correlations tested, four were selectively strengthened in disrupted-clock tumors: YAP/TAZ activity with Inflammatory signaling (p < 0.05), YAP/TAZ activity with TNF-α (p < 0.05), EMT Score with CCL2 (p < 0.05), and TGF-β Activators with TNF-α (p < 0.01). All four fell below the identity diagonal, indicating directional strengthening specifically in clock-disrupted human tumors.

## Limitations

- The CJL paradigm uses a repeated 6 h phase advance schedule in male mice only; effects on females, aged animals, or animals with pre-existing tumors are not addressed. The authors note the need to expand to other cancer types and metastatic sites.
- All in vivo work uses the B16F10 melanoma i.v. injection model, which bypasses intravasation and transit steps of the metastatic cascade. This limits conclusions specifically to the colonization and early outgrowth steps.
- The TCGA-SKCM analysis is cross-sectional: the temporal relationship between clock disruption and pathway rewiring cannot be formally established from this design. Most tumors are Metastatic/Disrupted (289/367), making the functioning-clock group comparatively small (n = 78), and the analysis cannot exclude that advanced metastatic stage itself causes clock disruption.
- Single-cell RNA-seq macrophage analysis (Figure 7G–I) was performed only under LD conditions from a single public dataset; direct CJL macrophage transcriptomics is not shown.
- The study does not integrate systemic endocrine measurements (corticosterone, melatonin, body temperature) that would allow attribution of lung microenvironmental changes to autonomous tissue-level clock disruption versus central/systemic signaling reorganization. [SPECULATION: the authors suggest tissue autonomy based on the stability of total macrophage numbers (Figure S5), but the endocrine mediators driving the nocturnal TNF-α surge under CJL are not identified.]
- The functional validation study uses only male mice (n = 9–10 per group), and statistical power to detect differential metastatic burden by foci size category (Figure 6C) may be limited.
