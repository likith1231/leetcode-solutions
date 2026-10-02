# 35. Search Insert Position

**Source:** https://leetcode.com/problems/search-insert-position/ | **Topic:** binary-search | **Difficulty:** Easy | **Solved:** 2026-07-26

## Approach
Lower-bound binary search: find the first index whose value is >= `target`. If the target exists that is
its index; otherwise it's where the target would be inserted to keep the array sorted.

## Complexity
- Time: O(log n)
- Space: O(1)
