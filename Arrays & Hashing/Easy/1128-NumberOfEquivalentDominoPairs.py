"""
LeetCode Problem: Number of Equivalent Domino Pairs
Problem Number: 1128
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
"""

class Solution:
    # Hash Table
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def numEquivDominoPairs(self, dominoes):
        seen = dict()
        res = 0
        for [f1, f2] in dominoes:
            piece = (f1, f2) if f1 <= f2 else (f2, f1)
            if piece in seen:
                res += seen[piece]
            seen[piece] = seen.get(piece, 0) + 1
        return res
