---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Sottoriva2015
type: paper
title: A Big Bang model of human colorectal tumor growth
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Sottoriva2015
tags: []
datasets:
- dataset:emtab-2140
- dataset:emtab-2247
- dataset:prjna230833
ontology_terms:
- Big Bang model
- VAF spectrum
- clonal dynamics
- colorectal cancer
- intratumor heterogeneity
- neutral evolution
- tumor growth model
---
## Key Findings

1. **Variegation in carcinomas, segregation in adenomas.** All 11 invasive carcinomas exhibited side-variegated and/or variegated private alterations (7/11 at the CNA level; 6/6 at the mutational level), whereas all 4 large adenomas showed only side-specific or unique private alterations — consistent with subclone mixing emerging at the adenoma→carcinoma transition rather than during preinvasive growth.
2. **High ITH within glands.** FISH analysis of HER2 in n = 65 tumour glands and n = 22 normal glands found uniformly high within-gland CN heterogeneity (Shannon index reaching the theoretical maximum of 1.79 in 99% of counts), implying no recent selective sweeps within glands and inconsistent with stepwise within-gland selection.
3. **Mutational-timeline inference.** By integrating gland-level CNA + mutation profiles into the ABC framework, the authors infer that for every assayed tumour, both public and the majority of private alterations (side-specific, side-variegated, variegated) occurred *early* — when the malignancy had fewer than 10⁵–10⁶ cells (Fig. 4b), 100–1000× smaller than detection threshold and ~10⁶× smaller than the surgical-resection size. Regional alterations occur later; unique alterations latest.
4. **Mutation rate inference.** Carcinomas had inferred mutation rates of 1×10⁻⁵ to 1×10⁻³ alterations per cell division, vs. ~1×10⁻⁶ in adenomas — quantitatively distinguishing the two.
5. **Subclone fitness changes are limited and not required.** Inferred subclone fitness differences are detectable but small in magnitude; the model recovers Big Bang dynamics robustly under microenvironment-aware extensions, indicating that *fitness* is not the dominant driver of the observed clonal architecture during the bulk expansion phase.
6. **"Born to be bad."** Some tumours show very early subclone mixing (early scattering events), implying that aggressive metastatic potential may be determined early rather than acquired through subsequent selective sweeps — a quantitative reformulation of the "born to be bad" hypothesis.

## Limitations

- **CRC-specificity acknowledged in paper.** Sottoriva et al. explicitly note: "Not every tumor may exhibit Big Bang dynamics, and 'selective bottlenecks' may be common for markedly different environments, such as in the context of metastatic seeding to foreign sites or during treatment." The model is positioned as describing primary CRC growth, not a universal cancer-evolution claim.
- **Sample size:** N = 15 tumours (4 adenomas + 11 carcinomas); 2 of these (adenoma S, carcinomas O and W) are MSI-H. Stage, treatment history, and MSI status are reported in Supplementary Table 1.
- **Static snapshot limitation:** Multi-region profiling at resection captures a single time point; the temporal dynamics that would distinguish Big Bang (early diversity, static thereafter) from ongoing neutral drift cannot be directly tested without longitudinal data.
- **Static microenvironment assumption:** The authors explicitly note that the model treats the microenvironment as a static spatial entity and does not allow tumour cells to dynamically alter the niche in late growth — a known simplification with implications for any inferences about late-arising clones.
- **Driver-mutation timing assumption:** The model classifies drivers as public (early) and infers private-alteration timing relative to tumour size; it cannot directly distinguish early selective sweeps before the bulk expansion from neutral founder fixation.
- **Known controversy — subsequently contested.** The 1/f neutral interpretation has been contested by Williams et al. 2018 (statistical-power critique) and by spatial-segregation findings in MSI-H CRC and other cancer contexts. These follow-on critiques are not part of this paper but should be read alongside it.
