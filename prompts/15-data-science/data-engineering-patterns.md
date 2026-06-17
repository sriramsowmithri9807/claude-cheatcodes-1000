---
title: "Apply Data Engineering Patterns"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [data-engineering, patterns, etl, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Apply data engineering patterns to my data platform.

Current situation: [DESCRIBE YOUR DATA INFRASTRUCTURE]

1. **Lambda Architecture**: batch (accurate) + speed (real-time) layers
2. **Kappa Architecture**: everything as stream (simpler)
3. **Data Lakehouse**: structured data in data lake (Delta Lake, Apache Iceberg)
4. **Medallion Architecture**: Bronze (raw) → Silver (clean) → Gold (aggregated)
5. **CDC (Change Data Capture)**: Debezium → Kafka → warehouse
6. **Slowly Changing Dimensions**: SCD Type 2 for historical accuracy
7. **Idempotent pipelines**: safe to rerun without side effects
8. **Data contracts**: schema agreements between producers and consumers
9. **Backfill strategy**: re-process historical data when logic changes
10. **Data catalog**: document all datasets with lineage

For my platform: which patterns to adopt in which order.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
