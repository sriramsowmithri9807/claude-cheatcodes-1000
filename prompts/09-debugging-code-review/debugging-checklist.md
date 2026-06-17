---
title: "Systematic Debugging Checklist"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [debugging, process, methodology, troubleshooting]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Walk me through systematic debugging for this problem:

Problem: [DESCRIBE THE BUG]
Expected behavior: [WHAT SHOULD HAPPEN]
Actual behavior: [WHAT IS HAPPENING]
Frequency: [ALWAYS / INTERMITTENTLY / RARELY]
Recent changes: [ANY DEPLOYMENTS OR CODE CHANGES]

Systematic debugging process:
1. **Reproduce**: confirm I can reproduce it consistently
2. **Isolate**: narrow down where the bug occurs (binary search the code)
3. **Understand**: trace the execution path, check assumptions
4. **Hypothesis**: form a specific hypothesis about the cause
5. **Test hypothesis**: make one change at a time
6. **Fix**: implement the fix
7. **Verify**: confirm the fix works and didn't break anything else
8. **Post-mortem**: why did this happen? How to prevent it?

Apply this process to my specific bug.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
