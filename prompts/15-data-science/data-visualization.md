---
title: "Create Data Visualizations"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [visualization, matplotlib, plotly, python]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Create professional data visualizations.

Data to visualize: [DESCRIBE YOUR DATA]
Audience: [TECHNICAL / BUSINESS STAKEHOLDERS]
Visualization goals: [WHAT STORY DO YOU WANT TO TELL]

Visualization types with code:
1. **Line chart**: trends over time
2. **Bar chart**: compare categories (horizontal for long labels)
3. **Scatter plot**: correlation between two variables
4. **Histogram**: distribution of one variable
5. **Box plot**: distribution with outliers
6. **Heatmap**: correlation matrix, confusion matrix
7. **Sankey diagram**: flow between states
8. **Geospatial**: choropleth map with plotly
9. **Dashboard**: Plotly Dash or Streamlit interactive dashboard
10. **Animation**: animated chart showing change over time

Design principles:
11. Less is more: remove chart junk
12. Color: meaningful, accessible palette
13. Annotations: highlight key insights
14. Titles: answer the question, not just label the axes

Using: Plotly Express + Matplotlib.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
