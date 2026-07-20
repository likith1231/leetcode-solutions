# 14. Longest Common Prefix

**Source:** https://leetcode.com/problems/longest-common-prefix/ | **Topic:** string | **Difficulty:** Easy | **Solved:** 2026-07-20

## Approach
Vertical scan: compare characters column by column using the first string as the reference. Stop at the
first column where some string ends or has a different character, and return the prefix up to there.

## Complexity
- Time: O(S) — S is the total number of characters
- Space: O(1) extra (besides the returned string)
