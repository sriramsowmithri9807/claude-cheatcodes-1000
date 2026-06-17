---
title: "Test AI-Powered Features"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, ai, llm, evaluation]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a testing strategy for AI-powered features.

AI feature to test: [DESCRIBE YOUR AI FEATURE]

Challenges with AI testing:
- Non-deterministic: same input → different output each time
- Hard to assert: what is a "correct" response?
- Expensive: can't run LLM calls in unit tests
- Prompt regression: changing prompt changes behavior unpredictably

Testing strategies:
1. **Mock Claude**: return canned responses in unit tests
2. **Eval datasets**: 100 input/expected-output pairs, run weekly
3. **LLM judge**: use Claude to evaluate Claude's own outputs
4. **Property tests**: test properties (length, format, tone) not exact text
5. **Regression testing**: compare new vs old prompt on same inputs
6. **Human evaluation**: periodic human review of 50 random outputs
7. **Red teaming**: adversarial inputs trying to break the system
8. **Latency testing**: measure p95 latency under load
9. **Cost regression**: alert if tokens per request increases 20%+
10. **Shadow mode**: run new prompt alongside old, compare before switching
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
