---
title: "Optimize Cloud Infrastructure Costs"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cost-optimization, aws, cloud, finops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize my cloud infrastructure costs.

Current spend: [DESCRIBE YOUR CURRENT CLOUD SPEND AND RESOURCES]

Optimization strategies:
1. **Right-sizing**: identify over-provisioned instances (CloudWatch metrics)
2. **Reserved instances / savings plans**: 30-70% discount for committed usage
3. **Spot instances**: 70-90% discount for non-critical workloads
4. **Auto-scaling**: don't run at peak capacity 24/7
5. **S3 lifecycle policies**: move old data to Glacier
6. **NAT Gateway**: expensive, minimize traffic through it
7. **Data transfer**: avoid cross-region and cross-AZ transfers
8. **RDS**: stop non-production databases on nights/weekends
9. **Unused resources**: find and delete orphaned volumes, old snapshots
10. **CloudWatch metrics**: which metrics you're paying for vs actually using

Target: 30% cost reduction. Show the calculation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
