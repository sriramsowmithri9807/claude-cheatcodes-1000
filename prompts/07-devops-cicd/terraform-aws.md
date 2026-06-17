---
title: "Infrastructure as Code with Terraform"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [terraform, aws, iac, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Write Terraform code for my AWS infrastructure.

Infrastructure to provision:
- [LIST YOUR RESOURCES: VPC, EC2, RDS, S3, CloudFront, ALB, etc.]

Best practices to follow:
1. **State management**: S3 backend + DynamoDB lock table
2. **Modules**: one module per logical group (networking, database, app)
3. **Variables**: with type, description, validation
4. **Locals**: computed values
5. **Outputs**: export values to other modules
6. **Data sources**: reference existing AWS resources
7. **Workspaces** or **separate state**: staging vs production
8. **Secrets**: never hardcode — use AWS Secrets Manager
9. **Tagging**: consistent tags on all resources
10. **Destroy protection**: `prevent_destroy = true` on critical resources

Output: complete, working Terraform code with modules.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
