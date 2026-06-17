---
title: "Build a Podcast Hosting Platform"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [podcast, audio, streaming, fullstack]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a podcast hosting and discovery platform.

Stack: Next.js + Node.js + S3 + PostgreSQL

Features:
1. Upload episodes: MP3/M4A, title, description, show notes, episode number
2. RSS feed generation (valid podcast RSS with all required tags)
3. Web player: custom HTML5 audio player with chapters support
4. Auto-submit to Apple Podcasts, Spotify (show RSS URL)
5. Transcription: auto-transcribe with Whisper API
6. Show notes: rich text editor with timestamps
7. Analytics: downloads per episode, listener geography (private feed tokens)
8. Embeddable player widget
9. Subscription: email list of listeners
10. Monetization: supporter donations (Stripe)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
