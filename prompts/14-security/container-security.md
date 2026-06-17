---
title: "Secure Container Deployments"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [docker, security, containers, kubernetes]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Secure my container deployment.

**Docker security**:
1. Non-root user in container
2. Read-only filesystem: `--read-only`
3. No privileged mode: never `--privileged`
4. Dropped capabilities: `--cap-drop ALL --cap-add NET_BIND_SERVICE`
5. Resource limits: `--memory 512m --cpus 0.5`
6. No host network: use Docker networks
7. Secrets: Docker secrets, not ENV vars in Dockerfile

**Image security**:
8. Minimal base image: distroless or alpine
9. Multi-stage build: no build tools in final image
10. Image scanning: Trivy in CI (fail on CRITICAL)
11. Signed images: cosign for supply chain security

**Kubernetes security**:
12. PodSecurityContext: `runAsNonRoot: true`
13. SecurityContext: `readOnlyRootFilesystem: true`
14. NetworkPolicy: default deny, explicit allow
15. RBAC: least-privilege ServiceAccount per pod
16. Secrets: External Secrets Operator (don't store in etcd)

Output: secure Dockerfile + Kubernetes security config.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
