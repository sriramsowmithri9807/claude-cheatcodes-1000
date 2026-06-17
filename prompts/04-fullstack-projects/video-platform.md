---
title: "Build a Video Streaming Platform"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [video, streaming, fullstack, s3]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a YouTube-style video platform.

Stack: Next.js + Node.js + PostgreSQL + AWS S3 + CloudFront + FFmpeg

Features:
1. **Upload**: multipart upload to S3, show progress
2. **Processing**: FFmpeg transcoding (1080p, 720p, 480p HLS)
3. **Player**: HLS.js player with quality selector, playback speed, captions
4. **Thumbnails**: auto-generate at 25%, 50%, 75% + user-set custom thumbnail
5. **Metadata**: title, description, tags, category, visibility
6. **Engagement**: likes, comments, subscribe
7. **Recommendations**: related videos
8. **Search**: title + description full-text
9. **Analytics**: views, watch time, traffic sources (for creators)
10. **Monetization**: tip button or membership (Stripe)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
