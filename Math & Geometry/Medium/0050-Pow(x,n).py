"""
LeetCode Problem: Pow(x, n)
Problem Number: 50
Difficulty: Medium
Topic: Math & Geometry
Link: https://leetcode.com/problems/powx-n/
"""

class Solution:
    # Linear Approach
    # Time Complexity: O(n) -> TLE
    # Space Complexity: O(1)
    def myPow(self, x, n):
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x = 1/x
            n = -n
        while n > 0:
            res *= x
            n -= 1
        return res

    # Exponential Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def myPow(self, x, n):
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x = 1/x
            n = -n
        while n > 0:
            if (n & 1):
                res *= x
            x *= x
            n >>= 1
        return res
