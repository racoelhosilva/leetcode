"""
LeetCode Problem: Alternating Groups I
Problem Number: 3206
Difficulty: Easy
Topic: Sliding Window
Link: https://leetcode.com/problems/alternating-groups-i/
"""

class Solution:
    # Modulo Comparison
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def numberOfAlternatingGroups(self, colors):
        res = 0
        n = len(colors)
        for i in range(n):
            if (colors[i-1 % n] == colors[i+1 % n]) and (colors[i-1 % n] != colors[i]):
                res += 1
        return res
