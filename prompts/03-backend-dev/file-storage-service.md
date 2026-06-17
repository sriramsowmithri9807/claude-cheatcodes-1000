---
title: "Build a File Storage Service"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [s3, storage, uploads, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a file storage service supporting uploads, downloads, and transformations.

Storage backend: AWS S3 (or Cloudflare R2 — S3-compatible, free egress)

API endpoints:
- POST /upload → presigned URL (client uploads directly)
- GET /download/:fileId → presigned download URL
- DELETE /files/:fileId → delete from S3 + database
- GET /files → list user's files with pagination

Features:
1. Virus scan integration (ClamAV or CloudScan)
2. File type validation (magic bytes, not just extension)
3. Image resizing on upload (Sharp)
4. Quota management per user
5. Signed URLs with expiry
6. CDN delivery
7. Resumable uploads for large files (S3 multipart)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
