---
title: "Design a Disaster Recovery Plan"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [disaster-recovery, rto, rpo, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a disaster recovery plan for my application.

Application: [DESCRIBE]
RTO (Recovery Time Objective): [e.g., < 4 hours]
RPO (Recovery Point Objective): [e.g., < 1 hour]

Failure scenarios to plan for:
1. Database failure → automated failover to replica
2. Single AZ outage → multi-AZ deployment
3. Entire region outage → multi-region failover
4. Application bug in production → rollback procedure
5. Data corruption → point-in-time restore
6. DDoS attack → rate limiting + CDN + WAF
7. Third-party API failure → circuit breaker + fallback
8. Developer error → change management, peer review gates

For each:
- Prevention measures
- Detection (how to know it happened)
- Response playbook (step by step)
- Recovery time estimate
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
