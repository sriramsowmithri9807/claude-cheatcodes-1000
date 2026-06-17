---
title: "Build a Text Classification System"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [classification, nlp, claude, ml]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a text classification system using Claude.

Classification task: [DESCRIBE: sentiment analysis, topic classification, spam detection, intent recognition]
Labels: [LIST YOUR CATEGORIES]
Input volume: [EXPECTED VOLUME]

1. **Zero-shot classification**: no examples needed (Claude understands)
2. **Few-shot classification**: provide examples for better accuracy
3. **Multi-label classification**: a document can belong to multiple categories
4. **Hierarchical classification**: coarse → fine-grained classification
5. **Confidence scores**: estimate confidence, flag low-confidence for review
6. **Batch processing**: classify thousands efficiently with caching
7. **Evaluation**: measure accuracy against labeled test set
8. **Confusion matrix**: which categories does the model confuse?
9. **Cost optimization**: cache results, use Haiku for simple cases
10. **Fine-tuning alternative**: when to use Claude vs a fine-tuned smaller model

Python implementation with async batching.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
