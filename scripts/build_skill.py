#!/usr/bin/env python3
"""Build the `claude-cheatcodes` Claude skill from prompts/.

Parses every prompt file, collapses generated combinatorial variants
(see generate_missing_prompts.py) into canonical parameterised prompts,
and writes skill/claude-cheatcodes/ plus skill/claude-cheatcodes.zip.

Usage: python3 scripts/build_skill.py
"""
import ast
import json
import re
import shutil
import string
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"
OUT_DIR = ROOT / "skill"
SKILL_DIR = OUT_DIR / "claude-cheatcodes"
REF_DIR = SKILL_DIR / "references"
MAX_REF_BYTES = 150 * 1024

CATEGORY_BLURBS = {
    "01-vibe-coding": "Rapid builds from an idea: scaffolds, landing pages, UI from screenshots, SaaS blueprints, common app features.",
    "02-frontend-dev": "React/Next.js, TypeScript, CSS, animations, forms, data tables, state management, frontend performance.",
    "03-backend-dev": "Server code: REST backends, auth, queues, caching, background jobs, graceful shutdown, many languages.",
    "04-fullstack-projects": "End-to-end apps: SaaS, dashboards, marketplaces, scaffolds on Next.js/SvelteKit/Nuxt/MERN stacks.",
    "05-api-design": "REST/GraphQL/gRPC/webhook design, OpenAPI specs, versioning, pagination, rate limits, error formats.",
    "06-database-design": "Schemas, indexing, migrations, sharding, replication for Postgres, MySQL, MongoDB, Redis, DynamoDB, etc.",
    "07-devops-cicd": "CI/CD pipelines, Docker, Kubernetes, Terraform/CDK, GitHub Actions/GitLab CI/Jenkins, deployments.",
    "08-ai-ml-integration": "LLM apps: Claude API, tool use, RAG, embeddings, agents, LangChain/LlamaIndex, prompt caching.",
    "09-debugging-code-review": "Debugging bugs, memory leaks, races, deadlocks, slow queries; structured code reviews and refactors.",
    "10-architecture-system-design": "System design: scaling, microservices, event-driven, caching, replication, classic design interviews.",
    "11-testing-qa": "Unit/integration/E2E tests, mocking, Jest/Vitest/Playwright/Cypress/Pytest, coverage, test strategy.",
    "12-mobile-dev": "React Native, Flutter, Swift, Kotlin, Expo: push, offline sync, biometrics, camera, app store prep.",
    "13-ui-ux-design": "UI components, design systems, accessibility, Tailwind/CSS/Framer Motion, UX writing, wireframes.",
    "14-security": "OWASP hardening, auth security, XSS/CSRF/SQLi defenses, secrets, encryption, audits, threat models.",
    "15-data-science": "Pandas, scikit-learn, PyTorch, forecasting, churn/fraud models, EDA, dashboards with Streamlit/Plotly.",
    "16-documentation": "READMEs, API docs, ADRs, runbooks, onboarding guides, changelogs, docstrings, technical writing.",
    "17-performance": "Profiling and optimisation: web vitals, bundles, caching, DB queries, memory, Node/Go/Python runtime.",
    "18-devex-tooling": "Developer experience: devcontainers, monorepos, linters, git hooks, CLIs, Makefiles, env management.",
    "19-student-learning": "CS learning: explain concepts, algorithms, Big O, data structures, interview prep, practice problems.",
    "20-vibe-coding": "Ship fast: MVPs, prototypes, automations, weekend projects, launch checklists, AI-assisted workflows.",
}

# Readable placeholder names for the generator's {tech}/{target}/{feature} slots.
SLOT_LABELS = {
    "03-backend-dev": ("STACK", "SYSTEM", "FEATURE"),
    "04-fullstack-projects": ("STACK", "APP", "FEATURE"),
    "05-api-design": ("SPEC_FORMAT", "DOMAIN", "POLICY"),
    "06-database-design": ("DATABASE", "WORKLOAD", "CONCERN"),
    "07-devops-cicd": ("TOOL", "DEPLOY_TARGET", "PIPELINE_FEATURE"),
    "08-ai-ml-integration": ("AI_STACK", "USE_CASE", "OPTIMIZATION"),
    "09-debugging-code-review": ("BUG_CLASS", "COMPONENT", "EVIDENCE"),
    "10-architecture-system-design": ("SYSTEM", "SCALE_REQUIREMENT", "INFRA_COMPONENT"),
    "11-testing-qa": ("TEST_FRAMEWORK", "TEST_TARGET", "TEST_FEATURE"),
    "12-mobile-dev": ("PLATFORM", "NATIVE_FEATURE", "APP_TYPE"),
    "13-ui-ux-design": ("STYLING", "COMPONENT", "UX_REQUIREMENT"),
    "14-security": ("DEFENSE", "APP_STACK", "CONTROL"),
    "15-data-science": ("LIBRARY", "ML_TASK", "ML_FEATURE"),
    "16-documentation": ("DOC_TYPE", "SUBJECT", "DOC_SECTION"),
    "17-performance": ("BOTTLENECK", "TECHNIQUE", "GOAL"),
    "18-devex-tooling": ("TOOL", "AUTOMATION_TARGET", "DX_GOAL"),
    "19-student-learning": ("TOPIC", "STUDY_FORMAT", "FOCUS"),
    "20-vibe-coding": ("PROJECT_TYPE", "INTEGRATION", "APPROACH"),
}

