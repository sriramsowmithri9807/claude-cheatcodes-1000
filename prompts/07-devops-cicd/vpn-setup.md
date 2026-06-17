---
title: "Set Up a VPN for Database Access"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [vpn, security, wireguard, devops]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up secure VPN access to my production databases.

Using: WireGuard (modern, fast, simple)

1. **WireGuard server setup** on a bastion EC2/VPS:
   - Installation (Ubuntu)
   - Generate server keys
   - Interface config (`/etc/wireguard/wg0.conf`)
   - Enable IP forwarding
   - iptables rules for routing
2. **Client config**: generate config for each developer
3. **Peer management**: add/remove peers without restart
4. **Routing**: route only production subnets through VPN (split tunneling)
5. **DNS**: resolve internal hostnames through VPN
6. **Automation**: script to generate new peer configs
7. **Security**: key rotation procedure
8. **Alternative**: AWS Client VPN (managed, per-hour cost)

Connect to: PostgreSQL (port 5432) and Redis (port 6379) without exposing to internet.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
