---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Kotliarov2020
kind: paper
title: Broad immune activation underlies shared set point signatures for vaccine responsiveness
  in healthy individuals and disease activity in patients with lupus
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Kotliarov2020
tags: []
authors:
- Kotliarov et al.
doi: 10.1038/s41591-020-0769-8
ontology_terms:
- baseline-immune-state
- plasmablast
- plasmacytoid-dendritic-cell
- systemic-lupus-erythematosus
- type-I-interferon-response
pmid: '32094927'
venue: Nature Medicine
year: 2020
dataset_usage:
- ref: dataset:immport-immunespace
  role: analyzed
  overlap: unknown
- ref: dataset:nih-influenza-vaccination-cohort
  role: analyzed
  overlap: unknown
- ref: dataset:websle-paediatric-sle
  role: analyzed
  overlap: unknown
- ref: dataset:yellow-fever-vaccination-cohort
  role: analyzed
  overlap: unknown
---
## One-Sentence Summary

A baseline peripheral blood transcriptional signature (TGSig, 10 genes) reflecting the frequency of activated CD20+CD38++ B cells predicts antibody responses to both influenza and yellow fever vaccination across multiple cohorts, and — evaluated at clinical quiescence — correlates with future disease flare activity in a plasmablast-associated subtype of SLE, revealing a shared type I IFN / plasmacytoid-dendritic-cell activation circuit underlying immune responsiveness and autoimmune disease activity.

## Key Findings

1. **TGSig predicts vaccine response across cohorts and vaccine types.** A 10-gene transcriptional surrogate of CD20+CD38++ B cell frequency (TGSig) distinguishes high and low influenza vaccine responders at baseline (AUC = 0.83, p=0.003 in the discovery NIH cohort at day 0). This predictive signal holds at a second pre-vaccination time point (day −7, AUC=0.70) and at a post-vaccination return-to-baseline time point (day 70, AUC=0.83), and validates in three of four independent influenza cohorts (Stanford 2008 AUC=0.81, Yale 2011 AUC=0.88, Yale 2012 AUC=0.80; all p<0.05) while failing to replicate in a fourth (Emory, four consecutive seasons). TGSig also predicts response to yellow fever vaccine (YF-17D) in naive subjects (AUC=0.86, p=0.014 in the larger of two trials), indicating the signature reflects general immune responsiveness rather than influenza-specific memory.

2. **TGSig evaluated at clinical quiescence predicts subsequent SLE disease activity in a plasmablast-associated subtype.** In a longitudinal paediatric SLE cohort, TGSig computed at low disease activity time points (SLEDAI < 3) is correlated with the disease-activity-associated change in plasmablast score (DaCP) — the quantitative extent of plasmablast-associated flares — in patient groups PG2, PG3, and PG4, whose disease activity was previously linked to a plasmablast/plasma cell signature (Pearson r=0.359, p=0.037 across groups 2,3,4; r=0.535, p=0.010 in PG2+3). TGSig is not predictive in patient groups not showing plasmablast-associated flares (PG1, PG5–7; r=−0.116, p=0.56), establishing subtype specificity.

3. **An independently derived SLE co-expression module (brown module, 370 genes) is enriched in type I IFN / DC activation biology and also associated with vaccine responses.** WGCNA on longitudinal SLE transcriptomics at low disease activity time points identified a brown module whose eigengene correlates with DaCP (Pearson r=0.31, p=0.04). GSEA shows this module is enriched for type I IFN response (LI.M127, LI.M75), innate antiviral response (LI.M150), and activated dendritic cells (LI.M165) at 1% FDR. Meta-analysis of four influenza vaccination cohort datasets confirms the brown module is significantly enriched for genes associated with antibody responses (p=0.01 GSEA). The brown module is itself enriched (GSEA p=0.0003) among genes ranked by correlation with CD20+CD38++ B cell frequency; its top 87 leading-edge genes (SLE-Sig) also carry predictive information for vaccine response (Extended Data Fig. 6a–c). TGSig and the brown module share only one gene (EPHB1) but are functionally linked through pDC activation and type I IFN.

4. **CITE-seq of 53,201 single PBMCs maps the cellular origin of the signatures.** Unbiased profiling of 10 high and 10 low influenza responders (82 surface proteins + transcriptome; average 2,660 cells per donor) identifies TGSig as highest in pDCs (cluster C9) and in switched B cells (C3.1.0), with CD40 activation score (CD40act, 49-gene set reflecting B cell CD40L stimulation / proliferation) significantly elevated in switched B cells of high responders (Fig. 5e, one-tailed Wilcoxon; exact p in Supplementary Table 7). CD40act score in switched B cells correlates with CD20+CD38++ B cell frequency (Spearman rho=0.70, p=0.0018). The LI.M165 DC activation module and IFN-I-DCact gene set are specifically elevated in pDCs (C9) of high responders (p=0.0073 and p=0.014). SLE-Sig is elevated broadly across naïve and memory T cells, CD4+ memory, mDCs, and transitional B cells.

