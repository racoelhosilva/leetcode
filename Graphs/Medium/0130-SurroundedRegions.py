"""
LeetCode Problem: Surrounded Regions
Problem Number: 130
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/surrounded-regions/
"""

class Solution:
    # Depth First Search
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def solve(self, board):
        ROWS, COLS = len(board), len(board[0])
        directions = [0, 1, 0, -1, 0]

        def dfs(row, col):
            board[row][col] = "T"
            for i in range(4):
                new_row, new_col = row + directions[i], col + directions[i+1]
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and board[new_row][new_col] == "O":
                    dfs(new_row, new_col)

        for row in range(ROWS):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][COLS - 1] == "O":
                dfs(row, COLS - 1)
        
        for col in range(COLS):
            if board[0][col] == "O":
                dfs(0, col)
            if board[ROWS - 1][col] == "O":
                dfs(ROWS - 1, col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"

    # Breadth First Search
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def solve(self, board):
        from collections import deque
        
        ROWS, COLS = len(board), len(board[0])
        directions = [0, 1, 0, -1, 0]

        queue = deque()

        for row in range(ROWS):
            if board[row][0] == "O":
                queue.append((row, 0))
            if board[row][COLS - 1] == "O":
                queue.append((row, COLS - 1))
        
        for col in range(COLS):
            if board[0][col] == "O":
                queue.append((0, col))
            if board[ROWS - 1][col] == "O":
                queue.append((ROWS - 1, col))
        
        while queue:
            row, col = queue.popleft()
            board[row][col] = "T"
            for i in range(4):
                new_row, new_col = row + directions[i], col + directions[i+1]
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and board[new_row][new_col] == "O":
                    queue.append((new_row, new_col))

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"
