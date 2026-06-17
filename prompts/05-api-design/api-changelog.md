---
title: "Manage Your API Changelog"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [changelog, api, versioning, documentation]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Create and maintain a professional API changelog.

My API: [DESCRIBE]
Changes this release: [LIST CHANGES]

Changelog format:
```
## [2.4.0] - 2026-01-15
### Added
- `GET /users/{id}/activity` endpoint
### Changed  
- `created_at` field is now an ISO 8601 string (was Unix timestamp)
### Deprecated
- `GET /users/{id}/feed` (use `GET /feed?user_id={id}` instead, sunset: 2026-07-01)
### Removed
- `POST /auth/token` (was deprecated in 2.0.0)
### Fixed
- Pagination cursor now works correctly with filters applied
### Security
- Fixed IDOR vulnerability in document access control
```

Also: how to:
1. Automate changelog from conventional commits
2. Notify API consumers of changes
3. Maintain breaking change log separately
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
