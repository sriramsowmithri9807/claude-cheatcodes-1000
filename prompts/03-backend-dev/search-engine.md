---
title: "Build a Full-Text Search Engine"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [search, elasticsearch, postgresql, backend]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Add full-text search to my app.

Data to index: [DESCRIBE YOUR DATA]

Option A — PostgreSQL Full-Text Search (no external service):
1. tsvector columns + GIN index
2. to_tsquery with multiple languages
3. Ranking results by relevance (ts_rank)
4. Highlighting matching terms
5. Trigram similarity for fuzzy search

Option B — Elasticsearch:
1. Index mapping design
2. Bulk indexing pipeline
3. Query DSL for: exact match, fuzzy, phrase, wildcard
4. Aggregations for faceted filtering
5. Highlighting
6. Keep ES in sync with DB (CDC or dual-write)

Include: search result pagination, typo tolerance, synonym support.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
