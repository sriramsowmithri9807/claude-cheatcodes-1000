---
title: "Solve System Design Interview Questions"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [system-design, interviews, architecture, scalability]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Walk me through the system design for: [SYSTEM — e.g., design Twitter, design a URL shortener, design a rate limiter].

Approach this like a system design interview:

1. **Clarify requirements**:
   - Functional: what should the system do?
   - Non-functional: scale, latency, availability, consistency
   - Constraints: read-heavy or write-heavy? Geography? Budget?
2. **Capacity estimation**: users, storage, bandwidth, QPS
3. **High-level design**: draw the components and data flow
4. **API design**: key APIs the system exposes
5. **Data model**: schema for the main entities
6. **Deep dive**: one component in detail (the interesting part)
7. **Bottlenecks**: what breaks at scale? How to fix?
8. **Tradeoffs**: what did you sacrifice for what?

Drawn as ASCII architecture diagram.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
