"""
LeetCode Problem: Graph Valid Tree
Problem Number: 261
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/graph-valid-tree/
"""

class Solution:
    # Depth First Search
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E)
    def validTree(self, n, edges):
        if n != len(edges) - 1:
            return False

        graph = [[] for _ in range(n)]
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for adjacent in graph[node]:
                if adjacent == parent:
                    continue
                if not dfs(adjacent, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

    # Breadth First Search
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E)
    def validTree(self, n, edges):
        if n != len(edges) - 1:
            return False
        
        from collections import deque
        
        graph = [[] for _ in range(n)]
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        visited = set()
        queue = deque()
        queue.append((0, -1))
        visited.add(0)

        while queue:
            node, parent = queue.popleft()
            for adjacent in graph[node]:
                if adjacent == parent:
                    continue
                if adjacent in visited:
                    return False
                queue.append((adjacent, node))
                visited.add(adjacent)
        
        return len(visited) == n
