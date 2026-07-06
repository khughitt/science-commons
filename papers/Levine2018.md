---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Levine2018
kind: paper
title: 'The Roles of Initiating Truncal Mutations in Human Cancers: The Order of Mutations and Tumor Cell Type Matters'
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Levine2018
tags: []
ontology_terms:
- branched evolution
- cancer initiation
- clonal evolution
- clonal hematopoiesis
- gatekeeper mutation
- inherited vs spontaneous mutation
- mutation order
- neoantigen
- tissue specificity
- truncal mutation
---
## Key Findings

**Mutation order is fixed and tissue-preferred**
- In CRC, the canonical sequence APC → KRAS → SMAD4 → TP53 is not merely observed but causally confirmed: reorganizing the order in organoids abrogates efficient tumor formation; SB mouse models reproduce the same rank ordering of survival times (Apc mutants die first, wild-type last).
- In Smad4-mutant GI tumors, APC is not the preferred WNT activator; R-spondin fusions (RSPO1/2) replace it, illustrating that a preexisting truncal mutation can rewire pathway preference for the next hit. In gastric tumors from the same mice, Rspo fusions are also disfavored; Lrp6 insertions occur instead — a further tissue-within-tissue specificity effect.
- In Trp53−/− thymic lymphoma, Pten deletion is clonally fixed before VDJ rearrangement; all clones within one mouse share the same Pten deletion, while different mice have different ones, proving Pten is selected as the second hit in a lineage-specific stem/progenitor cell before T cell commitment.

**Initiating truncal mutations in normal tissues are widespread**
- Sun-exposed normal eyelid skin contains NOTCH1 driver mutations in 18–32% of cells; the epithelium is a clonal patchwork.
- Normal esophageal epithelium from middle-aged donors shows clones with NOTCH1 mutations covering up to 80% of cells, and TP53 mutations in up to 37%, with no malignancy — truncal mutations are necessary but not sufficient without secondary hits.
- Clonal hematopoiesis increases from ~10% at age 60 to ~70% at age 80, driven by DNMT3A, TET2, TP53-pathway genes; these are pre-leukemic truncal states awaiting KRAS/NRAS/FLT3 as secondary hits for AML conversion.

**Inherited vs spontaneous mutations differ in tissue spectrum because of truncal fitness**
- TP53 germline mutations (Li-Fraumeni) produce 100–1,000× excess risk in ectodermal/mesodermal tissues but only 2–4× in endodermal tissues, because TP53 loss functions as a truncal initiating mutation in the former but not the latter.
- Li-Fraumeni breast cancers are ER+; population-level spontaneous TP53 mutations cluster in triple-negative breast cancer — same gene, opposite subtype, because the cellular context determines whether TP53 loss can serve a truncal survival-enhancing role.
- Retinoblastoma gene (RB1): initiating truncal role in retinal cells and osteoblasts only, even though spontaneous RB1 loss is found in many tumor types.

**Mutation order determines cancer identity even with the same driver set**
- In myeloproliferative neoplasms, JAK2-first versus TET2-first produces cancers with different gene expression in progenitors, different clonal dynamics, different clinical phenotype, and different optimal treatment — despite having the same two driver mutations in the end.

**Truncal mutations as neoantigen strategy for immunotherapy**
- Truncal mutations are present in every tumor cell; neoantigen vaccines or checkpoint combinations targeting truncal mutations should avoid the subclonal-escape problem.
- Algorithms predicting neoantigens from tumor DNA can already identify long-term survivors whose tumors presented clonally expanded T cell responses to truncal neoantigens (including TP53E191K examples from pancreatic cancer survivors).
- However, the paper raises the unresolved question of whether immune tolerance differs for inherited (germline) vs somatic truncal mutations.

**Non-commutative mathematics as a conceptual frame**
- The authors explicitly invoke matrix multiplication (non-commutativity, ab ≠ ba) as a formal analogy for why mutation order matters, suggesting this mathematical framework could in principle predict cancer phenotype or optimal drug combinations once mutation order is known.

## Limitations

- Perspective, not a primary study. All evidence is synthesized from prior work; no new data are generated.
- The non-commutative mathematics framing is metaphorical, not operational. No actual mathematical model, formal system, or predictive algorithm is provided; the analogy is evocative but does not yet generate testable quantitative predictions.
- The claim that "prior mutation selects for next mutation" is empirically supported by the examples discussed, but the mechanistic basis for most cases is not resolved (why does Smad4 loss redirect WNT activation from APC to RSPO? The paper acknowledges this is unclear).
- The paper focuses almost entirely on oncogene/tumor-suppressor point mutations and CNVs. It does not address structural variants, transposons, or epigenetic truncal initiating events in detail.
- Immune tolerance to inherited truncal mutations is raised as an open question but not addressed.
- The examples are heavily mouse-model-based (SB insertional mutagenesis, Trp53 knockouts); human validation of fixed mutation order beyond CRC is less complete.
- The paper does not quantify the fraction of cancers that follow ordered versus disordered mutation accumulation, leaving the generality of the claim unresolved.
