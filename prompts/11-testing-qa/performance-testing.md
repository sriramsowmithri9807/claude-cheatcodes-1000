---
title: "Write Performance Tests"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [performance, load-testing, k6, artillery]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Write performance tests for my application.

Application: [DESCRIBE]
Performance goals:
- Throughput: [X] requests/second
- Latency: p95 < [X]ms
- Error rate: < [X]%

Using: k6

1. **Baseline test**: single user, measure baseline latency
2. **Load test**: ramp to target load, hold, ramp down
3. **Stress test**: exceed target load, find breaking point
4. **Spike test**: sudden load spike (traffic burst)
5. **Soak test**: sustained load for [N] hours (find memory leaks)

For each test:
- k6 script with realistic user scenarios (not just one endpoint)
- Assertions: fail if performance goals not met
- Metrics to capture
- Analysis: how to read the results

Integrate into CI: run nightly, alert on regression.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
