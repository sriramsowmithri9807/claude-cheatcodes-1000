---
title: "Set Up Production Monitoring Stack"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [monitoring, prometheus, grafana, alerting]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up a complete production monitoring stack.

Stack: Prometheus + Grafana + Alertmanager

Using Docker Compose:
1. **Prometheus**: scrape config for your services + node exporter
2. **Grafana**: pre-configured datasource, provisioned dashboards
3. **Alertmanager**: route alerts to Slack/PagerDuty
4. **Node Exporter**: host-level metrics (CPU, memory, disk, network)
5. **cAdvisor**: Docker container metrics
6. **Blackbox Exporter**: HTTP endpoint monitoring (uptime)
7. **Application metrics**: your app exposes /metrics (Prometheus format)

Dashboards to create:
- System health (CPU, memory, disk)
- Application (request rate, error rate, latency)
- Business metrics (signups, revenue, active users)

Alerts: list the 10 most important alerts with thresholds.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
