# 7. Reverse Integer

**Source:** https://leetcode.com/problems/reverse-integer/ | **Topic:** math | **Difficulty:** Medium | **Solved:** 2026-07-20

## Approach
Pop the last digit with `% 10` and push it onto the result with `* 10 +`. Before each push, check that
the result won't leave the 32-bit range (only 64-bit storage is disallowed), returning 0 on overflow.
Java's truncating `%` and `/` handle negative numbers without special cases.

## Complexity
- Time: O(log |x|)
- Space: O(1)
