---
title: "Build a Complete Image Upload System"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [uploads, storage, react, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a complete image upload and management system.

Stack: [YOUR STACK]
Storage: S3 (or Cloudflare R2 / Supabase Storage)

Features:
1. **Frontend**: Drag-and-drop upload zone with progress bar
2. **Validation**: file type, size limit, dimension constraints
3. **Preview**: instant preview before upload
4. **Processing**: server-side resizing with Sharp (thumbnail, medium, full)
5. **Upload**: presigned S3 URL (client uploads directly to S3)
6. **Database**: store file metadata (URL, size, dimensions, user)
7. **CDN**: serve via CloudFront/CDN URL
8. **Deletion**: cleanup S3 when record is deleted

Include: TypeScript types, error states, and loading UX.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
