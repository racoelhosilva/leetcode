"""
LeetCode Problem: Minimum Recolors to Get K Consecutive Black Blocks
Problem Number: 2379
Difficulty: Easy
Topic: Sliding Window
Link: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
"""

class Solution:
    # Sliding Window (Two Loops)
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minimumRecolors(self, blocks, k):
        res = k
        cur = 0
        l = 0
        for r in range(k):
            if blocks[r] == 'W':
                cur += 1
        res = min(res, cur)
        for r in range(k, len(blocks)):
            if blocks[r] == 'W':
                cur += 1
            if blocks[l] == 'W':
                cur -= 1
            res = min(res, cur)
            l += 1
        return res

    # Sliding Window (One Loop)
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minimumRecolors(self, blocks, k):
        res = k
        cur = 0
        l = 0
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                cur += 1
            if r - l + 1 == k:
                res = min(res, cur)
                if blocks[l] == 'W':
                    cur -= 1
                l += 1
        return res
