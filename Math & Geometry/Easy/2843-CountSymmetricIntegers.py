"""
LeetCode Problem: Count Symmetric Integers
Problem Number: 2843
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/count-symmetric-integers/
"""

class Solution:
    # Enumeration
    # Since the integers have 2 * n digits, they either have 2 or 4 digits
    # Time Complexity: O(h - l)
    # Space Complexity: O(1)
    def countSymmetricIntegers(self, low, high):
        res = 0
        for num in range(low, high + 1):
            if 10 < num < 100 and num % 11 == 0:
                res += 1
            elif 1000 < num < 10000:
                l = num // 1000 + (num % 1000) // 100
                r = (num % 100) // 10 + (num % 10)
                if l == r:
                    res += 1
        return res
