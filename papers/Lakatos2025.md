---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Lakatos2025
kind: paper
title: Epigenetically driven and early immune evasion in colorectal cancer evolution
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: Lakatos2025
tags: []
ontology_terms:
- ATAC-seq
- Big Bang model
- antigen-presenting genes
- chromatin accessibility
- colorectal cancer
- epigenetic silencing
- immune evasion
- immune exclusion
- mismatch repair
- multiregion sequencing
- neoantigen silencing
- phylogenetics
- somatic chromatin accessibility alterations
- tumor microenvironment
dataset_usage:
- ref: dataset:epicc
  role: analyzed
  overlap: unknown
- ref: dataset:lakatos2025-ffpe-ps
  role: analyzed
  overlap: unknown
---
## Key Findings

### 1. SCAAs preferentially silence neoantigens and APGs — epigenetic immune editing

- Detected 45 SCAAs in promoter regions of APGs across 25 CRCs; 92% were losses of chromatin accessibility (statistically enriched vs. genome-wide distribution, P = 0.025).
- SCAAs did not co-occur with somatic mutations in those genes — epigenetic and genetic routes to APG silencing are mutually exclusive, suggesting they are alternative routes to the same immune evasion phenotype.
- Neoantigens were significantly enriched in genes with at least one SCAA loss in promoter regions (Fisher's exact test OR 1.46–2.03 in MMRd; 1.52 in MMRp; significant at cancer level, P = 0.017 for MMRd).
- Around 50% of neoantigens are transcriptomically silenced (immuno-edited via transcription), with epigenetic mechanisms implicated as the primary underlying mechanism for this silencing, particularly for clonal neoantigens.
- Clonal neoantigens were significantly less likely to be expressed (OR = 1.53 vs. non-antigenic expressed mutations) and more likely to fall in regions of closed chromatin.
- Key NFIC (nuclear factor I/C) identified as a likely TF regulator of immunomodulation via APG-SCAA loci; NFIC binding sites covered all recurrently SCAA-affected APGs. NFIC has recently been shown to promote immune escape in NSCLC (Polcaro et al., Mol. Cancer 2024).

### 2. Big Bang timing of immune evasion — early and clonally fixed

- Clonal immune escape mutations (shared across all or most glands within a cancer) detected in 8 of 29 cases; subclonal in 6 (all MMRp).
- Phylogenetic mapping showed that **the highest-impact immune escape alterations (B2M mutations, HLA LOH, NLRC5/RFXAP mutations) are clonal**, placed on or before the trunk of the evolutionary tree in all 4 cases carrying B2M mutations. HLA LOH was near-clonal in 4 out of 5 cases with HLA LOH.
- In matched adenoma-cancer pairs: adenomas had significantly lower proportional neoantigen burden than CRCs (Fig. 4e; P = 2.1 × 10⁻⁷), suggesting immune surveillance is more active in CRAs. No adenomas (except one advanced CRA in C516) carried immune escape mutations.
- Collectively: **immune escape occurs at or early during CRC outgrowth, not later during intratumoral evolution.** This is consistent with a "Big Bang" model (Sottoriva et al. 2015) where pre-expansion somatic alterations define the immunogenicity of the whole cancer.
- Previous work (Heide et al. 2022, Nature; Househam et al. 2022, Nature) showing genomic shift in immunogenicity before carcinoma expansion is directly supported and extended to the epigenome.

### 3. Intratumoral heterogeneity in immune editing is negligible outside invasion sites

- Multivariable regression of neoantigen burden showed that patient-specific effects and cancer progression status (adenoma vs. cancer) dominated; histological region (superficial, invasive, node) contributed negligibly.
- Subclonal immune escape mutations were NOT associated with higher neoantigen burden or higher immune dNdS compared to neighboring phylogenetically close biopsies (P = 0.222 and P = 0.866 for proportional burden and immune dNdS, respectively).
- Exception: enhanced immuno-editing was observed specifically at the invasive margin in small subclones (~100 cells) with high immunogenicity (depletion of neoantigens at low VAF, 0.05 < VAF < 0.1; P = 2 × 10⁻⁸), indicating a localized ongoing "skirmish" at the invasion front in MMRp CRCs.

### 4. Immune exclusion occurs at the outset; TME restructuring is early

- CyCIF analysis: CTL fraction per epithelial cell was significantly lower in superficial tumor than adjacent normal mucosa (P = 3 × 10⁻¹² for superficial; P = 3 × 10⁻³ for invasive), and CTL–tumor distance was highest in superficial regions.
- CTLA-4+ FOXP3+ Treg cells significantly enriched in tumor-associated regions vs. normal mucosa (P = 0.012–6 × 10⁻³).
- PD-L1+ tumor cells were dispersed within PD-L1+ neighborhoods even within single glands, indicating high plasticity of PD-L1 expression intratumorally.
- In epigenetically escaped cancers (without genetic escape), CD68+ macrophages and CD45RO+ memory T cells were enriched, suggesting an SCAA-loss-specific immune phenotype.
- Fibroblasts were more abundant in genetically escaped cancers, with TGFβ receptor 2 (TGFBR2) expression significantly higher in escaped vs. non-escaped biopsies — consistent with TGFβ-mediated T cell exclusion as a feature of genetically escaped cancers.

### 5. Epigenetic vs. genomic immune evasion comparison

| Feature | Epigenetic (SCAA-driven) | Genomic (mutation/LOH-driven) |
|---|---|---|
| Prevalence | 9/25 (36%) had ≥1 APG affected; 21/25 (84%) had ≥1 SCAA in APG promoters | 3/29 cancers had clonal escape; 8/29 total with immune escape mutations |
| Clonality | SCAAs show low phylogenetic signal (17/297 gene-cancer combos), indicating plasticity | Highest-impact mutations clonal (B2M, HLA LOH all clonal or near-clonal) |
| TME association | CD68+ macrophages, CD45RO+ memory T cells enriched | Fibroblasts enriched; higher PD-L1+ cells; TGFβ pathway active |
| Neoantigen burden | Proportional burden similar to non-escaped; intermediate immune dNdS | Lower proportional neoantigen burden (epigenetically escaped) |
| Timing | Early; part of founding event | Early for high-impact; subclonal for minor alterations |

Both routes converge on early immune evasion establishment, consistent with the Big Bang model.

### 6. APG expression heritability is low — plasticity dominates within cancers

- Phylogenetic signal for APG expression was weak (significant in only 17/297 gene-cancer combinations), indicating SCAA-driven expression changes have high intratumoral plasticity.
- APG expression variation is predominantly patient-specific and cancer stage-specific (adenoma vs. cancer), not spatially structured within individual cancers.

## Limitations

- ATAC-seq measures chromatin accessibility (open/closed chromatin) but not histone modifications (H3K27me3, H3K4me3). The mechanistic basis of SCAA establishment and maintenance is unknown — it could reflect PRC2-mediated bivalent silencing, DNMT-mediated methylation, or other mechanisms. The "epigenetic" label covers a mechanistically heterogeneous set of changes.
- The adenoma data (25 glands from 8 CRAs adjacent to 5 EPICC cases) are limited: these adenomas are coincidental to the CRCs (not the direct precursor lesions), so the adenoma–cancer comparison is not a strict temporal series. The authors acknowledge this explicitly.
- Phylogenetic signal analysis may underestimate SCAA heritability if the tumor-gland sampling resolution is insufficient to detect spatial structure in chromatin changes — the lack of signal could partly reflect technical noise in ATAC-seq from single glands.
- CyCIF imaging was performed on FFPE-PS samples (n = 11 CRCs), not EPICC samples — spatial imaging and multiomics data are from different cohorts, limiting direct integration of chromatin, transcriptome, and spatial immune data at the single-gland level.
- The FFPE-PS cohort is Stage III only (with lymph node metastases); findings on invasive margin immune editing and TME composition may not generalize to earlier-stage CRCs.
- No mechanistic experiments (CRISPR/chromatin perturbation, organoid co-culture) validate causality of SCAAs in neoantigen silencing or immune evasion — all findings are correlative/associative.
- NFIC's functional role in APG regulation in CRC is identified bioinformatically but not experimentally validated in this paper. Functional validation in patient-derived organoid models is called for.
- The study focuses on primary CRC; immune evasion dynamics in metastases or during therapy were not the primary focus (though lymph node deposits were sampled for imaging).
