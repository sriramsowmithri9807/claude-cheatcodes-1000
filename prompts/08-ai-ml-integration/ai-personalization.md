---
title: "Build AI-Powered Personalization"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [personalization, recommendations, claude, ai]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build an AI personalization system for my platform.

Platform type: [E-COMMERCE / CONTENT / LEARNING / OTHER]
User data available: [DESCRIBE: behavior, preferences, demographics, history]

1. **User profile building**: summarize user interests from behavior
2. **Content recommendations**: find items matching user profile
3. **Collaborative filtering**: users similar to you also liked...
4. **Explanation**: "We recommend this because..."
5. **Diversity**: avoid filter bubble (mix familiar + new)
6. **Cold start**: new users with no history
7. **Contextual**: time of day, device, location adjustments
8. **Real-time**: recommendations update as user interacts
9. **A/B testing**: compare AI recommendations vs rule-based
10. **Feedback**: thumbs up/down to refine recommendations

Claude + embeddings for user/item matching.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
