---
schema_profile: science-entity-base/1.0+paper/2.0
id: paper:Islam2024
type: paper
title: Fusing global context with multiscale context for enhanced breast cancer classification
version: "1.0.0"
created: "2026-05-22"
updated: "2026-05-22"
bibkey: Islam2024
tags: []
authors:
- Islam et al.
datasets:
- dataset:breakhis
doi: 10.1038/s41598-024-78363-w
ontology_terms: []
venue: Scientific Reports
year: 2024
---
## Key Findings

1. **Full fusion achieves near-perfect classification.** The fused model reaches 100% accuracy (precision, recall, F1, MCC all 1.0) on 100X and 400X magnification levels. At 40X: accuracy 0.9925, F1 0.9916, MCC 0.9834. At 200X: accuracy 0.9826, F1 0.9792, MCC 0.9585 (Table 6).

2. **Global stream outperforms multiscale stream alone.** ViT-based global stream: accuracy 0.9474/0.9209/0.9007/0.9313 across 40X-400X. Custom ASPP multiscale stream: 0.9198/0.6259/0.9007/0.8709 — notably poor at 100X (accuracy 0.6259, MCC 0.4194), indicating ASPP alone cannot handle all scales robustly. Fusion resolves this failure mode.

3. **Preprocessing contributes ~1-1.3% accuracy gain.** Ablation removing each preprocessing stage shows image denoising +1.29%, contrast enhancement +1.22%, unsharp masking +1.118% average accuracy improvement; largest impact at 400X magnification.

4. **Outperforms the majority of published BreakHis baselines.** Comparison against 11 prior methods (Table 7): the fusion model equals or exceeds all baselines at 40X (99.25%), 100X (100%), 400X (100%), and is competitive at 200X (98.26%). Notably beats DenseNet201+VGG1+ViT (Ukwuoma et al.) which achieved 100% only at 400X. Prior CNN-only methods typically achieve 87-99% depending on magnification.

5. **ROC AUC = 1.0 at 40X, 100X, 400X; 0.97 at 200X.** Micro-average AUC is perfect except at 200X (the magnification with most misclassifications: 5 benign as malignant, 2 malignant as benign in confusion matrix).

6. **Grad-CAM shows attention focused on diagnostically relevant structural regions** (glandular/ductal tissue architecture at 40X), suggesting the model's global self-attention mechanism is tracking tissue-level organization rather than noise artifacts.

## Limitations

- **No validation set, no data augmentation:** The 80/20 split without a held-out validation set means hyperparameter decisions were effectively made on the test set implicitly. No data augmentation is used despite class imbalance (~2.2:1); MCC is reported to partially address this.
- **No hyperparameter ablation:** The paper explicitly flags that hyperparameter impact is unknown (number of epochs, dropout rates, dilation rates, etc.). Reported 100% accuracy should be interpreted cautiously given these design choices.
- **BreakHis only:** All experiments are on a single dataset from one laboratory; generalization to other histopathology sources or staining protocols is not demonstrated.
- **Heavy compute:** Training exceeds 6 hours on GPU P100. The two-stream architecture is large and resource-intensive, limiting clinical deployment.
- **No transfer learning in the ASPP stream:** ViT is ImageNet-pretrained, but the ASPP multiscale stream is trained from scratch, which likely explains its instability at 100X.
- **Reported 100% accuracy is almost certainly an artifact of the limited test set and absence of a proper validation/test split protocol.** The BreakHis test set at 100X contains only ~416 images (20% of 2,081); achieving 100% on this is not the same as 100% error-free classification in deployment.
