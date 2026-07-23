# 28. Find the Index of the First Occurrence in a String

**Source:** https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ | **Topic:** string | **Difficulty:** Easy | **Solved:** 2026-07-23

## Approach
KMP: build the longest-proper-prefix-that-is-also-suffix (LPS) table for `needle`, then scan `haystack`
once. On a mismatch, fall back in `needle` using the LPS table instead of restarting, so no character of
`haystack` is re-read.

## Complexity
- Time: O(n + m)
- Space: O(m) for the LPS table
