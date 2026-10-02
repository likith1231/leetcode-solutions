# LeetCode Solutions — instructions for Claude

Java solutions to LeetCode problems, one folder per problem. The owner gives
problem names/numbers; Claude writes the solutions and commits them.

## Layout
```
<topic>/<number>-<slug>/
  Solution.java   # accepted LeetCode-style solution
  README.md       # metadata header + approach + complexity
scripts/new_problem.py     # scaffolds a problem folder, then regenerates README
scripts/update_readme.py   # regenerates root README.md from problem folders
```
Never edit the root `README.md` by hand — run `python3 scripts/update_readme.py`.

## Adding problems the owner already solved
For each problem the owner lists (name + number, optionally topic/difficulty/date):

1. Scaffold: `python3 scripts/new_problem.py <number> "<Exact LeetCode Title>" <topic> <Easy|Medium|Hard> --date <YYYY-MM-DD>`
   - Title and difficulty must match LeetCode exactly; the slug becomes the URL
     `https://leetcode.com/problems/<slug>/`, so check it is right (fix the Source line by hand if the official slug differs).
   - Topic: lowercase-hyphenated, reuse existing folders. Prefer: arrays, hashing, two-pointers,
     sliding-window, string, stack-queue, binary-search, linked-list, binary-tree, bst, heap,
     greedy, recursion, backtracking, graphs, dynamic-programming, bit-manipulation, math, trie, design.
   - Date: the date the owner gives; if none, use today.
2. `Solution.java`: replace the placeholder with a correct, optimal solution in `class Solution`
   using the exact LeetCode method signature. If the owner pastes their own code, use theirs as-is.
   Do not define `ListNode`/`TreeNode`/`Node` (LeetCode provides them) — leave a short comment with
   the definition, like LeetCode's template does. Clean, readable code, brief comments only where the trick isn't obvious.
3. `README.md`: replace the TODO with a 2–5 line Approach and real Time/Space complexity.
4. One commit per problem, backdated to the solve date so the contribution graph shows real days:
   ```bash
   python3 scripts/update_readme.py
   git add -A
   GIT_AUTHOR_DATE="<YYYY-MM-DD>T12:00:00" GIT_COMMITTER_DATE="<YYYY-MM-DD>T12:00:00" \
     git commit -m "Add solution: <Title> (<YYYY-MM-DD>)"
   ```
   Commit in chronological order (oldest first).
5. Push to `main` when done: `git push origin main`.

## Commit identity (required for GitHub contributions)
Commits must be authored as the owner, or they won't count on the contribution graph:
```bash
git config user.name "likith1231"
git config user.email "likithlu3@gmail.com"
```
Check with `git config user.email` before the first commit.

## Before pushing
- `python3 scripts/update_readme.py` runs cleanly and the README lists every problem.
- No duplicate problem numbers (`new_problem.py` refuses duplicates).
- Solutions are correct for LeetCode's constraints and edge cases.
