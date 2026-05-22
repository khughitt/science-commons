---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Gravenmier2025
type: paper
title: Cell State Transitions Drive the Evolution of Disease Progression in B-Lymphoblastic Leukemia
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Gravenmier2025
tags: []
datasets: []
ontology_terms:
- B-ALL
- BCR::ABL1
- CD34+/CD38-
- Markov chain model
- adaptive therapy
- cancer stem cell
- cell state transitions
- dedifferentiation
- flow cytometry
- hematopoietic stem cell
- minimal residual disease
- plasticity
---
## Key Findings

### Molecular remission establishes the baseline
Patients in molecular remission show low CD34+/CD38− self-renewal (M11) and high outflow to CD34−/CD38− (mature B-cell compartment). This baseline reflects normal hematopoietic maturation and provides the comparison target for leukemic samples.

### BCR::ABL1 status predicts a stem-like self-renewal signature
BCR::ABL1-positive patients cluster with high M11 (CD34+/CD38− self-renewal) and high incoming rates from all other states (M21, M31, M41 — i.e., dedifferentiation from multiple compartments). BCR::ABL1-negative patients show two alternative patterns: either low M11 and high CD34+/CD38+ incoming rates (M12, M32, M42) or high CD34−/CD38+ incoming rates (M13, M23, M43). The PCA waterfall confirms M11 as the dominant axis distinguishing BCR::ABL1 status, with violin plots showing statistically significant separation (two-sample t-test, p < 0.05).

### CD34+/CD38− self-renewal predicts post-induction MRD
Higher M11 at diagnosis associates with MRD positivity post-induction chemotherapy. No significant association was found with 3-year relapse status, consistent with other literature reporting poor relapse prediction from immunophenotyping alone.

### Cell state kinetics are stable between diagnosis and relapse, but differ between diagnosis and remission
Paired diagnosis–relapse samples show no statistically significant differences across all 16 transition parameters, suggesting that relapse B-ALL does not simply re-select a distinct state-transition phenotype relative to diagnosis. In contrast, matched diagnosis–remission pairs show significant differences in transitions into compartments 1 (CD34+/CD38−) and 3 (CD34−/CD38+), confirming that remission samples genuinely differ in their cell state kinetics rather than reflecting mere bulk dilution of leukemic cells.

### Differentiation bias distinguishes remission from relapse
Across remission patients, the differentiation bias (q31 − q13 > 0 in the CTMC) is consistently positive, indicating net forward differentiation. Relapse patients frequently display negative differentiation bias (dedifferentiation dominates), with higher variance across the cohort.

### Simulated intervention: blocking dedifferentiation beats promoting differentiation
In the three-state CTMC intervention model:
- Both differentiation promotion (increasing q31 and q01 outflows from the stem compartment) and dedifferentiation inhibition (reducing q13 and q01 inflows to the stem compartment) reduce the steady-state CD34+/CD38− fraction.
- Dedifferentiation inhibition is more effective: it achieves a lower CD34+/CD38− steady state and does not suffer the transient rebound seen with differentiation promotion.
- Time-course simulations show that differentiation-promoting therapy initially reduces stem-like cells but the population rebounds as dedifferentiation continues to replenish the compartment. Dedifferentiation inhibition avoids this rebound.

### Non-hierarchical cell state architecture
Transition values were non-zero for all but one patient for all 16 possible transitions, indicating that any cell state can in principle access any other. This is contrary to a strictly hierarchical CSC model and supports a non-hierarchical architecture in which the CD34+/CD38− compartment is a quasi-stable attractor maintained by ongoing bidirectional transitions rather than a fixed apex of a developmental hierarchy.

### Code and data availability
All code and anonymised data are publicly available at https://github.com/MathOnco/Cell-State-Transitions-B-ALL.

## Limitations

- The Markov chain model assumes immunophenotypic quasi-steady state and memoryless transitions. Temporal variation in CD34 and CD38 expression within single cells (confirmed by time-lapse microscopy in prior work cited by the authors) means individual transition events may not be identically distributed — the model captures a population-level average, not single-cell kinetics.
- States are defined by two binary markers (CD34, CD38), which is a severe dimensionality reduction of a complex cellular landscape. Transcriptomically or epigenomically distinct subpopulations may be conflated within a single immunophenotypic gate.
- The model cannot distinguish transitions caused by differentiation/dedifferentiation from transitions caused by selective expansion or contraction of pre-existing subclones within a gate. Genomic barcoding or clonal tracking was not integrated.
- The paired diagnosis–relapse comparison is underpowered (N = 22 for matched pairs), limiting detection of transition rate changes that might accompany therapy-induced selection.
- The intervention simulations are purely mathematical (CTMC steady-state calculations); no in vitro or in vivo validation of the dedifferentiation-inhibition vs. differentiation-promotion comparison is presented.
- CD34 and CD38 expression are not stable markers under all conditions; they are not observed to increase under chemotherapy in this study (unlike AML), which the authors note may limit the ability to detect treatment-based selection on these markers.
- Model prediction of 3-year relapse was not significant, consistent with prior literature. This limits clinical utility for stratification beyond MRD prediction.
- Generalisation beyond B-ALL is proposed (any hematolymphoid malignancy with flow cytometry data) but not demonstrated.
