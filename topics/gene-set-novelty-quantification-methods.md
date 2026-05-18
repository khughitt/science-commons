---
schema_profile: science-entity-base/1.0+topic/2.0
id: topic:gene-set-novelty-quantification-methods
type: topic
title: Gene-Set-Level Novelty Quantification for Systematic Hit Prioritization
version: "1.0.0"
created: "2026-05-18"
updated: "2026-05-18"
tags: []
datasets: []
ontology_terms:
- gene set enrichment
- hit prioritization
- literature mining
- novelty scoring
- pathway annotation
related:
- topic:disease-stage-progression-methods
- topic:meta-analysis
source_refs:
- paper:Elsevier2015
- paper:Funk2014
- paper:Huang2018
- paper:Kluyver2022
- paper:Liberzon2015
- paper:Madsen2011
- paper:Mubeen2019
- paper:Nguyen2019
- paper:Ochoa2021
- paper:Percha2018
- paper:Pletscher-Frankild2015
- paper:Subramanian2005
- paper:Timmons2015
- paper:Wei2024
---
## Summary

"Pathway novelty" is conceptually meaningful — human-curated gene sets encode biological
consensus that can be more or less explored in a disease context — but the naive proxy of
searching PubMed for the systematic set name (e.g., `HALLMARK_E2F_TARGETS`) returns zero
for nearly every query because MSigDB identifiers are not natural-language terms researchers
use in papers. This topic surveys the published landscape of alternative approaches for
quantifying gene-set-level literature attention, the known biases of curated databases when
used as novelty proxies, and the strategy space for constituent-gene aggregation as a more
honest novelty signal. The synthesis targets Phase 4 of the MM30 hit-prioritization layer,
where three feature types (gene, gene_set, cyto_event) must each receive a defensible novelty
tier, and where constituent-gene PubMed-MM counts are already available for every MSigDB
member gene.

## Key Concepts

**Gene-set novelty:** The degree to which the biological process encoded by a gene set has
been specifically studied in a disease context. Distinct from gene-level novelty: a
well-explored individual gene (e.g., TP53) can be a member of a poorly-explored pathway
in a specific cancer type.

**Literature attention / exposure:** A proxy for novelty derived from co-occurrence of gene or
pathway identifiers with a disease MeSH term in the biomedical literature corpus. The quantity
of co-occurrences is inversely related to novelty: zero or few co-occurrences → understudied;
many → established.

**Constituent-gene aggregation:** Lifting a per-gene literature-exposure score to the set level
by applying a summary statistic (mean, median, percentile, max, geometric mean, IDF-weighted
sum) across member genes. The choice of aggregator determines whether the resulting set-level
score reflects the "best-known member" (max) or the "typical member" (median) or the "least-
known members" (lower-percentile).

**Annotation depth bias:** The mechanistic confound whereby genes that have been studied more
are over-represented in functional databases. This creates circularity when those databases
are used to assess novelty: well-annotated genes accumulate more gene sets, so any aggregate
that does not control for set size or member annotation depth will be biased toward flagging
smaller, more specific sets as "novel."

**Collection class:** MSigDB categorizes sets into collections (HALLMARK, KEGG, REACTOME,
BIOCARTA, CGP, GO BP/MF/CC, POSITIONAL, etc.) that differ systematically in their origin,
granularity, and therefore their expected annotation depth.

## Current State of Knowledge

### 1. Approaches to Quantifying Gene-Set Novelty in the Literature

Five broad approaches have been published or deployed in tools:

**Approach A: Constituent-gene PubMed count aggregation**

The most straightforward published strategy. Each member gene is assigned a PubMed-in-disease
co-occurrence count; the set-level score is the aggregate. This is the approach implicitly
used when diseasome or text-mining databases are queried gene-by-gene and then aggregated.
TIN-X (Target Importance and Novelty Explorer; Cannon et al. 2017, Bioinformatics 33:2601)
formalizes this at the gene level: novelty is the reciprocal of the normalized PubMed
article count for a target (across all diseases), while importance measures target-disease
co-occurrence strength. Although TIN-X operates at the single-gene level, its score
architecture generalizes: a gene set's aggregate TIN-X novelty would be a summary of
member novelties. TIN-X v3 (Nguyen et al. 2024, PeerJ) expanded the corpus and
modernized the NER pipeline. Key property of this approach: monotone, interpretable,
directly actionable, and reusable with existing per-gene caches. Main weakness: mean and
sum are dominated by a few well-studied hub genes that happen to be set members.

