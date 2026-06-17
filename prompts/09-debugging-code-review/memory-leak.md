---
title: "Debug a Memory Leak"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [memory, debugging, node-js, performance]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Help me find and fix a memory leak in my Node.js application.

Symptoms: [DESCRIBE: heap growing over time, OOM crashes after N hours, memory never GC'd]
Code: [PASTE RELEVANT CODE — particularly long-lived objects, event listeners, caches]

1. **Common memory leak causes** in Node.js:
   - Event listeners not removed
   - Closures holding references
   - Global variables accumulating
   - Cache without eviction
   - Unresolved promises
   - Third-party library leaks
2. **Debugging tools**: heapdump, Chrome DevTools heap profiler, clinic.js
3. **Analysis**: compare heap snapshots — what's growing?
4. **Fix**: the specific fix for my code
5. **Prevention**: code patterns to avoid leaks

Provide heap snapshot analysis instructions + the fix.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
