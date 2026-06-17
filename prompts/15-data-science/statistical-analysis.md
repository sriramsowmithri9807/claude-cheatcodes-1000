---
title: "Perform Statistical Analysis"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [statistics, scipy, hypothesis-testing, python]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Perform rigorous statistical analysis.

Data: [DESCRIBE YOUR DATA]
Question: [WHAT STATISTICAL QUESTION ARE YOU ASKING]

**Descriptive statistics**:
1. Central tendency: mean, median, mode
2. Spread: variance, std, IQR, range
3. Shape: skewness, kurtosis
4. Confidence intervals for each statistic

**Hypothesis testing**:
5. Choose the right test:
   - t-test: compare two means
   - ANOVA: compare multiple means
   - Chi-squared: categorical association
   - Wilcoxon: non-parametric alternative
6. Check assumptions before running test
7. Interpret p-value correctly (not binary threshold)
8. Report effect size (not just p-value)
9. Statistical power: did you have enough data?

**Common analyses**:
10. A/B test analysis with confidence intervals
11. Correlation analysis with significance testing
12. Regression analysis with diagnostics

Output: analysis notebook with interpretation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
