---
title: "Add AI-Powered Search to Your App"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [search, embeddings, vector-db, ai]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Add semantic AI-powered search to my app.

Current setup: [DESCRIBE YOUR DATA AND TECH STACK]

Implement:
1. **Embedding generation** using Claude API (or OpenAI embeddings as fallback)
2. **Vector storage** with pgvector (PostgreSQL) or Pinecone
3. **Indexing pipeline**: ingest documents → chunk → embed → store
4. **Search API**: query → embed → vector similarity search → rerank
5. **Frontend search bar** with debouncing, loading states, highlighted results
6. **Hybrid search**: combine keyword (BM25) + semantic for better results

Performance target: < 500ms search latency for 100k documents.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
