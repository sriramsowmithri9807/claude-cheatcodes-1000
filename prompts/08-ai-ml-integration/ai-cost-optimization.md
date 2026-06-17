---
title: "Optimize AI API Costs"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cost, optimization, claude, tokens]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Optimize my Claude API usage costs without sacrificing quality.

Current usage: [DESCRIBE: how many calls/day, average tokens, which models]
Current monthly cost: [ESTIMATE]

Optimization strategies:
1. **Prompt caching**: cache shared system prompts (90% token discount)
2. **Model routing**: use Haiku for simple tasks, Sonnet for medium, Opus for complex
3. **Input compression**: remove unnecessary whitespace, abbreviate where safe
4. **Output length control**: `max_tokens` limits runaway outputs
5. **Batching**: batch API for non-real-time use cases (50% discount)
6. **Caching responses**: cache Claude responses for identical inputs (Redis)
7. **Streaming**: stream to user (doesn't affect cost, but better UX)
8. **Avoid retries on same prompt**: use exponential backoff for errors only
9. **Pre-computation**: generate and cache content in advance
10. **Monitor**: track cost per user, per feature, alert on anomalies

Target: 50% cost reduction. Show the math.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
