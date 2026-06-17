---
title: "Set Up and Use a Vector Database"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [vector-db, pgvector, pinecone, embeddings]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up a vector database for AI/ML applications.

Use case: [DESCRIBE: semantic search, RAG, recommendation, deduplication]
Data to vectorize: [DESCRIBE]
Scale: [EXPECTED RECORD COUNT]

Option A — pgvector (PostgreSQL extension):
1. Install: `CREATE EXTENSION vector`
2. Column type: `embedding vector(1536)`
3. IVFFlat index: `CREATE INDEX ON items USING ivfflat (embedding vector_cosine_ops)`
4. HNSW index: faster search, more memory
5. Query: `ORDER BY embedding <-> $1 LIMIT 10`
6. Hybrid: combine with PostgreSQL FTS

Option B — Pinecone (managed):
7. Namespace for isolation
8. Metadata filtering
9. Sparse-dense hybrid

For my scale and query patterns: which to use and why?
Full indexing + query implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
