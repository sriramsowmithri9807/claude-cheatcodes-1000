---
title: "Build a Transactional Email Service"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [email, sendgrid, nodejs, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a robust transactional email service.

Using: Resend (modern) or SendGrid

Emails to send: [LIST: welcome, password reset, invoice, notification, etc.]

Implement:
1. Email template system using React Email (beautiful HTML emails)
2. Template per email type with dynamic variables
3. Queue emails via BullMQ (don't send synchronously in API)
4. Retry logic for failed sends
5. Unsubscribe handling (one-click, per-category)
6. Email logging (track sent, delivered, bounced, opened)
7. Bounce handling webhook
8. Preview endpoint in development
9. Test mode (log to console instead of sending)
10. Rate limiting per recipient
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
