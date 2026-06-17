---
title: "Set Up Centralized Log Aggregation"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [logging, elk, grafana-loki, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up centralized log aggregation for my distributed application.

Logs to aggregate from: [LIST SERVICES]

Option A — ELK Stack (self-hosted):
1. Elasticsearch: store and index logs
2. Logstash: parse and transform
3. Kibana: visualize and search
4. Filebeat / Fluentd: ship logs from each service
5. Index lifecycle policy: hot → warm → cold → delete

Option B — Grafana Loki (cheaper):
6. Loki: log aggregation without full-text indexing
7. Promtail: log shipper
8. Grafana: query with LogQL
9. Cost: 10x cheaper than ELK for most use cases

For both:
- Structured JSON logging from applications
- Log retention and archiving policy
- Alerting on error patterns
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
