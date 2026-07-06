---
schema_profile: science-entity-base/1.0+dataset/1.0+bio.table/1.0
id: dataset:ccle-proteomics-nusinow-2020
kind: dataset
title: CCLE Proteomics (Nusinow 2020) — quantitative proteome across 375 cancer cell lines
version: "1.0.0"
created: "2026-05-19"
updated: "2026-06-28"
tags: []
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
  last_reviewed: '2026-05-19'
  verified_by: codex
  source_url: https://gygi.hms.harvard.edu/publications/ccle.html
  credentials_required: ''
accessions:
- Nusinow2020
columns:
- name: Protein_Id
  dtype: string
  kind: protein_identifier
- name: Gene_Symbol
  dtype: string
  kind: gene_symbol
- name: Description
  dtype: string
  kind: protein_description
- name: Group_ID
  dtype: integer
  kind: protein_group
- name: Uniprot
  dtype: string
  kind: uniprot_name
- name: Uniprot_Acc
  dtype: string
  kind: uniprot_accession
- name: abundance
  dtype: float
  kind: protein_abundance
- name: ccle_code
  dtype: string
  kind: cell_line_identifier
- name: tenplex
  dtype: string
  kind: batch
datapackage: datapackage.yaml
n_records: 76530
ontology_terms: []
origin: external
status: active
tier: use-now
update_cadence: static
benchmark:
  domains: ["biology", "cancer"]
  modalities: ["proteomics", "multimodal"]
  signal_types: ["cross-sectional", "multi-omic"]
  benchmark_kinds: ["static-association", "cross-context-generalization"]
  source_datasets: []
  related_beliefs: []
  notes:
    - "Seed benchmark for protein-level validation in cancer cell-line systems, especially when transcript-level evidence may not transfer directly to protein abundance."
    - "Useful as a compact proteomics benchmark with matched CCLE/DepMap context available outside this record."
  limitations:
    - "Cell-line context is not a primary-tumor substitute."
    - "Multiple-myeloma subset is small, so per-gene MM-only correlations have limited power."
  tasks:
    - id: protein-lineage-association
      task_type: "association-prediction"
      prediction_target: "protein abundance pattern across cancer cell lines"
      held_out_unit: "cell line"
      metric: "spearman-correlation"
      baseline: "lineage-average protein abundance"
      ground_truth:
        type: "measured-outcome"
        description: "TMT quantitative protein abundance across CCLE cancer cell lines"
      interpretation_limits:
        - "Positive performance supports protein-level transfer checks, not primary-tumor causal claims."
      contexts: ["cell line", "lineage", "TMT batch"]
      support:
        state: supported
        checked_at: "2026-07-03"
        evidence:
          - datapackage.yaml
          - datapackage.yaml#resources
        notes:
          - Runnable deposit benchmark for protein-level association checks across CCLE cancer cell lines.
          - Use as broad cell-line proteomics validation, not as a primary-tumor or causal benchmark.
---
# CCLE Proteomics (Nusinow 2020) — quantitative proteome across 375 cancer cell lines

## Summary

TMT-based quantitative proteome covering ~12,700 proteins across 375 CCLE cancer
cell lines, including ~25 MM cell lines (MM.1S, RPMI-8226, H929, U266, KMS11,
KMS12-BM, AMO1, KMS-26, KMS-28BM, others).
The closest resource to MM-specific proteomics that is publicly available,
and the natural bridge between MM30 transcript rankings and cell-line
functional (DepMap) data.

## Access and Scope

- Accessions: Nusinow et al. Cell 2020 supplementary data; also on DepMap portal
- Source URL: https://gygi.hms.harvard.edu/publications/ccle.html;
  https://depmap.org/portal/download/
- Organism/population: Human; 375 cancer cell lines (~25 MM)
- Modality: TMT10 quantitative proteomics
- Sample size: 375 cell lines × ~12,197 proteins in the normalized table
  (per Nusinow 2020 supplement). **Hematopoietic subset = 40 lines of
  which 6 are MM: KMS11, KMS12BM, KMS27, NCIH929, OPM2, RPMI8226**
  (verified directly against the protein-quant CSV column headers
  during t209 ingestion).
- License: Open (supplementary); CCLE / DepMap terms for DepMap-hosted copy
- Format: TSV / XLSX tables

## Thoughts

- **Strength**: 25 MM cell lines with matched CCLE transcriptomes, matched
  DepMap CRISPR dependencies, matched CTRP / PRISM drug response — the
  densest multi-modal layer available for MM-relevant functional validation.
- **Strength**: Covers the PRC2 axis (EZH2, SUZ12, EED, PHF19), cell cycle
  (E2F1/2, MCM, RB1), nuclear pore (NUP133, NUP155, XPO1), and ribosome
  biogenesis machinery — all key MM30 top-ranked modules.
- **Limitation**: only 6 MM lines (not 25 as initially estimated;
  verified during t209 ingestion). Per-gene transcript↔protein
  concordance statistics will have very modest power — n=6 Spearman
  correlations are only useful in aggregate, not per-gene. This is
  a hard upper bound that cannot be fixed with more processing.
- **Limitation**: Cell lines drift from primary biology; concordance here
  is a sanity check, not proof of translation relevance.
- **Limitation**: TMT normalization and batch design limits absolute comparisons
  between unrelated lines.

## Connections to Project

### Questions/hypotheses it can inform

- `hypothesis:h1-epigenetic-commitment` — protein-level PHF19/EZH2/E2F1
  in MM lines; cross-reference with Ren 2019 PHF19-KD effects on MM.1S.
- `hypothesis:h2-cytogenetic-distinct-entities` — stratify MM lines by
  virtual-FISH genotype (gain(1q), HD, translocation) and test whether
  stratum-specific transcript programs reflect in the proteome.
- `question:nucleoporin-signal` — MM-line protein levels for NUP133/NUP155
  and their correlation with XPO1 dependency.
- the 35-gene mutation × cytogenetic overlap set — protein expression of the
  overlap genes in MM lines; cross-reference with DepMap essentiality.

### Variables likely available

- Per-protein abundance per cell line
- Matched CCLE transcriptome, DepMap dependencies, drug response

### Planned usage

- Download Nusinow 2020 supplementary Table S2 (protein quant) and metadata.
- Filter to MM lineage; attach to the existing MM30 ↔ DepMap join.
- Build per-gene transcript ↔ protein Spearman correlation across MM lines.

## Related

- Article notes: Nusinow et al., Cell 2020
- See also: CPTAC pan-cancer (`data-cptac-pan-cancer-proteomics.md`) for
  primary-tumor proteomics
