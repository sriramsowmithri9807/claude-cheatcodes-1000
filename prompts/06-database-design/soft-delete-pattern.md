---
title: "Implement Soft Delete"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [soft-delete, postgresql, patterns, data]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Implement soft delete for my application.

Tables to soft-delete: [LIST]

Implement:
1. Add `deleted_at TIMESTAMPTZ NULL` to each table
2. PostgreSQL views: `active_users` that filters `WHERE deleted_at IS NULL`
3. RLS policy: automatically filter deleted rows for the API user role
4. Cascade soft deletes: when user is deleted, soft-delete their posts/comments too
5. Restore: undelete functionality (admin only)
6. Hard delete schedule: permanently delete soft-deleted records after 90 days (GDPR)
7. Indexes: partial index `WHERE deleted_at IS NULL` for performance
8. Application layer: always query through the view (prevent bugs)
9. Audit trail: who deleted what and when
10. Find deleted records: admin query to see deleted items
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
