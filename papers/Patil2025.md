---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Patil2025
type: paper
title: Preventing evolutionary rescue in cancer using two-strike therapy
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Patil2025
tags: []
datasets: []
ontology_terms:
- evolutionary rescue
- extinction therapy
- nadir timing
- stochastic extinction
- treatment scheduling
- two-strike therapy
---
## Key Findings

- The optimal switching population size is close to the nadir reached under the first treatment.
- When exact timing is uncertain, switching slightly after the nadir is often safer than switching too early because first-treatment selection can further reduce cells resistant to the second treatment.
- Two-strike therapy is most plausible for small residual tumors; under default assumptions, high extinction probability required switching at very small population sizes, and initial tumors above roughly `10^8` cells did not achieve high extinction probability in the modeled setting.
- High efficacy in both strikes maximizes the best-case extinction probability, but lower first-strike efficacy can widen the pre-nadir high-extinction window when resistance costs and preexisting second-drug resistance are substantial.
- Resistance cost, death rate, and turnover can improve extinction probability, but two-strike benefit is not completely contingent on resistance cost.
- Carrying capacity had limited influence for a given initial tumor size in the explored parameter range.
- The authors argue that conventional sequential therapy waits too long because it switches only after evident relapse, whereas two-strike therapy must act while disease is small or undetectable.

## Limitations

The model excludes toxicity, spatial structure, pharmacokinetics, immune effects, plastic resistance, lesion-level heterogeneity, and patient-specific measurement noise.
The authors intentionally focus on conditions where conventional single-strike therapy fails with high probability but residual disease may still be small enough for stochastic extinction.
The clinical feasibility of estimating nadir timing remains unresolved.
