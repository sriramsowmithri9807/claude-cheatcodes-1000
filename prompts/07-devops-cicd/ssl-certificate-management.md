---
title: "Automate SSL Certificate Management"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ssl, automation, certbot, devops]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Automate SSL certificate management at scale.

Infrastructure: [DESCRIBE: how many domains, how managed — Nginx, AWS, Cloudflare]

**Let's Encrypt automation**:
1. Certbot with `--webroot` or `--dns-cloudflare` challenge
2. Auto-renewal cron: `0 12 * * * /usr/bin/certbot renew --quiet`
3. Nginx reload hook after renewal
4. Wildcard certificates: `*.example.com` with DNS challenge

**AWS Certificate Manager**:
5. Auto-renewing certificates for ALB/CloudFront
6. DNS validation (add CNAME record)
7. Terraform: `aws_acm_certificate` + validation record

**Monitoring**:
8. Certificate expiry monitoring (alert at 30 days)
9. Certificate transparency log monitoring
10. Automated alerting: page on-call if renewal fails

Never have a certificate expire in production again.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
