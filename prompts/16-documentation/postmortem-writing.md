---
title: "Write Incident Postmortems"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [postmortem, incident, documentation, reliability]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write a blameless postmortem for an incident.

Incident: [DESCRIBE WHAT HAPPENED]
Impact: [DESCRIBE USER IMPACT AND DURATION]
Resolution: [DESCRIBE HOW IT WAS RESOLVED]

Postmortem template:

**Summary** (2-3 sentences): what happened, impact, duration

**Timeline**:
- HH:MM - First alert / user report
- HH:MM - On-call engineer paged
- HH:MM - Root cause identified
- HH:MM - Fix deployed
- HH:MM - Incident resolved

**Root cause**: the actual technical reason (not just 'human error')

**Contributing factors**: what made the system fragile

**What went well**: things that helped us resolve faster

**What went wrong**: gaps in our system

**Action items** (specific, assigned, with due dates):
| Action | Owner | Due Date |

**Blameless principle**: focus on systems and processes, not individuals
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
