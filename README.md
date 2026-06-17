<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=220&section=header&text=1000%2B%20Claude%20Prompts&fontSize=70&animation=fadeIn" alt="Header Banner" />
</p>

# 1000+ Claude Prompts Repository

[![Claude Models](https://img.shields.io/badge/Claude-Haiku%20%7C%20Sonnet%20%7C%20Opus%20%7C%20Fable-orange.svg)](#model-compatibility)
[![Total Prompts](https://img.shields.io/badge/Total%20Prompts-1007-blue.svg)](#repository-structure)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

<p align="center">
  <img src="https://media.giphy.com/media/26n6XC8EYdrGT8Gif/giphy.gif" alt="Vibe Coding with Claude" />
</p>

Welcome to the ultimate repository of **1,007 battle-tested prompts** specifically designed and optimized for all Anthropic Claude models—including the latest **Claude Fable 5**, **Opus 4**, **Sonnet 4**, and **Haiku 3.5**.

Whether you are a **vibe coder** shipping MVPs in a single weekend, a **software engineer** building enterprise systems, or a **student** learning core computer science concepts, this curated collection will elevate your productivity and AI-assisted development workflow.

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec59.gif" alt="Divider" />
</p>

## Repository Structure

The repository is organized into **20 specialized categories**, each containing at least 50 prompts:

| Category | Description | Target Audience |
| :--- | :--- | :--- |
| [01-vibe-coding](prompts/01-vibe-coding) | Rapid prototyping, MVP builders, and launch checkers. | Vibe Coders, Indie Hackers |
| [02-frontend-dev](prompts/02-frontend-dev) | Modern frameworks (React, Vue, Svelte), layout creation, and styles. | All Developers |
| [03-backend-dev](prompts/03-backend-dev) | Microservices, databases integration, error handlers, and servers. | Backend Engineers |
| [04-fullstack-projects](prompts/04-fullstack-projects) | Scaffolding complete projects, databases, authentication, and payments. | All Developers, Students |
| [05-api-design](prompts/05-api-design) | OpenAPI specs, REST design, GraphQL schemas, gRPC, and webhooks. | Backend Engineers |
| [06-database-design](prompts/06-database-design) | Relational database schemas, NoSQL design, indexing, and partitions. | Database Engineers, All Devs |
| [07-devops-cicd](prompts/07-devops-cicd) | CI/CD pipelines, Docker setup, Terraform, and cloud deployments. | DevOps, Platform Engineers |
| [08-ai-ml-integration](prompts/08-ai-ml-integration) | Prompt engineering, RAG pipelines, function calling, and agents. | AI Engineers, All Devs |
| [09-debugging-code-review](prompts/09-debugging-code-review) | Thread deadlocks, memory leaks, performance bugs, and race conditions. | Software Engineers |
| [10-architecture-system-design](prompts/10-architecture-system-design) | Scalable systems, CDN networks, distributed queues, and cache. | Senior Engineers, Students |
| [11-testing-qa](prompts/11-testing-qa) | Unit tests, integration routes, mocks, regression, and Playwright. | QA Engineers, All Devs |
| [12-mobile-dev](prompts/12-mobile-dev) | React Native, Flutter, offline syncing, biometric logins, and keychains. | Mobile Developers |
| [13-ui-ux-design](prompts/13-ui-ux-design) | Theme setups, animations, accessible components, and loading states. | Designers, Frontend Devs |
| [14-security](prompts/14-security) | SQL injections, XSS sanitizers, secure logins, and audits. | Security Engineers, All Devs |
| [15-data-science](prompts/15-data-science) | EDA, ML pipelines, Pandas tables, PyTorch loops, and dashboards. | Data Scientists, Students |
| [16-documentation](prompts/16-documentation) | Swagger specifications, ADRs, runbooks, and onboarding guides. | All Developers |
| [17-performance](prompts/17-performance) | Latency tuning, memory spikes profiles, and code compression. | Performance Engineers |
| [18-devex-tooling](prompts/18-devex-tooling) | Devcontainers, custom ESLint plugins, Husky scripts, and monorepos. | All Developers |
| [19-student-learning](prompts/19-student-learning) | Big O runtimes, BST nodes, observers, and sorting algorithms. | CS Students, Learners |
| [20-vibe-coding](prompts/20-vibe-coding) | Short validation workflows, fast landing pages, and AI pair workflows. | Vibe Coders, Hackers |

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec59.gif" alt="Divider" />
</p>

## Quick Start

<p align="center">
  <img src="https://media.giphy.com/media/13HgwGsXF0wDQs/giphy.gif" alt="Programmer Typing Fast" />
</p>

1. **Locate a Prompt**: Use the [Master Index](INDEX.md) to search for specific topics, technologies, or tags.
2. **Copy the Prompt**: Copy the contents inside the `## 🎯 Prompt` code block in the markdown file. (Note: Sub-pages preserve the emoji targets for compatibility).
3. **Fill the Placeholders**: Replace any `[BRACKETED PLACEHOLDERS]` with details specific to your codebase or requirements.
4. **Feed to Claude**: Paste the prompt into Claude (Sonnet, Opus, or Fable) and watch it generate production-ready code.

### Pro Tips for Claude
- **Use Extended Thinking**: When working with architecture design (`10-*`), debugging (`09-*`), or security (`14-*`), toggle **Extended Thinking** on Sonnet 4 or Fable 5. This forces the model to construct chain-of-thought analysis before outputting code.
- **Provide Context**: Copy relevant parts of your current files or directory structure and append it to the prompt.

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec59.gif" alt="Divider" />
</p>

## Model Compatibility

<p align="center">
  <img src="https://media.giphy.com/media/HTE7c014v9n0c/giphy.gif" alt="Claude Code Generator" />
</p>

| Model Series | Ideal For | Context Window | Key Features |
| :--- | :--- | :--- | :--- |
| **Claude Fable 5** | Heavy reasoning, complex refactoring, multi-file code editing, and full-stack projects | 200k tokens | Ultimate coding capability, deep context preservation |
| **Claude Opus 4** | Math modeling, scientific research, and complex data pipeline architectures | 200k tokens | Strong conceptual understanding, extremely nuanced output |
| **Claude Sonnet 4** | Daily software engineering tasks, API generation, debugging, and unit tests | 200k tokens | Fastest high-quality coding assistant, extremely up-to-date syntax |
| **Claude Haiku 3.5** | Fast scripting, single-file audits, shell script automation, and simple CRUD code | 200k tokens | Ultra-low latency, highly cost-effective for agentic workflows |

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec59.gif" alt="Divider" />
</p>

## Contributing

Contributions are welcome! If you have a prompt that has saved you hours of work, please feel free to open a PR. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on formatting, tags, and difficulty scores.

## License

This repository is available under the [MIT License](LICENSE).