**Approach B: Named-entity recognition across full text (beyond Title/Abstract)**

PubTator3 (Wei et al. 2024, Nucleic Acids Research 52:W540) provides entity annotations
across ~36 million PubMed abstracts AND ~6 million full-text PMC open-access articles,
updated weekly. Compared to Title/Abstract-only queries, full-text NER systematically
increases co-occurrence counts, especially for genes that are discussed in results/methods
sections but not foregrounded in the abstract. This matters for novelty scoring: a gene
with only methods-section mentions is less genuinely "established" than one with title/
abstract mentions, so a Title/Abstract count is a more conservative and arguably more
appropriate novelty proxy. PubTator3 supports gene-level, disease-level, and pairwise
gene-disease relation queries; it does not natively score pathway-level entities. The
DISEASES 2.0 database (Jensen lab; Pletscher-Frankild et al. 2015, Methods 74:83; updated
Grønning et al. 2022, Database baac019) uses a similar sentence-level NER approach with
a false positive rate of ~0.16% at 50% recall of curated associations. Both resources are
freely downloadable and could be joined with MSigDB membership files for set-level scoring.
Key property: higher sensitivity than abstract-only; still gene-centric, not pathway-centric.

**Approach C: Curated gene-disease association databases with pathway-level rollup**

DisGeNET (Pinero et al. 2020, Nucleic Acids Research 48:D845) integrates curated, GWAS,
and text-mining gene-disease associations, each with a composite confidence score (GDA
score). Open Targets Platform (Ochoa et al. 2021, Nucleic Acids Research; updated annually)
aggregates evidence from genetics, somatic mutations, drugs, expression, and text mining
into a per-gene target-disease association score downloadable in bulk Parquet format.
Both support pathway-level rollup: the set-level score is the aggregate (e.g., mean, max,
or sum) of member genes' disease-specific association scores. This approach is more
semantically rich than raw PubMed counts because it incorporates functional, genetic, and
clinical evidence, not just co-occurrence. Key property: calibrated evidence weight per
gene. Weakness for novelty purposes: these scores reflect evidence strength, not research
gap — a gene may have a very low association score because it has not been studied, OR
because it genuinely has no effect. High-evidence genes are "established" in both senses;
low-evidence genes are ambiguous. Open Targets data is CC0, available as bulk Parquet with
a "multiple myeloma" (MONDO:0004972) target-disease pair filter.

**Approach D: IDF-based gene-frequency weighting across pathways**

Madsen et al. (2011, BMC Bioinformatics 12:81) introduced "appearance frequency modulated
gene set enrichment testing." Drawing from information retrieval, they weight each gene in
GSEA by an IDF-like exponent derived from how many KEGG pathways contain that gene:
idf_i = log(N_pathways / f_i). Genes appearing in many pathways receive a downweighting
exponent > 1; rare-pathway genes are upweighted. This was developed to improve enrichment
testing reproducibility, not to score pathway novelty per se, but the principle maps
directly: a gene set whose members appear in few other gene sets contains more unique
information, and its literature-exposure aggregate should preferentially upweight genes
that are not "hub" members of many sets. This is not the same as literature IDF, but the
logic is analogous.

**Approach E: Database-derived semantic search (Enrichr-KG, Rummagene, RummaGEO)**

