"""
LeetCode Problem: Flood Fill
Problem Number: 733
Difficulty: Easy
Topic: Graphs
Link: https://leetcode.com/problems/flood-fill/
"""

class Solution:
    # Breadth First Search -> Queue
    # Initialize a queue with the starting coordinates
    # Iteratively remove the front coordinate and push all adjacent
    # coordinates that should be changed to the queue until empty
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def floodFill(self, image, sr, sc, color):
        old = image[sr][sc]
        if color == old:
            return image
        
        from collections import deque
        queue = deque()
        queue.append((sr,sc))
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            if r > 0 and image[r-1][c] == old:
                queue.append((r-1, c))
            if r < len(image) - 1 and image[r+1][c] == old:
                queue.append((r+1, c))
            if c > 0 and image[r][c-1] == old:
                queue.append((r, c-1))
            if c < len(image[r]) - 1 and image[r][c+1] == old:
                queue.append((r, c+1))
        return image

    # Depth First Search (Recursive) -> (Call) Stack
    # Starting with the root, visit one adjacent coordinate and change it
    # Recursively visit one adjacent coordinate from there until there are no more
    # After bubbling up, recursively visit the other adjacent coordinates
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def floodFill(self, image, sr, sc, color):
        old = image[sr][sc]
        if color != old:
            self.dfs(image, sr, sc, color, old)
        return image
    def dfs(self, image, r, c, color, old):
        image[r][c] = color
        if r > 0 and image[r-1][c] == old:
            self.dfs(image, r-1, c, color, old)
        if r < len(image) - 1 and image[r+1][c] == old:
            self.dfs(image, r+1, c, color, old)
        if c > 0 and image[r][c-1] == old:
            self.dfs(image, r, c-1, color, old)
        if c < len(image[r]) - 1 and image[r][c+1] == old:
            self.dfs(image, r, c+1, color, old)

    # Depth First Search (Iterative) -> Stack
    # Starting with the root, change it, visit one adjacent coordinate and change it
    # Iteratively repeat the process by adding adjacent nodes to the stack
    # Note: some changes were made to remove duplicates from this iterative DFS
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def floodFill(self, image, sr, sc, color):
        old = image[sr][sc]
        if color == old:
            return image
        stack = [(sr,sc)]
        image[sr][sc] = color
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while stack:
            r, c = stack.pop()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == old:
                    image[nr][nc] = color
                    stack.append((nr, nc))
        return image