---
title: "Set Up a Container Registry"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [docker, registry, ghcr, ecr]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up a container registry and image management workflow.

Registry options:
- **GitHub Container Registry (GHCR)**: free for public, free private with GitHub Team
- **AWS ECR**: pay-per-storage, no egress if in same region as ECS
- **Docker Hub**: easy, limited free tier
- **Artifact Registry (GCP)**: if using GCP

For MY choice:
1. Registry setup and authentication
2. Push workflow from GitHub Actions
3. Image tagging strategy: `latest`, git SHA, semantic version
4. Multi-architecture builds (linux/amd64 + linux/arm64)
5. Image scanning for vulnerabilities (before pushing)
6. Retention policy: keep last 10 images, delete older
7. Pull secrets in Kubernetes
8. Rate limiting considerations
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
