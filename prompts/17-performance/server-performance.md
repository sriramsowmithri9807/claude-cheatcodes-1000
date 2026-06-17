---
title: "Optimize Node.js Server Performance"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [node-js, performance, express, server]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize my Node.js server performance.

Server: Express.js / Fastify
Current performance: [DESCRIBE]
Target: [RPS, LATENCY]

**Event loop optimization**:
1. Avoid blocking: no sync filesystem, crypto, or parsing in request handlers
2. `setImmediate` vs `process.nextTick` — know the difference
3. Worker threads for CPU-intensive work
4. Async I/O: always use async versions of fs, crypto

**Fastify over Express** (2-5x faster):
5. JSON serialization with schemas (avoids JSON.stringify overhead)
6. Hooks: lifecycle hooks instead of middleware chain

**Clustering**:
7. `node:cluster` or PM2: use all CPU cores
8. N workers = N CPU cores

**HTTP optimizations**:
9. Keep-alive connections
10. Response compression: `compression` middleware
11. HTTP/2 push for critical assets

**Profiling tools**:
12. `clinic.js flame`: find CPU bottlenecks
13. `autocannon`: HTTP benchmark
14. `0x`: flame graph from Node.js

Output: performance optimizations for my server.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
