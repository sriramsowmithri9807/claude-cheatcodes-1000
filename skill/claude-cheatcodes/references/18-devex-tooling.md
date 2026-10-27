# 18-devex-tooling

Developer experience: devcontainers, monorepos, linters, git hooks, CLIs, Makefiles, env management.

21 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Run CI Locally

**id:** `18-devex-tooling/ci-local` · **Difficulty:** intermediate · **Tags:** ci, local-development, act, tooling

````text
Run CI pipeline locally before pushing.

CI system: GitHub Actions

Using: `act` (run GitHub Actions locally via Docker)

1. **Installation**: `brew install act`
2. **First run**: `act` runs `on: push` workflow
3. **Specific job**: `act -j test`
4. **Specific event**: `act pull_request`
5. **Secrets**: `act --secret-file .secrets`
6. **Container size**: `act --container-options '--memory 4g'`

Alternatives:
7. **Run steps manually**: document each CI step as npm script
8. **Docker**: reproduce CI environment locally
9. **Nx affected**: only test changed packages

Common CI issues to catch locally:
10. Missing environment variables
11. Wrong Node.js version
12. Test database not configured
13. Permissions issues
14. Missing secrets

`.actrc` file:
15. Default platform, secrets, environment settings

Output: act configuration + local CI guide.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Code Generation Tools

**id:** `18-devex-tooling/code-generation` · **Difficulty:** intermediate · **Tags:** code-generation, plop, hygen, scaffolding

**Placeholders:** [DESCRIBE: component, service, test, API route], [DESCRIBE]

````text
Set up code generation tools to scaffold components, modules, and files.

Project: [DESCRIBE]
Common boilerplate: [DESCRIBE: component, service, test, API route]

Using: Plop.js

