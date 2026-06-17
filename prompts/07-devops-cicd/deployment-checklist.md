---
title: "Production Deployment Checklist"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [deployment, checklist, devops, production]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Create a comprehensive production deployment checklist.

My app: [DESCRIBE YOUR STACK AND INFRASTRUCTURE]

**Pre-deployment**:
□ All tests passing (unit, integration, E2E)
□ Security scan passed (Snyk / npm audit)
□ Performance regression test passed
□ Database migrations tested on staging with production data copy
□ Feature flags set correctly for rollout plan
□ Rollback plan documented and tested
□ On-call engineer aware and available
□ Stakeholders notified (if user-visible change)

**During deployment**:
□ Deploy to staging first
□ Smoke test staging
□ Monitor error rates during rollout
□ Deploy to production (blue/green or rolling)
□ Watch dashboards for 15 minutes

**Post-deployment**:
□ Smoke test production
□ Alert the team
□ Update changelog
□ Close the deployment issue/PR
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
