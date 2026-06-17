---
title: "Build an AI Content Generation Pipeline"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [content, generation, claude, automation]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build an automated content generation pipeline using Claude.

Content type: [DESCRIBE: blog posts, product descriptions, social media, emails]
Input: [DESCRIBE: product data, topics list, customer segment]
Output: [DESCRIBE DESIRED FORMAT]

Pipeline:
1. **Input processing**: parse and validate input data
2. **Prompt construction**: dynamic prompt with input variables
3. **Parallel generation**: generate N pieces of content concurrently
4. **Quality filtering**: Claude self-evaluates each piece, reject below threshold
5. **Human review queue**: flag borderline content for review
6. **Post-processing**: format, add metadata, validate output schema
7. **Storage**: save to CMS or database
8. **Rate limiting**: respect Claude API rate limits
9. **Cost tracking**: track tokens and cost per run
10. **Monitoring**: alert on high rejection rates

Node.js implementation with BullMQ for queuing.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
