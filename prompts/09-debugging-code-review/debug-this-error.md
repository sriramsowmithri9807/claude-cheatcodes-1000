---
title: "Debug Any Error Message"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [debugging, errors, troubleshooting]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
You are an expert debugger. I'm getting this error:

```
[PASTE ERROR MESSAGE + STACK TRACE]
```

Context:
- Language/framework: [e.g., Node.js 20, Express 4]
- What I was doing when it happened: [DESCRIBE]
- Relevant code: [PASTE THE RELEVANT CODE]

Please:
1. Explain exactly what this error means in plain English
2. Identify the root cause (not just the symptom)
3. Show me the fix with before/after code
4. Explain why the fix works
5. Tell me how to prevent this class of error in the future
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
