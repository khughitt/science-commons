---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Marzban2024
kind: paper
title: Spatial interactions modulate tumor growth and immune infiltration
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Marzban2024
tags: []
ontology_terms:
- Allee effect
- Lenia
- collagen alignment
- immune infiltration
- spatial interactions
- tumor immune ecology
dataset_usage:
- ref: dataset:marzban2024-hnscc-shg
  role: analyzed
  overlap: unknown
---
## Key Findings

- Short-range interaction kernels can allow local tumor clusters to survive even when well-mixed Allee models would predict extinction.
- Both immune sensitivity and immune specificity need to be spatially localized for efficient tumor regression in the model.
- Asymmetric tumor-immune interaction kernels can produce poor immune response and spatially heterogeneous tumor killing.
- Late-stage HNSCC samples show more aligned collagen patterns, and the parallel immune-migration model predicts lower immune coverage with increasing disease stage.
- Collagen alignment can therefore act as an immune-escape mechanism by directing immune trafficking away from effective tumor coverage.

## Limitations

The model simplifies immune recognition and does not include immune exhaustion, checkpoint expression, acid-mediated immune inhibition, antigen heterogeneity, or plastic cell-state changes.
The collagen application is an in silico test of plausible migration hypotheses rather than direct observation of immune-cell migration in tumors.
Parameter identifiability from routine clinical data remains unresolved.
