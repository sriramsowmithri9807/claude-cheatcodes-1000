#!/usr/bin/env python3
"""Search the claude-cheatcodes prompt index by keyword and tag.

Usage:
    python3 scripts/search.py "react performance"
    python3 scripts/search.py "jwt auth api" -n 10
    python3 scripts/search.py "terraform" -c 07

Standard library only. Reads references/index.md next to this script.
"""
import argparse
import math
import re
import sys
from collections import Counter
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "references" / "index.md"

STOPWORDS = {"a", "an", "the", "for", "to", "of", "in", "on", "with", "and", "or", "my",
             "me", "i", "how", "do", "can", "you", "using", "use", "build", "create",
             "make", "write", "set", "up", "prompt", "app", "want", "need", "help", "is"}

# Light synonym expansion: query token -> extra tokens that count as matches.
SYNONYMS = {
    "jwt": ["auth", "token", "authentication"],
    "auth": ["authentication", "login", "jwt", "oauth"],
    "login": ["auth", "authentication"],
    "k8s": ["kubernetes"],
    "kubernetes": ["k8s"],
    "postgres": ["postgresql", "sql"],
    "postgresql": ["postgres", "sql"],
    "db": ["database"],
    "ci": ["cicd", "pipeline", "github-actions"],
    "cd": ["cicd", "deploy"],
    "rag": ["retrieval", "retrieval-augmented", "embeddings", "vector"],
    "llm": ["ai", "claude", "llm"],
    "perf": ["performance"],
    "optimize": ["optimization", "performance"],
    "speed": ["performance"],
    "slow": ["performance", "optimization"],
    "test": ["testing", "tests"],
    "tests": ["testing", "test"],
    "docs": ["documentation"],
    "bigo": ["big-o", "complexity", "algorithms"],
    "iac": ["terraform", "infrastructure"],
    "ts": ["typescript"],
    "js": ["javascript"],
}

FIELD_WEIGHTS = {"tags": 4.0, "title": 3.0, "id": 2.0, "options": 2.0, "category": 1.0}


def tokens(text):
    out = []
    for t in re.findall(r"[a-z0-9][a-z0-9+#.]*", text.lower()):
        t = t.strip(".")
        if len(t) > 3 and t.endswith("s") and not t.endswith("ss"):
            t = t[:-1]
        out.append(t)
    return out


def load_index():
    entries, category, ref_file = [], None, None
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            category = line[3:].split(":", 1)[0].strip()
        elif line.startswith("### "):
            ref_file = line[4:].strip()
        elif " | " in line and category:
            parts = [p.strip() for p in line.split(" | ")]
            options = parts.pop()[len("options:"):] if parts[-1].startswith("options:") else ""
            if len(parts) < 4:
                continue
            pid, title, tags, difficulty = parts[0], " | ".join(parts[1:-2]), parts[-2], parts[-1]
            tag_list = [t.strip() for t in tags.split(",") if t.strip()]
            entries.append({
                "id": pid, "title": title, "tags": tag_list, "difficulty": difficulty,
                "category": category, "file": ref_file,
                "f_tags": set(tokens(" ".join(tag_list))) | {t.lower() for t in tag_list},
                "f_title": set(tokens(title)),
                "f_id": set(tokens(pid.split("/", 1)[-1].replace("-", " "))),
                "f_category": set(tokens(category.replace("-", " "))),
                "f_options": set(tokens(options)),
                "title_lc": title.lower(),
            })
    return entries


def document_frequency(entries):
    df = Counter()
    for e in entries:
        df.update(set().union(*(e["f_" + f] for f in FIELD_WEIGHTS)))
    return df


def score(entry, query_terms, phrase, idf):
    """Sum of best field weight per query term, scaled by term rarity and coverage."""
    if not query_terms:
        return 0.0
    total, matched = 0.0, 0
    for term, alts in query_terms:
        best = 0.0
        for field, weight in FIELD_WEIGHTS.items():
            bag = entry["f_" + field]
            if term in bag:
                best = max(best, weight * idf(term))
            else:
                hits = [idf(a) for a in alts if a in bag]
                if hits:
                    best = max(best, weight * 0.6 * max(hits))
        if best:
            matched += 1
        total += best
    total *= 0.4 + 0.6 * matched / len(query_terms)   # favour entries matching every term
    if phrase and phrase in entry["title_lc"]:
        total += 5.0
    if "[" in entry["title"]:
        total *= 0.9                 # small preference for hand-written prompts
    return total


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="+")
    ap.add_argument("-n", type=int, default=5, help="number of results (default 5)")
    ap.add_argument("-c", "--category", help="restrict to a category prefix, e.g. 07 or devops")
    args = ap.parse_args(argv)

    query = " ".join(args.query)
    raw = [t for t in tokens(query) if t not in STOPWORDS]
    if re.search(r"\bbig[\s-]?o\b", query.lower()):
        raw = [t for t in raw if t not in ("big", "o")] + ["big", "o"]
    raw = [t for t in raw if len(t) > 1 or t == "o"]
    query_terms = [(t, SYNONYMS.get(t, [])) for t in dict.fromkeys(raw)]
    phrase = " ".join(w for w in query.lower().split() if w not in STOPWORDS)

    entries = load_index()
    if args.category:
        entries = [e for e in entries if args.category.lower() in e["category"].lower()]
    df = document_frequency(entries)
    idf = lambda t: 1.0 + math.log(len(entries) / (1 + df[t]))
    ranked = sorted(((score(e, query_terms, phrase, idf), e) for e in entries), key=lambda x: -x[0])
    ranked = [(s, e) for s, e in ranked if s > 0][: args.n]

    if not ranked:
        print(f'No matches for "{query}". Browse references/index.md by category instead.')
        return 1
    print(f'Top {len(ranked)} matches for "{query}":\n')
    for i, (s, e) in enumerate(ranked, 1):
        kind = "  [variant group]" if "[" in e["title"] else ""
        print(f"{i}. {e['title']}{kind}")
        print(f"   id:   {e['id']}   ({e['difficulty']}, score {s:.1f})")
        print(f"   open: {e['file']}")
        print(f"   tags: {', '.join(e['tags'][:8])}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
