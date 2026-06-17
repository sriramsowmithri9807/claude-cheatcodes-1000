---
title: "Deploy AWS Lambda Functions"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [aws, lambda, serverless, devops]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Deploy and manage AWS Lambda functions for my serverless backend.

Functions: [DESCRIBE YOUR FUNCTIONS AND THEIR TRIGGERS]

Using: AWS CDK (TypeScript) for infrastructure

1. **Lambda function code**: handler structure, cold start optimization
2. **CDK stack**: define Lambda, IAM role, triggers
3. **Triggers**:
   - API Gateway HTTP API
   - SQS queue trigger
   - EventBridge schedule
   - S3 object created
4. **Layers**: shared dependencies without bundling per function
5. **Environment variables + SSM Parameter Store**
6. **VPC config**: if function needs to access RDS
7. **Provisioned concurrency**: eliminate cold starts for latency-sensitive
8. **X-Ray tracing**: distributed tracing
9. **CloudWatch alarms**: error rate, duration, throttles
10. **CI/CD**: GitHub Actions → CDK deploy
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
