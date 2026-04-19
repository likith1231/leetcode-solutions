# 509. Fibonacci Number

**Source:** https://leetcode.com/problems/fibonacci-number/ | **Topic:** dynamic-programming | **Difficulty:** Easy | **Solved:** 2026-04-19

## Approach
Bottom-up DP keeping only the last two values: start from F(0) = 0 and F(1) = 1 and roll the pair forward
`n` times. This avoids the exponential blow-up of naive recursion and the O(n) memo table.

## Complexity
- Time: O(n)
- Space: O(1)
