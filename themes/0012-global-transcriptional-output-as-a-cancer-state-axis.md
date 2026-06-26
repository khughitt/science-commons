---
schema_profile: science-entity-base/1.0+theme/2.0
id: theme:0012-global-transcriptional-output-as-a-cancer-state-axis
type: theme
title: Global transcriptional output as a cancer-state axis
version: "1.0.0"
created: "2026-06-26"
updated: "2026-06-26"
tags: []
evidence_refs: []
related:
- question:0008-transcriptional-output-as-transportable-cancer-axi
- question:cancer-meta
source_refs:
- paper:Cao2022
- paper:Dai2026
- paper:Ortmayr2019
- paper:Zatzman2022
theme_kind: empirical
theme_scope: cross-project
---
## Definition

Beyond *which* genes are expressed, the **total transcriptional output** of cancer cells — global mRNA quantity per cell/genome — is emerging as a cross-cancer state axis with prognostic and mechanistic significance. Two independent measurement traditions converge here: **TmS** (tumor-specific total mRNA, recovered by DNA/RNA deconvolution; [[Cao2022]], [[Dai2026]]) and **hypertranscription / RNAmp** (VAF-based cancer-cell RNA output; [[Zatzman2022]]). Both are normally discarded by standard RNA-seq normalization, and both link to metabolic state ([[Ortmayr2019]]) and intra-tumor heterogeneity.

## Why It Matters

- A transportable, output-based prognostic axis would complement mutation- and subtype-based stratification, and is computable from existing bulk DNA+RNA cohorts (cBioPortal-scale).
- It reframes a measurement *artifact* (discarded total-RNA variation) as a first-class phenotype — directly the concern of [[theme:0004-observation-and-measurement-bias]].
- It connects transcriptional output to metabolism and to the TME (low-TmS = stromal/immune-excluded, [[Dai2026]]), bridging cell-intrinsic and microenvironmental programs.

## Boundaries

- **Inside:** total/global transcriptional output as a phenotype; methods to recover it from bulk data (TmS, RNAmp); its links to metabolism, ITH, prognosis, and treatment response.
- **Outside:** pathway-specific or signature-specific expression programs (belong with the relevant biology); the deconvolution *machinery* as a general tool (belongs with [[theme:0009-data-integration-and-multi-omics]]); cross-cancer generalizability claims (shared with [[theme:0005-transportability-across-cancer-types]]).

## Guardrails

- Prognostic *direction* is not universal: high TmS is adverse in most cancers but inverts in chemo-treated TNBC ([[Cao2022]], [[Dai2026]]) — a transportability boundary, not a contradiction. Do not assert a single sign across contexts.
- TmS and RNAmp are model-based deconvolutions resting on purity/ploidy and VAF assumptions; treat absolute values as method-conditional and validate cross-method agreement before merging.

## Open Questions

- Is the transcriptional-output axis transportable across cancer types, and what sets it? ([[question:0008-transcriptional-output-as-transportable-cancer-axi]])

## Update Triggers

- A paper unifying TmS and hypertranscription, or mapping the upstream regulatory control of total output.
- Child-project (e.g. multiple-myeloma) evidence that TmS/output stratifies that disease.
- Promotion of any of these papers to the shared commons (re-check cross-project relevance, esp. to health/meta aging frame).
