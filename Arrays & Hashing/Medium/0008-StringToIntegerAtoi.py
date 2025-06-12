"""
LeetCode Problem: String to Integer atoi
Problem Number: 8
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/string-to-integer-atoi/
"""

class Solution:
    # Single Traversal
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def myAtoi(self, s):
        MAX = 2 ** 31 - 1
        MIN = - 2 ** 31
        n = len(s)
        idx = 0
        res = 0

        while idx < n and s[idx] == ' ':
            idx += 1
        if idx == n:
            return res
        
        sign = 1
        if s[idx] == '-':
            sign = -1
            idx += 1
        elif s[idx] == '+':
            idx += 1
        if idx == n:
            return res
        
        while idx < n and s[idx].isdigit():
            res = res * 10 + (ord(s[idx]) - ord('0'))
            if res * sign > MAX:
                return MAX
            if res * sign < MIN:
                return MIN
            idx += 1

        return res
