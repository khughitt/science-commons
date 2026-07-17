---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Garraway2006
kind: paper
title: Lineage dependency and lineage-survival oncogenes in human cancer
version: "1.1.0"
created: "2026-07-11"
updated: "2026-07-16"
bibkey: Garraway2006
tags: []
ontology_terms:
- CDX1
- ESR1
- MITF
- TITF1
- androgen receptor
- developmental biology
- lineage addiction
- lineage conditioning
- lineage dependency
- lineage-survival oncogenes
- melanoma
- oncogene addiction
- oncogene amplification
- prostate cancer
- somatic mutation patterns
- synthetic dosage lethality
- tissue of origin
paper_kind: review
---
## Methods

A review/perspective article presenting no original experimental data. The argument is constructed
by surveying published gene amplification and mutation studies across major cancer types (drawn
from the literature and the COSMIC database, per the Figure 2 legend); drawing on functional RNAi
and overexpression experiments from multiple laboratories; synthesising patterns across canonical
examples (MITF/melanoma, AR/prostate, TITF1/lung, ESR1/breast, CCND1/mammary,
FLT3/myeloid); and contrasting lineage-survival oncogenes with broadly expressed oncogenes
(KRAS, EGFR, PIK3CA, BRAF, TP53, CDKN2A) to define the category boundary.

## Key Findings

### Definitions

**Lineage dependency (= lineage addiction):** a model in which tumour cells depend crucially on
survival mechanisms programmed into lineage precursor cells during development, which may then
be affected by acquired genetic alterations. Unlike oncogene addiction — a dependency on a
tumour-specific gain-of-function event — lineage addiction involves the *persistence and/or
deregulation* of crucial lineage-survival mechanisms during carcinogenesis or tumour progression.
No new cellular function is gained.

**Lineage-survival oncogene:** a gene whose lineage-dependency mechanisms promote tumour
progression — a master regulatory gene that also exerts key developmental survival roles. The
paper (Box 3) lists five predicted properties:

1. Crucial role(s) in normal lineage proliferation and/or survival during development.
2. Persistent or deregulated expression in cancers of the associated lineage.
3. Affected by somatic genetic alterations in tumour subsets.
4. Required for tumour survival and/or progression.
5. More likely to be lineage-associated transcription factors than signalling proteins.

The two mechanisms converge on excessive dependency but differ in origin: classical oncogene
addiction acts through growth-promoting genes (often tyrosine kinases) carrying activating somatic
mutations, whereas lineage addiction acts through deregulated master genes mediating normal
developmental functions.

### Lineage conditioning of somatic genetics

Lineage exerts a substantial effect on the distribution of genetic alterations across tumours
(Figure 2). Activating mutations in KRAS, NRAS, HRAS, BRAF, EGFR and PIK3CA, and
amplifications of CCND1, ERBB2 and EGFR, each concentrate in a small number of lineages; even
the distribution of mutations *within* a gene family can vary markedly by lineage. Hierarchical
clustering of SNP-array copy-number data from cancer cell lines and tumour samples reproduces
lineage groupings from copy number alone. Conversely, gatekeeper tumour-suppressor
inactivation (TP53, CDKN2A) is comparatively lineage-independent — though the *mechanism* of
inactivation still varies by lineage, e.g. TP53 point mutation is infrequent in melanoma, where
INK4a/ARF deletion serves the equivalent purpose.

### MITF as the prototype lineage-survival oncogene

MITF is a master transcriptional regulator required for both differentiation and survival of the
melanocyte lineage. Citing Garraway et al. 2005 (Nature):

- MITF is amplified in **15–20% of metastatic melanomas**.
- MITF cooperates with BRAF^V600E to transform immortalised human melanocytes.
- This transforming capacity is manifest only given both aberrant MAPK activation (BRAF^V600E)
  and cell-cycle deregulation via the **p16–CDK4–RB pathway**.

MITF has two separable developmental functions: regulation of the differentiation programme
(associated with growth arrest via p16/RB), and melanocyte lineage survival (proliferative via CDK2;
anti-apoptotic via BCL2). In MITF-dependent melanomas the differentiation/growth-arrest function is
dispensable — indeed detrimental — so these tumours require co-occurring CDKN2A deletion and
constitutive MAPK activation (NRAS or BRAF mutation) for oncogenic MITF function to emerge.
This explains why those specific alterations are so much more frequent in melanoma than
elsewhere: the lineage dependency *conditions* the genetic landscape.

### Androgen receptor as the second prototype

AR is required for development and survival of the prostate epithelial lineage; luminal
differentiation requires AR and leads to growth arrest after a defined period of proliferation. Ectopic
AR expression in prostate epithelial cells with inactivated RB and p53 checkpoints enables tumour
formation after orthotopic injection and androgen stimulation. Both MITF and AR are thus master
transcriptional regulators of their lineages that acquire oncogenic roles in specific genetic contexts.

### ESR1 nuance

