---
title: "Implement Data Quality Monitoring"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [data-quality, great-expectations, monitoring, validation]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement data quality monitoring for my data pipeline.

Data: [DESCRIBE YOUR DATA AND PIPELINE]

Using: Great Expectations

1. **Expectation suites**: define what 'good data' looks like
2. **Column expectations**:
   - not null: critical columns always have values
   - unique: primary keys are unique
   - between: numeric values in valid range
   - in set: categorical values are valid options
   - regex: strings match expected format
3. **Distribution expectations**: mean within ±2σ of baseline
4. **Completeness**: row count within N% of yesterday
5. **Freshness**: latest timestamp within N hours

Pipeline integration:
6. Validate at ingestion (fail fast before processing)
7. Validate before loading to warehouse
8. Data docs: auto-generated HTML report
9. Alerting: Slack when expectations fail
10. Quarantine: move bad records aside, don't fail entire pipeline

Output: Great Expectations suite for my data.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
