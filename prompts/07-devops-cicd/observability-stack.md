---
title: "Build Full Observability Stack"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [observability, otel, metrics, tracing]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a complete observability stack (metrics + traces + logs).

Using: OpenTelemetry + Grafana Stack (LGTM: Loki, Grafana, Tempo, Mimir)

1. **OpenTelemetry SDK** setup in your services (Node.js + Python)
2. **Auto-instrumentation**: HTTP, DB, Redis, message queues
3. **Manual spans** for business operations
4. **Metrics**: counters, histograms, gauges exported to Prometheus
5. **Traces**: OTLP export to Tempo
6. **Logs**: structured JSON → Promtail → Loki
7. **Correlation**: link log lines to traces (trace_id in logs)
8. **Dashboards**: pre-built Grafana dashboards from grafana.com
9. **SLOs**: define and track Service Level Objectives
10. **Alerting**: Grafana unified alerting

Docker Compose for local + Helm charts for production.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