ESR1 is treated differently from AR: it has not been convincingly shown to undergo somatic genetic
alteration in breast cancer. Instead, amplification of ER transcriptional co-factors is observed in
breast and ovarian cancer, suggesting other cellular means suffice to deregulate ER in
oestrogen-sensitive tumours. The paper explicitly notes this discrepancy between AR
(mutated/amplified in prostate) and ESR1 (not mutationally altered in breast).

### Catalogue of predicted lineage-survival oncogenes (Table 2)

| Gene | Lineage | Function | Genetic alterations confirmed? | Noted therapeutics |
|---|---|---|---|---|
| MITF | Melanocytic | Transcription factor; melanocyte differentiation/survival | Yes (amplification) | Antisense BCL2 |
| AR | Prostate epithelial | Transcription factor; luminal differentiation | Yes (expression deregulation) | Hormone therapy |
| CCND1 | Mammary | Cell-cycle regulator; mammary maturation | Yes (amplification) | CDK inhibitors |
| FLT3 | Myeloid | Receptor tyrosine kinase; myeloid maturation | Yes (activating mutations in AML) | FLT3 inhibitors |
| ESR1 | Mammary | Transcription factor; breast development | Co-activators amplified; ESR1 itself not mutationally altered in 2006 data | Hormone therapy |
| TITF1 | Lung | Transcription factor; thyroid and lung development | Not yet confirmed in 2006 | — |
| CDX1 | Intestinal | Transcription factor; intestinal development | Not yet confirmed in 2006 | — |
| Ets oncogenes | Prostate, mammary | Transcription factors | Yes (prostate) | — |

The paper uses the name **TITF1** (thyroid transcription factor 1 homeodomain protein) throughout,
not NKX2-1. It notes TITF1 is highly expressed in small-cell lung cancers and lung
adenocarcinomas and is a useful histological marker for primary pulmonary neoplasms, but states
that no genetic alterations had been confirmed at the time of writing.

### Poorly differentiated and lineage-independent cancers

Lineage addiction is not universal. A subset of melanomas downregulate MITF in aggressive
disease; ~1% of prostate cancers are PSA-negative, suggesting AR-independent biology. Poorly
differentiated cancers may rely on lineage-independent mechanisms, though some retain "lineage
memory": microRNA profiles reveal lineage identity even when mRNA expression does not, and
neural-crest lineage responses persist in poorly differentiated melanoma cells injected into chick
embryos.

### Therapeutic implications

Because lineage-survival oncogenes are active in normal lineage cells as well as tumour cells, direct
inhibition raises toxicity concerns. The paper proposes that optimal tumour-specific targets may lie
*outside* the lineage-survival pathway, via **synthetic dosage lethality** — identifying a buffering
factor that becomes essential only when the deregulated lineage-survival gene and its enabling
genetic alterations are both present. Examples cited: BCL2 antisense in MITF-dependent melanoma
(combined with MAPK and CDK inhibitors), FLT3 inhibitors, and AR/ER hormone therapy.

## Limitations

- **2006 snapshot.** Written before systematic pan-cancer sequencing (TCGA, ICGC, PCAWG); the
  catalogue of lineage-survival oncogenes has since expanded substantially. The paper notes that
  TITF1 and CDX1 lacked confirmed genetic alterations at the time; subsequent sequencing
  confirmed TITF1/NKX2-1 amplification at 14q13.3 in lung adenocarcinoma.
- **Amplification focus.** The framework emphasises gene amplification as the primary oncogenic
  mechanism; later work shows activating point mutations, epigenetic de-repression, and
  translocation can serve the same role.
- **Transcription-factor centric.** Box 3 states these genes are "more likely to be lineage-associated
  transcription factors than signalling proteins", so lineage-restricted cell-surface receptors,
  signalling kinases, and metabolic enzymes satisfying analogous logic receive less emphasis.
- **No quantitative definition.** The concepts are qualitative: there is no threshold for how restricted
  normal expression must be, nor for how specifically the cancer must arise from the expressing
  lineage, and Box 3's validation criteria provide no scoring framework. This makes the framework
  hard to operationalise systematically across a large gene × cancer matrix.
- **Lineage addiction is not universal**, applying only to a subset of tumours from each lineage;
  advanced or poorly differentiated tumours may escape lineage dependency.
- **Lineage conditioning is not mechanistically resolved.** The review does not deeply separate
  lineage conditioning as a *selective pressure* from lineage conditioning as a reflection of
  tissue-specific *mutational processes*.
- **The oncogene/tumour-suppressor generalisation has been refined.** The claim that most
  oncogene mutations are lineage-restricted while tumour-suppressor mutations are
  lineage-independent is a 2006 generalisation; IDH1, for example, shows strong lineage restriction
  in glioma and AML.
- **Pre-modern therapeutic era.** The therapeutic discussion (synthetic dosage lethality, BCL2
  antisense) was prescient but predates immunotherapy and BET inhibitors; clinical translation has
  evolved substantially.
