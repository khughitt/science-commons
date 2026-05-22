---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Singh2024
type: paper
title: A pan-tissue, pan-disease compendium of human orphan genes
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Singh2024
tags: []
authors:
- Singh et al.
datasets:
- dataset:geo
- dataset:gtex
- dataset:scrna-tissue-atlases
- dataset:sra-covid19-rnaseq
- dataset:sra-ribo-seq
- dataset:tcga
doi: 10.1101/2024.02.21.581488
ontology_terms:
- dark-transcriptome
- de-novo-gene
- evidence-based-transcript
- orphan-gene
- phylostrata
pmcid: ''
pmid: ''
venue: bioRxiv (preprint)
year: 2024
---
## One-Sentence Summary

A large-scale RNA-Seq meta-assembly across TCGA and GTEx identifies 54,794 highly expressed, unannotated human transcripts (heEB genes) — mostly orphan or human-specific — that show disease- and tissue-selective expression, harbor pathogenic variants, and associate with cancer patient survival, constituting a major poorly-annotated stratum of human disease biology invisible to standard pipelines.

## Key Findings

1. **Scale of the dark transcriptome.** Re-processing 26,985 paired-end RNA-Seq samples from GTEx (32 tissue types) and TCGA (33 tumor types) via a meta-assembly pipeline yielded 1,049,303 novel evidence-based (EB) transcripts merged with 335,239 Gencode-annotated transcripts. Filtering for high expression (median TPM ≥ Q75 of all annotated protein-coding transcripts, in a tissue/tumor/sex/ancestry-specific manner) retained 54,794 heEB transcripts (54,748 unique genes). These are expressed at levels comparable to annotated lncRNAs, lower than protein-coding genes, but well above noise.

2. **Most are human-specific orphan genes.** Phylostratigraphy via *phylostratr* + Liftoff across nine related species assigned 13,921 heEB transcripts to Hominoidea (ape-specific) and 29,813 to *Homo sapiens* specifically. By genomic context: 84% are intronic (located within introns of annotated genes), 26% are intergenic. The vast majority (>80% of total transcriptome mass in any tissue) is unannotated.

3. **Disease- and tissue-selective expression.** Only 59 heEB genes are highly expressed in all 39 GTEx undiseased tissues; 35,212 are expressed in at least one tumor type; 8,607 are expressed in both a matched undiseased tissue and its tumor type. Expression patterns differ markedly by tumor type vs. normal, sex (thousands DE between males and females), and self-reported ancestry (e.g., 670 heEB orphans upregulated in African-Americans vs. European-Americans in PRAD; 416 upregulated in the reverse direction in BRCA). These results were validated in an independent strand-specific study (66% of TCGA-COAD upregulated heEB genes replicated in an independent African-American COAD cohort; 73% of downregulated replicated).

4. **COVID-19-induced orphan expression.** 8,865 heEB transcripts are highly expressed in SARS-CoV-2-infected tissues but not in matched controls; 5,834 of those are orphans. This establishes that orphan genes respond to acute viral infection and may serve as biomarkers or pharmaceutical targets for COVID-19.

5. **Cell-type and developmental specificity.** scRNA-Seq reanalysis of liver, breast, and testis identified heEB genes as top markers of specific cell clusters — e.g., EB.chr21G14889 marks a liver cluster co-localizing with NEAT1; EB.chr17G27061 marks a breast cluster (cluster 11); EB.chr19G4801 and EB.chr1G70855 are Sertoli-cell subtype markers. snRNA-Seq of human lungs at fetal, child, and adult stages shows heEB orphans as cell-type and developmental-stage-specific, visualized via the Morpheus/Broad Cell Atlas tool.

6. **Pathogenic variant burden.** The 54,794 heEB transcripts harbor 327,565 COSMIC variants; 169,283 (52%) are predicted pathogenic by FATHMM. Skin, large intestine, and lung tissues carry the highest densities of pathogenic variants in heEB genes. Alt-spliced heEB transcripts have the highest mean CADD scores among genomic context classes.

7. **Cancer survival associations.** Cox regression (BH-adjusted p < 0.05, controlling for age, sex, race) identifies thousands of heEB orphan DE genes significantly associated with overall survival across TCGA tumor types. KIRC (kidney renal clear cell) and LGG (lower grade glioma) show the largest counts of survival-associated heEB genes. Specific examples: EB.chr15G26998 (median = 10; HR = 3.8; p = 9.9e-6) in COAD, high expression associated with poor survival; EB.chr3G1029 (median = 11.381; HR = 2; p = 1.1e-5) in KIRC. These genes are not captured by standard Gencode-based pipelines.

8. **Translation evidence.** Processing 289 Ribo-Seq samples identified 943 heEB transcripts with translation evidence via ribotricer. The majority of translated heEB genes (646/943) are human-specific orphans. Two intergenic heEB genes with translation evidence are assigned to the most ancient phylostrata (cellular organisms), suggesting convergent ORF use.

9. **Functional inference via co-expression.** MCL partitioning of a Spearman correlation matrix (threshold 0.9) across 2,630 GTEx brain samples yielded 156 clusters >10 genes. Gene Ontology enrichment was used to infer functions. Cluster 4945 — containing orphan EB.chr19G20849 and heEB EB.chr3G17848 — is enriched for oxidative respiration / proton motive force-driven ATP synthesis (adj p = 1.4E-50); its members span OXPHOS complexes I–V, suggesting both transcripts may be involved in mitochondrial energy metabolism.

10. **Chimpanzee cross-species validation.** Only 564 of 11,510 heEB transcripts that were unannotated in chimpanzee (5%) were detected as expressed in 8 chimpanzee strand-specific RNA-Seq samples, confirming the majority are human-specific. The 564 that do overlap are enriched in Homininae-assigned phylostrata.

## Limitations

- **Preprint status.** This is a bioRxiv preprint (posted February 2024); peer review status unknown at time of reading. Key claims (especially survival associations and COVID-19 results) should be treated as preliminary.
- **Expression ≠ function.** High expression is a necessary but not sufficient indicator of biological importance. Many heEB transcripts may be transcriptional noise selectively retained by the expression filter due to condition-specific artifacts (e.g., cellular stress responses, sequencing artifacts inflated in certain tissues).
- **Intronic majority.** 84% of heEB transcripts are intronic to annotated genes, raising the possibility that many are processing intermediates, retained introns, or antisense reads rather than independent transcriptional units. The authors argue co-expression independence (Spearman with host transcript), but this check is partial.
- **FATHMM/CADD on non-coding context.** Variant pathogenicity predictors are trained predominantly on coding sequence and annotated regulatory elements; applying them to intronic heEB transcripts whose functional significance is unestablished inflates apparent pathogenic variant density.
- **No direct PubTator integration.** The paper does not directly assess what fraction of heEB genes are mentioned in the biomedical literature or would be recoverable via text mining. The claim that they are "invisible to standard pipelines" is well-supported for alignment pipelines, but not explicitly tested against NLP pipelines.
- **Ancestry and sex DE results.** Differences by self-reported race and sex are acknowledged to be confounded by genetic, socioeconomic, and environmental factors; the paper explicitly notes the inability to disentangle these at the study design level.
- **COVID-19 analysis.** 8,865 COVID-induced heEB transcripts are derived from a heterogeneous collection of 32 SRA studies with variable tissue, severity, and platform — cross-study batch effects are not fully controlled despite study-level stratification.
