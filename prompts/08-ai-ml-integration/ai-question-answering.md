---
title: "Build a Question Answering System"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [qa, claude, knowledge-base, rag]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a question answering system over my knowledge base.

Knowledge base: [DESCRIBE: documentation, FAQ, product manual, internal wiki]
User types: [DESCRIBE WHO WILL ASK QUESTIONS]

1. **Document indexing**: chunk and embed all documents
2. **Question understanding**: rephrase/expand question for better retrieval
3. **Context retrieval**: find most relevant document sections
4. **Answer generation**: Claude answers using ONLY retrieved context
5. **Citation**: cite which document/section the answer comes from
6. **"I don't know"**: Claude admits when answer isn't in the knowledge base
7. **Followup handling**: conversational Q&A with memory
8. **Confidence**: flag uncertain answers for human review
9. **Analytics**: most common questions → improve documentation
10. **Feedback loop**: thumbs up/down improves retrieval over time

Full-stack implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
