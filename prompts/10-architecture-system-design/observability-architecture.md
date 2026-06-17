---
title: "Design Observability Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [observability, monitoring, architecture, telemetry]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a comprehensive observability architecture for my system.

System: [DESCRIBE YOUR SERVICES AND INFRASTRUCTURE]

Three pillars:

**Metrics** (Prometheus + Grafana):
1. Infrastructure: CPU, memory, disk, network
2. Application: request rate, error rate, latency
3. Business: signups, revenue, active users
4. SLIs and SLOs: define and track service levels

**Logs** (Loki or ELK):
5. Structured JSON logging from all services
6. Correlation IDs linking related log entries
7. Log-based alerting for error patterns

**Traces** (Tempo or Jaeger):
8. End-to-end request tracing
9. Service dependency map
10. Latency breakdown per component

Platform: Grafana LGTM stack (all open source)
Alerts: define on-call playbook for each alert
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
