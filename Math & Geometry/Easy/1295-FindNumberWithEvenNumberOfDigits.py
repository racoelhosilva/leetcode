"""
LeetCode Problem: Find Number with Even Number of Digits
Problem Number: 1295
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/find-number-with-even-number-of-digits/
"""

class Solution:
    # Constraint Analysis
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findNumbers(self, nums):
        res = 0
        for num in nums:
            if 10 <= num < 100 or 1000 <= num < 10000 or num == 100000:
                res += 1
        return res
