---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Bigge2024
kind: paper
title: Expression quantitative trait loci influence DNA damage-induced apoptosis in
  cancer
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Bigge2024
tags: []
authors:
- Bigge et al.
doi: 10.1186/s12864-024-11068-6
ontology_terms:
- DNA-damage-response
- apoptosis
- cancer-hallmarks
- expression-quantitative-trait-locus
venue: BMC Genomics
year: 2024
dataset_usage:
- ref: dataset:bigge2024-cd8-cohort
  role: analyzed
  overlap: unknown
- ref: dataset:gtex
  role: analyzed
  overlap: unknown
---
## Key Findings

1. **Broad transcriptional repression upon DNA damage.** 5,373 genes are DEG across all stimuli (adj. p < 0.05, |log2FC| > 1.5); 85–99% are suppressed depending on stimulus. Common downregulated DEGs are shared across stimuli and enrich for autophagy/organelle organization/transport (TBOOH, MMS) or protein modification (BPDE, UVC). Only 8 common upregulated genes identified. Hallmark GSEA: apoptosis (q = 1.22×10⁻⁴), p53 signalling (q = 1.22×10⁻⁴), oxidative phosphorylation (q = 2.17×10⁻²), E2F targets (q = 4.6×10⁻²) enriched in upregulated genes, driven by BPDE and HC.

2. **654 eGenes identified; 47 are e²QTL (4–5% per stimulus).** 550/654 eGenes were present in unstimulated T cells; stimulation reduces eGene count (409–271 per condition) and eQTL effect sizes. Effect size correlation with GTEx whole blood: Spearman ρ = 0.73. 38 eGenes showed consistently opposite slope direction vs GTEx, including SMPD4 (NSMASE3), which had |Δslope| = 0.44–1.12 (the largest cell-type-specific eQTL divergence observed).

3. **KLF2 e²QTL colocalizes with multiple myeloma GWAS.** KLF2 is a downregulated DEG across all BER/NER-associated stimuli (MMS, BPDE, UVC, TBOOH). Its e²QTL (GWAS variant rs11086029; eQTL/e²QTL variant rs3745318–rs7246538 depending on stimulus) has |Δslope| = 0.7–0.75 across conditions. MM GWAS risk allele carriers show increased KLF2 expression at baseline and a reduced e²QTL effect upon stimulation. Colocalization with the MM GWAS at the KLF2 locus: PP.H4 > 0.993 and PP.H4/PP.H3 > 143 across all conditions — the strongest colocalization result in the paper. KLF2 knockdown is known to trigger apoptosis in MM cells, and the KDM3A–KLF2–IRF4 axis is established as a myeloma maintenance pathway.

4. **Additional GWAS-linked eGenes.** A total of 3 eQTL and 8 e²QTL referring to 7 eGenes represent GWAS risk variants for 5 oncological and 2 neuropsychiatric diseases (Table 1):
   - **XBP1** (eQTL): breast cancer (rs5997389, r² = 0.802) and ovarian cancer (rs6005807, r² = 0.73 / 0.746). Risk alleles have opposite expression direction for the two cancers.
   - **PLEC** (eQTL, BPDE): bipolar disorder (rs7822511, r² = 0.852) and multiple sclerosis (rs3923387, r² = 0.804); risk alleles → decreased PLEC expression.
   - **PIP4K2A** (e²QTL, MMS): B-cell ALL (rs10430590, r² = 0.761); risk alleles → increased expression.
   - **GPR160** (e²QTL, TBOOH): testicular germ cell tumour (rs6778888, r² = 0.824); risk alleles → increased expression.
   - **RPS18** (e²QTL, HC): breast cancer (same variant rs17215231, r² = 1); only eGene where the top GWAS SNP equals the top eQTL SNP; risk allele → reduced expression.
   - **ARL17B** (e²QTL, UVC): breast cancer (rs141783865, r² = 0.91).

5. **Context-specificity of eQTL.** HC exposure yields the highest number of stimulus-specific eGenes and the most distinct GO enrichment profile (RNA metabolism rather than immune processes). SMPD4 shows a uniquely large context-specific regulatory switch not previously characterised.

## Limitations

- **Single cell type (CD8+ T cells).** Results may not transfer to tumour cells, BM plasma cells, or other relevant tissue types. The authors explicitly acknowledge unknown transferability.
- **European-only cohort.** Regulatory variant effects and GWAS LD patterns may differ in non-European populations.
- **6-hour stimulation window.** Early apoptosis only; repair-phase and late apoptosis gene regulation not captured.
- **Dose calibration by DEG count.** Stimulation doses were chosen to maximise DEG yield, not to mimic physiological exposure; pharmacological relevance is uncertain.
- **Small e²QTL fraction (4–5% of eGenes per stimulus).** Most eQTL are not context-modified by DNA damage; whether this reflects biology or statistical power is unclear.
- **Raw data access restricted.** EGA accession EGAS50000000666; data available "on reasonable request and with permission of Inventum Genetics GmbH" — not freely reusable for downstream integration.
