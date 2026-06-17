---
title: "Track ML Experiments with MLflow"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [mlflow, experiment-tracking, mlops, python]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up ML experiment tracking with MLflow.

ML workflow: [DESCRIBE YOUR MODEL TRAINING PROCESS]

1. **MLflow setup**: local tracking server or Databricks
2. **Experiment**: group of runs with the same goal
3. **Run**: single training run with params + metrics
4. **Log parameters**: hyperparameters for this run
5. **Log metrics**: training + validation metrics each epoch
6. **Log artifacts**: model file, plots, feature importance
7. **Log model**: versioned model with schema
8. **Tags**: run metadata (git commit, dataset version)

Best practices:
9. **Autologging**: `mlflow.sklearn.autolog()` for auto-tracking
10. **Model registry**: promote best model to staging → production
11. **Comparison**: compare metrics across runs in UI
12. **Reproducibility**: log data version, random seed, environment

Integrate with:
13. scikit-learn: autolog
14. PyTorch: log epoch metrics
15. Optuna: log hyperparameter search

Output: complete MLflow-instrumented training script.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
