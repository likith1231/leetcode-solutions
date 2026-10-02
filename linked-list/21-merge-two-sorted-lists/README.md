# 21. Merge Two Sorted Lists

**Source:** https://leetcode.com/problems/merge-two-sorted-lists/ | **Topic:** linked-list | **Difficulty:** Easy | **Solved:** 2026-07-26

## Approach
Use a dummy head and a tail pointer. Repeatedly attach the smaller of the two current nodes and advance
that list; once one list runs out, link the remainder of the other. Nodes are re-linked, not copied.

## Complexity
- Time: O(m + n)
- Space: O(1)
