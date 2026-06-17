---
title: "Design Distributed Tracing System"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [tracing, opentelemetry, observability, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a distributed tracing system for my microservices.

Services: [LIST YOUR SERVICES]
Languages: [NODE.JS / PYTHON / GO]

Design:
1. **Trace propagation**: W3C TraceContext headers across all services
2. **Instrumentation strategy**:
   - Auto-instrumentation: HTTP, DB, Redis, message queues
   - Manual spans: business-critical operations
3. **Sampling**: 100% dev, 10% prod, 100% for errors
4. **Span attributes**: tenant_id, user_id, feature_flag versions
5. **Context propagation**: through queues (special headers)
6. **Backend**: Jaeger (self-hosted) or Tempo (Grafana) or DataDog
7. **Correlation**: link trace_id to log lines and metrics
8. **SLO tracking**: trace-based SLI calculation
9. **Alerting**: trace-based anomaly detection
10. **Cost**: sampling to manage backend storage cost

OpenTelemetry SDK setup for Node.js.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
