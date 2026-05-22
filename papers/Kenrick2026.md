---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Kenrick2026
type: paper
title: Pan-disease blood protein profiles of rheumatic autoimmune diseases
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Kenrick2026
tags: []
authors:
- Kenrick et al.
datasets:
- dataset:human-disease-blood-atlas
- dataset:kenrick2026-olink-sards
doi: 10.64898/2026.02.05.26345462
ontology_terms:
- disease-specific-biomarker
- plasma-proteome
- systemic-autoimmune-rheumatic-disease
venue: medRxiv (preprint)
year: 2026
---
## One-Sentence Summary

Pan-disease plasma proteomics of five systemic autoimmune rheumatic diseases (SARDs) identifies 377 shared inflammatory proteins plus disease-specific protein signatures that enable high-accuracy machine-learning classification (AUC 0.977–0.995), with IIM and SLE showing the broadest proteome perturbation and SSc the strongest individual specificity signal.

## Key Findings

1. **Shared SARD-wide inflammatory core.** 377 proteins are elevated (adj. p < 0.01, logFC > 0.25) in every one of the five SARDs versus healthy controls, dominated by inflammatory-response and oxygen-compound-response pathways. Proteins LTA4H, CCN1, and CXCL13 are among the most elevated shared markers. Only 16 proteins are universally decreased across all SARDs.

2. **Between-SARD differential landscape is highly asymmetric.** Comparing each SARD against the grouped remaining four reveals stark differences in proteome breadth: IIM has 266 proteins elevated and 101 decreased; SLE has 135 elevated and 44 decreased; SSc has 85 elevated and 127 decreased; SjD has 33 elevated and 134 decreased; RA has just 23 elevated but 138 decreased relative to other SARDs. The largest inter-disease overlap is between SSc and IIM (76 shared proteins elevated).

3. **Disease-specific candidate proteins from combined analysis.** Twelve proteins were robustly elevated in one SARD over all other SARDs and both control groups, and consistently selected by machine learning across all five folds (Table 2):
   - **IIM:** LTA4H (logFC 3.74 vs healthy), CA3, EREG
   - **RA:** CRTAC1, COMP (cartilage-matrix proteins)
   - **SjD:** IRAG2 (also selected for SLE)
   - **SLE:** AXL, TNFSF11/RANKL, IRAG2
   - **SSc:** KLK4 (logFC 2.0 vs healthy), CD93, FABP2

4. **Machine learning classification at near-perfect AUC.** A multinomial GLMnet lasso classifier using nested 5-fold cross-validation achieves average AUCs of 0.988 (IIM), 0.995 (RA), 0.977 (SjD), 0.981 (SLE), and 0.992 (SSc) on held-out test sets. SjD is the most frequently misclassified disease. The top-10 important proteins per disease (47 proteins total) improve UMAP separation substantially compared to using all 1,158 proteins.

5. **Infectious disease controls are essential.** Several proteins elevated in SARDs vs healthy controls are also elevated in acute infections (e.g. IL-6, IL-10, CSF3), emphasising that inflammation-related markers lack SARD specificity. The pan-disease design with infectious disease controls (streptococcal soft tissue infection n=77, influenza n=98, malaria n=43) allows disentangling SARD-specific from generic inflammatory signals.

6. **SSc biology dominated by fibrosis and endothelial markers.** Proteins elevated specifically in SSc include KLK4 (kallikrein/enamel-formation), CCN3 (fibrosis/cell communication), MCAM/CD146 and CD93 (endothelial), FAP (fibroblast activation — better known as a tumor marker), and multiple cancer-biology-related proteins (CDH6, CCN3, MCAM, KLK4), consistent with the known SSc-cancer interplay.

7. **SLE proteome reflects apoptotic debris and MMP dysregulation.** MFAP5, PCSK9, TNFSF11/RANKL, AXL, DEFA1_DEFA1B, and multiple MMP-related proteins are SLE-elevated. The authors note that impaired clearance of nuclear debris — a SLE hallmark — may drive broad plasma protein elevation; RANKL/RANK axis elevation is notable for bone-density implications.

8. **IIM proteome enriched for muscle-tissue and mitochondrial proteins.** NOS1, CA3, HSPB6, WARS1/TrpRS (aminoacyl-tRNA synthetase known autoantigen), and NDUFS6 (mitochondrial complex I subunit) show IIM-specific elevation; LTA4H and EREG are top ML features. The innate-immune proteins CXCL10, CCL7, and GBP2 are higher in IIM than other SARDs but lower than acute infectious controls.

## Limitations

- **Cross-sectional design; no longitudinal validation.** All samples collected at diagnosis; disease activity and treatment effects are not modelled. Protein profiles may shift substantially with treatment.
- **Imbalanced cohort sizes** (IIM n=210 vs RA n=84) — machine learning classification is vulnerable to class imbalance; the authors note this and use cross-validation, but acknowledge overfitting risk.
- **No external validation cohort.** All analysis is within the Karolinska cohort; biomarkers need independent replication.
- **Focused on proteins with increased abundance.** Proteins with decreased levels in specific SARDs (potentially equally informative) were not the primary focus of discussion.
- **Autoantibody interference.** In autoimmune diseases, circulating autoantibodies may bind assay targets or detection antibodies (noted explicitly for rheumatoid factor in RA), potentially confounding NPX measurements.
- **Within-SARD heterogeneity not addressed.** Clinical and serological subgroups of each SARD (e.g., antisynthetase syndrome within IIM, anti-CCP+ vs anti-CCP- RA) are collapsed; subgroup protein profiles likely differ.
- **PEA assay coverage.** 1,472-protein panel is large but not proteome-complete; low-abundance proteins and proteins not covered by Olink's binders are invisible.
