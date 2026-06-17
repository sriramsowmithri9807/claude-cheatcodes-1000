---
title: "Build a Time Series Forecasting Model"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [time-series, forecasting, prophet, python]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a time series forecasting model.

Data: [DESCRIBE YOUR TIME SERIES: what you're measuring, frequency, history length]
Forecast horizon: [HOW FAR AHEAD TO PREDICT]
Metric: [MAPE / MAE / RMSE]

Approaches:
1. **Baseline**: seasonal naive, simple average
2. **Statistical**: ARIMA, SARIMA (statsmodels)
3. **Machine Learning**: LightGBM with lag features
4. **Deep Learning**: LSTM / Temporal Fusion Transformer
5. **Meta-learning**: Prophet (Facebook, good for business metrics with seasonality)

For Prophet:
6. Trend, seasonality (weekly, yearly)
7. Holiday effects
8. Changepoints
9. Forecasting and uncertainty intervals
10. Cross-validation with time-series split (no data leakage)

Evaluate:
11. Time-series cross-validation
12. Plot forecast vs actual
13. Error analysis: where does the model fail?
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
