"""
LeetCode Problem: N Queens II
Problem Number: 52
Difficulty: Hard
Topic: Backtracking
Link: https://leetcode.com/problems/n-queens-ii/
"""

class Solution:
    # Backtracking
    # Time Complexity: O(n!)
    # Space Complexity: O(n^2)
    def totalNQueens(self, n):
        board = [["."] * n for _ in range(n)]

        def is_valid(row, col):
            for r in range(row):
                if board[r][col] == "Q":
                    return False
                if col + (row - r) < n and board[r][col + (row - r)] == "Q":
                    return False
                if col - (row - r) >= 0 and board[r][col - (row - r)] == "Q":
                    return False
            return True

        def backtrack(row):
            if row == n:
                return 1

            res = 0
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = "Q"
                    res += backtrack(row + 1)
                    board[row][col] = "."
            return res
        return backtrack(0)
    
    # Backtracking with Hash Set
    # Time Complexity: O(n!)
    # Space Complexity: O(n)
    def totalNQueens(self, n):
        cols = set()
        positives = set()
        negatives = set()

        def backtrack(row):
            if row == n:
                return 1

            res = 0
            for col in range(n):
                if col in cols or (row + col) in positives or (row - col) in negatives:
                    continue
                
                cols.add(col)
                positives.add(row + col)
                negatives.add(row - col)

                res += backtrack(row + 1)
                
                negatives.remove(row - col)
                positives.remove(row + col)
                cols.remove(col)

            return res
        return backtrack(0)
    
    # Backtracking with Bitmask
    # Time Complexity: O(n!)
    # Space Complexity: O(n)
    def totalNQueens(self, n):
        def backtrack(row, cols, positives, negatives):
            if row == n:
                return 1

            res = 0
            for col in range(n):
                if cols & (1 << col) or positives & (1 << (row + col)) or negatives & (1 << (row - col + n)):
                    continue
                
                cols ^= 1 << col
                positives ^= 1 << (row + col)
                negatives ^= 1 << (row - col + n)

                res += backtrack(row + 1, cols, positives, negatives)
                
                negatives ^= 1 << (row - col + n)
                positives ^= 1 << (row + col)
                cols ^= 1 << col
            
            return res
        return backtrack(0, 0, 0, 0)
