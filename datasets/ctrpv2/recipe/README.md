# CTRPv2.0 recipe

## Source

Broad Institute CTD² **Cancer Therapeutics Response Portal v2.0** (CTRPv2.0),
distributed by the NCI CTD² Data Portal:

- <https://ctd2-data.nci.nih.gov/Public/Broad/CTRPv2.0_2015_ctd2_ExpandedDataset/>

Primary references: Seashore-Ludlow et al., *Cancer Discov* 2015
(DOI:10.1158/2159-8290.CD-15-0235); Rees et al., *Nat Chem Biol* 2016
(DOI:10.1038/nchembio.1986); Basu et al., *Cell* 2013
(DOI:10.1016/j.cell.2013.08.003).

Release flat files consumed (tab-delimited):

- `v20.data.curves_post_qc.txt` — per experiment × compound curve fits (AUC).
- `v20.meta.per_experiment.txt` — `experiment_id` → `master_ccl_id`.
- `v20.meta.per_cell_line.txt` — cell-line dimension (CCLE site/histology/subtype).
- `v20.meta.per_compound.txt` — compound dimension (target gene, activity, SMILES).

## Build (workflow-owned)

Produced by the MM30 project's Snakemake workflow (the promote source):

- Workflow: `workflows/external/ctrp_v2.smk`
- Scripts: `scripts/external/ctrp_v2/build_sensitivity_table.py` (join → Parquet),
  `scripts/external/ctrp_v2/build_data_package.py` (Frictionless manifest).
- Raw release path is resolved from `config/workflow.yml::external_raw.ctrp_v2`
  (not hard-coded).

Reproduce:

```bash
# from the MM30 project root
bin/snakemake ctrp_v2_all
```

This joins the post-QC curves to the cell-line and compound dimension tables and
emits the **full pan-cancer** release (no MM subset):

- `ctrpv2-sensitivity-long.parquet` — 395,263 rows (cell line × compound): AUC,
  apparent EC50 (µmol), predicted high-conc viability.
- `ctrpv2-cell-lines.parquet` — 1,107 cell lines.
- `ctrpv2-compounds.parquet` — 545 compounds.

The Parquet payloads are regenerable build artifacts (gitignored in the source
project); `datapackage.json` is the tracked promote-source manifest.
