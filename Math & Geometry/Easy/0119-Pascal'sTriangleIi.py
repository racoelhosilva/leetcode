"""
LeetCode Problem: Pascal's Triangle II
Problem Number: 119
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/pascals-triangle-ii/
"""

class Solution:
    # Top-Down Dynamic Programming
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        
        prev = self.getRow(rowIndex-1)
        cur = [1] * (rowIndex+1)
        for idx in range(1, rowIndex):
            cur[idx] = prev[idx-1] + prev[idx]
        return cur
    
    # Bottom-Up Dynamic Programming
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def getRow(self, rowIndex):
        row = [1]
        for n in range(1, rowIndex + 1):
            row.append(1)
            for k in range(n-1, 0, -1):
                row[k] += row[k-1]
        return row
    
    # Combinatorics Formula
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def getRow(self, rowIndex):
        res = []

        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n-1)

        for k in range(rowIndex+1):
            res.append(factorial(rowIndex) / (factorial(k) * factorial(rowIndex-k)))
        return res

    # Pre-Computed Factorials
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def getRow(self, rowIndex):
        res = []

        factorial = [1]
        for r in range(1, rowIndex+1):
            factorial.append(factorial[r-1] * r)

        for k in range(rowIndex+1):
            res.append(factorial[rowIndex] / (factorial[k] * factorial[rowIndex-k]))
        return res

    # Combinatorics Property
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def getRow(self, rowIndex):
        res = [1]
        for k in range(1, rowIndex+1):
            res.append(res[k-1] * (rowIndex - k + 1) // (k))
        return res
