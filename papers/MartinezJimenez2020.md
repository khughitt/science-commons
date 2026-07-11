---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:MartinezJimenez2020
kind: paper
title: A Compendium of Mutational Cancer Driver Genes
version: "1.0.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: MartinezJimenez2020
tags: []
ontology_terms:
- IntOGen
- cancer driver genes
- cancer hallmarks
- mutational landscape
- oncogene
- pan-cancer
- positive selection
- somatic mutation
- tumor suppressor
paper_kind: review
---
## Key Findings

- **568 mutational driver genes** identified across 66 cancer types; ~75% overlap the CGC, providing strong validation; >80% of driver gene–tumor type associations are novel relative to CGC annotations.
- **152 potential new driver genes** not previously listed in the CGC; five are highlighted with independent supporting evidence (RASA1, KDM3B, FOXA2, KLF5, BRD7).
- **Most drivers are tissue-restricted:** 360 of 568 drive only 1–2 tumor types. A small subset of 12 genes are "cancer-wide" drivers (active in >20 malignancies), including canonical genes such as TP53 and KRAS.
- **Mutational features distinguish oncogenes from tumor suppressors:** Oncogenes show narrow, high-density missense clusters (e.g., KRAS codons 12/13 concentrate 85% of mutations in a colorectal cohort); tumor suppressors show broader, lower-density clusters enriched for nonsense mutations.
- **Protein domain landscape:** The TP53 domain is the most broadly enriched domain across cancer types (42 types); tyrosine kinase domains of 13 genes are enriched across 24 types; BRAF tyrosine kinase domain is enriched across 14 types.
- **Genes already mutated in non-malignant tissue:** Published studies show that several driver genes are positively selected in histologically normal somatic tissue, implying that a driver mutation alone is insufficient for transformation — tissue-specific selective constraints and cooperating events are required.
- **Treatment-resistance drivers in metastatic context:** ESR1 (breast) and AR (prostate) are rarely mutated in primary tumors but are clear drivers in treatment-resistant metastatic cohorts.
- **Future gaps acknowledged:** Low-frequency drivers (<10% mutational prevalence), drivers in under-represented populations, metastatic and pediatric-specific drivers, non-coding driver elements, and the temporal ordering of multi-driver cooperativity remain open challenges.

## Limitations

- **Point mutations only:** Copy-number alterations, structural variants, epigenetic silencing, and non-coding drivers are excluded. The compendium is therefore a subset of the full driver landscape.
- **Short indels excluded from background modeling:** Accurate background rate modeling for indels is harder; they are not the main focus.
- **Cohort-level analysis:** Each cohort analyzed independently due to technical heterogeneity in mutation calling; cross-cohort pooling is not yet feasible at this scale, limiting power for rare drivers.
- **Static snapshot:** The 2020 snapshot reflects publicly available data through ~2019; the intogen.org platform is designed to release updates, but the published findings are tied to this snapshot.
- **CGC as imperfect ground truth:** The CGC itself is incomplete and may contain false positives, so the overlap analysis is a relative benchmark, not an absolute validation.
- **Mode of action is inferred, not experimentally validated:** Oncogene vs. tumor suppressor classification from mutational features is a proxy; some genes (e.g., KDM3B) have conflicting functional evidence.
- **Non-European populations underrepresented:** The paper explicitly flags this as a gap, particularly for drivers in specific ethnic backgrounds.
