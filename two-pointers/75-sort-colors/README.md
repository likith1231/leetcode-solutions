# 75. Sort Colors

**Source:** https://leetcode.com/problems/sort-colors/ | **Topic:** two-pointers | **Difficulty:** Medium | **Solved:** 2026-07-25

## Approach
Dutch National Flag partition in one pass with three pointers: everything before `low` is 0, everything
after `high` is 2, and `mid` scans the unknown region. Swap 0s down to `low`, 2s up to `high`
(without advancing `mid`, since the swapped-in value is unchecked), and skip over 1s.

## Complexity
- Time: O(n)
- Space: O(1)
