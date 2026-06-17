---
title: "Deploy a Multi-Region Architecture"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [multi-region, aws, global, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design and deploy a multi-region architecture for global availability.

Current: Single region [us-east-1]
Goal: Add [eu-west-1] for European users with < 50ms latency from Europe

Design:
1. **DNS routing**: Route 53 latency-based routing (user → nearest region)
2. **Primary region**: active, handles all writes
3. **Secondary region**: read replica + static content
4. **Database**: PostgreSQL streaming replication to secondary
5. **Read routing**: read from local replica, write to primary
6. **CDN**: CloudFront (global edge already)
7. **Session state**: Redis with cross-region sync (ElastiCache Global Datastore)
8. **Failover**: if primary fails, promote secondary to primary
9. **Data residency**: European user data stays in EU (GDPR)
10. **Cost**: estimate the additional monthly cost
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
