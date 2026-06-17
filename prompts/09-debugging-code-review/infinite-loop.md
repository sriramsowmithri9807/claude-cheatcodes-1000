---
title: "Debug Infinite Loops and Hangs"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [debugging, loops, async, performance]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Debug an infinite loop or hang in my code.

Code: [PASTE CODE]
Symptoms: [DESCRIBE: CPU spikes, process hangs, browser freezes, async never resolves]

1. **Identify the type**:
   - Infinite loop: condition never becomes false
   - Infinite recursion: base case missing or never reached
   - Async deadlock: waiting for something that never resolves
   - Event loop blockage: synchronous code blocking Node.js
2. **Find the loop**: which loop/recursion is infinite?
3. **Check the termination condition**: what should make it stop?
4. **Off-by-one**: is the counter changing correctly?
5. **Mutation**: is the loop modifying the array it's iterating?
6. **Async**: is there a circular dependency in async resolution?
7. **Fix and verify**: add a maximum iteration guard as safety net
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
