---
title: "Build a ChatGPT-Style Chatbot UI"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ai, chat, react, streaming]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a beautiful ChatGPT-style chatbot UI that connects to an AI API.

Features:
- Message thread with user/assistant bubbles
- Streaming response (character by character using SSE/ReadableStream)
- Markdown rendering in assistant messages (code blocks, lists, bold)
- Code block with syntax highlighting + copy button
- Auto-scroll to latest message
- Stop generation button
- Conversation history sidebar
- New chat button
- Model selector dropdown
- Message timestamps
- Regenerate response button

Tech: React + TypeScript. API: Claude API or OpenAI compatible.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
