---
title: "Build a Resume Builder"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [resume, pdf, react, fullstack]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build an online resume builder that generates beautiful PDFs.

Stack: Next.js + PostgreSQL + react-pdf

Features:
1. Sections: contact, summary, experience, education, skills, projects, certifications
2. Multiple templates: modern, classic, minimal, creative
3. Live preview: see changes in real-time
4. Export: PDF + ATS-friendly plain text
5. AI enhancement: improve bullet points (Claude API)
6. ATS score: analyze against a job description
7. Shareable URL: public resume page
8. Version history: save multiple versions
9. Import from LinkedIn
10. Cover letter generator (AI)

React PDF renders the exact same layout in both preview and export.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
