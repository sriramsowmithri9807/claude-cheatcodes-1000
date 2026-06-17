---
title: "Build a Complete Backend with Supabase"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [supabase, postgresql, backend, auth]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a complete backend for [APP TYPE] using Supabase.

Include:
1. Database schema with all tables, columns, types, and constraints
2. Row Level Security (RLS) policies for each table
3. PostgreSQL functions and triggers
4. TypeScript types generated from schema
5. Supabase client setup with proper TypeScript generics
6. Auth configuration (email/password + OAuth)
7. Storage bucket setup for file uploads
8. Edge Functions for any custom logic

Output as: SQL migration files + TypeScript client code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
