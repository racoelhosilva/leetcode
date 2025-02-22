"""
LeetCode Problem: Transpose Matrix
Problem Number: 867
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/transpose-matrix/
"""

class Solution:
    # Transpose
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def transpose(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        res = [[0] * rows for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                res[col][row] = matrix[row][col]
        return res
