---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:SkoufouPapoutsaki2026
kind: paper
title: Clonal biases dictate availability of colonic cancer driver mutations for transformation
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: SkoufouPapoutsaki2026
tags: []
ontology_terms:
- clonal dynamics
- clonal fixation
- colorectal cancer
- crypt fission
- driver mutation
- mutation ordering
- normal tissue evolution
- preneoplastic evolution
- somatic evolution
- spatial transcriptomics
---
## Key Findings

### Operational definition of "clonal bias"
Clonal bias is operationalised as a statistically elevated fixation rate (ΔC_fix; probability of stem cell replacement yielding a mutant clone that goes on to monoclonally convert the crypt) and/or an elevated crypt fission rate (ρ; rate of crypt division generating multicrypt clonal patches). These two parameters are inferred jointly from the VAF distributions observed in Micro-seq samples.

### Driver-specific clonal behaviours
- **FBXW7 R465C:** Primarily a *fixation* bias. Individual ΔC_fix substantially elevated versus synonymous mutations in the same trinucleotide context (GCG>T); stem cell replacement probability P_R = 0.7 versus 0.5 for a neutral mutation. Fission rate intermediate (~2.5% per year, 95% CI 1.9–3.7%) relative to neutral baseline. This leads to FBXW7 R465C clones being the most prevalent driver in normal colon by middle age: ~0.1% of crypts estimated to carry this mutation by age 55.
- **KRAS G12 (G12D/C/V):** Primarily a *fission* (clonal expansion) bias. Elevated ρ of ~3.9% of crypts undergoing fission per year (95% CI 2.0–7.7%), compared to synonymous (~1.1%) or other KRAS driver mutations (Q61L, A146P; ~1.6%). No detectable fixation bias above neutral in humans (in contrast to mouse data). Although only 0.038% of crypts carry any single KRAS G12 variant by age 55 — far less than FBXW7 R465C — the high fission rate means KRAS G12 mutational burden eventually overtakes APC truncating and TP53 missense burdens by lifetime age ~95.
- **Monoallelic APC truncations and TP53 missense mutations:** Selectively neutral at the monoallelic stage in normal human colonic epithelium (fission and fixation rate credible intervals overlapping synonymous mutations). Their cumulative burden is therefore governed primarily by the underlying mutational process (SBS1 clock), not by selection. APC requires biallelic inactivation to gain positive selection.
- **CTNNB1:** Only 4 mutations detected; excluded from downstream analysis.

### Mutation ordering and age dependence
- Simulation of triple-mutant crypt formation (carrying at least one driver mutation in each of APC, TP53, and KRAS) shows a strong age-dependent shift in founder event identity.
- By age 80, 92% of triple-mutant clones are predicted to have acquired two independent APC hits first, making APC-first the dominant pathway in older individuals.
- In younger individuals (~age 50), KRAS G12 driver mutations are the most likely single founder event in triple-mutant crypts (42.9% at age 50 versus 4.7% at age 80), giving KRAS-first pathways comparable probability to APC-first pathways.
- This age dependence arises mechanistically because the biallelic APC selection bias (strong but manifest only after a second hit) requires a longer evolutionary window to dominate, while KRAS's fission bias rapidly generates large clone populations even from a monoallelic event.
- Without incorporating a selection bias for biallelic APC-null clones in the simulation, the predicted frequency of triple-mutant crypts matches CRC incidence at age ~85, suggesting ~3 events suffice. With strong APC-null bias, triple-mutant crypt frequency exceeds CRC incidence by orders of magnitude, implying ~5 total events are required for malignant transformation.

### Phenotypic characterisation of KRAS mutant clones
- Only KRAS G12 mutant clones produced a transcriptomically detectable signal distinct from normal colonic tissue by 10x Visium spatial transcriptomics; APC, TP53, and FBXW7 mutant clones were phenotypically indistinguishable from normal tissue at the bulk transcriptomic level (likely due to small clone size).
- REG4 is the dominant overexpressed gene in KRAS mutant clones and serves as a validated surrogate IHC marker; 68% of Micro-seq-identified KRAS mutant clones were REG4+ by IHC (92% for G12-specific mutations).
- KRAS mutant clones show a transcriptomic signature of 628 genes enriched for non-intestinal epithelial cell types (oesophageal, gastric, foetal), indicating altered differentiation state.
- 60% of KRAS mutant clones co-express gastric marker MUC5AC alongside intestinal marker CDX2 (mixed lineage / incomplete metaplasia state). This lineage confusion state — not previously described in morphologically normal human colonic epithelium — mirrors incomplete metaplasia in stomach and oesophagus, which is associated with elevated risk of dysplasia and cancer. Complete gastric conversion (MUC5AC+/CDX2−) seen in only one clone.
- KRAS mutant clones are enriched for CMS3/iCMS3 transcriptional subtype markers (REG4, SPINK4 are defining genes of iCMS3), suggesting that the CMS3/iCMS3 transcriptomic identity of KRAS-mutated CRCs may be a direct consequence of an early KRAS founding mutation retained throughout tumour evolution.

## Limitations

- Amplicon panel covers only hotspot regions (1180 bp); mutations outside these hotspots in APC, KRAS, TP53, FBXW7 are missed. The neutral inference for monoallelic APC may not generalise to all APC truncating variants.
- Inference of fixation biases for APC truncating mutations was limited by low count (paucity of detected events), reducing statistical power for this gene.
- Selection bias for biallelic APC-null clones cannot be directly inferred from normal tissue data (requires adenoma/ACF data); the two opposing scenarios modelled (no bias vs. high bias) bracket a large uncertainty in the predicted total number of hits required for CRC initiation.
- Spatial transcriptomics on FFPE VISIUM is performed on sections serial to sequenced sections; clone-level transcriptomics therefore relies on positional correspondence, not perfect co-registration of the same cells.
- Human cohort is cancer-normal (colectomy specimens from cancer patients); possible selection or field effects from the tumour-bearing colon cannot be fully excluded.
- Mouse studies have demonstrated both fixation and expansion biases for KRAS mutations; the absence of a detected fixation bias in human tissue is interpreted as a potential species difference but may also reflect statistical power constraints.
- The REG4 surrogate approach identifies ~20% false negatives among KRAS G12 mutant clones by IHC, and some REG4+ clones without KRAS mutations may carry BRAF V600E or NRAS variants.
