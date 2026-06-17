---
title: "Build Semantic Search"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [search, embeddings, vector-db, claude]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build semantic search for my content.

Content to search: [DESCRIBE YOUR DATA]
Expected queries: [DESCRIBE WHAT USERS WILL SEARCH FOR]

1. **Embeddings**: choose embedding model (Voyage AI for best quality)
2. **Chunking strategy**: optimal chunk size for your content type
3. **Vector store**: pgvector (PostgreSQL) vs Pinecone vs Weaviate
4. **Indexing pipeline**: new content → embed → store
5. **Search**: embed query → similarity search → retrieve top-K
6. **Hybrid search**: combine BM25 (keyword) + semantic for best results
7. **Re-ranking**: use cross-encoder to re-rank top-20 → top-5
8. **Metadata filtering**: filter by date, category, author before vector search
9. **Query expansion**: use Claude to generate alternative queries
10. **Evaluation**: recall@K, NDCG metrics
11. **Result display**: highlight matching terms, show source

Full implementation with Node.js + pgvector.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
