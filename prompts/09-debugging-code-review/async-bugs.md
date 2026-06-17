---
title: "Debug Async/Await Problems"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [async, debugging, promises, node-js]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Debug these async/await problems in my code:

```javascript
[PASTE YOUR ASYNC CODE]
```

Errors/symptoms: [DESCRIBE: unhandled rejections, race conditions, sequential when should be parallel, deadlock]

Check for:
1. Missing `await` — sync when should be async
2. `await` in loops — sequential when could be `Promise.all()`
3. Unhandled promise rejections
4. Race conditions — two async ops modifying same state
5. Error swallowing — catch block does nothing
6. Promise constructor antipattern
7. async function returning a value that isn't awaited by caller
8. Finally block issues

Fix all issues and explain each one.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
