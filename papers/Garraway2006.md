---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Garraway2006
kind: paper
title: Lineage dependency and lineage-survival oncogenes in human cancer
version: "1.0.0"
created: "2026-07-11"
updated: "2026-07-11"
bibkey: Garraway2006
tags: []
ontology_terms:
- MITF
- androgen receptor
- developmental biology
- lineage addiction
- lineage conditioning
- lineage dependency
- lineage-survival oncogenes
- melanoma
- oncogene addiction
- prostate cancer
- somatic mutation patterns
- tissue of origin
paper_kind: review
---
## Key Findings

1. **Lineage conditioning of somatic genetics.** Activating mutations in KRAS, NRAS, HRAS, BRAF, EGFR, and PIK3CA, and amplifications of CCND1, ERBB2, and EGFR, each concentrate in a small number of lineages. Tumour-suppressor inactivation (TP53, CDKN2A) is comparatively lineage-independent, though the *mechanism* of inactivation still varies by lineage (e.g., TP53 direct mutation is infrequent in melanoma; INK4a/ARF deletion serves the equivalent purpose). SNP array hierarchical clustering of cancer cell lines and tumor samples reproduces lineage groupings from copy-number data alone.

2. **Lineage addiction vs. oncogene addiction.** Oncogene addiction (BCR–ABL in CML, KIT in GIST, EGFR in NSCLC) requires a tumour-specific gain-of-function alteration. Lineage addiction requires only the persistence and deregulation of developmental survival pathways — no new cellular function is gained. Both converge on the concept of excessive dependency, but the origin and nature of the dependency differ.

3. **MITF as prototype lineage-survival oncogene.** MITF controls melanocyte differentiation and survival (via BCL2, CDK2). SNP array studies identified MITF amplification in 15–20% of metastatic melanomas. Functional assays showed MITF cooperates with BRAFV600E to transform immortalized human melanocytes, but only when p16–CDK4–RB pathway activity is also disrupted. This explains why melanomas co-select for constitutive MAPK activation (NRAS/BRAF mutations) and CDKN2A deletion: these create the permissive genetic context for MITF-dependent oncogenesis.

4. **Androgen receptor as second prototype.** AR is required for prostate luminal epithelial development; ectopic AR expression in RB/p53-deficient prostate epithelial cells drives tumour formation under androgen stimulation. AR exemplifies how a lineage-survival function can be co-opted as an oncogenic dependency across prostate cancer progression.

5. **Catalogue of predicted lineage-survival oncogenes.**

   | Gene | Lineage | Key property | Genetic alteration confirmed? |
   |---|---|---|---|
   | MITF | Melanocytic | TF; melanocyte differentiation/survival | Yes (amplification) |
   | AR | Prostate epithelial | TF; prostate luminal differentiation | Yes (expression deregulation) |
   | CCND1 | Mammary | Cell-cycle regulator; mammary maturation | Yes (amplification) |
   | FLT3 | Myeloid | RTK; myeloid maturation | Yes (activating mutations in AML) |
   | ESR1 | Mammary | TF; breast development | Coactivators amplified; ESR1 itself not mutationally altered in 2006 data |
   | TITF1 | Lung | TF; thyroid and lung development | Not yet confirmed in 2006 |
   | CDX1 | Intestinal | TF; intestinal development | Not yet confirmed in 2006 |
   | Ets oncogenes | Prostate, mammary | TFs | Yes in prostate |

6. **Poorly differentiated and lineage-independent cancers.** Not all tumours maintain lineage dependency; a subset of melanomas downregulate MITF in aggressive disease and AR-negative prostate cancers exist (~1% PSA-negative). Poorly differentiated cancers may rely on lineage-independent mechanisms, though some retain "lineage memory" (microRNA profiles reveal lineage identity even when mRNA expression does not; neural-crest lineage responses persist in poorly differentiated melanoma cells in chick embryo injection experiments).

7. **Therapeutic implications.** Targeting lineage dependencies may require combinatorial or synthetic-lethal approaches because lineage-survival pathways are also active in normal cells, raising toxicity concerns for direct inhibition. Synthetic dosage lethality — identifying factors that buffer the altered cellular state created by deregulated lineage survival plus enabling genetic events — is proposed as an approach to cancer-type-specific vulnerabilities.

## Limitations

- This is a 2006 conceptual review; the catalogue of lineage-survival oncogenes is now substantially expanded by genome-wide cancer sequencing efforts (e.g., TCGA, COSMIC v3, Pan-Cancer Atlas).
- Functional validation criteria for lineage-survival oncogenes (Box 3) are qualitative; the review does not provide a quantitative scoring framework.
- The distinction between "lineage conditioning" as a selective pressure vs. as a reflection of tissue-specific mutational processes is not deeply resolved (this is precisely what question:0002 asks about).
- The claim that most oncogene mutations are lineage-restricted while tumour-suppressor mutations are lineage-independent is a 2006 generalisation that has since been refined; for example, IDH1 mutations show strong lineage restriction in glioma and AML.
- The therapeutic discussion (synthetic dosage lethality, BCL2 antisense) was prescient but reflects the pre-modern-immunotherapy, pre-BET-inhibitor era; clinical translation has evolved substantially.
