# 4. Median of Two Sorted Arrays

**Source:** https://leetcode.com/problems/median-of-two-sorted-arrays/ | **Topic:** binary-search | **Difficulty:** Hard | **Solved:** 2026-07-20

## Approach
Binary search a partition on the shorter array so that the left halves of both arrays together hold
half the elements. A partition is valid when every element on the left is <= every element on the right;
then the median comes from the max of the left side and/or the min of the right side.

## Complexity
- Time: O(log(min(m, n)))
- Space: O(1)
