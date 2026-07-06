---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Persi2025
kind: paper
title: Genome-level selection in tumors as a universal marker of resistance to therapy
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Persi2025
tags: []
ontology_terms:
- dN/dS
- evolutionary monitoring
- neutral evolution
- prognosis
- selection regime
- therapy resistance
dataset_usage:
- ref: dataset:persi2025-myeloma
  role: analyzed
  overlap: unknown
---
## Key Findings

- In untreated primary settings, patient-specific `dN/dS` values are broadly stable despite natural progression and regional heterogeneity.
- Progression to metastasis can show cancer-specific shifts, including positive or relaxed selection in some cohorts.
- In treated cancers that developed resistance, post-treatment samples showed a near-universal tendency toward neutral evolution.
- Post-treatment tumors near neutrality or moving toward neutrality had worse prognosis in glioblastoma and multiple myeloma analyses.
- The authors propose a translational rule: if treatment moves a tumor from neutrality toward a selective regime, continue; if treatment moves a tumor toward neutrality or leaves it stably neutral despite therapy, consider changing treatment.

## Limitations

The treated datasets are enriched for resistant or failed-treatment cases, so the proposed clinical rule still needs prospective validation in cohorts with successful and failed responses.
The method depends on sufficient mutation counts and assumptions about synonymous neutrality and saturation.
It is also sample-level and exome-based, so it may miss copy-number, ecDNA, epigenetic, spatial, and plasticity-driven resistance.
