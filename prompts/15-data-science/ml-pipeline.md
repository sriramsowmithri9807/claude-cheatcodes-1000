---
title: "Build a Machine Learning Pipeline"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [machine-learning, scikit-learn, pipeline, python]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a production-ready machine learning pipeline.

Problem type: [CLASSIFICATION / REGRESSION / CLUSTERING]
Dataset: [DESCRIBE: size, features, target]
Success metric: [ACCURACY / AUC / RMSE / etc.]

Pipeline steps:
1. **Data loading**: from CSV/database/API
2. **Feature engineering**: create new features from raw data
3. **Preprocessing**:
   - Numeric: StandardScaler or MinMaxScaler
   - Categorical: OneHotEncoder or OrdinalEncoder
   - Missing values: SimpleImputer or IterativeImputer
4. **Model selection**: try 3-5 algorithms
5. **Cross-validation**: 5-fold CV for model evaluation
6. **Hyperparameter tuning**: RandomizedSearchCV or Optuna
7. **Model interpretation**: feature importance, SHAP values
8. **Evaluation**: confusion matrix, classification report
9. **Serialization**: joblib save/load
10. **Inference**: predict on new data

Using: scikit-learn Pipeline for reproducibility.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
