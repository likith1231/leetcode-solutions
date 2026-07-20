# 3. Longest Substring Without Repeating Characters

**Source:** https://leetcode.com/problems/longest-substring-without-repeating-characters/ | **Topic:** sliding-window | **Difficulty:** Medium | **Solved:** 2026-07-20

## Approach
Sliding window over the string, remembering the last index where each character appeared. When the
current character was last seen inside the window, jump the left edge just past that occurrence.
The answer is the largest window size seen.

## Complexity
- Time: O(n)
- Space: O(1) — fixed 128-entry table for ASCII
