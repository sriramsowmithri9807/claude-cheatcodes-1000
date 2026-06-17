---
title: "Implement Background Tasks in Node.js"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [background-tasks, workers, nodejs, performance]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement efficient background task processing in Node.js.

Tasks to offload: [LIST: email sending / image processing / report generation / etc.]

Without a queue (for simple cases):
1. `setImmediate()` for CPU tasks
2. `process.nextTick()` — when and when NOT to use
3. Worker threads for CPU-intensive work
4. `child_process.fork()` for isolation

With a queue (BullMQ for production):
1. Queue definition and job types
2. Worker implementation with concurrency
3. Job priorities
4. Error handling + retry
5. Job events (progress, completed, failed)
6. Clean up completed jobs

When to use queue vs worker thread vs async — decision matrix.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
