"""
LeetCode Problem: Spiral Matrix
Problem Number: 54
Difficulty: Medium
Topic: Math & Geometry
Link: https://leetcode.com/problems/spiral-matrix/
"""

class Solution:
    # Simulation
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def spiralOrder(self, matrix):
        res = []
        op = 0
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        while l <= r and t <= b:
            match op % 4:
                case 0:
                    for idx in range(l, r + 1):
                        res.append(matrix[t][idx])
                    t += 1
                case 1:
                    for idx in range(t, b + 1):
                        res.append(matrix[idx][r])
                    r -= 1
                case 2:
                    for idx in range(r, l - 1, -1):
                        res.append(matrix[b][idx])
                    b -= 1
                case 3:
                    for idx in range(b, t - 1, -1):
                        res.append(matrix[idx][l])
                    l += 1
            op += 1
        return res
