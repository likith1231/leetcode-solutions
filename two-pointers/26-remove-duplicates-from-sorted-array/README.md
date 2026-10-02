# 26. Remove Duplicates from Sorted Array

**Source:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/ | **Topic:** two-pointers | **Difficulty:** Easy | **Solved:** 2026-07-20

## Approach
Since the array is sorted, duplicates are adjacent. A write pointer `k` marks the end of the unique prefix;
a read pointer scans ahead and copies each value that differs from the last unique one written.

## Complexity
- Time: O(n)
- Space: O(1)
