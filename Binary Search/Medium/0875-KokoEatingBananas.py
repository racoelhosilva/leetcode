"""
LeetCode Problem: Koko Eating Bananas
Problem Number: 875
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/koko-eating-bananas/
"""

class Solution:
    # Binary Search
    # Time Complexity: O(n log m)
    # Space Complexity: O(1)
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2

            total = 0
            for pile in piles:
                total += (pile + m - 1) // m
            
            if total > h:
                l = m + 1
            else:
                res = m
                r = m - 1
        
        return res
