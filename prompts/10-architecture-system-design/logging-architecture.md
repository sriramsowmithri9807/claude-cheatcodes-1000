---
title: "Design a Logging Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [logging, architecture, elk, loki]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a centralized logging architecture for my distributed system.

Services: [LIST]
Log volume: [ESTIMATED GB/DAY]
Retention: [COMPLIANCE REQUIREMENTS]

Design:
1. **Log format**: structured JSON with standard fields (timestamp, level, service, trace_id, user_id)
2. **Log levels**: define what goes in each level across all services
3. **Shipping**: Fluentd or Vector (pull logs from stdout → ship to backend)
4. **Backend option A (ELK)**:
   - Elasticsearch: store and index (expensive)
   - Kibana: search and visualize
5. **Backend option B (Loki + Grafana)**:
   - Label-based (not full-text indexed → cheaper)
   - LogQL for queries
6. **Retention tiers**: hot (7d fast) → warm (30d medium) → cold (1y S3)
7. **Search**: full-text search vs label filter
8. **Alerting**: pattern-based alerts on error spikes
9. **Cost**: estimate $/GB for each option
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
