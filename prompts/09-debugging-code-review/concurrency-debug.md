---
title: "Debug Concurrency Issues"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [concurrency, async, race-conditions, debugging]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Debug concurrency issues in my application.

Code: [PASTE CODE]
Issue: [DESCRIBE: data inconsistency, duplicate processing, lost updates]
Environment: [SINGLE SERVER / MULTIPLE SERVERS / SERVERLESS]

1. **Identify shared state**: what data can be modified concurrently?
2. **Is this a real race or just looks like one?**
3. **Database-level fix**: `SELECT FOR UPDATE`, transactions, advisory locks
4. **Application-level fix**: distributed lock (Redis SETNX), queue, debounce
5. **Idempotency**: make the operation safe to run multiple times
6. **Optimistic locking**: version column + retry on conflict
7. **Testing**: how to write a test that reliably triggers the race
8. **Monitoring**: track and alert on conflict rate in production

Fix for my specific concurrency issue.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
