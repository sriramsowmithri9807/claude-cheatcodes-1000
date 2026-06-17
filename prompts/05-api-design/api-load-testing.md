---
title: "Load Test Your API"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [load-testing, k6, performance, api]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design and run a comprehensive load test for my API.

API to test: [DESCRIBE YOUR API]
Performance targets: [e.g., 1000 RPS, p99 < 200ms, error rate < 0.1%]

Using: k6

1. Baseline test: 1 user, 30s — establish baseline latency
2. Load test: ramp to 1000 VUs over 5min, sustain 10min
3. Spike test: instant jump to 10x normal traffic
4. Stress test: find breaking point (keep increasing until failure)
5. Soak test: moderate load for 24h (find memory leaks)

For each test:
- k6 script with realistic scenarios (not just one endpoint)
- Metrics to capture
- Pass/fail thresholds
- Results interpretation

Output: k6 scripts + Grafana dashboard for results.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
