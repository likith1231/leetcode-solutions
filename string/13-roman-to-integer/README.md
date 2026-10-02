# 13. Roman to Integer

**Source:** https://leetcode.com/problems/roman-to-integer/ | **Topic:** string | **Difficulty:** Easy | **Solved:** 2026-07-23

## Approach
Map each symbol to its value and scan left to right. A symbol smaller than the one after it is a
subtractive pair (e.g. IV, CM), so subtract it; otherwise add it.

## Complexity
- Time: O(n)
- Space: O(1)
