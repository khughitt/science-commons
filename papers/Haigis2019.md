---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Haigis2019
kind: paper
title: 'Tissue-specificity in cancer: The rule, not the exception'
version: "1.1.0"
created: "2026-07-11"
updated: "2026-07-16"
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
## Methods

A two-page Perspective. No new experimental data or computational analyses are presented.
The authors draw on published literature (12 cited references) to illustrate context-dependent
oncogenesis, support the epigenetic-landscape hypothesis, and argue for a conceptual reframing
of how driver genes should be understood.

## Key Findings

**Tissue specificity is the rule, not the exception.**
Only a handful of drivers — TERT, TP53, CDKN2A, MYC — show broad multi-tissue
mutation spectra. The overwhelming majority of driver gene alterations are enriched
in one or a few tissue types, even when the driver is ubiquitously expressed (e.g.,
VHL restricted to renal cancer; APC to colorectal cancer; KRAS predominantly to
pancreatic, colon, and lung cancers; BRCA1/2 to breast and ovarian cancer).

**Three classes where the mechanism is already known.**
The authors open by conceding the cases that are not mysterious, which sharpens what the
rest of the paper is about. Tissue-specific *expression*: ESR1 is highly expressed and controls
proliferation in estrogen-responsive tissues, explaining its role in ovarian, endometrial, and
breast cancer. Tissue-specific *exposure*: xeroderma pigmentosum proteins (ERCC3, XPC) perform
excision repair of UV-induced damage, so their loss primarily causes skin cancers. Tissue-specific
*differentiation program*: GATA3 regulates breast ductal differentiation and participates in a
lineage-specific circuit limiting stem-cell expansion.

**The unexplained cases are the argumentative core.**
Broadly expressed, essential genes with tissue-restricted driver patterns cannot be explained by
the three classes above. BRCA1/BRCA2 are ubiquitously expressed and function in homologous
recombination, yet inherited inactivating mutations predispose largely to breast and ovarian
cancer; the authors offer two candidate explanations — complete loss of function may be tolerated
only in these tissues, or the cyclical estrogen response there generates greater demand for
homologous recombination. VHL (renal), APC (colorectal), and KRAS (pancreas, colon, lung) are
broadly expressed with similarly restricted driver activity.

**Empirical support that specificity is the rule.**
Genetic screens of proliferation across cell types (Sack et al. 2018, Cell 173:499) found that
while core cell-cycle regulators (D-type cyclins, CDK inhibitors) universally affected
proliferation, 80–90% of proliferation-promoting genes differed between cell types.
Tissue-specific oncogenes and tumor suppressors identified through cancer genomics affected
proliferation only in their cognate tissue types. This is the paper's strongest quantitative
support, and it is borrowed rather than generated.

**Epigenetic landscape as the permissivity gatekeeper.**
The authors propose that each tissue's developmental lineage establishes a baseline
chromatin and proteomic state (the "epi-proteome") that dictates which oncogenic
signals can be productively sensed and transduced. The same mutation produces
different transcriptional outputs in different chromatin contexts — illustrated with the
glucocorticoid receptor, whose activation yields different transcriptional readouts across cell
types because accessible chromatin differs (John et al. 2011, Nat. Genet. 43:264) — and
TGF-beta acts as an oncogene in some tissues but a tumor suppressor in others.

**EZH2 as a paradigm of context-dependent driver function.**
Gain-of-function EZH2 mutations are oncogenic in lymphomas and melanomas.
Loss-of-function EZH2 mutations (and loss of other PRC2 components SUZ12, EED) drive T-ALL,
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
ERBB2 mutations (Hyman et al. 2018, Nature 554:189) — which the authors flag as evidence that
genotype-alone trials must be powered to detect tissue-to-tissue variation.

**Epigenetic plasticity enables therapeutic resistance.**
RB1 mutations are common in small-cell lung cancer (SCLC) but rare in NSCLC.
However, EGFR-mutant NSCLCs can acquire EGFR-inhibitor resistance by
transdifferentiating into SCLC, downregulating EGFR and acquiring RB1 mutations —
demonstrating that the epigenetic state is fluid and can shift under therapeutic
pressure, enabling lineage switching as a resistance mechanism.

**The authors' prescription for driver discovery.**
Tissue-specificity remains phenomenological, and the authors call for mechanistic investigation
comparing the effects of cancer genes in permissive versus nonpermissive tissues. A deconstruction
of the transcriptional, epigenetic, proteomic, and biological responses to a given alteration
across tissues should reveal both developmental insight and therapeutic vulnerabilities.

## Limitations

- Short Perspectives piece (~2 pages); no new primary data or quantitative analysis.
  It provides illustrative examples rather than a systematic survey: the claim that
  tissue-specificity is "the rule" rests on the Sack et al. 2018 screen (the 80–90% figure) and
  selected genomic examples, not a comprehensive statistical analysis across all known drivers.
- The epigenetic-permissivity hypothesis is explicitly labelled phenomenological by the
  authors themselves: mechanistic evidence for most tissue-specific drivers is absent.
  Mechanistic explanations remain incomplete for several named examples (BRCA1/2, VHL, APC,
  KRAS), which the paper candidly acknowledges and frames as motivation for future work.
- Does not provide a computational or experimental framework for identifying or
  predicting permissive vs. nonpermissive tissue states for a given driver — it is a framing
  piece, not a predictive tool.
- The EZH2 and KRAS examples are well chosen but not systematically sampled from
  all known drivers; selection bias toward the most-studied cases cannot be ruled out.
- Does not address how the epigenetic landscape is reshaped by field cancerization,
  precursor states, or aging.
- Epigenetic reprogramming, tumor microenvironment signaling, and clonal selection dynamics are
  acknowledged implicitly but not elaborated as distinct mechanisms.
- Genotype-driven trial implications are speculative; no power calculations or
  quantitative effect-size estimates are given for tissue-stratified trial design.
