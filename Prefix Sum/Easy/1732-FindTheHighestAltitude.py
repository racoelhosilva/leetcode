"""
LeetCode Problem: Find the Highest Altitude
Problem Number: 1732
Difficulty: Easy
Topic: Prefix Sum
Link: https://leetcode.com/problems/find-the-highest-altitude/
"""

class Solution:
    def largestAltitude(self, gain):
        res = cur = 0
        for g in gain:
            cur += g
            res = max(res, cur)
        return res
