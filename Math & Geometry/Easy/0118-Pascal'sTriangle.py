"""
LeetCode Problem: Pascal's Triangle
Problem Number: 118
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/pascals-triangle/
"""

class Solution:
    # Combinatorics Formula
    # Time Complexity: O(n^3)
    # Space Complexity: O(n^2)
    def generate(self, numRows):
        res = []

        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n-1)

        for n in range(numRows):
            cur = []
            for k in range(n+1):
                cur.append(factorial(n) / (factorial(k) * factorial(n-k)))
            res.append(cur)
        return res
    
    # Top-Down Dynamic Programming
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        
        prev = self.generate(numRows-1)
        cur = [1] * numRows
        for idx in range(1, numRows-1):
            cur[idx] = prev[-1][idx-1] + prev[-1][idx]
        prev.append(cur)
        return prev

    # Bottom-Up Dynamic Programming
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)    
    def generate(self, numRows):
        res = []
        for n in range(numRows):
            cur = [1] * (n + 1)
            for k in range(1, n-1):
                cur[k] = res[n-1][k-1] + res[n-1][k]
            res.append(cur)
        return res
