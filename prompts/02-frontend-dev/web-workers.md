---
title: "Offload Heavy Work to Web Workers"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [web-workers, performance, javascript, concurrency]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Offload these CPU-intensive tasks to Web Workers:

Tasks: [DESCRIBE: image processing / data parsing / complex calculations / etc.]

Implement:
1. Worker setup with TypeScript (using Comlink for RPC-style API)
2. Main thread ↔ worker communication (with TypeScript types)
3. Transferable objects for large data (avoid copying)
4. Worker pool for parallel processing
5. Progress reporting from worker to main thread
6. Worker error handling and recovery
7. SharedArrayBuffer + Atomics for advanced use case
8. React integration: `useWorker` hook

Benchmark: show the before (main thread blocking) vs after.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
