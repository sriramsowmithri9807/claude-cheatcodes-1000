---
title: "Identify and Fix Race Conditions"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [concurrency, race-conditions, async, debugging]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Identify and fix race conditions in this concurrent code:

```[LANGUAGE]
[PASTE CODE]
```

Symptoms: [DESCRIBE: inconsistent state, different results on each run, intermittent failures]

1. **Identify the shared state**: what data is accessed by concurrent operations?
2. **Identify the race window**: where can the interleaving cause issues?
3. **Reproduce**: minimal test case to trigger the race
4. **Fix options**:
   - Mutex/lock: serialize access
   - Atomic operations: use atomic compare-and-swap
   - Immutable data: avoid shared mutable state
   - Actor model: single writer
   - Database transactions: SERIALIZABLE isolation
5. **Verify**: test that proves the fix eliminates the race

For Node.js: remember — single-threaded, but async can still race.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
