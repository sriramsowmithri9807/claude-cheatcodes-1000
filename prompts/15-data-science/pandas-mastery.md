---
title: "Master Pandas Data Manipulation"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [pandas, data-manipulation, python, data-science]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Master pandas for data manipulation and analysis.

Dataset: [DESCRIBE YOUR DATAFRAME]
Task: [DESCRIBE WHAT YOU NEED TO DO WITH THE DATA]

Pandas techniques to apply:
1. **Filtering**: boolean indexing, query(), isin()
2. **Groupby**: groupby + agg with multiple functions
3. **Pivot tables**: pivot_table() for cross-tabulation
4. **Merge/Join**: merge() types (inner, left, outer)
5. **String operations**: .str accessor, regex extraction
6. **DateTime**: parse dates, resample, rolling windows
7. **Apply**: apply() vs vectorized operations (performance)
8. **Stack/Unstack**: reshaping wide to long and back
9. **Missing data**: fillna(), interpolate(), dropna()
10. **Window functions**: rolling(), expanding(), ewm()
11. **Categorical**: convert to Categorical for memory + performance
12. **Performance**: use numpy where possible, avoid iterrows

For each: show the correct pandas pattern + common mistakes.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
