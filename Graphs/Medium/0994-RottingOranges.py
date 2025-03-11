"""
LeetCode Problem: Rotting Oranges
Problem Number: 994
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/rotting-oranges/
"""

from collections import deque

class Solution:
    # Breadth First Search
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def orangesRotting(self, grid):
        directions = (0, -1, 0, 1, 0,)
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = 0
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                for idx in range(4):
                    nr, nc = r + directions[idx], c + directions[idx+1]

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            time += 1
        
        return time if fresh == 0 else -1
