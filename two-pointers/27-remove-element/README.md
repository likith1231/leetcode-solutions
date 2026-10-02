# 27. Remove Element

**Source:** https://leetcode.com/problems/remove-element/ | **Topic:** two-pointers | **Difficulty:** Easy | **Solved:** 2026-07-20

## Approach
Use a write pointer `k`: scan the array and copy every element not equal to `val` to position `k`.
The first `k` slots then hold the kept elements, and their order beyond that doesn't matter.

## Complexity
- Time: O(n)
- Space: O(1)
