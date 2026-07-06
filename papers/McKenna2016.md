---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:McKenna2016
kind: paper
title: Whole-organism lineage tracing by combinatorial and cumulative genome editing
version: 1.0.0
created: '2026-05-22'
updated: '2026-05-22'
bibkey: McKenna2016
tags: []
ontology_terms:
- CRISPR lineage tracing
- GESTALT
- barcode editing
- clonal dynamics
- combinatorial barcoding
- phylogenetic reconstruction
- zebrafish development
---
## Key Findings

### Data-derived findings (D)

- **Combinatorial barcode diversity.** HEK293T experiments generated 1,650 uniquely edited barcodes (≥25 reads); single 30 hpf zebrafish embryo yielded 1,323 distinct alleles; adult fish ADR1: 1,138 alleles; ADR2: 2,016 alleles; 72 hpf larva: up to 4,195 unique alleles from 31,639 cells. No saturation was reported at developmental timepoints tested.

- **Editing confined to early embryogenesis.** The majority of editing occurred before dome stage (4.3 hpf, ~12 synchronous cell divisions). Edits present in ~50% of cells were introduced at the two-cell stage; edits present in >10% of cells were introduced before the 16-cell stage. After dome stage, the proportion of edited sites remained relatively stable — confirming scar accumulation is temporally restricted to a narrow early window under transient Cas9 delivery.

- **Per-cell-division scar rate: not directly calibrated.** The paper does NOT report an explicit scar rate per cell division. It infers editing timing from clone frequency (edits in X% of cells → introduced at the N-cell stage) but does not express this as a rate per division. Maximum lineage depth experimentally probed: ~12 synchronous divisions (dome stage). [UNVERIFIED: whether any later divisions produced any new scars — the "stable proportion" observation suggests near-zero rate after dome stage under these delivery conditions.]

- **Clonal dominance in adult blood.** Only 5 alleles defined >98% of blood cells in adult fish, consistent with extreme clonal bottleneck in hematopoiesis. Across all organs, fewer than 7 alleles comprised >50% of cells (median 4, range 2–6); fewer than 25 alleles comprised >90% of cells except brain.

- **Organ-specific ancestral clades.** Ancestral clades reconstructed from shared early edits showed highly non-uniform contributions across organs: major clades contributed almost exclusively to mesendodermal or ectodermal lineages. Brain showed greatest clonal diversity.

- **Head-to-head diversity comparison.** In cell culture, 1,650 unique barcodes were generated from a single 10-target array — more combinatorial states than needed to tag all cells in a small organism individually. In zebrafish, the number of unique alleles observed (up to 4,195) was well below theoretical maximum, indicating the system was not saturated at sampled cell numbers.

### Author interpretations (L)

- **GESTALT is generically applicable beyond development.** Authors state the approach "is not limited to normal development but can also be applied to animal models of developmental disorders, as well as to investigate the origins and progression of cancer." No cancer data are shown. This is a forward-looking claim.

- **Scar accumulation encodes a faithful lineage record.** Authors interpret shared scar patterns as evidence of common ancestry; however, they acknowledge "chance recurrence of identical edits...can confound lineage inference" — the same edit can arise independently at the same target site (homoplasy). This limitation is stated but its quantitative magnitude is not modeled.

- **Non-uniform editing efficiencies are surmountable.** Authors note that "non-uniform editing efficiencies and inter-target deletions...contribute to suboptimal sequence diversity" but frame this as an engineering challenge rather than a fundamental barrier. No quantitative estimate of the diversity cost is provided.

- **The platform is scalable to organ-scale lineage tracing.** The authors argue the method can "scalably query lineage information from at least hundreds of thousands of cells with a single sequencing read per single cell." This scalability claim is correct for the read count but understates the computational and statistical challenges of phylogenetic reconstruction at that scale.

- **Transient Cas9 delivery restricts editing to early embryogenesis — but persistent delivery would enable later tracing.** This is implicit in the paper's framing of the limitation; the KP-Tracer solution (constitutive Cas9 under tumor-specific promoter) directly addresses this, but is not anticipated here.

## Limitations

1. **No per-division scar rate provided.** The paper estimates editing timing from clone frequency but does not report a scar rate per cell division. This is the key number for q057's resolution-floor analysis. [UNVERIFIED: rates from CARLIN (Bowling2020) or scGESTALT (Raj et al. 2018) may provide calibrated estimates under persistent Cas9.]

2. **Editing restricted to early embryogenesis under transient delivery.** Scar accumulation ceases after ~12 divisions (dome stage). For cancer applications requiring months-scale lineage tracing (as in KP-Tracer), persistent Cas9 expression is required — this limitation is acknowledged but not solved in this paper.

3. **Scar saturation not systematically characterized.** The point at which the 10-site array becomes fully scarred — and thus uninformative for later lineage events — is not quantified. Maximum observed diversity (4,195 unique alleles from 31,639 cells) implies no saturation at the timepoints tested, but long-term accumulation behavior is unstudied.

4. **Homoplasy (convergent editing).** Independent scarring of the same target at the same position can create false shared ancestry. The authors acknowledge this but do not quantify its frequency or model its effect on tree accuracy.

5. **No single-cell transcriptomics in this paper.** GESTALT barcodes are read by bulk amplicon sequencing. There is no cell-type or state information alongside the lineage barcode — a limitation directly solved by scGESTALT (Raj et al. 2018, pairing with scRNA-seq) and KP-Tracer.

6. **Non-cancer model.** Zebrafish normal development is the sole experimental system. Cancer is proposed as a future application but is not demonstrated.

7. **Lack of spatial information.** No anatomical position is recorded per cell. Spatial transcriptomics extensions of the GESTALT principle (e.g., SLIDE-seq + barcode) came later.
