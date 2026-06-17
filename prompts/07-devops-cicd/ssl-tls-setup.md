---
title: "Set Up SSL/TLS Correctly"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ssl, tls, https, certbot]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up SSL/TLS correctly for my web application.

Setup: Nginx + Let's Encrypt (Certbot)

1. **Certbot installation and certificate issuance** (webroot or DNS challenge)
2. **Auto-renewal**: cron job + Nginx reload hook
3. **TLS configuration**:
   - Minimum TLS 1.2 (drop TLS 1.0/1.1)
   - Strong cipher suites (ECDHE + AES-GCM)
   - Perfect Forward Secrecy
   - Diffie-Hellman params (4096-bit)
4. **HSTS**: Strict-Transport-Security header with preload
5. **OCSP stapling**: reduce latency on handshake
6. **HTTP/2**: enable for performance
7. **Testing**: SSL Labs A+ rating target
8. **Wildcard certificate**: if needed for subdomains
9. **Certificate monitoring**: alert 30 days before expiry
10. **CAA DNS record**: restrict certificate issuance to Let's Encrypt
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
