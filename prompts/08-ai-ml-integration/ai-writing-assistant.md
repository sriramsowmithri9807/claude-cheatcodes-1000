---
title: "Build an AI Writing Assistant"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [writing, assistant, claude, nlp]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build an AI writing assistant for [DESCRIBE YOUR PLATFORM: blog, email, code comments, etc.].

Features:
1. **Grammar correction**: fix errors while preserving voice
2. **Tone adjustment**: rewrite as formal, casual, professional, friendly
3. **Expansion**: make this paragraph longer with more detail
4. **Condensation**: make this shorter, get to the point
5. **Subject line generation**: given email body, generate 5 subject options
6. **Headline generation**: SEO-optimized headlines for blog posts
7. **Completion**: continue writing from where user stopped
8. **Rephrasing**: say this differently (offer 3 options)
9. **Plagiarism check** (heuristic): flag if output looks copied
10. **Brand voice**: learn brand guidelines, apply to all rewrites

React integration with selection-based actions (like Notion AI).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
