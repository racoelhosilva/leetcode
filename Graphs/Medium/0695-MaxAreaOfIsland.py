"""
LeetCode Problem: Max Area of Island
Problem Number: 695
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/max-area-of-island/
"""

class Solution:
    # Depth First Search
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def maxAreaOfIsland(self, grid):
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r-1,c) + dfs(r,c-1) + dfs(r+1,c) + dfs(r,c+1)

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res

    # Breadth First Search
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def maxAreaOfIsland(self, grid):
        from collections import deque
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def bfs(r, c):
            res = 1
            queue = deque()
            queue.append((r,c))
            grid[r][c] = 0

            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 0:
                        continue
                    res += 1
                    queue.append((nr, nc))
                    grid[nr][nc] = 0
            return res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res
