---
title: "Convert a Website to a PWA"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [pwa, service-worker, offline, mobile]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Convert my existing web app into a Progressive Web App (PWA).

[DESCRIBE YOUR CURRENT APP]

Implement:
1. Web App Manifest (`manifest.json`) with all required fields
2. Service Worker with: cache-first strategy, network-first for API calls, offline fallback page
3. App install prompt (beforeinstallprompt handling)
4. Push notifications setup (with permission flow)
5. Background sync for offline form submissions
6. Update notification when new version is available

Lighthouse PWA score target: 100.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
