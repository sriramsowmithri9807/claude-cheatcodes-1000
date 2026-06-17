---
title: "Build a Production Chatbot"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [chatbot, claude, conversational-ai, nlp]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a production-grade AI chatbot powered by Claude.

Bot purpose: [DESCRIBE: customer support, internal knowledge base, onboarding]
Knowledge base: [DESCRIBE YOUR CONTENT]

1. **System prompt engineering**: persona, tone, capabilities, guardrails
2. **Context management**: conversation history with token budget
3. **RAG integration**: retrieve relevant knowledge base articles
4. **Intent classification**: route to specialized handlers (FAQ, human escalation)
5. **Guardrails**: refuse off-topic, harmful, or confidential-info requests
6. **Escalation**: hand off to human agent with conversation summary
7. **Multi-language**: detect language, respond in same language
8. **Feedback collection**: thumbs up/down → improve prompts
9. **Analytics**: most common questions, satisfaction score
10. **A/B testing**: compare different system prompts

React UI + Node.js backend with streaming.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
