---
title: "Build an Analytics Dashboard"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [analytics, charts, react, fullstack]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a web analytics dashboard (like a lightweight Plausible or Fathom).

Stack: Next.js + ClickHouse (time-series DB) + React

Metrics to track:
1. Pageviews, unique visitors, sessions
2. Traffic sources (direct, search, social, referral)
3. Top pages by views
4. Countries and cities
5. Devices (desktop/mobile/tablet), browsers, OS
6. Bounce rate, session duration
7. Goal conversions

Dashboard features:
- Date range picker (today, 7d, 30d, custom)
- Real-time visitors (WebSocket)
- Comparison to previous period
- Charts: line, bar, donut

Data collection: lightweight JS snippet (< 1KB, no cookies, GDPR-friendly)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
