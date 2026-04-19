# 9. Palindrome Number

**Source:** https://leetcode.com/problems/palindrome-number/ | **Topic:** math | **Difficulty:** Easy | **Solved:** 2026-04-19

## Approach
Negative numbers and non-zero numbers ending in 0 can't be palindromes. Otherwise, reverse only the
second half of the digits by popping from `x` until the reversed half is at least as large as what remains.
The number is a palindrome if the halves match (dropping the middle digit for odd lengths).

## Complexity
- Time: O(log n) — half of the digits are processed
- Space: O(1)
