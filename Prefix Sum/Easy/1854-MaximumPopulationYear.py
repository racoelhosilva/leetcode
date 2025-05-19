"""
LeetCode Problem: Maximum Population Year
Problem Number: 1854
Difficulty: Easy
Topic: Prefix Sum
Link: https://leetcode.com/problems/maximum-population-year/
"""

class Solution:
    # Sweep Line
    # Time Complexity: O(n + k)
    # Space Complexity: O(100) -> O(1)
    def maximumPopulation(self, logs):
        from collections import defaultdict
        
        changes = defaultdict(int)
        for birth, death in logs:
            changes[birth] += 1
            changes[death] -= 1
        
        mx, res = -1, -1
        cur = 0
        
        for year in range(1950, 2051):
            cur += changes[year]
            if cur > mx:
                mx = cur
                res = year
        return res
