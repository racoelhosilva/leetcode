"""
LeetCode Problem: Excel Sheet Column Title
Problem Number: 168
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/excel-sheet-column-title/
"""

class Solution:
    # Iterative
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def convertToTitle(self, columnNumber):
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            res = chr(columnNumber % 26 + ord('A')) + res
            columnNumber //= 26
        return res
