---
title: "Implement Cloud Cost Allocation Tags"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cost, aws, finops, tagging]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement comprehensive cost allocation tagging for AWS resources.

Business context: [TEAMS, PROJECTS, COST CENTERS]

Tagging strategy:
1. **Mandatory tags**: Environment, Team, Project, CostCenter, Owner
2. **AWS Organizations**: tag policies to enforce mandatory tags
3. **Resource-specific tags**: Service, Version, Tier
4. **Propagation**: EC2 → EBS, ECS → tasks, RDS → snapshots
5. **Cost Explorer**: filter and group by tags
6. **Budgets**: per-team budget with alerts at 80%, 100%, 120%
7. **Anomaly detection**: alert on unexpected cost spikes
8. **Showback reports**: monthly cost per team email
9. **Untagged resource hunting**: find and tag orphaned resources
10. **Terraform tagging**: `default_tags` in provider config

Output: tagging policy document + Terraform provider config.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
