# 1. Two Sum

**Source:** https://leetcode.com/problems/two-sum/ | **Topic:** hashing | **Difficulty:** Easy | **Solved:** 2026-07-20

## Approach
Walk the array once, storing each value's index in a hash map. For each element, check whether its
complement `target - nums[i]` was already seen; if so, return both indices.

## Complexity
- Time: O(n)
- Space: O(n)
