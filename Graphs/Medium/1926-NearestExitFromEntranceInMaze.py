"""
LeetCode Problem: Nearest Exit from Entrance in Maze
Problem Number: 1926
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
"""

class Solution:
    # Breadth First Search
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def nearestExit(self, maze, entrance):
        from collections import deque

        ROWS, COLS = len(maze) - 1, len(maze[0]) - 1
        directions = [0,1,0,-1,0]

        queue = deque()
        r, c = entrance
        queue.append((r, c))
        maze[r][c] = "*"

        steps = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for i in range(4):
                    nr, nc = r + directions[i], c + directions[i+1]
                    if 0 <= nr <= ROWS and 0 <= nc <= COLS and maze[nr][nc] == ".":
                        if nr == 0 or nr == ROWS or nc == 0 or nc == COLS:
                            return steps + 1
                        queue.append((nr, nc))
                        maze[nr][nc] = "X"
            steps += 1
        return -1
