---
title: "Profile and Optimize Application Performance"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [profiling, performance, node-js, optimization]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Profile and optimize my application's performance.

Application: [DESCRIBE]
Performance goal: [e.g., reduce API response time from 2s to 200ms]

**Profiling in Node.js**:
1. `node --prof app.js` + `node --prof-process` → isolate output
2. Chrome DevTools CPU profiler via `--inspect`
3. `clinic.js`: `clinic doctor`, `clinic flame`, `clinic bubbleprof`
4. `autocannon`: HTTP load testing to identify bottlenecks under load

**Common optimizations I'll look for**:
5. Database queries (add indexes, reduce queries, add caching)
6. Synchronous code blocking the event loop
7. Expensive computation that can be cached or moved to worker thread
8. Unnecessary object creation in hot paths
9. Memory allocation patterns

After profiling MY code: specific fixes with before/after benchmarks.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
