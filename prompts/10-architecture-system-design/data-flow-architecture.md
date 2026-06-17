---
title: "Design Data Flow Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [data-flow, pipelines, architecture, etl]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design the data flow architecture for my system.

Data sources: [LIST: user actions, external APIs, IoT devices, etc.]
Destinations: [OLTP database, analytics, ML training, CDN, search index]

Design:
1. **Ingestion**: how data enters the system (REST API, webhooks, batch upload, streaming)
2. **Validation**: schema check, business rules, deduplication
3. **Transformation**: normalize, enrich, join with reference data
4. **Storage routing**: which data goes where
5. **Stream processing**: real-time with Kafka Streams or Flink
6. **Batch processing**: nightly with Airflow or dbt
7. **CDC**: Change Data Capture (Debezium) for DB replication
8. **Backfilling**: re-process historical data
9. **Lineage**: track where each piece of data came from
10. **Monitoring**: data quality, freshness, volume anomalies

Diagram the full data flow.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
