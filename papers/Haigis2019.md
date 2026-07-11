---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Haigis2019
kind: paper
title: 'Tissue-specificity in cancer: The rule, not the exception'
version: "1.0.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: Haigis2019
tags: []
dataset_usage: []
ontology_terms:
- cancer driver genes
- chromatin
- developmental lineage
- epigenetic landscape
- oncogene
- therapeutic resistance
- tissue specificity
- tumor suppressor
paper_kind: review
---
## Key Findings

**Tissue specificity is the rule, not the exception.**
Only a handful of drivers — TERT, TP53, CDKN2A, MYC — show broad multi-tissue
mutation spectra. The overwhelming majority of driver gene alterations are enriched
in one or a few tissue types, even when the driver is ubiquitously expressed (e.g.,
VHL restricted to renal cancer; APC to colorectal cancer; KRAS predominantly to
pancreatic, colon, and lung cancers; BRCA1/2 to breast and ovarian cancer).

**Epigenetic landscape as the permissivity gatekeeper.**
The authors propose that each tissue's developmental lineage establishes a baseline
chromatin and proteomic state (the "epi-proteome") that dictates which oncogenic
signals can be productively sensed and transduced. The same mutation produces
different transcriptional outputs in different chromatin contexts (illustrated with the
glucocorticoid receptor), and TGF-beta acts as an oncogene in some tissues but a
tumor suppressor in others.

**EZH2 as a paradigm of context-dependent driver function.**
Gain-of-function EZH2 mutations are oncogenic in lymphomas and melanomas.
Loss-of-function EZH2 mutations (and loss of other PRC2 components) drive T-ALL,
malignant peripheral nerve sheath tumors (MPNSTs), and myeloproliferative
disorders. The same gene acts as oncogene or tumor suppressor depending on the
tissue's preexisting epigenetic architecture.

**Tissue context governs therapeutic response.**
BRAF-V600E inhibition (RAF inhibitors) is effective in melanoma but largely
ineffective as monotherapy in colorectal cancer (CRC) carrying the same mutation.
The resistance in CRC arises from EGFR-mediated reactivation of MAPK signaling —
a feedback circuit absent in melanoma because EGFR is not expressed there.
Similarly, IDH inhibition works in IDH-mutant AML but not in gliomas with the same
IDH mutation; EGFR inhibition works in EGFR-mutant NSCLC but not in gliomas.
A pan-HER kinase inhibitor showed efficacy in ERBB2-mutant breast, biliary tract,
and cervical cancers but poor responses in lung, bladder, and CRC with the same
ERBB2 mutations.

**Epigenetic plasticity enables therapeutic resistance.**
RB1 mutations are common in small-cell lung cancer (SCLC) but rare in NSCLC.
However, EGFR-mutant NSCLCs can acquire EGFR-inhibitor resistance by
transdifferentiating into SCLC, downregulating EGFR and acquiring RB1 mutations —
demonstrating that the epigenetic state is fluid and can shift under therapeutic
pressure, enabling lineage switching as a resistance mechanism.

## Limitations

- Short Perspectives piece (~2 pages); no new primary data or quantitative analysis.
- The epigenetic-permissivity hypothesis is explicitly labelled phenomenological by the
  authors themselves: mechanistic evidence for most tissue-specific drivers is absent.
- Does not provide a computational or experimental framework for identifying or
  predicting permissive vs. nonpermissive tissue states for a given driver.
- The EZH2 and KRAS examples are well chosen but not systematically sampled from
  all known drivers; selection bias toward the most-studied cases cannot be ruled out.
- Does not address how the epigenetic landscape is reshaped by field cancerization,
  precursor states, or aging — all relevant to the pre-cancer child project.
- Genotype-driven trial implications are speculative; no power calculations or
  quantitative effect-size estimates are given for tissue-stratified trial design.
