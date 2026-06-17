---
title: "Evaluate and Compare ML Models"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [evaluation, machine-learning, metrics, python]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Evaluate and compare machine learning models rigorously.

Models to compare: [LIST YOUR CANDIDATE MODELS]
Problem type: [BINARY CLASSIFICATION / MULTI-CLASS / REGRESSION]

**For classification**:
1. **Accuracy**: misleading for imbalanced classes
2. **Precision, Recall, F1**: trade-off based on business need
3. **AUC-ROC**: discriminative ability (threshold-independent)
4. **PR-AUC**: better for imbalanced datasets
5. **Confusion matrix**: understand error types
6. **Calibration**: predicted probabilities vs actual (Platt scaling)

**For regression**:
7. **MAE**: robust to outliers
8. **RMSE**: penalizes large errors more
9. **MAPE**: relative error (interpretable as %)
10. **R²**: variance explained

**Statistical comparison**:
11. McNemar's test: are two classifiers significantly different?
12. Cross-validation variance: is one model more stable?
13. Learning curves: is model underfitting or overfitting?

Output: model comparison table + visualization.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
