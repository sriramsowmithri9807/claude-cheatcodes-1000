---
title: "Perform Exploratory Data Analysis"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [eda, pandas, data-science, python]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Perform exploratory data analysis on my dataset.

Dataset: [DESCRIBE YOUR DATA OR PASTE FIRST FEW ROWS]
Goal: [WHAT BUSINESS QUESTION ARE YOU TRYING TO ANSWER]

EDA steps:
1. **Shape**: rows, columns, memory usage
2. **Data types**: check dtypes, fix miscasts
3. **Missing values**: count per column, visualize with heatmap
4. **Distributions**: histograms for numeric, bar charts for categorical
5. **Outliers**: boxplots, IQR method, z-score detection
6. **Correlations**: correlation matrix heatmap
7. **Target analysis**: distribution of target variable
8. **Feature relationships**: scatter plots, grouped statistics
9. **Time trends**: if time-series, plot over time
10. **Summary statistics**: mean, median, std, min/max per column

Output: complete Jupyter notebook with all plots and insights.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
