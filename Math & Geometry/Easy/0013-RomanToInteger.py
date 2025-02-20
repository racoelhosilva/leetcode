"""
LeetCode Problem: Roman to Integer
Problem Number: 13
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    # Hash Map
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def romanToInt(self, s):
        convert = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res = 0
        for idx in range(len(s)):
            if idx < len(s) - 1 and convert[s[idx]] < convert[s[idx+1]]:
                res -= convert[s[idx]]
            else:
                res += convert[s[idx]]
        return res