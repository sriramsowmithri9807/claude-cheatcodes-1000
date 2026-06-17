---
title: "Implement GitOps with ArgoCD"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [gitops, argocd, kubernetes, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement GitOps workflow using ArgoCD for Kubernetes deployments.

Setup:
- Kubernetes cluster (EKS / GKE / self-hosted)
- Multiple environments: dev, staging, production

Implement:
1. **ArgoCD installation** in the cluster
2. **App of Apps pattern**: manage multiple apps from one ArgoCD app
3. **Repository structure**:
   ```
   gitops-repo/
     apps/          # ArgoCD Application definitions
     environments/
       dev/         # Kustomize overlays for dev
       staging/
       production/
     base/          # Base Kubernetes manifests
   ```
4. **Sync policies**: auto-sync dev, manual approval for production
5. **Health checks**: define custom health assessment
6. **Notifications**: Slack on sync/failure
7. **RBAC**: developer can view, SRE can sync, admin can delete
8. **Secret management**: Sealed Secrets or External Secrets Operator
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
