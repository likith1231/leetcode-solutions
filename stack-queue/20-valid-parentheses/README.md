# 20. Valid Parentheses

**Source:** https://leetcode.com/problems/valid-parentheses/ | **Topic:** stack-queue | **Difficulty:** Easy | **Solved:** 2026-07-23

## Approach
Push the expected closing bracket whenever an opening bracket appears. For a closing bracket, the stack
must be non-empty and its top must be exactly that bracket. The string is valid if the stack ends empty.

## Complexity
- Time: O(n)
- Space: O(n)
