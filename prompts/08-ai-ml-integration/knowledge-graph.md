---
title: "Build a Knowledge Graph with AI"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [knowledge-graph, neo4j, ai, claude]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a knowledge graph powered by AI extraction.

Source content: [DESCRIBE: documents, articles, research papers]
Knowledge to extract: [ENTITIES, RELATIONSHIPS]

1. **Entity extraction**: Claude identifies named entities (people, orgs, concepts, products)
2. **Relationship extraction**: Claude identifies relationships between entities
3. **Coreference resolution**: "he" refers to "CEO John Smith"
4. **Entity deduplication**: "Apple Inc" and "Apple" are the same entity
5. **Confidence scoring**: flag low-confidence extractions for review
6. **Graph storage**: Neo4j for property graph
7. **Graph queries**: find connections, shortest path, influential nodes
8. **Visualization**: interactive graph UI (vis.js or D3 force graph)
9. **Updates**: add new documents without duplicating existing entities
10. **Export**: SPARQL-compatible RDF format

Python implementation with async processing.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
