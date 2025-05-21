"""
LeetCode Problem: Set Matrix Zeroes
Problem Number: 73
Difficulty: Medium
Topic: Math & Geometry
Link: https://leetcode.com/problems/set-matrix-zeroes/
"""

class Solution:
    # Naive Approach
    # Time Complexity: O(n * m)
    # Space Complexity: O(n + m)
    def setZeroes(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in range(ROWS):
            for c in range(COLS):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0

    # Optimized
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)
    def setZeroes(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        row0 = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row0 = True
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if row0:
            for c in range(COLS):
                matrix[0][c] = 0
