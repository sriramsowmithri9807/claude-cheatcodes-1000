---
title: "Build an Anomaly Detection System"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [anomaly-detection, machine-learning, monitoring, python]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build an anomaly detection system.

Data: [DESCRIBE: time series metrics / transaction data / sensor data]
What to detect: [DESCRIBE ANOMALIES: fraud, system failures, unusual behavior]

Methods:
1. **Statistical**: z-score, IQR for simple cases
2. **Isolation Forest**: tree-based, good for high-dimensional
3. **Autoencoder**: neural network, high reconstruction error = anomaly
4. **LSTM**: for sequential/time-series anomalies
5. **LOF (Local Outlier Factor)**: density-based
6. **Prophet**: anomalies vs seasonal forecast
7. **DBSCAN**: clustering-based outlier detection

For time series specifically:
8. Changepoint detection (ruptures library)
9. Seasonal decomposition → residual anomaly
10. Alert thresholds: dynamic vs static
11. Alert fatigue: tune to minimize false positives

Evaluation:
12. Label known anomalies, measure precision/recall
13. Tune threshold: precision-recall trade-off

Output: production anomaly detection pipeline.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
