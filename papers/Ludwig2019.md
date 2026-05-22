---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Ludwig2019
type: paper
title: Lineage Tracing in Humans Enabled by Mitochondrial Mutations and Single-Cell Genomics
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Ludwig2019
tags: []
datasets: []
ontology_terms:
- clonal dynamics
- hematopoiesis
- heteroplasmy
- lineage tracing
- mitochondrial DNA
- single-cell genomics
---
## Key Findings

### Data-derived findings (D)

- **(D) Heteroplasmic mtDNA mutations are stable clonal markers down to ~5% VAF.** In TF1 serial bottleneck experiments (8 generations, ~3 weeks each), clone-specific mutations were stably propagated and distinguishable; 96% accuracy in identifying most-recent common ancestors between first-generation clones and 79% accuracy for sub-clones.

- **(D) mtDNA sequencing scales ~1,000-fold relative to nuclear genome sequencing.** ~18,000 individual cells' mitochondrial genomes can be sequenced at 100× coverage for the cost of sequencing one nuclear genome at 10× — a depth too shallow for confident nuclear somatic variant calling.

- **(D) Minimum reliably detectable heteroplasmy: ~3–5% VAF.** Tissue-specific mutations in GTEx were catalogued at ≥3% heteroplasmy (2,762 such mutations found across 49 tissues). Colony-specific markers in primary hematopoietic cells were confidently called at ≥5%.

- **(D) mtDNA genotyping outperforms CNV-based clonality in clinical leukemia.** In AML/CML samples, mtDNA-based clonal inference achieved 95% accuracy in trio analysis for predicting shared clonality versus 84% for copy-number variation approaches.

- **(D) 44 high-confidence heteroplasmic variants identified across TF1 clonal lines.** 2,762 tissue-specific mutations catalogued in GTEx population cohort. Predominant mutation signature: C>T transitions (G>A on opposite strand), consistent with known mtDNA mutation patterns.

### Author interpretations (L)

- **(L) mtDNA mutations accumulate over cell divisions at a rate 10–100× higher than nuclear DNA,** making them suitable as natural clonal barcodes for retrospective lineage reconstruction. (This 10–100× figure is cited from prior literature, not directly measured per-division in this study.)

- **(L) The approach is broadly applicable to native human tissues**, including immune cells, hematopoietic progenitors, and solid tumors, enabling studies of clonal dynamics without exogenous barcoding or genetic manipulation.

- **(L) Horizontal mitochondrial transfer and unknown phenotypic effects** of tracked variants at their observed heteroplasmy levels are potential confounders, acknowledged as limitations.

- **(L) mtDNA lineage tracing integrated with transcriptome / chromatin accessibility readouts** (scRNA-seq + scATAC-seq) will enable joint reconstruction of cell state and clonal history, supporting large-scale initiatives such as the Human Cell Atlas.

- **(L) The per-cell-division mutation accumulation rate is not directly quantified** in this paper; the authors rely on the comparative 10–100× elevated rate relative to nuclear DNA but do not provide an absolute mutations-per-genome-per-division estimate for their cell types of interest.

## Limitations

- **No per-division mutation rate.** The absolute rate of new heteroplasmic mutation acquisition per mitochondrial genome per cell division is not measured; the paper relies on comparative estimates from prior literature (10–100× nuclear rate).
- **Detection floor limits resolution of recent transitions.** The ≥5% VAF threshold means very recent clonal events (within the last few divisions) may be invisible; the temporal floor is set by when a mutation drifts above the detection threshold, not by when it arose.
- **TF1 is a cell line.** The 8-generation proof-of-concept used an immortalized hematopoietic line under artificial bottlenecking, not in vivo human tissue dynamics. Drift rates and segregation kinetics may differ in primary tissues.
- **Mutation signature is mutation-type-biased.** Predominantly C>T transitions; other mutation classes may be underrepresented or under-called.
- **Potential horizontal mitochondrial transfer** (acknowledged by authors) could produce false clonal assignments in tissues with active cell-cell communication.
