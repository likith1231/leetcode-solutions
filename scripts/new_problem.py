#!/usr/bin/env python3
"""Scaffold a new LeetCode problem folder.

Usage:
    python3 scripts/new_problem.py <number> "<title>" <topic> <Easy|Medium|Hard> [--date YYYY-MM-DD]

Example:
    python3 scripts/new_problem.py 1 "Two Sum" arrays Easy

Creates <topic>/<number>-<slug>/ with a README.md and Solution.java,
then regenerates the root README.
"""
import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIFFICULTIES = ("Easy", "Medium", "Hard")


def slugify(title: str) -> str:
    slug = title.lower().replace("'", "")
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("number", type=int)
    parser.add_argument("title")
    parser.add_argument("topic", help="folder name, e.g. arrays, binary-search, dynamic-programming")
    parser.add_argument("difficulty", type=str.capitalize, choices=DIFFICULTIES)
    parser.add_argument("--date", default=datetime.date.today().isoformat(), help="date solved (YYYY-MM-DD)")
    args = parser.parse_args()

    slug = slugify(args.title)
    topic = slugify(args.topic)
    folder = ROOT / topic / f"{args.number}-{slug}"

    existing = [p for p in ROOT.glob(f"*/{args.number}-*") if p.is_dir()]
    if existing:
        print(f"Problem {args.number} already exists at {existing[0].relative_to(ROOT)}", file=sys.stderr)
        return 1

    folder.mkdir(parents=True)
    (folder / "README.md").write_text(
        f"# {args.number}. {args.title}\n\n"
        f"**Source:** https://leetcode.com/problems/{slug}/ | **Topic:** {topic} | "
        f"**Difficulty:** {args.difficulty} | **Solved:** {args.date}\n\n"
        "## Approach\n"
        "TODO: explain the idea in a few lines.\n\n"
        "## Complexity\n"
        "- Time: O(?)\n"
        "- Space: O(?)\n"
    )
    (folder / "Solution.java").write_text(
        "class Solution {\n"
        "    // Paste your accepted LeetCode solution here.\n"
        "}\n"
    )

    subprocess.run([sys.executable, str(ROOT / "scripts" / "update_readme.py")], check=True)
    print(f"Created {folder.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
