---
title: "Create a Helm Chart for Kubernetes"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [helm, kubernetes, charts, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Create a Helm chart for deploying my application to Kubernetes.

App: [DESCRIBE YOUR APPLICATION]

Chart structure:
```
mychart/
  Chart.yaml
  values.yaml
  templates/
    deployment.yaml
    service.yaml
    ingress.yaml
    configmap.yaml
    secret.yaml
    hpa.yaml
    pdb.yaml
    _helpers.tpl
```

Values to parameterize:
- Image repo and tag
- Replica count
- Resource limits
- Ingress host and TLS
- Environment variables
- Secrets (from external secrets operator)
- Enable/disable optional components

Include: `Chart.yaml`, complete `values.yaml` with comments, and all templates.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
