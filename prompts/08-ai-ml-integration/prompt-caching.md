---
title: "Implement Claude Prompt Caching"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [caching, claude, optimization, tokens]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement Claude's prompt caching feature to reduce costs and latency.

Use cases with large system prompts or repeated context: [DESCRIBE]

1. **What gets cached**: system prompt + any content before the last user message
2. **Cache breakpoint**: mark where to cache with `cache_control: {type: 'ephemeral'}`
3. **Cache window**: 5 minutes (extended with usage)
4. **Cost**: input tokens 90% cheaper when served from cache
5. **Latency**: cached tokens skip processing (faster TTFT)
6. **Pattern 1**: long system prompt with instructions + knowledge
7. **Pattern 2**: many-shot examples prepended to every request
8. **Pattern 3**: entire document as context for Q&A
9. **Measuring**: cache hits in API response headers
10. **Multi-turn**: cache grows as conversation continues

Calculate ROI: cost savings for your specific usage pattern.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
