# 88. Merge Sorted Array

**Source:** https://leetcode.com/problems/merge-sorted-array/ | **Topic:** two-pointers | **Difficulty:** Easy | **Solved:** 2026-07-22

## Approach
Merge from the back: compare the largest remaining elements of both arrays and write the bigger one into
the last free slot of `nums1`. Filling from the end never overwrites unread values, and any leftovers in
`nums1` are already in place.

## Complexity
- Time: O(m + n)
- Space: O(1)
