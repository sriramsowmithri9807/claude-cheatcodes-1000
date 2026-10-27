---
name: claude-cheatcodes
description: Library of ~670 proven prompt templates (1,007 originals, variants merged) for software work. Use whenever the user asks for "a prompt for X", wants a better prompt, or starts a coding, frontend, backend, full-stack, API, database, DevOps/CI/CD, cloud, AI/ML/LLM/RAG, debugging, code review, architecture/system design, testing, mobile, UI/UX, security, data science, documentation, performance, developer-tooling or CS-learning task where a structured template would help, e.g. "optimize my React app", "design a Postgres schema", "set up CI for a monorepo", "explain Big O". Finds the best-matching template, fills its [PLACEHOLDERS] from the conversation, then returns a copy-paste-ready prompt or runs it to produce the result.
---

# Claude Cheatcodes

A searchable library of prompt templates from the claude-cheatcodes-1000 repo, in 20 categories. Each template is a fenced prompt with `[PLACEHOLDERS]`, tags, a difficulty level and tips. Generated combinatorial variants (same sentence, different tech swapped in) are merged into one **variant group** whose placeholders list the allowed options.

Never load the whole library. Open `references/index.md` or run the search script, then open **only** the reference file you need.

## Files

- `references/index.md`: one line per prompt, `id | title | tags | difficulty`, grouped by category. Each `### references/<file>.md` heading names the file that holds those prompts.
- `references/<category>.md`: full prompts for one category. Each prompt sits under a `## <title>` heading with a `**id:**` line.
- `scripts/search.py`: keyword and tag search over the index. Uses only the standard library.

## Categories

| File | Covers |
|---|---|
| `01-vibe-coding` | Rapid builds from an idea: scaffolds, landing pages, UI from screenshots, SaaS blueprints, common app features |
| `02-frontend-dev` | React/Next.js, TypeScript, CSS, animations, forms, data tables, state management, frontend performance |
| `03-backend-dev` | Server code: REST backends, auth, queues, caching, background jobs, graceful shutdown |
| `04-fullstack-projects` | End-to-end apps: SaaS, dashboards, marketplaces, scaffolds on Next.js/SvelteKit/Nuxt/MERN |
| `05-api-design` | REST/GraphQL/gRPC/webhook design, OpenAPI, versioning, pagination, rate limits, error formats |
| `06-database-design` | Schemas, indexing, migrations, sharding, replication for Postgres, MySQL, MongoDB, Redis, DynamoDB |
| `07-devops-cicd` | CI/CD pipelines, Docker, Kubernetes, Terraform/CDK, GitHub Actions/GitLab CI/Jenkins, deployments |
| `08-ai-ml-integration` | LLM apps: Claude API, tool use, RAG, embeddings, agents, LangChain/LlamaIndex, prompt caching |
| `09-debugging-code-review` | Memory leaks, races, deadlocks, slow queries; structured code reviews and refactors |
| `10-architecture-system-design` | Scaling, microservices, event-driven design, caching, replication, design-interview systems |
| `11-testing-qa` | Unit/integration/E2E tests, mocking, Jest/Vitest/Playwright/Cypress/Pytest, coverage strategy |
| `12-mobile-dev` | React Native, Flutter, Swift, Kotlin, Expo: push, offline sync, biometrics, camera, store prep |
| `13-ui-ux-design` | Components, design systems, accessibility, Tailwind/CSS/Framer Motion, UX writing, wireframes |
| `14-security` | OWASP hardening, auth security, XSS/CSRF/SQLi defenses, secrets, encryption, threat models |
| `15-data-science` | Pandas, scikit-learn, PyTorch, forecasting, churn/fraud models, EDA, Streamlit/Plotly dashboards |
| `16-documentation` | READMEs, API docs, ADRs, runbooks, onboarding guides, changelogs, technical writing |
| `17-performance` | Profiling and optimisation: web vitals, bundles, caching, DB queries, memory, runtime tuning |
| `18-devex-tooling` | Devcontainers, monorepos, linters, git hooks, CLIs, Makefiles, env management |
| `19-student-learning` | Explaining CS concepts, algorithms, Big O, data structures, interview prep, practice problems |
| `20-vibe-coding` | Ship fast: MVPs, prototypes, automations, weekend projects, launch checklists |

A category file over ~150 KB is split into `<category>-a.md`, `-b.md` and so on. The index heading always names the right file.

## Workflow

1. **Find candidates.** Run
   `python3 scripts/search.py "<the user's request in a few keywords>"`
   (add `-n 10` for more results or `-c 07` to limit to one category). It prints the top matches with their id and the reference file to open. If you can't run scripts, read `references/index.md` and scan the section for the most likely category.
2. **Open only that reference file.** Search it for the `**id:** \`<id>\`` line or the `## <title>` heading and read just that entry, not the whole file.
3. **Choose 1–3 prompts.** Pick the closest match. Combine two prompts only when the request clearly spans both, for example a schema prompt plus an indexing prompt. Prefer a specific hand-written prompt over a generic variant group when both fit.
4. **Fill the placeholders.**
   - Replace every `[PLACEHOLDER]` with facts from the conversation, open files or the repo: stack, versions, domain names, constraints, symptoms.
   - For a **variant group**, choose one listed option per placeholder, or substitute the user's own tech if it isn't listed. The template still applies.
   - Ask the user only about placeholders you cannot reasonably infer, in one short message. If a placeholder is optional, fill in a sensible default and say so.
   - Keep the rest of the prompt text word for word. Don't rewrite the template.
5. **Deliver.**
   - If the user asked for a prompt, return the filled prompt in one fenced code block ready to copy and paste. Add a one-line note on which template it came from (its id) and, if useful, one tip from the entry.
   - If the user wants the result itself (code, a schema, a design, an explanation), treat the filled prompt as your own instructions and do the work. Don't show the prompt unless they ask.
   - If unsure which they want, deliver the result and offer the prompt.

## Tips

- Tips that mention model names (Sonnet 4, Fable 5, and so on) come from the original repo. Treat them as hints, not requirements.
- Several templates end in an "Output:" line that sets the deliverable format. Keep it, because it is what makes the output predictable.
- If nothing scores well in search, say so and write a fresh prompt in the same style: role, context, numbered requirements, then the output format.
