---
title: "Build an ETL Data Pipeline"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [etl, data-pipeline, airflow, python]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a production ETL data pipeline.

Sources: [DESCRIBE YOUR DATA SOURCES]
Destination: [DATA WAREHOUSE / LAKE / DATABASE]
Schedule: [HOURLY / DAILY / REAL-TIME]

Pipeline design:
1. **Extract**: connect to sources, handle authentication, pagination
2. **Transform**:
   - Schema normalization
   - Data type coercion
   - Business rules application
   - Deduplication
   - Validation
3. **Load**: upsert to destination, handle conflicts

Reliability:
4. **Idempotency**: safe to run multiple times
5. **Incremental loading**: only process new/changed records
6. **Checkpointing**: resume from failure point
7. **Alerting**: fail loudly with clear error messages

Orchestration (Apache Airflow):
8. DAG structure and dependencies
9. Retry policy
10. SLA monitoring
11. Backfill strategy

Output: Airflow DAG + Python transform functions.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
