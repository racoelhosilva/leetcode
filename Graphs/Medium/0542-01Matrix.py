"""
LeetCode Problem: 01 Matrix
Problem Number: 542
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/01-matrix/
"""

class Solution:
    # Breadth First Search
    # Search from all the 0 nodes to the rest of the matrix
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def updateMatrix(self, mat):
        from collections import deque
        
        ROWS,COLS = len(mat), len(mat[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1
        
        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr,nc))
        
        return mat

    # Dynamic Programming
    # Initially search up->down left->right and then down->up right->left
    # Time Complexity: O(m * n)
    # Space Complexity: O(1)
    def updateMatrix(self, mat):
        ROWS,COLS = len(mat), len(mat[0])
        INF = float("inf") 
        
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] > 0:
                    up = mat[r-1][c] if r > 0 else INF
                    left = mat[r][c-1] if c > 0 else INF
                    mat[r][c] = min(up, left) + 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if mat[r][c] > 0:
                    down = mat[r+1][c] if r < ROWS - 1 else INF
                    right = mat[r][c+1] if c < COLS - 1 else INF
                    mat[r][c] = min(mat[r][c], down + 1, right + 1)

        return mat
