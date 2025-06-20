"""
LeetCode Problem: Maximum Manhattan Distance After K Changes
Problem Number: 3443
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/
"""

class Solution:
    # Greedy
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxDistance(self, s, k):
        x = y = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "N":
                y += 1
            elif s[i] == "S":
                y -= 1
            elif s[i] == "E":
                x += 1
            elif s[i] == "W":
                x -= 1
            res = max(res, min(abs(x) + abs(y) + 2 * k, i + 1))
        return res
