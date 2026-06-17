---
title: "Monitor Serverless Functions"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [serverless, monitoring, lambda, devops]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up monitoring for my serverless (Lambda/Vercel) functions.

Functions: [LIST YOUR FUNCTIONS AND THEIR IMPORTANCE]

Key metrics:
1. **Invocation count**: requests per minute per function
2. **Error rate**: 4xx, 5xx, unhandled exceptions
3. **Duration**: p50, p95, p99 cold starts vs warm starts
4. **Throttling**: when functions are throttled (capacity issue)
5. **Concurrent executions**: approaching account limit?
6. **Memory utilization**: right-size memory allocation

Alerting:
7. Error rate > 1%: Slack alert
8. Cold start > 2s: investigate provisioned concurrency
9. Duration > 25s (approaching 30s timeout): alert + optimize
10. Throttle rate > 0: alert + request limit increase

Dashboard: Lambda Insights or Lumigo or custom CloudWatch.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
