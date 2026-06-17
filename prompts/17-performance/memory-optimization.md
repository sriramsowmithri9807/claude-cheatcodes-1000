---
title: "Optimize Memory Usage"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [memory, performance, node-js, optimization]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize memory usage in my application.

App: [DESCRIBE]
Symptoms: [MEMORY GROWTH, OOM CRASHES, HIGH RSS]

**Profiling Node.js**:
1. `process.memoryUsage()`: baseline RSS, heapUsed, external
2. `--inspect` + Chrome DevTools: heap snapshot comparison
3. `clinic.js bubble`: visualize memory over time
4. `heapdump`: capture heap snapshot

**Common memory leaks to fix**:
5. **Event listeners**: always call `removeEventListener`
6. **Closures**: check what's captured in long-lived closures
7. **Global variables**: accidentally accumulated in modules
8. **Cache without eviction**: LRU cache with max size
9. **Unresolved promises**: pending promises hold references
10. **Circular references**: prevent GC (in older V8)
11. **Timer references**: always call `clearInterval`

**Optimization techniques**:
12. Stream large files (don't buffer all in memory)
13. Worker threads: isolate memory-intensive work
14. Process limits: `--max-old-space-size=512`

Output: memory leak fixes for my specific case.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
