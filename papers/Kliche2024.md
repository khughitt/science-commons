---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Kliche2024
type: paper
title: Proteome-scale characterisation of motif-based interactome rewiring by disease mutations
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Kliche2024
tags: []
authors:
- Kliche et al.
datasets:
- dataset:clinvar-gnomad-cosmic
- dataset:genvar-hd2
- dataset:tcga
doi: 10.1038/s44320-024-00055-4
ontology_terms:
- intrinsically-disordered-region
- missense-variant
- protein-protein-interaction
- short-linear-motif
venue: Molecular Systems Biology
year: 2024
---
## One-Sentence Summary

A pan-disease peptide-phage display screen of 12,301 disease-associated SNVs in intrinsically disordered regions identifies 366 domain-mutation pairs where mutations disrupt, enhance, or create short-linear-motif-mediated protein-protein interactions, providing a proteome-scale map of how missense variants rewire the IDR interactome.

## Key Findings

1. **Scale and coverage.** The GenVar_HD2 phage library tiles ~57,000 peptides from the IDRs of 1,915 human proteome proteins, covering 12,301 SNVs drawn from ClinVar, gnomAD, COSMIC, TCGA, and UniProt. 91.9% of mutations are pathogenic or likely pathogenic; 82% are somatic. Eleven disease classes are represented; 22.9% of mutations span more than one class (mixed categorisation). Bait collection: 80 purified protein domains screened in 4-round phage selections with ≥ 5 replicates per domain.

2. **366 mutation-modulated interactions identified.** Selections yielded 2,225 domain-peptide interactions; 366 of these domain-mutation pairs (275 mutations, 279 PPIs) are significantly modulated by mutations (Mann-Whitney p ≤ 0.001). 173 interactions are diminished or abrogated; 193 are enhanced or de novo created. About 70% of bait proteins had at least one mutation-affected interaction.

3. **Split between disabling and enabling mutations.** Mutations that abolish interactions cluster in ubiquitin system (E3 ligase) and transcriptional regulation bait categories. Mutations that create or enhance interactions are proportionally more common for autophagy-related baits (ATG8 proteins) and scaffolding proteins — a pattern with functional implications for mislocalisation and aberrant degradation.

4. **Motif consensus mapping explains mechanism.** For 298 of 366 domain-mutation pairs a motif consensus was found in the wild-type or mutant sequence. Of those: 110 mutations hit key residues of existing SLiMs (75 disrupt, 35 enable); 35 create novel motif instances; 85 map to wild-card positions; 103 are in motif-flanking regions. Key-residue mutations are enriched for moderately-radical amino acid changes (Grantham score); motif-creating mutations also skew radical.

5. **Affinity validation at 87% concordance.** 24 wild-type/mutant peptide pairs binding 15 domains were validated by fluorescence polarisation (FP) displacement assay. 19 of 24 (79%) confirmed the phage-display direction; agreement rises to 87% when restricting to motif-key-residue mutations, matching the prior phosphomimetic ProP-PD benchmark.

6. **Cellular validation of selected interactions.** KEAP1 KELCH / SQSTM1 P348L: 25-fold loss of affinity confirmed by FP (K_D: 0.9 µM → 23 µM); co-IP confirms disruption in HeLa cells; mutation linked to frontotemporal dementia and ALS. KPNA4 ARM / CDC45 R157C: 400-fold loss (K_D: 0.09 µM → 7 µM major pocket); R157C is associated with Meier-Gorlin syndrome; cellular imaging shows CDC45 delocalises from nucleus to cytoplasm in R157C mutant cells, confirming loss of the NLS-importin interaction. MAP1LC3B ATG8 / BUB1 S492F: 4-fold gain (K_D: 7 µM → 1.6 µM); creates neo-interaction with autophagy machinery.

7. **Disease-category panorama.** Ion-channel mutations (SCNN1B, SCN9A, CACNA1H, KCND1, TRPC6) predominantly disrupt interactions with NEDD4 WW2 (E3 ubiquitin ligase) and ATG8 autophagy domains — suggesting altered channel turnover underlies neurological and cardiovascular phenotypes. Cancer-associated mutations (62 domain-mutation pairs) split 28 enabling / 34 disabling; cancer hotspots validated include CTNNB1 S33F (creates G3BP1 binding; simultaneously destroys β-TrCP degron), BRCA1 D695Y (creates novel FERM-binding site for MSN/RDX), and five PMS2/MUTYH/CTNNB1 hotspot mutations.

8. **Drug target assessment.** Most bait and prey proteins in mutation-modulated pairs are categorised as Tbio (well-studied but lacking approved drugs). Only Tchem: 11 bait domains + 20 prey proteins; Tclin: 5 bait + 5 prey. Of 62 cancer-associated pairs, 16 involve proteins with Chronos score < −0.5 (cancer-essential), and 10 of those have druggable bait or prey — including TLN1/TLN2 PTB-RET and BRCA1-ABRAXAS1/BRCA2 interactions.

## Limitations

- **Bait protein coverage is sparse.** Only 80 protein domains screened; the recall of SLiM-based interactions is estimated at ~20%. The map is a sample, not a census. Many disease-relevant IDR interactions are simply not covered.
- **Cellular validation of enabling mutations is harder than disabling.** Three enabling interactions tested by co-IP in HeLa/HEK293T could not be confirmed at full-protein level, likely because endogenous ligand competition is high. Disabling interactions are more readily validated.
- **IDR-only scope.** ~40% of disease-associated missense mutations map to structured domains, not IDRs; those mutations are not assayed here. The paper explicitly excludes SLiM-independent PPI mechanisms.
- **Mutation origin mix (somatic 82%, germline ~18%).** Somatic and germline mutations differ in evolutionary constraint and cellular context; mixing them in a single library without stratifying analyses limits mechanistic interpretation for specific diseases (relevant for channelopathy Track B diseases, which are predominantly germline).
- **Library age cutoff.** Mutations compiled as of December 2019; variants added to ClinVar/gnomAD since then are absent.
- **No disease-similarity scoring.** The paper maps mutations to disease categories post hoc but does not compute any disease-disease similarity; mapping to a disease-taxonomy framework requires external crosswalk.
