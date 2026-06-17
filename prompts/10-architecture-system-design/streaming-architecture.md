---
title: "Design a Real-Time Streaming Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [streaming, kafka, flink, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a real-time data streaming architecture.

Data types and volume: [DESCRIBE]
Latency requirement: [e.g., < 1 second end-to-end]
Use case: [DESCRIBE: live dashboard, fraud detection, IoT, recommendation]

Architecture:
1. **Ingestion**: Kafka (partitioned by key for ordering + parallelism)
2. **Stream processing**: Kafka Streams or Apache Flink
   - Filtering, transformation, aggregation
   - Windowing: tumbling, sliding, session windows
   - State management (count, sum, average)
3. **Serving layer**: Redis for materialized views (sub-ms reads)
4. **Batch reconciliation**: nightly batch corrects any streaming errors
5. **Replay**: reprocess stream from beginning
6. **Schema evolution**: Avro + schema registry
7. **Exactly-once**: Kafka transactions for strong consistency

Latency budget: where does the time go in the pipeline?
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
