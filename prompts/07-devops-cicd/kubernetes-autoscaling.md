---
title: "Set Up Kubernetes Autoscaling"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [kubernetes, autoscaling, hpa, keda]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up comprehensive autoscaling for my Kubernetes deployment.

App: [DESCRIBE YOUR WORKLOAD PATTERN — steady, bursty, schedule-based]

1. **Horizontal Pod Autoscaler (HPA)**:
   - Scale on CPU utilization > 70%
   - Scale on custom metrics (queue depth, requests per pod)
   - Min replicas, max replicas
   - Scale-down delay (prevent flapping)
2. **Vertical Pod Autoscaler (VPA)**:
   - Automatically right-size CPU/memory requests
   - Off mode for recommendations only
3. **KEDA** (event-driven autoscaling):
   - Scale to zero when no traffic
   - Scale on SQS queue depth
   - Scale on Kafka consumer lag
4. **Cluster Autoscaler**:
   - Add/remove nodes based on pod demand
   - Node group configuration
5. **Spot instances**: use spot for bursty workloads

Output: YAML manifests for all autoscalers.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
