---
title: "Build AI Content Moderation"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [moderation, safety, claude, content]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build an AI content moderation system using Claude.

Content types to moderate: [DESCRIBE: text posts, images, user bios, comments]
Violation categories: [SPAM / HATE / ADULT / VIOLENCE / OTHER]

1. **Text moderation**: classify content by violation type
2. **Severity scoring**: 0-1 score for each category
3. **Action triggers**: auto-remove (high severity) vs human review (medium) vs allow (low)
4. **Context awareness**: same text may be ok in one community, not another
5. **Appeal system**: users can appeal, human reviews with AI suggestion
6. **Consistency**: same content → same decision (deterministic where possible)
7. **Adversarial inputs**: detect attempts to bypass moderation
8. **Performance**: < 100ms for text moderation (use Haiku)
9. **Audit log**: every decision logged with reasoning
10. **Calibration**: track false positive rate, adjust thresholds
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
