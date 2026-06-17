---
title: "Build a Multimodal AI App"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [multimodal, vision, claude, images]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a multimodal application using Claude's text + vision capabilities.

Application: [DESCRIBE: photo analysis app, document processor, visual Q&A, design feedback tool]

1. **File upload**: support images (JPEG, PNG, WebP, GIF) and PDFs
2. **Image preprocessing**: resize large images (< 5MB limit), convert format
3. **PDF handling**: extract pages as images for vision analysis
4. **Vision API call**: send image + text prompt to Claude
5. **Structured extraction**: extract structured data from images
6. **Multiple images**: compare multiple images in one prompt
7. **Conversation over image**: multi-turn conversation about uploaded image
8. **Caching**: cache analysis for same image hash
9. **Access control**: ensure users can only see their own uploaded images
10. **Usage tracking**: track image processing costs separately

Full-stack implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
