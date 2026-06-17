---
title: "Deploy to Kubernetes"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [kubernetes, k8s, deployment, helm]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Write Kubernetes manifests to deploy my application.

App: [DESCRIBE YOUR APP: what containers, what dependencies]

Manifests to create:
1. **Namespace**: isolate resources
2. **Deployment**: replicas, container spec, resource requests/limits, liveness/readiness probes
3. **Service**: ClusterIP for internal, LoadBalancer or NodePort for external
4. **Ingress**: route traffic with Nginx ingress controller
5. **ConfigMap**: non-sensitive config
6. **Secret**: sensitive values (base64 encoded, or External Secrets Operator)
7. **HorizontalPodAutoscaler**: scale on CPU or custom metrics
8. **PodDisruptionBudget**: ensure at least N pods always available
9. **ServiceAccount**: least-privilege RBAC
10. **NetworkPolicy**: restrict pod-to-pod traffic

Also: `kubectl apply` order and health check commands.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
