#!/usr/bin/env python3
"""
Generate the master INDEX.md from all prompt files.
Run: python3 scripts/generate_index.py
"""

import os
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
PROMPTS_DIR = ROOT / "prompts"
INDEX_FILE = ROOT / "INDEX.md"

CATEGORY_EMOJIS = {
    "01-vibe-coding": "🎨",
    "02-frontend-dev": "🖥️",
    "03-backend-dev": "⚙️",
    "04-fullstack-projects": "🏗️",
    "05-api-design": "🔌",
    "06-database-design": "🗄️",
    "07-devops-cicd": "🚀",
    "08-ai-ml-integration": "🤖",
    "09-debugging-code-review": "🐛",
    "10-architecture-system-design": "🏛️",
    "11-testing-qa": "✅",
    "12-mobile-dev": "📱",
    "13-ui-ux-design": "🎭",
    "14-security": "🔐",
    "15-data-science": "📊",
    "16-documentation": "📝",
    "17-performance": "⚡",
    "18-devex-tooling": "🛠️",
    "19-student-learning": "🎓",
    "20-vibe-coding": "🎨",
}

def parse_frontmatter(content):
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    fm = {}
    if match:
        lines = match.group(1).split('\n')
        for line in lines:
            if not line or ':' not in line:
                continue
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            if val.startswith('[') and val.endswith(']'):
                items = [item.strip() for item in val[1:-1].split(',') if item.strip()]
                fm[key] = items
            elif val.lower() == 'true':
                fm[key] = True
            elif val.lower() == 'false':
                fm[key] = False
            elif val.isdigit():
                fm[key] = int(val)
            else:
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                fm[key] = val
    return fm

def generate_index():
    lines = [
        "# 📚 Master Index — 1000 Claude Prompts\n",
        "> Auto-generated. Run `python3 scripts/generate_index.py` to refresh.\n\n",
        "| # | Category | Prompts |\n",
        "|---|----------|---------|\n",
    ]
    
    total = 0
    category_sections = []

    for cat_dir in sorted(PROMPTS_DIR.iterdir()):
        if not cat_dir.is_dir():
            continue
        
        emoji = CATEGORY_EMOJIS.get(cat_dir.name, "📌")
        prompt_files = sorted([f for f in cat_dir.glob("*.md") if f.name != "README.md"])
        count = len(prompt_files)
        total += count
        
        cat_name = cat_dir.name.replace("-", " ").title()
        lines.append(f"| {emoji} | [{cat_name}](prompts/{cat_dir.name}/README.md) | {count} |\n")
        
        section = [f"\n## {emoji} {cat_name}\n\n"]
        for i, pf in enumerate(prompt_files, 1):
            fm = parse_frontmatter(pf.read_text())
            title = fm.get("title", pf.stem.replace("-", " ").title())
            difficulty = fm.get("difficulty", "")
            tags = ", ".join(fm.get("tags", []))
            section.append(f"{i}. [{title}](prompts/{cat_dir.name}/{pf.name})")
            if difficulty:
                section[-1] += f" `{difficulty}`"
            if tags:
                section[-1] += f" — _{tags}_"
            section.append("\n")
        category_sections.extend(section)

    lines.append(f"\n**Total: {total} prompts**\n")
    lines.extend(category_sections)
    
    INDEX_FILE.write_text("".join(lines))
    print(f"✅ INDEX.md generated with {total} prompts.")

if __name__ == "__main__":
    generate_index()
