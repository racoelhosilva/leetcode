"""
LeetCode Problem: Equal Row and Column Pairs
Problem Number: 2352
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/equal-row-and-column-pairs/
"""

class Solution:
    # Brute Force
    # Time Complexity: O(n ^ 3)
    # Space Complexity: O(1)
    def equalPairs(self, grid):
        n = len(grid)
        res = 0
        for r in range(n):
            for c in range(n):
                check = True
                for d in range(n):
                    if grid[r][d] != grid[d][c]:
                        check = False
                        break
                if check:
                    res += 1
        return res

    # Hash Comparison
    # Time Complexity: O(n ^ 2)
    # Space Complexity: O(n)
    def equalPairs(self, grid):
        n = len(grid)

        table = dict()
        res = 0
        for row in grid:
            table[str(row)] = table.get(str(row), 0) + 1
        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
            res += table.get(str(col), 0)
        return res
