---
title: "Clean Messy Datasets"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [data-cleaning, pandas, etl, python]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Clean this messy dataset.

Dataset: [DESCRIBE THE MESS: missing values, duplicates, inconsistent formats, outliers]

Data cleaning steps:
1. **Duplicates**: find and remove (or flag) duplicate rows
2. **Missing values**:
   - Structural missingness: MCAR, MAR, MNAR analysis
   - Strategy: drop, fill with mean/median/mode, interpolate, or flag
3. **Inconsistent formats**:
   - Dates: standardize to ISO 8601
   - Categories: 'NY', 'New York', 'new york' → 'New York'
   - Phone numbers, addresses: standardize
4. **Outliers**: IQR method, isolation forest, visual inspection
5. **Type corrections**: strings that should be numbers, dates as strings
6. **Invalid values**: negative ages, future dates, impossible values
7. **Case normalization**: all lowercase for text comparisons
8. **Whitespace**: strip leading/trailing spaces
9. **Unicode**: normalize unicode characters
10. **Schema validation**: check all columns after cleaning

Output: cleaning script + before/after statistics.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
