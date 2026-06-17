---
title: "Design a Time-Series Database"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [time-series, timescaledb, influxdb, iot]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a time-series data storage solution for: [DESCRIBE YOUR DATA: IoT sensors / metrics / financial ticks / events].

Option A — TimescaleDB (PostgreSQL extension):
1. Hypertable setup (auto-partition by time)
2. Chunk interval (1 hour vs 1 day vs 1 week)
3. Retention policy (drop data older than N months)
4. Compression (50-90% storage reduction)
5. Continuous aggregates (pre-compute hourly/daily summaries)
6. Time-series queries: time_bucket, lag, interpolation

Option B — InfluxDB:
7. Measurement, tags, fields design
8. Flux query language examples
9. Retention policies

For my use case: which is better and why?
Benchmark: expected query latency for 1B rows.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