SECTION_RE = re.compile(r"^## (🎯|📦|💡|🔗)\s*(.*)$")
PLACEHOLDER_RE = re.compile(r"\[[A-Z][A-Z0-9_ /&'.,-]*(?::[^\]\n]*)?\](?!\()")
BANNER_RE = re.compile(r"<img\b|<p\s+align|<div\s+align|!\[[^\]]*\]\([^)]*\)|\.gif\b", re.I)


# ── Parsing ────────────────────────────────────────────────────────────────────

def parse_scalar(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        return [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        return v[1:-1].replace('\\"', '"')
    return v


def parse_file(path):
    """Return (record, errors, warnings)."""
    errors, warnings = [], []
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, ["missing or malformed YAML frontmatter"], warnings
    fm = {}
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"unparseable frontmatter line: {line!r}")
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = parse_scalar(v)
    for key in ("title", "category", "models", "tags", "difficulty", "author", "tested"):
        if key not in fm:
            errors.append(f"frontmatter missing '{key}'")

    sections, current = {}, None
    for line in m.group(2).splitlines():
        sm = SECTION_RE.match(line)
        if sm:
            current = sm.group(1)
            sections[current] = []
        elif current:
            sections[current].append(line)

    prompt_body = ""
    if "🎯" not in sections:
        errors.append("missing '## 🎯 Prompt' section")
    else:
        lines = sections["🎯"]
        fences = [i for i, l in enumerate(lines) if l.startswith("```")]
        if len(fences) < 2:
            errors.append("prompt section has no fenced code block")
        else:
            # Outer fence = first and last fence lines; inner fences are prompt text.
            prompt_body = "\n".join(lines[fences[0] + 1:fences[-1]]).strip("\n")
            if not prompt_body.strip():
                errors.append("prompt code block is empty")

    produces = ""
    if "📦" in sections:
        produces = " ".join(l.lstrip("> ").strip() for l in sections["📦"]
                            if l.strip() and not BANNER_RE.search(l))
    else:
        warnings.append("missing '## 📦 What Claude Produces' section")

    tips = []
    if "💡" in sections:
        tips = [l.rstrip() for l in sections["💡"] if l.strip() and not BANNER_RE.search(l)]
    else:
        warnings.append("missing '## 💡 Tips & Variations' section")

    cat = path.parent.name
    record = {
        "id": f"{cat}/{path.stem}",
        "category": cat,
        "title": fm.get("title", path.stem),
        "tags": fm.get("tags", []) if isinstance(fm.get("tags"), list) else [fm.get("tags")],
        "difficulty": fm.get("difficulty", ""),
        "models": fm.get("models", []),
        "prompt_body": prompt_body,
        "produces": produces,
        "tips": tips,
        "placeholders": sorted(set(PLACEHOLDER_RE.findall(prompt_body))),
    }
    return (None if errors else record), errors, warnings


# ── Variant grouping ───────────────────────────────────────────────────────────

def load_generator_config():
    """Read CATEGORIES_CONFIG from the generator without executing it."""
    src = (ROOT / "scripts" / "generate_missing_prompts.py").read_text()
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "CATEGORIES_CONFIG":
            return ast.literal_eval(node.value)
    raise RuntimeError("CATEGORIES_CONFIG not found")


SLOT_KEYS = {"tech": "techs", "target": "targets", "targets": "targets",
             "feature": "features", "features": "features"}
SLOT_INDEX = {"techs": 0, "targets": 1, "features": 2}


def template_regex(template, cfg):
    parts, slots = [], []
    for literal, field, _, _ in string.Formatter().parse(template):
        parts.append(re.escape(literal))
        if field:
            key = SLOT_KEYS[field]
            opts = sorted(cfg[key], key=len, reverse=True)
            parts.append("(" + "|".join(re.escape(o) for o in opts) + ")")
            slots.append(key)
    return re.compile("^" + "".join(parts) + "$", re.S), slots


def fill_template(template, labels):
    names = {k: f"[{labels[SLOT_INDEX[v]]}]" for k, v in SLOT_KEYS.items()}
    return template.format(**names)


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return re.sub(r"-+", "-", s)


def group_variants(records, config):
    groups, singles = [], []
    by_cat = defaultdict(list)
    for r in records:
        by_cat[r["category"]].append(r)
    for cat, recs in sorted(by_cat.items()):
        cfg = config.get(cat)
        if not cfg:
            singles.extend(recs)
            continue
        labels = SLOT_LABELS[cat]
        # Match on the prompt body: older generator runs used shorter titles
        # (e.g. "Explain X to a CS student") with the same body template.
        matchers = [(t_title, t_body, *template_regex(t_body, cfg)) for t_title, t_body in cfg["templates"]]
        buckets = defaultdict(list)
        for r in recs:
            for t_title, t_body, bre, bslots in matchers:
                bm = bre.match(r["prompt_body"].strip())
                if bm:
                    values = defaultdict(set)
                    for key, val in zip(bslots, bm.groups()):
                        values[key].add(val)
                    buckets[(t_title, t_body)].append((r, values))
                    break
            else:
                singles.append(r)
        for (t_title, t_body), members in buckets.items():
            if len(members) < 2:
                singles.extend(m[0] for m in members)
                continue
            options = defaultdict(set)
            for _, vals in members:
                for k, v in vals.items():
                    options[k] |= v
            title = fill_template(t_title, labels)
            tags = []
            for r, _ in members:
                tags += [t for t in r["tags"] if t not in tags]
            groups.append({
                "id": f"{cat}/{slugify(title.replace('[', '').replace(']', ''))}",
                "category": cat,
                "title": title,
                "tags": tags,
                "difficulty": "/".join(sorted({r["difficulty"] for r, _ in members},
                                              key=["beginner", "intermediate", "advanced"].index)),
                "prompt_body": fill_template(t_body, labels),
                "options": [(labels[SLOT_INDEX[k]], sorted(options[k]))
                            for k in ("techs", "targets", "features") if options.get(k)],
                "tips": members[0][0]["tips"],
                "produces": "",
                "members": sorted(r["id"] for r, _ in members),
                "placeholders": sorted({f"[{labels[SLOT_INDEX[k]]}]" for k in options}),
            })
    return groups, singles


# ── Rendering ──────────────────────────────────────────────────────────────────

def fence_for(body):
    longest = max((len(m) for m in re.findall(r"`{3,}", body)), default=0)
    return "`" * max(4, longest + 1)


def render_entry(e):
    out = [f"## {e['title']}", ""]
    meta = f"**id:** `{e['id']}` · **Difficulty:** {e['difficulty']} · **Tags:** {', '.join(e['tags'])}"
    out += [meta, ""]
    if e.get("members"):
        out.append(f"**Variant group** ({len(e['members'])} generated prompts collapsed). Pick one value per placeholder:")
        out += [f"- `[{name}]`: {' | '.join(vals)}" for name, vals in e["options"]]
        out.append("")
    elif e["placeholders"]:
        out += [f"**Placeholders:** {', '.join(e['placeholders'])}", ""]
    fence = fence_for(e["prompt_body"])
    out += [fence + "text", e["prompt_body"], fence, ""]
    if e["produces"]:
        out += [f"**Produces:** {e['produces']}", ""]
    if e["tips"]:
        out += ["**Tips:**"] + e["tips"] + [""]
    if e.get("members"):
        out += ["**Covers:** " + ", ".join(m.split("/", 1)[1] for m in e["members"]), ""]
    return "\n".join(out) + "\n"


def write_references(entries_by_cat):
    """Write one file per category, splitting any over MAX_REF_BYTES. Returns {cat: [(file, [entries])]}."""
    layout = {}
    for cat, entries in entries_by_cat.items():
        chunks, cur, size = [], [], 0
        for e in entries:
            text = render_entry(e)
            n = len(text.encode())
            if cur and size + n > MAX_REF_BYTES - 2048:
                chunks.append(cur)
                cur, size = [], 0
            cur.append((e, text))
            size += n
        chunks.append(cur)
        files = []
        for i, chunk in enumerate(chunks):
            name = f"{cat}.md" if len(chunks) == 1 else f"{cat}-{'abcdefgh'[i]}.md"
            part = "" if len(chunks) == 1 else f" (part {i + 1} of {len(chunks)})"
            header = (f"# {cat}{part}\n\n{CATEGORY_BLURBS[cat]}\n\n"
                      f"{len(chunk)} prompts. Search `## ` headings or ids; see index.md for the one-line list.\n\n")
            (REF_DIR / name).write_text(header + "\n".join(t for _, t in chunk), encoding="utf-8")
            files.append((name, [e for e, _ in chunk]))
        layout[cat] = files
    return layout


def write_index(layout):
    lines = ["# Prompt index", "",
             "One line per prompt: `id | title | tags | difficulty`. "
             "Each `###` heading names the reference file holding those prompts. "
             "Titles containing `[PLACEHOLDERS]` are variant groups; their trailing `options:` column "
             "lists the values each placeholder can take.", ""]
    for cat, files in layout.items():
        lines += [f"## {cat}: {CATEGORY_BLURBS[cat]}", ""]
        for name, entries in files:
            lines += [f"### references/{name}", ""]
            for e in entries:
                line = f"{e['id']} | {e['title']} | {', '.join(e['tags'])} | {e['difficulty']}"
                if e.get("options"):
                    line += " | options: " + "; ".join(v for _, vals in e["options"] for v in vals)
                lines.append(line)
            lines.append("")
    (REF_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    files = sorted(PROMPTS_DIR.glob("*/*.md"))
    files = [f for f in files if f.name.lower() != "readme.md"]
    per_cat = defaultdict(int)
    records, failures, warnings = [], [], defaultdict(list)
    for f in files:
        per_cat[f.parent.name] += 1
        rec, errs, warns = parse_file(f)
        rel = str(f.relative_to(ROOT))
        if errs:
            failures.append((rel, errs))
        for w in warns:
            warnings[w].append(rel)
        if rec:
            records.append(rec)

    print("== 01 Inventory ==")
    for cat in sorted(per_cat):
        print(f"  {cat:32s} {per_cat[cat]:4d}")
    print(f"  {'TOTAL':32s} {len(files):4d}")
    print(f"  parsed OK: {len(records)}  failed: {len(failures)}")
    for rel, errs in failures:
        print(f"  FAIL {rel}: {'; '.join(errs)}")
    for w, rels in warnings.items():
        print(f"  WARN {len(rels)} files: {w}")

    groups, singles = group_variants(records, load_generator_config())
    grouped = sum(len(g["members"]) for g in groups)
    print("\n== 03 Dedupe ==")
    print(f"  prompts in: {len(records)}")
    print(f"  hand-written kept as-is: {len(singles)}")
    print(f"  generated variants: {grouped} -> {len(groups)} canonical groups")
    print(f"  prompts out: {len(singles) + len(groups)}")

    # SKILL.md and scripts/search.py are maintained by hand; only references/ is generated.
    if REF_DIR.exists():
        shutil.rmtree(REF_DIR)
    REF_DIR.mkdir(parents=True)

    entries_by_cat = defaultdict(list)
    for e in sorted(singles, key=lambda r: r["id"]) + sorted(groups, key=lambda g: g["id"]):
        entries_by_cat[e["category"]].append(e)
    layout = write_references(dict(sorted(entries_by_cat.items())))
    write_index(layout)
    (OUT_DIR / "records.json").write_text(json.dumps(
        {"prompts": records, "groups": groups, "failures": failures}, indent=1, ensure_ascii=False))

    print("\n== 09 Validate ==")
    ref_text = "".join(p.read_text() for p in REF_DIR.glob("[0-9]*.md"))
    present = set(re.findall(r"\*\*id:\*\* `([^`]+)`", ref_text))
    member_of = {m: g["id"] for g in groups for m in g["members"]}
    missing = []
    for r in records:
        slug = r["id"].split("/", 1)[1]
        if r["id"] in present:
            continue
        if r["id"] in member_of and member_of[r["id"]] in present and slug in ref_text:
            continue
        missing.append(r["id"])
    print(f"  coverage: {len(records) - len(missing)}/{len(records)} prompts present or in a variant group"
          f" ({len(present & {r['id'] for r in records})} verbatim, {len(member_of)} via groups)")
    for m in missing:
        print(f"  MISSING {m}")
    for p in sorted(REF_DIR.iterdir()):
        kb = p.stat().st_size / 1024
        print(f"  {p.name:36s} {kb:7.1f} KB{'  OVER LIMIT' if kb > 150 else ''}")

    zpath = OUT_DIR / "claude-cheatcodes.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(SKILL_DIR.rglob("*")):
            if p.is_file() and "__pycache__" not in p.parts:
                z.write(p, p.relative_to(OUT_DIR))
    print(f"\n  wrote {zpath.relative_to(ROOT)} ({zpath.stat().st_size / 1024:.0f} KB)")
    return 1 if missing or failures else 0


if __name__ == "__main__":
    sys.exit(main())
