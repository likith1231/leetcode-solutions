# 53. Maximum Subarray

**Source:** https://leetcode.com/problems/maximum-subarray/ | **Topic:** dynamic-programming | **Difficulty:** Medium | **Solved:** 2026-07-25

## Approach
Kadane's algorithm: the best subarray ending at index `i` either extends the best one ending at `i - 1`
or starts fresh at `nums[i]`, whichever is larger. Track the maximum of these running values.

## Complexity
- Time: O(n)
- Space: O(1)
