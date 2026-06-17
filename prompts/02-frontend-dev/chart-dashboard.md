---
title: "Build a Charts and Analytics Dashboard"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react, charts, recharts, analytics]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a beautiful analytics dashboard with interactive charts.

Metrics to display: [LIST YOUR METRICS]
Library: Recharts (or Visx for more control)

Include:
1. Area chart for time series (with brushing for date range selection)
2. Bar chart for comparisons (horizontal and vertical)
3. Pie/Donut chart for distribution
4. Metric cards with trend indicators (↑↓)
5. Data table with sort for detailed view
6. Date range picker to filter all charts simultaneously
7. Responsive grid layout
8. Loading skeletons for each chart
9. Tooltip with formatted numbers
10. Color theme consistent with brand

Dark mode support included.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
