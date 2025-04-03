"""
LeetCode Problem: Pacific Atlantic Water Flow
Problem Number: 417
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
"""

class Solution:
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        directions = (0, 1, 0, -1, 0)
        pacific, atlantic = set(), set()

        def dfs(row, col, ocean):
            ocean.add((row, col))
            for i in range(4):
                new_row, new_col = row + directions[i], col + directions[i+1]
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in ocean and heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, ocean)

        for row in range(ROWS):
            dfs(row, 0, pacific) 
            dfs(row, COLS-1, atlantic)
        for col in range(COLS):
            dfs(0, col, pacific) 
            dfs(ROWS-1, col, atlantic)
        
        return list(atlantic & pacific)
    
    def pacificAtlantic(self, heights):
        from collections import deque

        ROWS, COLS = len(heights), len(heights[0])
        directions = (0, 1, 0, -1, 0)
        pacific, atlantic = set(), set()

        def bfs(queue, ocean):
            while queue:
                row, col = queue.popleft()
                for i in range(4):
                    new_row, new_col = row + directions[i], col + directions[i+1]
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in ocean and heights[new_row][new_col] >= heights[row][col]:
                        ocean.add((new_row, new_col))
                        queue.append((new_row, new_col))
        
        pacific_queue, atlantic_queue = deque(), deque()
        for row in range(ROWS):
            pacific_queue.append((row, 0))
            pacific.add((row, 0))
            atlantic_queue.append((row, COLS-1))
            atlantic.add((row, COLS-1))
        for col in range(COLS):
            pacific_queue.append((0, col))
            pacific.add((0, col))
            atlantic_queue.append((ROWS-1, col))
            atlantic.add((ROWS-1, col))

        bfs(pacific_queue, pacific)
        bfs(atlantic_queue, atlantic)
        return list(pacific & atlantic)
