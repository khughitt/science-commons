---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Shostak2017
type: paper
title: 'Circadian Clock, Cell Division, and Cancer: From Molecules to Organism'
version: "1.0.0"
created: "2026-05-30"
updated: "2026-05-30"
bibkey: Shostak2017
tags: []
datasets: []
ontology_terms:
- DNA-damage-response
- cancer
- cell-cycle
- chronobiology
- circadian-clock
- clock-controlled-genes
---
## Key Findings

### Molecular coupling interface

Clock proteins directly regulate key cell-cycle nodes through transcription and post-translational modification:

- **WEE1 kinase** (inhibits G2/M via CDK1 phosphorylation) is transcriptionally driven by CLOCK/BMAL1; Cry1,2−/− mice show delayed mitosis after partial hepatectomy.
- **p53 pathway:** BMAL1 directly controls p53 transcription (anti-proliferative in pancreatic cancer); PER2 binds and stabilizes p53 by blocking Mdm2-mediated ubiquitination; PER1 controls CHK2 phosphorylation via direct interaction with ATM, enhancing cell-cycle arrest and apoptosis upon DNA damage.
- **p16INK4A** (G1/S inhibitor) expression is activated by PERIOD proteins through the circadian output effector NONO.
- **p21Cip1** (CDK inhibitor) is rhythmically regulated via the REV-ERB/ROR loop through conserved RORE motifs.
- **CRY2** acts as a key regulator of MYC oncogene turnover: it cooperates with FBXL3 to degrade MYC phosphorylated at Thr58, restraining proliferation.
- **E2F transcription factor** (master G1/S activator) is time-dependently phosphorylated; mutation of its phosphorylation sites uncouples cell division from the circadian clock in unicellular algae.
- **TIMELESS (TIM):** dual function in clock (required for circadian rhythmicity) and DNA-damage response (facilitates CHK1/ATR and CHK2/ATM checkpoint signaling).
- Key coupling nodes summarized in Figure 2: MYC, WEE1, ATM/ATR, p16, p21, p53.

### Coupling modes: gating vs. phase-locking

- In cyanobacteria, cell proliferation is clearly gated by the circadian clock even when division periods are ~10 h (shorter than 24 h).
- In NIH 3T3 cells, mitotic events show a trimodal frequency distribution relative to circadian phase (not random), and mathematical modelling characterizes the interaction as **1:1 phase locking** (oscillations at a common frequency) rather than simple gating.
- Intercellular coupling: in 3D intestinal organoids, secretory Paneth cells drive Wnt-dependent circadian entrainment of adjacent stem cell divisions — a paracrine gating mechanism.
- Cell-cycle duration variability shows a "cousin-mother inequality" (sister and cousin cells correlated, mother-daughter cells uncorrelated), interpreted as a deterministic inherited oscillator whose identity may be the circadian clock.
- Important caveat: rat1 fibroblasts and Lewis lung carcinoma cells show robust rhythmic expression of cell-cycle reporters that are uncoupled from the Bmal1 oscillator — coupling is context-dependent, not universal.

### Physiological significance in stem cell compartments

- Skin: diurnal mitotic rhythms reported in UV-exposed epidermis; local clock disruption causes premature epidermal aging and predisposes to carcinogenesis; BMAL1 controls keratinocyte proliferation and DNA-damage sensitivity.
- Hair follicle: disruption of Per1, Bmal1, or Clock prolongs the anagen (intensive proliferation) phase.
- Hematopoietic stem cells: clock-controlled release and circadian oscillation of inflammatory monocytes in blood.
- Intestinal stem cells: circadian Wnt from Paneth cells required for efficient crypt renewal.
- Brain: adult hippocampal neurogenesis shows time-of-day dependent progenitor activation requiring intact clock genes.

### Circadian clock as tumor suppressor (prevailing view)

