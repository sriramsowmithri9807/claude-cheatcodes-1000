---
title: "Write Ansible Playbooks for Server Config"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ansible, configuration-management, devops, linux]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Write Ansible playbooks to configure and manage my servers.

Servers: [DESCRIBE: Ubuntu 22.04, what services run on them]

Playbooks to write:
1. **base.yml**: system updates, timezone, NTP, swap, kernel params
2. **security.yml**: UFW firewall, fail2ban, SSH hardening (no root, no password auth)
3. **docker.yml**: install Docker + Docker Compose, manage with systemd
4. **nginx.yml**: install, configure, SSL with Certbot, test config
5. **app.yml**: deploy application, environment config, systemd service
6. **monitoring.yml**: install node exporter, configure log shipping
7. **backup.yml**: configure database backup cron job

Inventory: staging and production groups
Vault: encrypt sensitive values
Idempotent: safe to run multiple times
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
