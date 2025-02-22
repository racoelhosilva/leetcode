"""
LeetCode Problem: Island Perimeter
Problem Number: 463
Difficulty: Easy
Topic: Graphs
Link: https://leetcode.com/problems/island-perimeter/
"""

from collections import deque

class Solution:
    # Depth First Search
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def islandPerimeter(self, grid):
        height, width = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if (row, col) in visited:
                return 0
            if row < 0 or row >= height or col < 0 or col >= width or grid[row][col] == 0:
                return 1
            visited.add((row, col))
            return dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)

        for row in range(height):
            for col in range(width):
                if grid[row][col]:
                    return dfs(row, col)
        return 0

    # Breadth First Search
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def islandPerimeter(self, grid):
        height, width = len(grid), len(grid[0])
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            perimeter = 0

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nrow, ncol = row + dr, col + dc
                    if nrow < 0 or nrow >= height or ncol < 0 or ncol >= width or grid[nrow][ncol] == 0:
                        perimeter += 1
                    elif (nrow, ncol) not in visited:
                        queue.append((nrow, ncol))
                        visited.add((nrow,ncol))    
            return perimeter

        for row in range(height):
            for col in range(width):
                if grid[row][col]:
                    return bfs(row, col)
        return 0
    
    # Iterative
    # Time Complexity: O(m * n)
    # Space Complexity: O(1)
    def islandPerimeter(self, grid):
        height, width = len(grid), len(grid[0])
        res = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == 1:
                    if row - 1 < 0 or grid[row-1][col] == 0:
                        res += 1
                    if row + 1 >= height or grid[row+1][col] == 0:
                        res += 1
                    if col - 1 < 0 or grid[row][col-1] == 0:
                        res += 1
                    if col + 1 >= width or grid[row][col+1] == 0:
                        res += 1
        return res
    
    # Iterative
    # Start by considering that a block of land is surrounded by water (add 4)
    # In case the block on the left was land, subtract 2 (current block and adjacent block)
    # Do the same for the block above and propagate the behaviour through the whole grid
    # Time Complexity: O(m * n)
    # Space Complexity: O(1)
    def islandPerimeter(self, grid):
        height, width = len(grid), len(grid[0])
        res = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == 1:
                    res += 4
                    if row > 0 and grid[row - 1][col] == 1:
                        res -= 2
                    if col > 0 and grid[row][col - 1] == 1:
                        res -= 2
        return res
