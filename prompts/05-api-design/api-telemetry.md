---
title: "Add Distributed Tracing to APIs"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [tracing, opentelemetry, observability, api]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Add distributed tracing across my API services using OpenTelemetry.

Services: [LIST YOUR SERVICES AND THEIR STACK]

Implement:
1. OpenTelemetry SDK setup in each service (Node.js + Python examples)
2. Trace context propagation (W3C TraceContext headers)
3. Auto-instrumentation: HTTP, DB, Redis, message queues
4. Manual spans for business-critical operations
5. Trace attributes: user ID, request ID, customer tier
6. Sampling: 100% in dev, 10% in prod (head-based sampling)
7. Export to Jaeger (open source) or DataDog APM
8. Baggage: propagate tenant ID across service boundaries

Visualize: trace waterfall showing where time is spent.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