- Epidemiology: shift work and short sleep associate with elevated cancer risk across multiple cohort studies.
- Mouse models of circadian disruption (SCN lesion, jet lag schedules): accelerated tumor growth, increased Myc expression.
- Clock-gene knockouts: Per2m/m mice sensitive to γ-radiation–induced tumor development; Per1,2−/− and Cry1,2−/− cancer-prone, especially under phase-shifted conditions; Bmal1 heterozygous mice show higher spontaneous tumor rates.
- Molecular mechanism: K-rasLSL-G12D/+; p53flox/flex lung cancer model — jet lag and Per2/Bmal1 mutations increase tumorigenesis and MYC expression levels.
- Liver cancer: wild-type mice under chronic jet lag develop steatohepatitis → fibrosis → hepatocellular carcinoma; accelerated by Cry1,2−/−, Per1,2−/−, or liver-specific Bmal1 knockout.
- Clock restoration: circadian synchronization (dexamethasone) in tumor cells impinges on the cell cycle and reduces cellular growth.

### Counter-evidence: clock genes can promote tumorigenesis (Section 8)

This section presents the important caveat that disrupts a simple tumor-suppressor narrative:

- Clock∆19 MEFs proliferate more slowly than wild-type — consistent with CLOCK/BMAL1 supporting proliferation.
- Human colorectal cancers often overexpress Clock or Bmal1 relative to healthy tissue; CLOCK overexpression increases colorectal carcinoma proliferation in vitro and in vivo.
- Breast cancer: ER-driven upregulation of Clock transcription is required to maintain high proliferation; elevated CLOCK in ERα-positive tumors.
- BMAL1 overexpressed in certain pleural mesotheliomas; Bmal1 knockdown reduces growth in tumorigenic but not healthy cells; both Clock and Bmal1 are survival factors for leukemia stem cells (AML); BMAL1 disruption induces AML differentiation and growth arrest while sparing healthy hematopoiesis — making Bmal1 an anti-leukemia target.
- Also: spontaneous tumor rates are not elevated in some Per1−/−, Per2−/−, or Cry1,2−/− strains relative to wild-type in certain experimental settings.
- Shostak's resolution: cancer-type-specific epigenetic signatures likely define distinct CCG subsets, modulating whether the clock promotes or restrains proliferation. Clock gene knockout effects may partly reflect pleiotropic (non-clock) functions.

### Cancer disrupts host circadian rhythms systemically (Section 9)

- Malignant transformation suppresses circadian rhythms in tumors (oncogenic Ras weakens cellular oscillations; MYC silences the clock across tumor types via Myc/Miz1-dependent repression).
- PASD1 (cancer/testis antigen) interacts with CLOCK/BMAL1 and inhibits transactivation activity.
- Arrhythmic liver metastases of colorectal cancer phase-shift clock genes in healthy distal liver and kidney tissue via humoral factors.
- Lung adenocarcinomas rewire hepatic circadian metabolism systemically (altered metabolic gene oscillations, reduced insulin, elevated blood glucose) — tumor shapes host physiology to serve its energetic requirements.
- Hormone-secreting tumors (Cushing syndrome, pheochromocytoma) directly disrupt circadian blood pressure and cortisol rhythms.

## Limitations

- **Review coverage bias:** Published April 2017; literature on BMAL1-in-AML (ref 119) and some liver-cancer data are from 2015–2016. Rapidly evolving field — some mechanistic claims are likely revised or extended by post-2017 work.
- **Mechanism specificity:** The paper explicitly acknowledges that the precise molecular mechanisms in particular tissues or tumor types remain unclear due to the redundancy of cell cycle regulation components.
- **Cancer-type context missing:** The bidirectionality argument (Section 8) is descriptively convincing but the paper does not offer a mechanistic explanation for why the clock is tumor-suppressive in some cancers and tumor-promoting in others — attributes it to cancer-type-specific epigenetic CCG profiles without specifying them.
- **Coupling direction and causality:** Most evidence from mouse knockouts and pharmacological disruption cannot distinguish clock-to-cell-cycle direction from the reverse; the bidirectional framing is conceptually appropriate but causality is rarely established.
- **Human data thin:** Epidemiological (shift work) evidence is correlational; mechanistic claims rest primarily on rodent and cell line experiments.
- **Temporal resolution:** In vivo cancer studies rarely record time-of-day covariates; the paper does not address whether apparent tumor-suppressor failures reflect phase disruption vs. amplitude loss vs. period change.
