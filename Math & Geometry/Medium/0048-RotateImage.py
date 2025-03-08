"""
LeetCode Problem: Rotate Image
Problem Number: 48
Difficulty: Medium
Topic: Math & Geometry
Link: https://leetcode.com/problems/rotate-image/
"""

class Solution:
    # Quadrant + 4 Swaps
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def rotate(self, matrix):
        N = len(matrix)
        for i in range(N // 2):
            for j in range(N - N // 2):
                matrix[i][j], matrix[N-j-1][i], matrix[N-i-1][N-j-1], matrix[j][N-i-1] = \
                              matrix[N-j-1][i], matrix[N-i-1][N-j-1], matrix[j][N-i-1], matrix[i][j]

    # Reverse (Horizontally) + Transpose
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)    
    def rotate(self, matrix):
        matrix.reverse()
        N = len(matrix)
        for i in range(N):
            for j in range(i+1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
