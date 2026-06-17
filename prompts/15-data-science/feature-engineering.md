---
title: "Master Feature Engineering"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [feature-engineering, machine-learning, pandas, python]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Apply advanced feature engineering to my dataset.

Raw features: [DESCRIBE YOUR COLUMNS]
Target: [DESCRIBE WHAT YOU'RE PREDICTING]
Domain: [e.g., e-commerce, healthcare, finance]

Feature engineering techniques:
1. **Interaction features**: multiply/divide two features
2. **Polynomial features**: x^2, x^3 for non-linear relationships
3. **Binning**: convert continuous to bins (age groups)
4. **Log transform**: handle skewed distributions
5. **Ratios**: relative metrics (conversion rate, revenue per user)
6. **Lag features**: previous N timesteps (time-series)
7. **Rolling statistics**: 7-day rolling mean, max, std
8. **Target encoding**: encode categorical with target mean (careful of leakage)
9. **Embeddings**: text → dense vector features
10. **Clustering features**: cluster assignment as feature
11. **Domain features**: [SPECIFIC TO YOUR DOMAIN]

For each feature: why it might help + implementation + how to validate it improves model.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
