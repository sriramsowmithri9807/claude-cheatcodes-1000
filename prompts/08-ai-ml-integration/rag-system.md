---
title: "Build a RAG System"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [rag, embeddings, vector-db, claude]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a Retrieval-Augmented Generation (RAG) system using Claude.

Documents to search: [DESCRIBE YOUR CORPUS — docs, PDFs, codebase, support tickets]

Architecture:
1. **Document ingestion**:
   - Load documents (PDF, Markdown, HTML, code)
   - Chunk documents (strategies: fixed size, sentence, semantic)
   - Generate embeddings (Voyage AI or OpenAI embeddings)
   - Store in vector database (pgvector or Pinecone)
2. **Query pipeline**:
   - Embed user query
   - Vector similarity search (top-K results)
   - Re-rank results (cross-encoder)
   - Build context from retrieved chunks
   - Claude generates answer grounded in context
3. **Evaluation**: retrieval accuracy, answer faithfulness
4. **Optimizations**: hybrid search, metadata filtering, hypothetical document embeddings

Node.js + TypeScript implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
