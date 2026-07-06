---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Nishimura2023
kind: paper
title: Evolutionary histories of breast cancer and related clones
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Nishimura2023
tags: []
ontology_terms:
- breast cancer
- clonal evolution
- der(1;16)
- normal tissue evolution
- phylogenetics
- precancer
- somatic mosaicism
dataset_usage:
- ref: dataset:tcga
  role: analyzed
  overlap: unknown
---
## Key Findings

**1. Mutation clock in normal mammary epithelium.**
SNV accumulation rate is 19.5 mutations/genome/year before menopause, dropping to 8.1/year after menopause. Rate is also reduced ~54.8 mutations per delivery (parity effect). PIK3CA driver mutations increase SNV count by ~210 (small n, treat as preliminary). Indel rate: 1.3/year pre-menopause, 0.72/year post-menopause.

**2. Der(1;16) acquired in puberty/early adolescence, MRCA by early 30s.**
In five index cases with der(1;16)(+) cancers, der(1;16) was estimated to be acquired at median 10.6 years of age (range 5.8–16.9). The MRCA from which both cancer and non-cancer clones descended emerged at median 26.5 years (range 18.1–34.4). Thus ~10–17 years elapsed between initial driver event and first cancer founder emergence.

**3. Non-cancer clones occupy a large area of the premenopausal breast.**
Der(1;16)(+) non-cancer clones spanned a median 62 mm (range 35–90 mm) in premenopausal patients. In postmenopausal patients the der(1;16)(+) non-cancer lesions were smaller (<10 mm lobules), consistent with regression after menopause under reduced estrogen. The large pre-menopausal expansion is not fully explained by the physiological growth of mammary glands during puberty, implicating der(1;16) itself in driving expansion.

**4. Multiple independent cancer founders from the shared non-cancer ancestor.**
In four of five index cases, multiple independent cancer founders (≥2) independently evolved from the shared MRCA (non-cancer ancestor), not from each other. This polyclonal initiation from a pre-existing non-cancer field directly produces intratumour heterogeneity without requiring branching within the tumour.

**5. Histology does not predict the number of driver events; epigenetic drivers may act.**
Number and type of driver events did not correlate with histological grade or subtype across cancer vs. non-cancer lesions. In some cases, additional drivers were only in high-grade but not non-cancer clones; in others the reverse was true. This lack of consistent correlation suggests local microenvironments and/or epigenetic events contribute to the cancer transition.

**6. Der(1;16) enriched in ILC vs IDC; clonality higher with driver mutations.**
In TCGA, der(1;16)+ was more enriched in ILC (49.6%) than IDC (12.7%, P=3.2×10^−16). Der(1;16)(+) Luminal A tumours had significantly longer overall survival (median 33.1 vs 28.3 months, P=1.0×10^−3). VAF significantly higher in driver-mutated samples vs unmutated (0.33 vs 0.25, P=1.8×10^−3), supporting positive selection.

**7. AKT1-mutated case (KU582) shows an analogous pattern without der(1;16).**
One case lacking der(1;16) had an AKT1-mutated MRCA that similarly gave rise to a large field of non-cancer clones before cancer founders appeared, suggesting the der(1;16) evolutionary pattern generalises to other early driver events in breast.

**8. Driver mutations in normal mammary lobules are common but expansion is selective.**
In the contralateral quadrant samples (n=77 LCM from 3 premenopausal patients), 12 of 66 histologically normal lobules (18.2%) harboured driver mutations (PIK3CA or PIK3R1). However, clones present at age 1 were detected in ≥2 lobules more often than those present at age 13 (P=2.1×10^−2), and maximum diameter was larger for clones originating at age 1 vs 13 (P=2.2×10^−1 ns). Most driver-mutated normal lobules did not show widespread expansion.

## Limitations

- Only five index cases with full phylogenetic reconstruction; the full diversity of breast cancer evolutionary histories is not captured.
- All five index cases are premenopausal, Luminal A-like IDC or DCIS — findings may not extend to triple-negative, HER2-enriched, or postmenopausal breast cancers.
- Selection of cases was heavily enriched for der(1;16)+ and for patients with multiple BBLs (rare in the general surgical population), introducing ascertainment bias.
- Organoid-based mutation clock assumes a constant mutation rate per division; deviation from this (e.g., stress-induced mutagenesis) could bias timing estimates.
- PIK3CA-driven increase in SNV rate was estimated from only n=4 driver-mutated organoids — treat as preliminary.
- The postmenopausal regression of der(1;16)(+) clones is speculative; the reduced clone diameter in postmenopausal patients could reflect acquisition timing rather than regression.
- Epigenetic driver events (suggested by the histology–driver mismatch) are not directly measured here — the claim is inferential.
