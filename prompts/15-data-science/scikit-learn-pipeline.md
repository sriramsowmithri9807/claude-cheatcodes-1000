---
title: "Build Scikit-Learn Pipelines"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [scikit-learn, pipeline, machine-learning, python]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build scikit-learn Pipelines for reproducible ML workflows.

Problem: [DESCRIBE YOUR ML TASK]
Features: [LIST YOUR FEATURE TYPES: numeric, categorical, text, dates]

Pipeline construction:
1. **ColumnTransformer**: different processing per feature type
2. **Numeric**: StandardScaler or RobustScaler
3. **Categorical**: OneHotEncoder or OrdinalEncoder
4. **Text**: TfidfVectorizer
5. **Missing**: SimpleImputer before transformers
6. **Estimator**: your chosen model at the end

Benefits:
7. **No data leakage**: fit only on training data
8. **Cross-validation**: Pipeline + cross_val_score
9. **Hyperparameter tuning**: GridSearchCV with pipeline params
10. **Serialization**: `joblib.dump(pipeline, 'model.pkl')`
11. **Inference**: `pipeline.predict(new_data)` handles all transforms

Output: complete Pipeline for my ML task.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
