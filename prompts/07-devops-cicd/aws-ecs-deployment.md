---
title: "Deploy with AWS ECS and Fargate"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [aws, ecs, fargate, containers]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up complete deployment to AWS ECS Fargate.

App: [DESCRIBE YOUR CONTAINERIZED APP]

Infrastructure (using Terraform):
1. VPC with public/private subnets (2 AZs)
2. Application Load Balancer in public subnets
3. ECS Cluster
4. ECS Task Definition: container spec, CPU/memory, env vars from Secrets Manager
5. ECS Service: desired count, deployment config (rolling update)
6. Auto Scaling: scale on CPU > 70%
7. Security Groups: ALB → ECS only, ECS → RDS only
8. IAM Role for task: least privilege
9. CloudWatch logs
10. ECR repository for Docker images

CI/CD:
- GitHub Actions: build → push to ECR → update ECS service
- Blue/green deployment using CodeDeploy
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
