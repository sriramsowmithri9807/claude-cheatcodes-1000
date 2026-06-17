---
title: "Design CDN and Edge Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cdn, edge, cloudflare, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a CDN and edge architecture for my application.

Application: [DESCRIBE: global users, content types, real-time requirements]

1. **Static asset delivery**: JS, CSS, images at edge (long TTL)
2. **Dynamic content caching**: API responses at edge (short TTL or bypass)
3. **Edge compute**: Cloudflare Workers or Lambda@Edge for logic
4. **Geo-routing**: serve from nearest POP
5. **Cache keys**: vary by: URL, cookie segment, accept-language
6. **Purging**: instant cache invalidation on content update
7. **Origin shielding**: protect origin from traffic spikes
8. **WAF**: block malicious traffic at edge
9. **DDoS protection**: absorb attacks at edge
10. **Analytics**: real user monitoring at edge

Cost optimization: what NOT to cache at CDN (saves money).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
