---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Koronowski2021
kind: paper
title: Communicating clocks shape circadian homeostasis
version: 1.0.0
created: '2026-05-30'
updated: '2026-05-30'
bibkey: Koronowski2021
tags: []
ontology_terms:
- SCN
- chronomedicine
- circadian-clock
- circadian-homeostasis
- circadian-misalignment
- clock-network
- inter-tissue-communication
- peripheral-clocks
---
## Key Findings

### Molecular oscillator and cell coupling
- The core CLOCK:BMAL1 / PER:CRY feedback loop generates ~24-hour periodicity; auxiliary loops (REV-ERB/ROR via ROR elements, DBP/TEF/HLF via D-boxes) contribute phased transcription across clock-controlled genes (CCGs).
- Individual dispersed neurons and fibroblasts show wide period and phase distributions; coupling (through gap junctions, paracrine signals, neurotransmitters) narrows these distributions and produces a more precise, robust population rhythm.
- SCN neurons form a self-perpetuating network whereas isolated peripheral tissue explants desynchronize over time, indicating lower intrinsic coupling strength.

### Coupling in the brain: neurons and astrocytes
- Astrocytes harbor autonomous clocks that operate in antiphase to neurons; glutamate released nocturnally from astrocytes entrains SCN neurons via NMDA receptors and CREB-mediated Per2 induction.
- The sleep-wake cycle adds a posttranslational circadian layer through rhythmic synaptic protein phosphorylation and accumulation.
- Connexin 43 hemichannels mediate astrocyte-neuron crosstalk; pharmacological blockade desynchronizes SCN slices.
- Olfactory bulb and cochlear clocks show sequential phase gradients along anatomical axes, illustrating tissue-level clock topology.

### Peripheral tissue clocks and systemic coupling
- Peripheral clocks (liver, pancreatic islets, skeletal muscle, adipose, immune cells, gut) can drive a small fraction (~10–20%) of local rhythms autonomously; the majority depend on central clock–derived or network-derived signals.
- Tissue-specific reconstitution of the clock in otherwise clockless mice demonstrates that peripheral clocks alone are insufficient for full circadian output — they rely on incoming centrally coordinated signals.
- Genetic reconstitution of the hepatic clock recovers only a subset of liver rhythms; muscle-derived serum factors and feeding-dependent signals are required to recover the remainder (consistent with Greco et al. 2021).
- Pancreatic islets: α, β, and δ cells secrete glucagon, insulin, and somatostatin in a phase-locked pattern; physical paracrine contact helps establish this phase relationship, which can be disrupted by high-fat diet.
- Single-nucleus RNA-seq of isolated liver cell populations shows clock disruption in hepatocytes alters molecular rhythms of neighboring endothelial and immune cells, suggesting direct intercellular clock programming.

### Systemic clock communication routes (Table 1 synthesized)
- **Neural**: SCN → hypothalamic nuclei (VMH, DMH, ARC) via neuropeptides; ANS efferents to peripheral tissues modulate sympathetic tone and clock phase; pituitary → endocrine organs.
- **Endocrine/humoral**: glucocorticoids, melatonin, vasopressin, thyroid hormone, insulin, glucagon, GLP-1, FGF21, angiopoietin-like proteins (ANGPTL8), IGF-1, leptin, adiponectin, ghrelin, oxyntomodulin — each acts on tissue-specific receptors and clock promoter elements.
- **Metabolic**: feeding-fasting cycle generates rhythmic nutrient flux, coupled energy/redox sensors (AMPK, SIRTs), CO₂, O₂ — these entrain clocks independently of the light-dark cycle.
- **Temperature**: 2–3°C daily body temperature fluctuation is sufficient to synchronize clock gene expression via HSF1-dependent transcription from Per2 heat-shock response elements.
- **mTOR signaling**: a convergence point for multiple input pathways; mTOR activation adjusts period and amplitude of peripheral clocks.
- **Direct cell-cell contact**: gap junctions (connexins), physical contact between islet α and β cells; pannexin and connexin channels debated as universal clock coupling in Drosophila (INX gap junctions control brain clock permeability).

### Peripheral-to-brain feedback
- The SCN is not merely a top-down commander; it receives inputs from the ARC, DMH, and other hypothalamic nuclei that relay metabolic feedback from peripheral clocks.
- Liver-specific deletion of Per2 abolishes food-anticipatory activity (FAA), demonstrating a peripherally derived circadian signal to the brain.
- Inverted extra-SCN feeding disrupts clock gene rhythms in the SCN itself, implicating peripheral metabolic feedback in fine-tuning central clock status.
- Peripheral clocks acting on distal tissues: liver-specific REV-ERBα/β disruption reprograms enhancers, transcripts, and metabolites of neighboring endothelial and Kupffer cells.

### Clock input-output architecture
- Loss of feeding rhythm, microbiota, or nonhepatic Bmal1 induces hundreds of de novo oscillating genes in the liver, suggesting inputs partially inhibit portions of the local output repertoire.
- Nuclear receptors (NRs) integrate clock signals with ligand fluctuations from extracellular sources; at least 4 sources of rhythmic information converge on NR function (cyclic ligand, NR protein oscillation, cooperative TF oscillation, protein interactions).
- BMAL1 chromatin binding is cell-autonomous, tissue-distinguishable by nucleosome state; complete temporal transcriptome control requires signals from the whole network.

### Circadian misalignment and disease
- Mice with SCN-specific Bmal1 deletion maintain peripheral clocks under light-dark conditions but desynchronize in constant darkness, linking internal coherence to external entrainment.
- Hepatocyte-specific Bmal1 deletion increases clock gene amplitude in muscle, suggesting compensatory cross-tissue coupling.
- Clock desynchrony is linked mechanistically to: obesity, impaired glucose utilization, cardiovascular disorders, neurological dysfunction, increased cancer risk.
- Restricted feeding (12-hour window) rescues weight, glucose, and liver gene expression in SCN-lesioned mice, showing that behavioral rhythms can restore metabolic homeostasis partly independent of the central pacemaker.
- Ten-hour time-restricted eating reduces weight, blood pressure, and atherogenic lipids in patients with metabolic syndrome (cites Wilkinson et al. 2020, Cell Metabolism).
- Shift workers and hospital nurses show internal desynchrony as a consequence of inverted work schedules, with tissue- and time-specific disruption profiles.

## Limitations

- Narrative review; no new empirical data. Mechanistic claims rest on the primary literature cited, which is mostly rodent-based (predominantly nocturnal C57BL/6 mice).
- The scope is primarily mammalian with limited discussion of how findings translate quantitatively to diurnal humans or human tissue heterogeneity.
- Table 1 contains multiple entries with "?" for unknown mediators or clock targets, reflecting genuine gaps in mechanistic understanding at time of publication.
- The "peripheral feedback to the brain" section acknowledges that how synchrony in peripheral tissues is established remains poorly understood.
- No quantitative modeling of coupling dynamics; the review is descriptive rather than predictive.
- Published February 2021; developments in spatial transcriptomics, single-cell multi-omics, and wearable-based circadian profiling since then would substantially expand the picture.
