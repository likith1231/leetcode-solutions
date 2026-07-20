# 202. Happy Number

**Source:** https://leetcode.com/problems/happy-number/ | **Topic:** math | **Difficulty:** Easy | **Solved:** 2026-07-20

## Approach
Repeatedly replacing a number by the sum of its digits' squares either reaches 1 or enters a cycle.
Detect the cycle with Floyd's tortoise and hare: advance `slow` one step and `fast` two steps until they
meet, then the number is happy exactly when they met at 1.

## Complexity
- Time: O(log n)
- Space: O(1)
