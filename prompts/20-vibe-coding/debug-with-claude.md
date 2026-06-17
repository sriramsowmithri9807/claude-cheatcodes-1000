---
title: "Use Claude as Your Pair Programmer"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [claude, pair-programming, vibe-coding, debugging]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Use Claude effectively as your AI pair programmer.

Current coding challenge: [DESCRIBE WHAT YOU'RE BUILDING OR STUCK ON]

Best prompts for different situations:

**When starting a feature**:
'I'm building [FEATURE] in [STACK]. What's the best approach? Show me the implementation.'

**When stuck on a bug**:
'Here's my code: [CODE]. Here's the error: [ERROR]. What's wrong and how do I fix it?'

**When you want a code review**:
'Review this code for bugs, performance, and best practices: [CODE]'

**When you need to understand code**:
'Explain this code line by line: [CODE]'

**When building step by step**:
'I'm building [PROJECT]. So far I have: [CODE]. Next I need to add [FEATURE]. How?'

**Tips for better results with Claude**:
1. Share ALL relevant context (stack, framework versions, constraints)
2. Share the actual error message (not 'it doesn't work')
3. Tell Claude what you've already tried
4. Ask for explanations, not just code
5. Iterate: 'That worked but now I have this problem...'

Apply to my current challenge.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