1. **Installation**: `npm install --save-dev plop`
2. **Plopfile**: define generators
3. **Generator structure**:
   - Name (what you're generating)
   - Prompts (questions to ask user)
   - Actions (what files to create)
4. **Templates**: Handlebars templates for each file

Generators to create:
5. **React component**: component.tsx + styles + test + stories
6. **API route**: handler.ts + types + test
7. **Database model**: schema + migration + seed
8. **Zustand store**: store.ts + types
9. **Service**: service.ts + interface + mock

Usage:
```bash
npx plop component
# ? Component name: UserProfile
# ✓ Created src/components/UserProfile/UserProfile.tsx
# ✓ Created src/components/UserProfile/UserProfile.test.tsx
```

Output: Plopfile + templates for my generators.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Track Code Quality Metrics

**id:** `18-devex-tooling/code-quality-metrics` · **Difficulty:** intermediate · **Tags:** code-quality, metrics, sonarqube, tooling

**Placeholders:** [DESCRIBE]

````text
Track and improve code quality metrics.

Project: [DESCRIBE]

**Metrics to track**:
1. **Test coverage**: line, branch, function coverage
2. **Cyclomatic complexity**: cognitive load of functions
3. **Code duplication**: DRY violations
4. **Technical debt**: estimated fix time
5. **Dependency vulnerabilities**: known CVEs
6. **Bundle size**: JS bundle weight over time
7. **TypeScript strictness**: any usage, untyped imports

**Tools**:
8. **SonarQube** (self-hosted) / **SonarCloud** (cloud):
   - Connect to GitHub
   - Gate: block PRs below quality threshold
9. **CodeClimate**: maintainability grade
10. **Codecov**: coverage reports with PR comments

**Local tools**:
11. `complexity-report`: cyclomatic complexity
12. `jscpd`: copy-paste detection
13. `ts-prune`: find unused TypeScript exports
14. `depcheck`: find unused dependencies

GitHub Actions integration:
15. PR comment with quality summary
16. Fail PR on threshold breach

Output: complete quality pipeline setup.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Debugging Tools

**id:** `18-devex-tooling/debugging-tools` · **Difficulty:** intermediate · **Tags:** debugging, devtools, node-js, chrome

**Placeholders:** [NODE.JS / BROWSER / REACT]

````text
Set up comprehensive debugging tools for my stack.

Stack: [NODE.JS / BROWSER / REACT]

**Node.js debugging**:
1. VS Code debugger: `.vscode/launch.json` configuration
2. `--inspect` flag: `node --inspect server.js`
3. Chrome DevTools: `chrome://inspect`
4. `debugger` statement: pause execution in debugger
5. `console.trace()`: print stack trace
6. Logging: structured logging with pino

**Browser debugging**:
7. Chrome DevTools: Elements, Network, Console, Sources
8. `console.table()`: visualize arrays of objects
9. `$0` in console: last selected element
10. Network conditions: throttle to simulate slow connection
11. Breakpoints: conditional, XHR, event listener

**React debugging**:
12. React DevTools: component tree, props, state
13. Why Did You Render: log unnecessary re-renders
14. Redux/Zustand DevTools: state inspection

**Remote debugging**:
15. ngrok: expose localhost to webhook services

Output: VS Code launch.json + debugging tips.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Perfect Development Environment

**id:** `18-devex-tooling/dev-environment` · **Difficulty:** intermediate · **Tags:** dev-environment, dotfiles, tooling, productivity

**Placeholders:** [DESCRIBE], [LANGUAGE/STACK]

````text
Set up a perfect development environment for [LANGUAGE/STACK].

OS: [Mac / Linux / Windows]
Stack: [DESCRIBE]

**Terminal setup**:
1. iTerm2 (Mac) or Warp — better than default terminal
2. Zsh + Oh My Zsh or Starship prompt
3. Plugins: zsh-autosuggestions, zsh-syntax-highlighting, fzf
4. Aliases: shortcuts for common commands

**Package management**:
5. Homebrew (Mac) — install everything
6. `mise` or `nvm` — manage Node.js versions
7. `pyenv` — manage Python versions

**Essential tools**:
8. `git` configuration: user, aliases, delta for diffs
9. `gh` — GitHub CLI
10. `jq` — JSON processor
11. `httpie` or `curl` — API testing
12. `k9s` — Kubernetes dashboard in terminal

**Dotfiles**:
13. Track in git repo
14. `stow` or `chezmoi` for symlinks
15. Bootstrap script: new machine ready in 10 minutes

Output: complete setup script + dotfiles for my stack.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Useful Development Scripts

**id:** `18-devex-tooling/development-scripts` · **Difficulty:** intermediate · **Tags:** scripts, automation, bash, tooling

**Placeholders:** [DESCRIBE]

````text
Write useful automation scripts for my development workflow.

Project: [DESCRIBE]

Scripts to create:

1. **setup.sh**: bootstrap new developer environment
   - Install dependencies
   - Setup local databases
   - Copy .env.example → .env
   - Run migrations
   - Seed data
   - Start services

2. **reset-db.sh**: reset database to clean state
   - Drop and recreate database
   - Run all migrations
   - Run seeds

3. **generate-migration.sh**: create new migration file
   - Ask for migration name
   - Create timestamped file
   - Open in editor

4. **deploy.sh**: deployment script
   - Run tests
   - Build
   - Deploy
   - Health check
   - Notify Slack

5. **clean.sh**: cleanup script
   - Delete build artifacts
   - Clear caches
   - Optional: reset database

Best practices:
6. `set -e`: exit on error
7. Color output: success=green, error=red
8. Dry run mode: `--dry-run` flag

Output: all scripts for my project.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize Dockerfiles

**id:** `18-devex-tooling/dockerfile-optimization` · **Difficulty:** intermediate · **Tags:** docker, optimization, build-time, image-size

**Placeholders:** [PASTE YOUR DOCKERFILE], [SIZE], [TIME]

````text
Optimize my Dockerfiles for build time and image size.

Current Dockerfile: [PASTE YOUR DOCKERFILE]
Current image size: [SIZE]
Current build time: [TIME]

Optimization techniques:
1. **Multi-stage build**: separate build stage from runtime stage
2. **Layer ordering**: COPY package files → install → COPY code
   (dependencies change less often than code)
3. **Minimize layers**: combine RUN commands with &&
4. **Minimal base image**: node:20-alpine instead of node:20
5. **Distroless**: no shell, no package manager, smallest attack surface
6. **Cache mount**: `--mount=type=cache,target=/root/.npm`
7. **.dockerignore**: exclude node_modules, .git, .env, test files
8. **Non-root user**: `USER node` before CMD
9. **Specific versions**: pin base image version
10. **HEALTHCHECK**: define health check

Before/after comparison:
- Image size reduction target: 50%+
- Build time reduction: explain caching strategy

Output: optimized Dockerfile.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Manage Environment Variables

**id:** `18-devex-tooling/env-management` · **Difficulty:** beginner · **Tags:** environment, secrets, config, tooling

**Placeholders:** [DESCRIBE]

````text
Manage environment variables across development, staging, and production.

Project: [DESCRIBE]

**Local development**:
1. `.env` file: local secrets (git-ignored)
2. `.env.example`: template with fake values (committed)
3. `dotenv`: load .env automatically
4. Validation: check required vars on startup

**Multiple environments**:
5. `.env.local` > `.env.development` > `.env` (priority)
6. `.env.test` for test environment
7. Never commit `.env` with real values

**Validation with Zod**:
```typescript
const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  PORT: z.coerce.number().default(3000),
});
export const env = envSchema.parse(process.env);
```

**Production**:
8. Platform secrets: Vercel, Railway, EAS
9. Secrets manager: AWS Secrets Manager or Vault
10. Inject at deploy time, not stored in codebase

**CI/CD**:
11. GitHub Secrets for CI
12. Environment-specific secrets

Output: env validation schema + .env.example.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Configure ESLint for Your Project

**id:** `18-devex-tooling/eslint-config` · **Difficulty:** intermediate · **Tags:** eslint, linting, code-quality, javascript

````text
Configure ESLint for maximum code quality.

Project type: [React / Next.js / Node.js / TypeScript]

ESLint flat config (`eslint.config.js`):
1. **Parser**: @typescript-eslint/parser for TypeScript
2. **Plugin bundles**:
   - `@typescript-eslint/eslint-plugin`: TypeScript rules
   - `eslint-plugin-react`: React best practices
   - `eslint-plugin-react-hooks`: Hooks rules
   - `eslint-plugin-import`: import ordering
   - `eslint-plugin-unicorn`: modern JS best practices
3. **Rules to enable**:
   - No any: `@typescript-eslint/no-explicit-any`
   - No unused vars (with destructuring exception)
   - Consistent returns
   - No floating promises
   - Import organization
4. **Rules to disable** (with reason)
5. **Override**: different rules for test files
6. **Prettier integration**: `eslint-config-prettier`
7. **Pre-commit hook**: run ESLint via lint-staged
8. **CI**: fail if ESLint errors

Output: complete `eslint.config.js` for my project.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Advanced Git Hooks

**id:** `18-devex-tooling/git-hooks-advanced` · **Difficulty:** advanced · **Tags:** git, hooks, automation, quality

````text
Set up advanced Git hooks for automation and quality.

Hooks to implement:

**pre-commit** (< 10 seconds):
1. Lint staged files
2. Format staged files
3. Check for secrets (detect-secrets)
4. Type check changed files

**commit-msg**:
5. Enforce Conventional Commits format
6. Link to Jira ticket if team policy

**pre-push**:
7. Run unit tests
8. Check for TODO/FIXME without ticket
9. Verify no debug statements left

**post-merge** (informational):
10. Remind to run `pnpm install` if package.json changed
11. Remind to run migrations if schema changed

**prepare-commit-msg**:
12. Pre-populate commit message with branch name

Implementation:
13. Husky for hook management
14. lint-staged for staged files
15. Parallel execution for speed
16. Skip in CI: `CI=true` bypasses hooks

Output: complete hook setup.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Git Workflow for Teams

**id:** `18-devex-tooling/git-workflow` · **Difficulty:** intermediate · **Tags:** git, workflow, branching, team

**Placeholders:** [DAILY / MULTIPLE TIMES A DAY]

````text
Set up a Git workflow for my engineering team.

Team size: [N engineers]
Deployment frequency: [DAILY / MULTIPLE TIMES A DAY]

Branching strategy:
**GitHub Flow** (simple, for continuous deployment):
1. `main` → always deployable
2. Feature branches → PR → merge
3. Deploy from main automatically

**Git Flow** (for scheduled releases):
4. `main` → production
5. `develop` → integration
6. `feature/` → develop
7. `release/` → main
8. `hotfix/` → main

Branch naming: `type/short-description` where type = feat/fix/docs/chore

Commit conventions:
9. Conventional Commits: `feat: add user avatar upload`
10. Commitlint: enforce in pre-commit hook

PR process:
11. PR template: description, test plan, screenshots
12. Minimum 1 review required
13. CI must pass before merge
14. Squash merge to keep history clean

Output: Git workflow documentation + hook configs.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Pre-Commit Hooks

**id:** `18-devex-tooling/husky-lint-staged` · **Difficulty:** beginner · **Tags:** husky, lint-staged, git-hooks, quality

**Placeholders:** [DESCRIBE YOUR STACK]

````text
Set up pre-commit hooks to enforce code quality.

Project: [DESCRIBE YOUR STACK]

1. **Install Husky**: `npx husky init`
2. **Install lint-staged**: `npm install --save-dev lint-staged`

3. **`.husky/pre-commit`**:
```bash
npx lint-staged
```

4. **`.husky/commit-msg`** (Conventional Commits):
```bash
npx --no -- commitlint --edit $1
```

5. **`lint-staged` config** in `package.json`:
```json
{
  'lint-staged': {
    '*.{ts,tsx}': ['eslint --fix', 'prettier --write'],
    '*.{css,scss}': ['stylelint --fix', 'prettier --write'],
    '*.{json,md}': ['prettier --write']
  }
}
```

6. **Commitlint**: enforce Conventional Commits format

7. **Pre-push hook**: run tests before push
```bash
npm test -- --passWithNoTests
```

8. **Bypass**: `git commit --no-verify` for emergencies (document when ok to use)

Output: complete hook setup.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Create a Project Makefile

**id:** `18-devex-tooling/makefile-commands` · **Difficulty:** beginner · **Tags:** makefile, automation, developer-experience, scripts

**Placeholders:** [DESCRIBE YOUR STACK]

````text
Create a project Makefile with useful developer commands.

Project: [DESCRIBE YOUR STACK]

Makefile targets to create:

```makefile
.PHONY: help up down logs shell db test lint build deploy

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk '...'

up:  ## Start all services
	docker compose up -d

down:  ## Stop all services  
	docker compose down

logs:  ## Tail logs
	docker compose logs -f

shell:  ## Open shell in app container
	docker compose exec app sh

db:  ## Open database CLI
	docker compose exec db psql -U postgres

test:  ## Run tests
	npm test

lint:  ## Run linters
	npm run lint

build:  ## Build for production
	npm run build

migrate:  ## Run database migrations
	npm run migrate

deploy:  ## Deploy to production
	./scripts/deploy.sh
```

For my specific project: all relevant targets.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Monorepo Tooling

**id:** `18-devex-tooling/monorepo-tooling` · **Difficulty:** advanced · **Tags:** monorepo, turborepo, pnpm, nx

**Placeholders:** [LIST WHAT'S IN YOUR MONOREPO]

````text
Set up tooling for my monorepo.

Apps/packages: [LIST WHAT'S IN YOUR MONOREPO]

**pnpm workspaces** (package manager):
1. `pnpm-workspace.yaml`: define workspace packages
2. Hoist: shared dependencies at root
3. Protocol: `workspace:*` for internal packages

**Turborepo** (build system):
4. `turbo.json`: define pipeline tasks
5. Task caching: skip rebuilding if inputs unchanged
6. Remote cache: share cache across CI and team
7. Filtering: `turbo build --filter=@myorg/web`

Workspace structure:
```
apps/
  web/
  api/
packages/
  ui/
  utils/
  tsconfig/
```

Shared configs:
8. Root `tsconfig.json` extended by all packages
9. Root ESLint config extended by all
10. Root Prettier config

CI optimization:
11. Only build/test affected packages
12. Remote cache for CI speed

Output: complete monorepo setup.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Organize npm Scripts

**id:** `18-devex-tooling/npm-scripts` · **Difficulty:** beginner · **Tags:** npm, scripts, automation, package-json

**Placeholders:** [DESCRIBE YOUR STACK]

````text
Organize npm scripts for my project.

Project: [DESCRIBE YOUR STACK]

Standard npm scripts every project should have:
```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "lint:fix": "eslint . --fix",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "type-check": "tsc --noEmit",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "test:ui": "vitest --ui",
    "e2e": "playwright test",
    "e2e:ui": "playwright test --ui",
    "db:migrate": "prisma migrate dev",
    "db:seed": "ts-node prisma/seed.ts",
    "db:studio": "prisma studio",
    "prepare": "husky",
    "clean": "rm -rf .next node_modules"
  }
}
```

Cross-platform scripts:
- Use `cross-env` for env variables
- Use `rimraf` instead of `rm -rf`
- Use `concurrently` for parallel scripts

Output: complete package.json scripts section.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master Package Management

**id:** `18-devex-tooling/package-management` · **Difficulty:** intermediate · **Tags:** npm, pnpm, packages, dependencies

````text
Master package management for my Node.js project.

**pnpm (recommended)**:
1. Why pnpm: 2-3x faster than npm, disk efficient
2. `pnpm install`, `pnpm add`, `pnpm remove`
3. Lock file: `pnpm-lock.yaml`
4. Workspace: manage monorepos

**Dependency management**:
5. `dependencies` vs `devDependencies` vs `peerDependencies`
6. Pinning: `^` (compatible) vs `~` (patch only) vs exact
7. `npm outdated`: see what can be updated
8. `npx npm-check-updates -u`: update all deps
9. Renovate bot: automate dependency updates

**Security**:
10. `pnpm audit`: check for vulnerabilities
11. `pnpm audit --fix`: fix automatically

**Troubleshooting**:
12. Peer dependency conflicts: resolution field
13. Duplicate packages: `pnpm dedupe`
14. Clear cache: `pnpm store prune`

**Publishing**:
15. `pnpm pack`: preview what's published
16. `pnpm publish --access public`

Output: package.json best practices + scripts.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Configure Prettier for Consistent Formatting

**id:** `18-devex-tooling/prettier-config` · **Difficulty:** beginner · **Tags:** prettier, formatting, code-style, tooling

**Placeholders:** [DESCRIBE]

````text
Configure Prettier for consistent code formatting.

Project: [DESCRIBE]

1. **Installation**: `npm install --save-dev prettier`
2. **Config file** (`.prettierrc.json`):
```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "all",
  "printWidth": 100,
  "bracketSpacing": true,
  "arrowParens": "always",
  "endOfLine": "lf"
}
```

3. **`.prettierignore`**: exclude generated files, build output
4. **Editor integration**: VS Code settings to format on save
5. **ESLint integration**: `eslint-config-prettier` (disable conflicting rules)
6. **Pre-commit hook**: `lint-staged` + `husky` → format on commit
7. **CI check**: `prettier --check .` fails if not formatted
8. **Format all files**: `prettier --write .` to format existing codebase
9. **Plugins**: Prettier plugin for Tailwind, JSON, MDX
10. **Opinionated decision**: stop bikeshedding formatting forever
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Testing Tools

**id:** `18-devex-tooling/testing-tools-setup` · **Difficulty:** intermediate · **Tags:** testing, vitest, playwright, setup

**Placeholders:** [DESCRIBE]

````text
Set up comprehensive testing tools for my project.

Project: [DESCRIBE]

**Vitest** (unit + component tests):
1. Install: `npm install --save-dev vitest @vitest/ui`
2. `vitest.config.ts`: configure jsdom, coverage, aliases
3. React setup: `@testing-library/react` + `@testing-library/user-event`
4. Global: `describe`, `it`, `expect`, `vi` available without imports
5. Coverage: `@vitest/coverage-v8`, HTML report
6. UI: `vitest --ui` — browser interface for tests

**Playwright** (E2E tests):
7. Install: `npx playwright install`
8. `playwright.config.ts`: browsers, base URL, workers
9. Page Object Model: one class per page
10. Fixtures: extend test with reusable setup
11. API testing: `request` fixture for API calls
12. Visual testing: `expect(page).toHaveScreenshot()`

**MSW** (API mocking):
13. Define handlers for your API
14. Browser: ServiceWorker mode
15. Node.js: setupServer() for unit tests

Output: complete testing setup with example tests.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Configure VS Code for Productivity

**id:** `18-devex-tooling/vs-code-setup` · **Difficulty:** beginner · **Tags:** vscode, editor, productivity, tooling

**Placeholders:** [LANGUAGE/FRAMEWORK]

````text
Configure VS Code for maximum productivity for [LANGUAGE/FRAMEWORK].

Extensions to install:
1. **Language support**: TypeScript, Python, Go extensions
2. **Linting**: ESLint, Pylint integration
3. **Formatting**: Prettier
4. **AI coding**: GitHub Copilot or Cody
5. **Git**: GitLens, Git Graph
6. **Database**: Database Client or Prisma extension
7. **REST API**: REST Client or Thunder Client
8. **Containers**: Docker extension
9. **Productivity**: Todo Highlight, Path Intellisense

Settings (`settings.json`):
10. Format on save
11. Auto-import organize
12. Terminal font (JetBrains Mono or Fira Code)
13. Theme: One Dark Pro or Catppuccin
14. Font size and line height
15. Tab size: 2 spaces

Keybindings:
16. Custom shortcuts for common actions
17. Multi-cursor editing
18. Quick open, file search, symbol search

Output: complete `settings.json` + extension list.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Create custom [TOOL] to automate [AUTOMATION_TARGET]

**id:** `18-devex-tooling/create-custom-tool-to-automate-automation-target` · **Difficulty:** beginner/intermediate/advanced · **Tags:** custom, docker, devex, productivity, automated, dx, dotenv, server, eslint, git, code, shell, turborepo

**Variant group** (25 generated prompts collapsed). Pick one value per placeholder:
- `[TOOL]`: Docker devcontainers | ESLint and Prettier custom plugins | Turborepo monorepos | custom CLI automation scripts | git pre-commit Husky hooks | shell terminal configuration aliases
- `[AUTOMATION_TARGET]`: CI syntax formatting validators | automated local PostgreSQL setups | code boilerplate scaffold engines | dotenv variables sync scripts | server system logs parsers
- `[DX_GOAL]`: automated build alerts | consistent team code styling | faster engineer onboarding | lowered pipeline verification times

````text
Build custom scripts or settings for [TOOL] that targets [AUTOMATION_TARGET]. Focus on [DX_GOAL] to improve daily developer experience.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** create-custom-custom-cli-automation-scripts-to-automate-automated-local-postgresql-setups, create-custom-custom-cli-automation-scripts-to-automate-ci-syntax-formatting-validators, create-custom-custom-cli-automation-scripts-to-automate-dotenv-variables-sync-scripts, create-custom-docker-devcontainers-to-automate-automated-local-postgresql-setups, create-custom-docker-devcontainers-to-automate-ci-syntax-formatting-validators, create-custom-docker-devcontainers-to-automate-dotenv-variables-sync-scripts, create-custom-docker-devcontainers-to-automate-server-system-logs-parsers, create-custom-eslint-and-prettier-custom-plugins-to-automate-automated-local-postgresql-setups, create-custom-eslint-and-prettier-custom-plugins-to-automate-ci-syntax-formatting-validators, create-custom-eslint-and-prettier-custom-plugins-to-automate-dotenv-variables-sync-scripts, create-custom-eslint-and-prettier-custom-plugins-to-automate-server-system-logs-parsers, create-custom-git-pre-commit-husky-hooks-to-automate-automated-local-postgresql-setups, create-custom-git-pre-commit-husky-hooks-to-automate-code-boilerplate-scaffold-engines, create-custom-git-pre-commit-husky-hooks-to-automate-dotenv-variables-sync-scripts, create-custom-git-pre-commit-husky-hooks-to-automate-server-system-logs-parsers, create-custom-shell-terminal-configuration-aliases-to-automate-automated-local-postgresql-setups, create-custom-shell-terminal-configuration-aliases-to-automate-ci-syntax-formatting-validators, create-custom-shell-terminal-configuration-aliases-to-automate-code-boilerplate-scaffold-engines, create-custom-shell-terminal-configuration-aliases-to-automate-dotenv-variables-sync-scripts, create-custom-shell-terminal-configuration-aliases-to-automate-server-system-logs-parsers, create-custom-turborepo-monorepos-to-automate-automated-local-postgresql-setups, create-custom-turborepo-monorepos-to-automate-ci-syntax-formatting-validators, create-custom-turborepo-monorepos-to-automate-code-boilerplate-scaffold-engines, create-custom-turborepo-monorepos-to-automate-dotenv-variables-sync-scripts, create-custom-turborepo-monorepos-to-automate-server-system-logs-parsers


## Set up [TOOL] for local development

**id:** `18-devex-tooling/set-up-tool-for-local-development` · **Difficulty:** beginner/intermediate/advanced · **Tags:** custom, docker, devex, productivity, automated, dx, dotenv, eslint, git, shell, code, turborepo

**Variant group** (6 generated prompts collapsed). Pick one value per placeholder:
- `[TOOL]`: Docker devcontainers | ESLint and Prettier custom plugins | Turborepo monorepos | custom CLI automation scripts | git pre-commit Husky hooks | shell terminal configuration aliases
- `[AUTOMATION_TARGET]`: automated local PostgreSQL setups | code boilerplate scaffold engines | dotenv variables sync scripts

````text
Build a configuration setup for [TOOL] to optimize development workflow. Ensure it handles [AUTOMATION_TARGET] and helps developers get running faster.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** set-up-custom-cli-automation-scripts-for-local-development, set-up-docker-devcontainers-for-local-development, set-up-eslint-and-prettier-custom-plugins-for-local-development, set-up-git-pre-commit-husky-hooks-for-local-development, set-up-shell-terminal-configuration-aliases-for-local-development, set-up-turborepo-monorepos-for-local-development

