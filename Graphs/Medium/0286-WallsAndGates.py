"""
LeetCode Problem: Walls and Gates
Problem Number: 286
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/walls-and-gates/
"""

class Solution:
    # Breadth First Search
    # Time Complexity: O((m * n)^2)
    # Space Complexity: O(m * n)
    def walls_and_gates(self, rooms):
        from collections import deque
        
        ROWS, COLS = len(rooms), len(rooms[0])
        INF = 2 << 31 - 1
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def bfs(r, c):
            visited = set()
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            
            distance = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    if rooms[nr][nc] == "0":
                        return distance
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr,nc) in visited or rooms[nr][nc] == "-1": 
                            continue
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                distance += 1
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == INF: 
                    rooms[r][c] = bfs(r,c)

    # Multi-Source BFS
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def walls_and_gates(self, rooms):
        from collections import deque
        
        ROWS, COLS = len(rooms), len(rooms[0])
        INF = 2 << 31 - 1
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0: 
                    queue.append((r,c))

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or rooms[nr][nc] != INF:
                    continue
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr,nc))
