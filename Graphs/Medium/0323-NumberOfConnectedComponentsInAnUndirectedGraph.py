"""
LeetCode Problem: Number of Connected Components in an Undirected Graph
Problem Number: 323
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""

class Solution:
    # Depth First Search
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E)
    def countComponents(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for adjacent in graph[node]:
                if adjacent not in visited:
                    dfs(adjacent)

        res = 0
        for node in range(n):
            if n not in visited:
                dfs(n)
                res += 1
        return res
    
    # Breadth First Search
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E)
    def countComponents(self, n, edges):
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def bfs(node):
            queue = deque([node])
            visited.add(node)
            while queue:
                v = queue.popleft()
                for neighbor in graph[v]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        res = 0
        for node in range(n):
            if n not in visited:
                bfs(n)
                res += 1
        return res
