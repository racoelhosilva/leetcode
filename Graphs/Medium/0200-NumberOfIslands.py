"""
LeetCode Problem: Number of Islands
Problem Number: 200
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/number-of-islands/
"""

class Solution:
    # Depth First Search
    # This solution could be pruned by always searching left->right top->bottom
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def numIslands(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(r, c):
            grid[r][c] = "0"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == "0": 
                    continue
                dfs(nr, nc)

        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands
    
    # Breadth First Search
    # This solution could be pruned by always searching left->right top->bottom
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def numIslands(self, grid):
        from collections import deque
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == "0": 
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"

        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
        return islands
