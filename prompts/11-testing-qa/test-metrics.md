---
title: "Track and Improve Test Quality Metrics"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [metrics, testing, quality, ci-cd]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Track and improve test quality metrics for my project.

Metrics to track:
1. **Coverage**: line, branch, function coverage trends
2. **Test duration**: total suite time, slowest tests
3. **Flakiness rate**: % of tests that fail intermittently
4. **Test failure rate**: % of CI runs that fail due to tests
5. **Defect escape rate**: bugs found in production vs in tests
6. **MTTR**: how long to fix a broken test suite

Implement:
7. Coverage report → PR comment (threshold check)
8. Slow test detection: flag tests > 1 second
9. Flaky test detection: track tests that pass/fail on retry
10. Test report: HTML report in CI artifacts

Dashboard:
- Grafana: coverage over time, flakiness trend
- GitHub Actions: test result annotations

Output: GitHub Actions workflow for all metrics.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
