"""
LeetCode Problem: N Queens
Problem Number: 51
Difficulty: Hard
Topic: Backtracking
Link: https://leetcode.com/problems/n-queens/
"""

class Solution:
    # Backtracking
    # Time Complexity: O(n!)
    # Space Complexity: O(n^2)
    def solveNQueens(self, n):
        res = []
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
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        backtrack(0)
        return res
    
    # Backtracking with Hash Set
    # Time Complexity: O(n!)
    # Space Complexity: O(n^2)
    def solveNQueens(self, n):
        cols = set()
        positives = set()
        negatives = set()
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row + col) in positives or (row - col) in negatives:
                    continue
                
                cols.add(col)
                positives.add(row + col)
                negatives.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)
                
                board[row][col] = "."
                negatives.remove(row - col)
                positives.remove(row + col)
                cols.remove(col)

        backtrack(0)
        return res
    
    # Backtracking with Bitmask
    # Time Complexity: O(n!)
    # Space Complexity: O(n^2)
    def solveNQueens(self, n):
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row, cols, positives, negatives):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if cols & (1 << col) or positives & (1 << (row + col)) or negatives & (1 << (row - col + n)):
                    continue
                
                cols ^= 1 << col
                positives ^= 1 << (row + col)
                negatives ^= 1 << (row - col + n)
                board[row][col] = "Q"

                backtrack(row + 1, cols, positives, negatives)
                
                board[row][col] = "."
                negatives ^= 1 << (row - col + n)
                positives ^= 1 << (row + col)
                cols ^= 1 << col

        backtrack(0, 0, 0, 0)
        return res