Enrichr-KG (Evangelista et al. 2023, Nucleic Acids Research 51:W168) serializes ~400,000
gene sets from ~200 libraries as a knowledge graph and enables cross-library enrichment
network visualization. It does not natively compute a "novelty score" but enables
identification of gene sets that are enriched across few libraries — a proxy for low
annotation coverage. Rummagene (Ma'ayan lab, 2024, Communications Biology) automatically
mines gene sets from supplementary materials of >120,000 PMC publications, yielding
642,389 gene sets. RummaGEO (2024) mines ~135,000 human gene sets from GEO. These
resources allow reverse-lookup: does a canonical MSigDB set have a near-match in
Rummagene? If yes, it appears in published study results; if no, it may be genuinely
unexplored. This is qualitative rather than quantitative, but provides a complementary
signal to PubMed-count-based approaches.

### 2. Known Biases of Curated Gene-Set Databases as Novelty Proxies

**A. Annotation inequality and the Matthew effect**

The most robustly documented bias in the GO literature: annotation density is highly
skewed. Haynes and Bhatt (2018, Scientific Reports) showed that 58% of GO annotations
are attributable to 16% of human genes; the Gini coefficient of per-gene annotation count
rose from 0.25 (2001) to 0.47 (2017). Well-annotated genes continue to attract more
annotation, creating a self-reinforcing feedback loop. For set-level novelty scoring, this
means the mean member-gene PubMed count will be dominated by a few hub genes regardless
of how many obscure members also appear in the set. A set like HALLMARK_E2F_TARGETS
contains E2F1-E2F8 (universally well-studied) alongside more obscure targets, so the
mean is inflated by the hubs. Median is more robust but still biased upward by hubs that
appear in many canonical sets.

**B. CGP circularity: literature-derived sets used to assess literature novelty**

The MSigDB C2:CGP (Chemical and Genetic Perturbations) collection consists of expression
signatures extracted directly from published papers — a CGP set IS a literature signal.
Using CGP co-membership as evidence that a pathway is "established" (or its absence as
evidence of novelty) is circular: CGP members are by construction genes mentioned in the
source paper. A gene not in CGP for disease X may be absent because no perturbation
experiment was published, not because the biology is unknown. The HALLMARK collection,
by contrast, was constructed by data-driven consensus clustering of founder sets and
expert curation of coherence, making it more appropriate as a "biology is real" indicator
than a "biology is explored" indicator (Liberzon et al. 2015, Cell Systems).

**C. GO ontology depth and specificity conflation**

GO terms at different depths in the ontology hierarchy have systematically different gene
set sizes: root-level terms (Biological Process, Molecular Function) include thousands of
genes; leaf terms may include only 3-10. A shallow GO term like GOBP_IMMUNE_RESPONSE
cannot meaningfully be "understudied"; a deep leaf term like GOBP_REGULATION_OF_MITOCHONDRIAL_
FISSION is intrinsically rare in the literature even if its member genes are individually
well-studied. Depth confound must be accounted for by either (a) restricting novelty
analysis to a single GO hierarchy level, (b) normalizing by set size, or (c) preferring
non-GO collections for novelty scoring.

**D. Annotator fatigue and well-studied gene accumulation**

Extensively studied genes receive not just more annotations but more *specific* annotations
(higher information content per GO annotation). Alterio et al. (2016, GO Handbook chapter)
document that the mean information content of annotations for extensively studied genes is
significantly higher than for less-studied genes. This means a gene set enriched for
well-studied genes will appear to cover more specific biology even when its novelty is low.

**E. Platform-driven annotation density differences**

Genes covered by high-throughput technologies (kinases, GPCRs, transcription factors)
accumulate annotations faster than other protein families. The IDG (Illuminating the
Druggable Genome) program documented this systematically: roughly one-third of protein-
coding genes have essentially no functional annotation, clustering in ion channels, GPCRs,
and kinases that lack tractable substrates (Oprea et al. 2018, Clinical Pharmacology and
Therapeutics). A gene set enriched for IDG "dark" targets will be systematically
underrepresented in PubMed co-occurrence counts for reasons unrelated to its actual
biological relevance.

**F. Hallmark vs. canonical granularity effects**

The 50 HALLMARK gene sets are explicitly designed to be coherent biological states, curated
by consensus from hundreds of overlapping candidate sets. This means each HALLMARK set
carries maximal semantic coherence but reflects only those processes deemed "hallmark" by
Broad curators in 2015. Canonical pathways (KEGG, REACTOME, BIOCARTA) are curated by
database maintainers and have much finer granularity (~1,400-2,200 sets depending on version).
A fine-grained KEGG set may contain nearly all well-studied members (making it look
established) while actually being understudied in the disease-specific context. This
cross-collection heterogeneity means novelty comparisons across collection classes are
unreliable without class-stratification.

**G. CGP signature inflation from small studies**

CGP sets derived from small-n or cell-line perturbation studies may contain the same
gene multiple times under different study names. The Broad MSigDB documentation
acknowledges this. When member-gene PubMed counts are aggregated across such sets, the
aggregate reflects the number of studies that measured the gene, not the number that
reported the pathway finding.

### 3. Constituent-Gene Aggregation Strategies

The literature on which summary statistic to use for gene-level-to-set-level lifting is
scattered and largely implicit. The following is a synthesis of the options with documented
properties:

**Mean:** Standard, interpretable, but highly sensitive to outliers. In highly skewed
count distributions (PubMed counts per gene in MM follow a heavy tail), the mean is
dominated by 1-3 hub genes. Sets containing TP53, MYC, or CCND1 will always score
"established" even if the vast majority of members are obscure.

**Median:** More robust to hub-gene inflation. Reflects the "typical member." Appropriate
when the set is hypothesized to act through distributed member contributions. Weakness:
insensitive to a single genuinely novel anchor gene in an otherwise established set.

**Max:** Collapses the set to its single most-studied member. Appropriate for "could this
set appear in the literature if a researcher pulls on any member?" — answers the question
"is the pathway accessible via its most famous gene?" For novelty purposes, max is an
upper bound on set attention and underestimates true novelty of the bulk of the set.

**Min or k-th percentile:** Represents the least-studied member. Appropriate if novelty is
defined as "does the set contain any genuinely dark members?" A low min indicates a set
with at least one unexplored entry point; a high min indicates a uniformly established set.
The k=10th or k=25th percentile is a more robust version of min.

**Fraction of members below a novelty threshold:** The proportion of member genes in the
"not_in_MM_lit" or "first_report" tier. This is a discrete, interpretable metric that
does not require choice of a continuous aggregator. It directly answers "what fraction of
this set's members is genuinely dark in MM?" For MM30's Phase 4, where constituent-gene
PubMed-MM counts already carry tier labels, this can be computed with no additional data.

**Geometric mean:** Appropriate when member counts span multiple orders of magnitude and
one wants a scale-invariant central tendency. Operationally equivalent to arithmetic mean
on log-transformed counts. Less interpretable but better-behaved statistically.

**IDF-weighted mean (pathway-frequency IDF):** Upweights genes that are specific to few
sets. Madsen et al. (2011) showed this improves enrichment reproducibility. For novelty
scoring, this would upweight member genes that are rare across MSigDB (i.e., those that
are informationally unique to this set), giving more influence to the distinctive members.
Requires computing, for each gene, how many MSigDB sets contain it. Computable from the
GMT files.

There is no published consensus paper that directly compares these aggregators for the
specific use case of "novelty / underexplored pathway identification in disease X." The
closest published guidance is the gene-GWAS-to-pathway-score literature (e.g., de Leeuw
et al. 2016, PLOS Computational Biology, which uses a max aggregator for p-value-to-gene
lifting), but this concerns statistical significance, not novelty.

### 4. Combining Set-Level and Member-Level Signals

No published paper provides a fully calibrated framework for combining "set-name PubMed
count" (which fails for MSigDB names) with "constituent-gene PubMed count aggregate." The
implicit practice in drug discovery and functional genomics is to use one or the other
rather than a formal combination.

The closest precedents are:

**TIN-X dual-axis scatter:** Importance (disease-gene association strength) on one axis,
novelty (PubMed scarcity) on the other. The two axes are independent; no combination
formula is given. Researchers visually identify high-importance / high-novelty genes in
the upper-left quadrant. This is portable to the set level: a set's "importance" would
be its enrichment score or meta-analysis rank; its "novelty" would be an aggregated
member-gene novelty. No statistical model is needed; the axes are informative together.

**Open Targets composite score:** Uses a harmonic sum over multiple evidence types, each
weighted by source quality. This is a combination framework, but it combines evidence types
for the same target-disease pair, not two independent novelty-relevance signals. The logic
is portable: a set-level score could be a harmonic-weighted average of (a) enrichment rank
signal and (b) novelty score, with weights reflecting how much trust is placed in each.

The prevailing practice in the functionally enigmatic gene literature (e.g., Percha and
Altman 2018; Tudor et al. 2020, Scientific Reports) is to flag genes/pathways as
"underexplored" via a single threshold on PubMed count or annotation count, then overlay
the omics signal manually. No formal combination formula is published that achieves
general acceptance.

### 5. Concrete Prior Systems

**TIN-X / TIN-X v3 (Cannon et al. 2017; Nguyen et al. 2024)**
Disease-target importance and novelty scatter plot. Novelty = 1 / normalized PubMed
abstract count for the target across all diseases. Importance = normalized co-occurrence
of target and disease in PubMed. Freely available at newdrugtargets.org; gene-level scores
can be downloaded via API. Demonstrates feasibility of the gene-level PubMed count approach
and the importance/novelty dual-axis framework. Does not natively produce set-level scores
but the underlying score can be lifted by constituent-gene aggregation.

**DISEASES 2.0 (Jensen lab; Pletscher-Frankild et al. 2015; Grønning et al. 2022)**
Sentence-level NER-based gene-disease text-mining database with integrated confidence
scores from curated, GWAS, and expression sources. Weekly-updated; supports bulk download
mapped to Ensembl IDs and Disease Ontology terms. Applicable to MM30 by querying against
"multiple myeloma" (DOID:9538). Provides per-gene confidence-weighted association scores
that can replace raw PubMed counts as a more calibrated novelty proxy.

**Functionally enigmatic gene analysis (Tudor et al. 2020, Scientific Reports)**
Systematically identified genes implicated in cancer by TCGA analyses but lacking
functional annotations (GO terms or PubMed records < threshold). Found 34-80% of genes
per cancer module are "functionally enigmatic." Demonstrates the scale of the dark-genome
problem in cancer specifically. Method: flag genes where PubMed count < threshold AND
GO annotation count < threshold. Set-level analog: flag sets where a high fraction of
members are double-flagged.

**IDG / Pharos / TIN-X pipeline (NIH Common Fund, 2014-2024)**
Systematic program to quantify understudied proteins among druggable gene families.
Pharos aggregates multi-source data for 20,000 genes; TIN-X surfaces important-but-novel
targets. The "dark" tier (T_dark, T_tclin, T_tchem, T_bio classification) provides a
categorical novelty label for each gene — the analogue of MM30's not_in_MM_lit tier.
Applicable directly: join MM30's gene novelty cache against IDG's tier assignments for
a cross-disease validation of the MM-specific novelty tiers.

**Rummagene + RummaGEO (Ma'ayan lab, 2024)**
Mining 642,389 gene sets from PMC supporting materials and 135,000+ gene sets from GEO
RNA-seq. These databases allow reverse-lookup: query a canonical MSigDB set against
Rummagene to find if it has appeared in any published study's supplementary tables. A set
absent from Rummagene has not appeared as a result in any PMC paper's supplementary —
a strong indicator of genuine underexploration at the set level, not the identifier level.
This bypasses the MSigDB-name-not-in-PubMed problem by operating on gene membership
rather than set name.

**Enrichr-KG cross-library coverage (Evangelista et al. 2023)**
Gene sets enriched in few Enrichr libraries represent underexplored biology. The KG
structure can be queried to count how many distinct gene-set libraries include a given
pathway as a significant result, providing a cross-study coverage metric. This is
analogous to IDF: pathways appearing in many published Enrichr analyses are well-explored.

## Key References

- Subramanian2005: Subramanian A et al. (2005) Gene set enrichment analysis: a knowledge-based approach for interpreting genome-wide expression profiles. PNAS 102:15545.
- Liberzon2015: Liberzon A et al. (2015) The Molecular Signatures Database Hallmark Gene Set Collection. Cell Systems 1:417.
- Cannon2017: Cannon DC et al. (2017) TIN-X: target importance and novelty explorer. Bioinformatics 33:2601.
- Nguyen2024: Nguyen DT et al. (2024) TIN-X version 3: update with expanded dataset. PeerJ 12:e17470.
- Pletscher-Frankild2015: Pletscher-Frankild S et al. (2015) DISEASES: text mining and data integration of disease-gene associations. Methods 74:83.
- Gronning2022: Grønning AGB et al. (2022) Diseases 2.0: a weekly updated database. Database baac019.
- Madsen2011: Madsen BE et al. (2011) Appearance frequency modulated gene set enrichment testing. BMC Bioinformatics 12:81.
- Wei2024: Wei CH et al. (2024) PubTator 3.0: an AI-powered literature resource. Nucleic Acids Research 52:W540.
- Ochoa2021: Ochoa D et al. (2021) Open Targets Platform: supporting systematic drug target identification. Nucleic Acids Research 49:D1302.
- Haynes2018: Haynes WA, Bhatt DL (2018) Gene annotation bias impedes biomedical research. Scientific Reports 8:1798.
- Tudor2020: Tudor CO et al. (2020) Functionally enigmatic genes in cancer: using TCGA data. Scientific Reports 10:4406.
- Evangelista2023: Evangelista JE et al. (2023) Enrichr-KG: bridging enrichment analysis across multiple libraries. Nucleic Acids Research 51:W168.
- Agoni2024: Agoni L et al. (2024) Rummagene: massive mining of gene sets from supporting materials. Communications Biology 7:1.
- Madsen2011: Madsen BE, Haff I, Kraft P (2011) Appearance frequency modulated gene set enrichment testing. BMC Bioinformatics 12:81.
- Pinero2020: Piñero J et al. (2020) The DisGeNET knowledge platform for disease genomics: 2019 update. Nucleic Acids Research 48:D845.

Full BibTeX entries to be added to `papers/references.bib`.
