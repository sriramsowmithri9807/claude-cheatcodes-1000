---
title: "Set Up Production Logging and Monitoring"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [logging, monitoring, opentelemetry, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up production-grade logging and monitoring for my Node.js app.

**Logging** (using pino — fastest Node.js logger):
1. Structured JSON logs with correlation IDs
2. Log levels: error, warn, info, debug
3. Redact sensitive fields (passwords, tokens, PII)
4. Request/response logging middleware
5. Error logging with stack traces
6. Log shipping to [ELK / Datadog / Grafana Loki]

**Metrics** (using OpenTelemetry):
1. HTTP request duration histogram
2. Custom business metrics (signups, payments)
3. Node.js runtime metrics (heap, CPU)
4. Prometheus endpoint for scraping

**Tracing**: distributed trace IDs across services

**Alerts**: define 5 critical alerts and their thresholds.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
