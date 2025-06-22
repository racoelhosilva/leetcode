"""
LeetCode Problem: Divide a String Into Groups of Size k
Problem Number: 2138
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
"""

class Solution:
    # Traversal in k steps + Fill
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def divideString(self, s, k, fill):
        res = []
        i = 0
        while i < len(s):
            res.append(s[i:i+k])
            i += k
        res[-1] = res[-1] + fill * (k - len(res[-1]))
        return res
