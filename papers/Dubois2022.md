---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Dubois2022
type: paper
title: Structural Variations in Cancer and the 3D Genome
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Dubois2022
tags: []
datasets: []
ontology_terms:
- 3D genome
- chromatin compartments
- chromothripsis
- cis-regulatory elements
- enhancer hijacking
- extrachromosomal DNA
- punctuated evolution
- structural variation
- topologically associated domains
---
## Key Findings

### 3D architecture constrains SV formation

- SV frequency across the genome decreases as the reciprocal of span length — the same distribution as contact frequency in Hi-C data — indicating that the 3D proximity of loci in normal tissue largely determines which pairs fuse when DSBs occur.
- The BCR-ABL1 fusion (Philadelphia chromosome) arises in myeloid cells because BCR (chr9) and ABL1 (chr22) are in close 3D proximity specifically in hematopoietic cells; they are distant in other cell types. IGH-MYC is present in 9/10 Burkitt lymphomas for the same spatial reason.
- TMPRSS2-ERG fusions in prostate cancer: TMPRSS2 and ERG are 2 Mb apart on chr21 but brought into close nuclear contact by androgen receptor-driven chromatin looping; TOP2B is recruited to relieve transcriptional tension, creating DSBs at both loci.
- Actively transcribed open-chromatin ("A compartment") sites are prone to TOP2B-associated DSBs and preferential repair by HR during S-phase; error-prone NHEJ during G1 preferentially affects heterochromatic loop anchors. These compartment-specific repair pathways mechanistically link 3D state to SV type.
- Chromothripsis: Hi-C analysis showed SVs arising from chromothripsis are significantly enriched between loci sharing similar replication timing and A-compartment status — consistent with 3D proximity preceding the catastrophic shattering event.

### SVs alter 3D genome architecture

- Deletion of a CTCF anchor fuses two adjacent TADs. Duplications of CTCF anchors create "neo-TADs." Inversions swap DNA territory between TADs. Translocations can fuse or swap TAD territories across chromosomes.
- In multiple myeloma, translocation of NSD2 (histone methyltransferase) causes H3K36 pervasive methylation and remodels A/B compartments and TAD structure genome-wide — a trans mechanism rather than a local CRE effect.

### Five mechanisms of SV-driven oncogene activation (Figure 4)

1. **Enhancer juxtaposition (hijacking):** SVs place a tissue-specific lineage enhancer proximal to an oncogene promoter. Canonical example: pediatric medulloblastoma group 3/4 SVs on chr1/9 juxtapose distal active enhancers with GFI1/GFI1B, causing high-level upregulation. TERT promoter-associated SVs activate telomerase across multiple cancer types by co-opting open active-chromatin partner loci.
2. **CRE-gene fusion:** Entire regulatory machinery of one gene is fused to a second. TMPRSS2:ERG hijacks the TMPRSS2 promoter and enhancers to drive ERG expression and simultaneously removes a degron in the ERG N-terminus, conferring proteasome resistance.
3. **Enhancer de novo looping:** SVs generate new long-range E:P loops. Lung squamous carcinoma SVs at a CTCF loop-anchor disrupt the TAD boundary adjacent to IRS4 (100 kb away), spreading active H3K27ac chromatin and enabling ectopic looping to normally silent enhancer. Medulloblastoma: complex SVs flip a super-enhancer across a TAD boundary to activate PRDM6 >600 kb away.
4. **Enhancer amplification:** Strong lineage-specific enhancers controlling MYC are amplified in AML, T-ALL, lung, and endometrial carcinoma. In CRPC, androgen-deprivation selects for amplification of AR lineage-specific enhancers, re-activating AR expression through increased E:P interaction.
5. **Extrachromosomal amplification:** ecDNA circular topology circumvents insulators, allowing all enhancers on the amplicon to interact with all contained oncogenes — a uniquely permissive regulatory environment. ecDNA incorporates EGFR or MYC along with enhancers from adjacent TADs (glioblastoma, neuroblastoma). ecDNA can also act in trans as enhancers for promoters on the linear genome, and ecDNA hubs co-localize multiple amplicons for cooperative oncogene expression.

### Tissue-type specificity of SVs

- SVs are substantially more cancer-type-specific than SNVs. This specificity arises from two sources: (a) the tissue-specific pre-cancerous 3D folding determines which loci are in proximity to form SVs; (b) the enhancer landscape is highly tissue-specific, so enhancer-hijacking SVs only confer fitness in the lineage where the hijacked enhancer is active.
- BRAF V600E mutations occur across many cancer types; BRAF-KIAA1549 rearrangements are almost exclusively found in juvenile pilocytic astrocytoma. TMPRSS2-ERG is common in prostate cancer and essentially absent elsewhere.
- SVs affect one-third of the genome in the average cancer (via copy-number alterations); driver fusion events from regulatory hijacking have been observed in over a quarter of cancers.

### Chromothripsis and punctuated evolution

- Chromothripsis causes several hundred SVs in a single event. Essential genes (~10% of all genes) are frequently disrupted, generating strong negative selection. On rare occasions, a subset of the tens-to-hundreds of SVs has strong positive fitness effects, producing "punctuated evolution" — a single catastrophic event can simultaneously generate multiple driver alterations and launch clonal expansion.
- Complex SV mechanisms include chromothripsis, BFB cycles, ecDNA formation, chromoanasynthesis (MMBIR-based replication template switching), templated insertions, and chromoplexy (chains involving multiple chromosomes).
- TAD disruption per se is insufficient — in PCAWG across 2,700 tumor genomes, only a minority of TAD-disrupting SVs show marked gene expression changes. Effective oncogenic SVs require both TAD disruption and the right CRE constituents (active promoter, active enhancer) to be brought into contact.

## Limitations

- Synthesis review; does not provide new primary data or systematic quantification of the relative frequency of the five oncogenic SV mechanisms across cancer types.
- The claim that "only a minority of TAD-disrupting SVs show marked gene expression changes" is a pan-cancer aggregate; the fraction likely varies substantially by cancer type, SV type, and specific locus context — this heterogeneity is acknowledged but not resolved.
- ecDNA's role is discussed primarily through chromatin accessibility and enhancer-oncogene looping (Wu2019, Morton 2019, Koche 2020, Zhu 2021); the non-Mendelian segregation axis (Turner2017, deCarvalho2018) is not the focus of this review.
- SV detection from WGS remains technically limited by short-read ambiguity at complex SVs and common fragile sites; the review notes that the true rate of recurrent oncogenic SVs is likely underestimated.
- The five CRE-activation mechanisms are presented as conceptually distinct but in practice overlap (e.g., ecDNA formation combines enhancer hijacking + looping + amplification simultaneously).
