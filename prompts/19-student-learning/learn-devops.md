---
title: "Learn DevOps as a Developer"
category: student-learning
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [devops, learning, docker, ci-cd]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Teach me DevOps concepts as a developer.

Development background: [DESCRIBE YOUR STACK]
Current DevOps knowledge: [NONE / BASIC / INTERMEDIATE]

DevOps learning path:

**Phase 1 — Foundations** (Month 1):
1. Linux basics: commands, file system, permissions
2. Git: branching, CI triggers, git ops
3. Docker: build, run, compose, multi-stage
4. Shell scripting: automate repetitive tasks

**Phase 2 — CI/CD** (Month 2):
5. GitHub Actions: write your first workflow
6. Testing in CI: run tests on every PR
7. Build and push Docker images
8. Deploy to staging automatically

**Phase 3 — Infrastructure** (Month 3):
9. Cloud basics (AWS or GCP): EC2, S3, RDS, networking
10. Terraform: infrastructure as code basics
11. Monitoring: Prometheus + Grafana setup
12. Logs: centralized logging with Loki

**Phase 4 — Kubernetes** (Month 4+):
13. Kubernetes concepts: pods, deployments, services
14. Helm: package manager for K8s
15. GitOps: ArgoCD

For each concept: hands-on exercise to apply it.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
