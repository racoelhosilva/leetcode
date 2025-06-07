"""
LeetCode Problem: Distribute Candies Among Children II
Problem Number: 2929
Difficulty: Medium
Topic: Math & Geometry
Link: https://leetcode.com/problems/distribute-candies-among-children-ii/
"""

class Solution:
    # Setting 1 barrier + Math
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def distributeCandies(self, n, limit):
        res = 0
        for i in range(min(limit, n)+1):
            if n - i > 2 * limit:
                continue
            res += min(limit, n - i) + 1 - max(0, n - i - limit)
        return res
    
    # Math: Inclusion-Exclusion Principle
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def distributeCandies(self, n, limit):
        def aux(n):
            if n <= 0:
                return 0
            return n * (n - 1) // 2
        return aux(n + 2) \
            - 3 * aux(n + 2 - (limit + 1)) \
            + 3 * aux(n + 2 - 2 * (limit + 1)) \
            - aux(n + 2 - 3 * (limit + 1))
