"""
LeetCode Problem: Word Search
Problem Number: 79
Difficulty: Medium
Topic: Backtracking
Link: https://leetcode.com/problems/word-search/
"""

class Solution:
    # Backtrack Depth First Search
    # Time Complexity: O(m * n * (4 ^ l))
    # Space Complexity: O(l)
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def backtrack(row, col, idx):
            if idx >= len(word):
                return True
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or \
                board[row][col] != word[idx] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            if backtrack(row+1, col, idx + 1) or backtrack(row-1, col, idx + 1) or \
                backtrack(row, col+1, idx + 1) or backtrack(row, col-1, idx + 1):
                return True
            visited.remove((row, col))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False
    
    # Space Optimization
    # Space Complexity is still the same, but no visited set is needed
    # Instead we keep track of visited cells on the matrix itself
    # Time Complexity: O(m * n * (4 ^ l))
    # Space Complexity: O(l)
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])

        def backtrack(row, col, idx):
            if idx >= len(word):
                return True
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or \
                board[row][col] != word[idx] or board[row][col] == "":
                return False
            
            board[row][col] = ""
            if backtrack(row+1, col, idx + 1) or backtrack(row-1, col, idx + 1) or \
                backtrack(row, col+1, idx + 1) or backtrack(row, col-1, idx + 1):
                return True
            board[row][col] = word[idx]
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False