5. **Proposed cellular circuit: pDC-type I IFN-CD40L-switched B cell axis programmes the immune set point.** High responders have more persistently activated pDCs at baseline → elevated type I IFNs → broader lymphocyte activation (T and B cells) including CD40 pathway activation in switched B cells → higher frequency of CD20+CD38++ B cells, encoding a systemic state of partial activation. This same circuit is over-activated in SLE patients with plasmablast-associated flares. In low responders / quiescent SLE patients the circuit is underactivated. Mechanistically, full plasmablast / plasma cell expansion requires additional antigen-specific or inflammatory co-stimulation; the set point encodes responsiveness potential, not constitutive plasmablast output.

6. **TGSig is not driven by genetics, pre-existing antibody titer, or influenza-specific memory.** TGSig is independent of pre-existing influenza antibody levels (by construction of the adjMFC metric), not associated with any trans-eQTL in a large blood GWAS, not associated with age in the NIH cohort, and showed no enrichment for HLA-DR / CD86 genetic associations. Females tend to have higher TGSig than males (consistent with higher vaccine responses and autoimmune susceptibility in females), but TGSig predicted response within sexes.

## Methods

The signature (TGSig) was derived from the NIH/CHI influenza vaccination cohort (n=51 subjects, 136 samples across three baseline time points: day −7, day 0, and day 70 post-vaccination, when parameters had returned to baseline). High/low responders were defined by the adjMFC metric (antibody fold-change independent of pre-existing titer). Flow cytometry identified CD19+CD20+CD38++ B cell frequency (CBSig) as the best-performing predictive population (FlowJo v9.9.3). A 10-gene transcriptional surrogate (TGSig) was built from 726 temporally stable, day-0-correlated genes ranked by a subsampling-robust Spearman correlation (231 iterations), selecting k=10 genes maximizing AUC across all three time points. AUC/permutation-test significance used the pROC package; group comparisons used one-tailed Wilcoxon tests.

TGSig was evaluated, without retraining, in independent influenza cohorts (Stanford 2008, Yale 2011, Yale 2012 — blood transcriptomics via ImmuneSpace/ImmPort) and an Emory cohort (four consecutive seasons, GSE29619/GSE74817), plus two yellow-fever (YF-17D) trials (naive adults; GSE13486).

For SLE, a longitudinal pediatric cohort (previously published) was analyzed; disease-activity-associated change in plasmablast score (DaCP) was estimated via a linear mixed-effects model (R/lme4) in patient groups (PG) 2, 3, 4 (plasmablast-associated; n=34) versus PG1, 5–7 (n=27). WGCNA (soft power 4, signed hybrid) on temporally stable genes at low-disease-activity visits yielded 18 co-expression modules; the "brown" module (370 genes) was tested against DaCP. GSEA (fgsea) identified the 87-gene leading-edge set (SLE-Sig) and enrichment in Blood Transcription Modules (tmod/CERNO test).

CITE-seq (10 high/10 low NIH responders; 82 proteins + transcriptome; Seurat clustering, DSB protein normalization) mapped signatures to cell clusters. Meta-analysis (MetaDE, random-effects) combined four influenza datasets. [UNVERIFIED: complete software version list per Supplementary Table 8, not accessible from main text.]

## Limitations

- **Plasmablast-subtype specificity:** TGSig only predicted DaCP in SLE patient groups whose disease activity was linked to plasmablast signatures (PG2, PG3, PG4); it was uninformative for the majority of SLE patients (PG1, PG5–7). Generalisability to SLE subtypes without plasmablast involvement, and to other autoimmune diseases, is not demonstrated.
- **Paediatric SLE cohort, longitudinal design.** The SLE sample is a paediatric cohort; adult SLE disease activity may be driven by different transcriptional programs. The longitudinal structure requires multiple visits and DaCP estimation via mixed effects models, introducing model-specific assumptions.
- **Small cohort for CITE-seq.** n=10 high + 10 low responders for CITE-seq. Many cluster-level comparisons are nominally significant but underpowered; SLE-Sig differences are not significant in several clusters.
- **TGSig not universally predictive.** TGSig failed to predict response in one Emory influenza dataset (four consecutive seasons from the same US institution; season-specific AUCs 0.46, 0.27, 0.62, 0.51 — all non-significant, spanning chance), highlighting that geographic, demographic, or longitudinal factors can reduce its predictive utility. The authors attribute this to unmeasured cohort-specific factors.
- **Causal direction not established.** The paper identifies correlates of a shared immune set point but does not establish whether pDC activation causes higher vaccine responses (interventional evidence is lacking). Candidate upstream drivers (microbiome, CMV, genetic factors) are explored but none definitively accounts for the set point variation.
- **TGSig derived from CD38++ B cell correlation:** The gene selection procedure is directly driven by the CD20+CD38++ B cell frequency, which means TGSig is by construction a surrogate for this cell population. Novel mechanistic insights come from CITE-seq rather than TGSig itself.
