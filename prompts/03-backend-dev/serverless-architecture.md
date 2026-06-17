---
title: "Design a Serverless Architecture"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [serverless, aws-lambda, api-gateway, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a complete serverless architecture on AWS for: [APP DESCRIPTION].

Using: AWS Lambda + API Gateway + DynamoDB + S3 + SQS

Design:
1. Lambda functions (one per API endpoint — thin handlers)
2. API Gateway routes and auth (JWT or API Key)
3. DynamoDB table design (single-table design)
4. S3 buckets and access policies
5. SQS queues for async processing
6. EventBridge for scheduled tasks
7. CloudWatch alarms and dashboards
8. IAM roles (principle of least privilege)
9. Infrastructure as Code (AWS CDK in TypeScript)
10. Local development with SAM CLI
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
