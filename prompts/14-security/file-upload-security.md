---
title: "Secure File Uploads"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [file-upload, security, validation, malware]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement secure file upload handling.

File types accepted: [DESCRIBE]

**Client-side validation** (UX only, not security):
1. MIME type from file input (`accept` attribute)
2. File size check before upload
3. Preview for images

**Server-side validation** (actual security):
4. **MIME type**: read magic bytes (not extension or Content-Type header)
   - `file-type` npm package for detection
5. **Extension allow-list**: only allow specific extensions
6. **File size limit**: enforce in server/nginx
7. **Virus scanning**: ClamAV or Cloudmersive API
8. **Image reprocessing**: re-save images through Sharp to strip metadata and exploits
9. **Rename**: generate UUID filename, don't use user's filename
10. **Isolate**: serve uploads from separate domain (prevent XSS)
11. **No execution**: uploads directory outside webroot, no execute permissions
12. **Malicious SVG**: SVG can contain JavaScript — treat as code
13. **ZIP bombs**: limit extracted size
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
