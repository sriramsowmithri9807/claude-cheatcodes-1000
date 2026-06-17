---
title: "Load Test Infrastructure"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [load-testing, k6, infrastructure, performance]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Load test my infrastructure to find the breaking point.

Infrastructure: [DESCRIBE: Nginx + App + DB]

Using: k6

Test scenarios:
1. **Smoke test**: 1 VU, 1 minute — verify test script works
2. **Load test**: ramp to [TARGET] RPS over 5 min, sustain 10 min
3. **Stress test**: keep increasing until failure — find capacity
4. **Spike test**: instant jump to 10x normal
5. **Soak test**: moderate load for 1-2 hours (memory leaks)

Metrics to collect:
- HTTP request rate, error rate, response times (p50/p95/p99)
- Server CPU, memory, network
- Database connections, query latency
- Redis hit rate

Results analysis: where did it break? What's the fix?
Output: complete k6 script for realistic user scenarios.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
