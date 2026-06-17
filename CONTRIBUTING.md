# Contributing to Claude Prompts 🤝

Thank you for helping make this the best Claude prompt library on the internet!

## How to Add a Prompt

### 1. Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/claude-prompts.git
cd claude-prompts
git checkout -b feat/add-my-prompt
```

### 2. Choose or Create a Category
All prompts live in `prompts/<category>/`. Pick the most relevant category from the 20 available.

### 3. Use the Prompt Template
Copy `templates/prompt_template.md` to the appropriate category folder with a descriptive kebab-case filename:
```
prompts/03-backend-dev/build-graphql-api-with-subscriptions.md
```

### 4. Quality Bar ✅
Every prompt must:
- [ ] Have a **complete, copy-paste-ready** prompt (not a vague idea)
- [ ] Include all YAML front-matter fields
- [ ] Have a meaningful title (not "write code for me")
- [ ] Specify which Claude models it works best with
- [ ] Include at least one practical tip or usage note
- [ ] Be tested — you've actually run it through Claude and it produces great results
- [ ] Be original — not a verbatim copy from another source

### 5. Submit a PR
```bash
git add .
git commit -m "feat: add [short description] prompt to [category]"
git push origin feat/add-my-prompt
```
Then open a Pull Request with the **Prompt Submission** template.

---

## Prompt Quality Guidelines

### ✅ Good Prompts
- **Specific**: "Build a rate-limited REST API in Express.js with JWT auth, Redis caching, and Swagger docs"
- **Actionable**: Tells Claude exactly what to produce
- **Contextual**: Includes tech stack, constraints, output format
- **Reusable**: Works for many people's projects with minor tweaks

### ❌ Bad Prompts
- Vague: "Help me build an app"
- Too niche: Only works for one very specific private project
- Duplicate: Already exists in the repo
- Non-Claude: Works with any LLM, not leveraging Claude's strengths

---

## Categories Overview

| # | Folder | Prompts |
|---|--------|---------|
| 01 | `01-vibe-coding` | Rapid prototyping, ideas → code |
| 02 | `02-frontend-dev` | React, Vue, Svelte, HTML/CSS |
| 03 | `03-backend-dev` | Node, Python, Go, Rust, APIs |
| 04 | `04-fullstack-projects` | End-to-end project scaffolding |
| 05 | `05-api-design` | REST, GraphQL, gRPC design |
| 06 | `06-database-design` | SQL, NoSQL, migrations, ORMs |
| 07 | `07-devops-cicd` | Docker, K8s, GitHub Actions, AWS |
| 08 | `08-ai-ml-integration` | Claude API, OpenAI, LangChain |
| 09 | `09-debugging-code-review` | Bug fixing, refactoring, review |
| 10 | `10-architecture-system-design` | HLD/LLD, patterns, scalability |
| 11 | `11-testing-qa` | Unit, integration, E2E tests |
| 12 | `12-mobile-dev` | React Native, Flutter |
| 13 | `13-ui-ux-design` | Design systems, components, UX |
| 14 | `14-security` | Auth, OWASP, pen testing prompts |
| 15 | `15-documentation-writing` | READMEs, API docs, wikis |
| 16 | `16-learning-education` | CS concepts, tutorials, explanations |
| 17 | `17-startup-product` | PRDs, MVPs, pitch decks |
| 18 | `18-data-engineering` | Pipelines, ETL, analytics |
| 19 | `19-open-source-collab` | OSS tooling, community, changelogs |
| 20 | `20-advanced-claude-techniques` | Extended thinking, Claude Fable 5 |

---

## Code of Conduct

- Be respectful and inclusive
- No prompts that produce harmful, illegal, or unethical content
- Credit original sources where applicable
- English prompts preferred (translations welcome in a `translations/` subfolder)

---

*Questions? Open a [Discussion](https://github.com/YOUR_USERNAME/claude-prompts/discussions) — we're friendly!*
