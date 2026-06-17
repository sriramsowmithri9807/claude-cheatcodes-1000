---
title: "Monitor Your API in Production"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [monitoring, api, apm, observability]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up comprehensive monitoring for my production API.

Current setup: [DESCRIBE YOUR STACK]

Metrics to track:
1. **Availability**: uptime percentage (target: 99.9%)
2. **Latency**: p50, p95, p99 response times per endpoint
3. **Error rate**: 4xx and 5xx rates separately
4. **Throughput**: requests per second over time
5. **Saturation**: CPU, memory, DB connections

Alerting:
6. Error rate > 1% for 5 minutes → PagerDuty
7. p95 latency > 500ms → Slack
8. Uptime drops → immediate alert

Tools: Prometheus + Grafana (self-hosted) or DataDog (managed)

Output: dashboard JSON + alerting rules + runbook template.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
