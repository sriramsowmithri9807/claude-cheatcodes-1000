---
title: "Design a Serverless Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [serverless, aws, lambda, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a complete serverless architecture for my application.

Application: [DESCRIBE]

AWS Serverless components:
1. **Lambda**: one function per API endpoint (thin handlers)
2. **API Gateway**: HTTP API (cheaper, faster than REST API)
3. **DynamoDB**: single-table design for data storage
4. **S3**: file storage + static website hosting
5. **SQS**: async processing queue
6. **EventBridge**: event bus, cron jobs
7. **Cognito**: user auth (or Auth0)
8. **CloudFront**: CDN in front of everything
9. **Secrets Manager**: environment secrets
10. **CDK**: infrastructure as code

Design decisions:
- When to use Lambda vs container (ECS Fargate)
- DynamoDB access patterns and key design
- Cold start mitigation strategy
- Local development setup (SAM CLI)

Draw complete architecture diagram.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
