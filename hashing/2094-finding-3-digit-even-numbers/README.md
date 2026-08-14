# 2094. Finding 3-Digit Even Numbers

**Source:** https://leetcode.com/problems/finding-3-digit-even-numbers/ | **Topic:** hashing | **Difficulty:** Easy | **Solved:** 2026-08-14

## Approach
Count how many times each digit 0–9 is available. Then try every even number from 100 to 998 in
increasing order and keep it if its three digits can be taken from the counts. This checks only 450
candidates and yields a sorted, duplicate-free result directly.

## Complexity
- Time: O(n) — counting the digits, plus a constant 450 candidates
- Space: O(1) extra (besides the output)
