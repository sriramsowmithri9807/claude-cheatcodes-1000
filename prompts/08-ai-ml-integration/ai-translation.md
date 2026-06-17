---
title: "Build AI-Powered Translation"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [translation, multilingual, claude, nlp]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Add AI-powered translation and localization to my app.

Use case: [DESCRIBE: user content, UI strings, documents, real-time chat]
Language pairs: [SOURCE → TARGET LANGUAGES]

1. **Basic translation**: Claude translates between any language pair
2. **Context-aware**: provide surrounding context for better translation
3. **Tone preservation**: formal vs informal, brand voice
4. **Domain-specific**: legal, medical, technical — use domain vocabulary
5. **Glossary**: maintain consistent translation of key terms
6. **Transliteration**: romanize scripts (Arabic, Chinese, etc.)
7. **Back-translation**: verify quality by translating back
8. **Streaming**: stream translation for real-time feel
9. **Caching**: cache translations to reduce API calls
10. **Quality evaluation**: BLEU score approximation

Integrate with i18next for UI string management.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
