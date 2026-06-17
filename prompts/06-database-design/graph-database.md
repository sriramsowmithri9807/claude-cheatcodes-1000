---
title: "Design a Graph Database Schema"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [neo4j, graph, database, relationships]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a graph database schema using Neo4j for: [DESCRIBE YOUR DOMAIN — social network, recommendation engine, dependency graph, fraud detection].

1. **Nodes**: define all node labels and their properties
2. **Relationships**: define all relationship types and directions
3. **Properties on relationships**: when to put data on the edge
4. **Indexes**: node property indexes for lookup
5. **Constraints**: unique constraints on node properties

Cypher queries for your key use cases:
6. Find all connections within N degrees
7. Shortest path between two nodes
8. Recommend based on similar users (collaborative filtering)
9. Detect cycles (fraud rings)
10. Pattern matching queries

When to use Neo4j vs relational DB — decision matrix.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
