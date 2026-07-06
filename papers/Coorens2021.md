---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Coorens2021
kind: paper
title: Extensive phylogenies of human development inferred from somatic mutations
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Coorens2021
tags: []
ontology_terms:
- embryogenesis
- lineage tracing
- phylogenetics
- somatic mutation
- whole-genome sequencing
---
## Key Findings

### Data-derived findings (D)

- **Per-division SNV rate (first two embryonic generations):** 2.4 SNVs/division (combined; 95% CI 1.7–3.2). Per-individual: PD28690 = 2.3 (1.3–3.9), PD43850 = 1.6 (0.8–3.1), PD43851 = 3.2 (1.9–4.9). (D)
- **Per-division SNV rate (subsequent embryonic generations):** 0.64 SNVs/division (combined; 95% CI 0.51–0.77). Drop coincides with zygotic genome activation at the ~8-cell stage. (D)
- **Zygote-split asymmetry:** Ranges from 60:40 to 93:7 across the three donors. PD28690 major/minor = 69:31 (95% CI 66.7–70.2); PD43851 brain = 93:7 (95% CI 87.9–96.1), colon = 81:19 (95% CI 74.3–87.3) — same individual, tissue-specific asymmetry, p=0.004. (D)
- **Colonic embryonic patch size:** Posterior mean radius 9.79 crypts (95% CI 8.94–10.82), translating to ~301 crypts per patch (95% CI 251–368). Median shared SNVs within a patch: 27, consistent with patch founding at ~7–9 weeks post-conception. (D)
- **Mitochondrial SNVs are uninformative for developmental phylogenies:** Four distinct mtDNA sharing patterns observed, none providing additional lineage resolution beyond the nuclear tree. Specifically, no mtDNA mutations were clade-specific to multi-tissue developmental branches. (D)
- **Tissues covered:** Colon crypts, small bowel crypts, appendix crypts, skin (epidermis, hair follicle), bronchial/oesophageal epithelium, thyroid follicles, prostate acini, seminiferous tubules, kidney (distal tubule, glomerulus), liver (bile duct, parenchyma), adrenal gland (ZF/ZG/ZR zones), pancreas (duct, acinus, islet), bladder urothelium, and brain (bulk) via targeted re-sequencing. (D)
- **Cancer-adjacent findings:** A microscopic neoplastic polyp in PD28690 colon carried biallelic *APC* inactivation (Q1429* + A896fs*15); all eight crypts (normal + adenomatous) from the section share 19 embryonic SNVs, placing the polyp within a normal embryonic clone. A *BRAF* D594G appendiceal expansion was timed to ~age 23. Benign prostatic hyperplasia clonal expansion timed to ~age 19. (D)
- **Germline / soma divergence:** Seminiferous tubules shared on average 7.0–8.7 mutations with any somatic lineage (pre-gastrulation origin); in PD43851 this divergence occurred as early as the second observed division. In 5/12 individuals in an extended cohort, a subset of seminiferous tubules shared no SNVs with bulk colon. (D)

### Author interpretations (L)

- The drop in per-division mutation rate after the first two divisions is attributed to bolstered DNA repair machinery coinciding with zygotic genome activation; prior to ZGA the embryo relies on maternal (oocyte-derived) repair proteins. (L)
- The first-generation asymmetry (60:40 to 93:7) is attributed to differential cell allocation to inner cell mass vs trophectoderm at blastulation. The minor lineage's higher SNV burden per branch (~4.3 vs 1.7 for the major) is interpreted as the minor branch traversing more cell divisions before fate commitment. (L)
- Tissue-specific asymmetries within PD43851 (brain 93:7, colon 81:19, seminiferous tubules 35:65) are interpreted as reflecting multiple successive bottlenecks at later lineage-commitment stages, not solely the first ICM/trophectoderm split. (L)
- The early extra-embryonic contribution to primordial germ cells is inferred from the seminiferous-tubule lineage distribution being inconsistent with derivation from the same inner-cell-mass lineage as somatic tissues. (L)
- Cancer relevance: The study "provides a fundamental background" for understanding pre-malignant clonal expansions; early-life driver mutations can be detected and timed in their normal-tissue context using the same somatic-mutation phylogenetic framework. (L)

## Limitations

- Requires rapid-autopsy material with LCM capability; not applicable to living individuals or routinely collected biopsies. Restricted to tissues with morphologically clonal units (crypts, tubules, follicles, acini).
- The number of LCM samples per individual is modest relative to the full body; the tree topology at later-generation nodes is partially constrained by sampling depth.
- Mitochondrial SNVs were uninformative here; this may reflect heteroplasmy dynamics or selection filtering mtDNA variants in normal tissues rather than a fundamental resolution limit of the mtDNA approach.
- The thesis/pre-publication version used; minor differences from the published paper are possible in exact figures. Per-crypt SNV burden differs by tissue type and turnover rate; the per-division rate is an average over early embryogenesis.
- WGS at ~30× may miss low-VAF branches; sensitivity corrections applied but embryonic variants at VAF ~0.4 can be confused with heterozygous germline variants if pooled depth is insufficient.
