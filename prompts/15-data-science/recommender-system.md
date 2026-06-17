---
title: "Build a Recommender System"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [recommendations, collaborative-filtering, machine-learning, python]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a recommender system.

Data available: [DESCRIBE: user-item interactions, ratings, purchase history, content features]
Recommendation goal: [MOVIES / PRODUCTS / CONTENT / USERS TO FOLLOW]

Approaches:
1. **Collaborative filtering**: users who liked X also liked Y
   - Memory-based: user-user, item-item similarity
   - Model-based: matrix factorization (SVD, ALS)
2. **Content-based**: recommend similar items to what user liked
3. **Hybrid**: combine collaborative + content
4. **Neural**: two-tower model (embedding user + item)

Implement:
5. Surprise or implicit library for collaborative filtering
6. Cosine similarity for item-to-item
7. Evaluation: NDCG@K, Recall@K, Precision@K
8. Cold start: handle new users and new items
9. Diversity: don't just recommend safe choices
10. A/B test: measure click-through improvement

Output: working recommender + evaluation pipeline.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
