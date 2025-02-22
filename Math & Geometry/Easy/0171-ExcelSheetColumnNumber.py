"""
LeetCode Problem: Excel Sheet Column Number
Problem Number: 171
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/excel-sheet-column-number/
"""

class Solution:
    def titleToNumber(self, columnTitle):
        res = 0
        for char in columnTitle:
            res *= 26
            res += ord(char) - ord('A') + 1
        return res
