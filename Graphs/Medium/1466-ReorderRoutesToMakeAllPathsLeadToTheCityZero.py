"""
LeetCode Problem: Reorder Routes to Make All Paths Lead to the City Zero
Problem Number: 1466
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
"""

class Solution:
    # Depth First Search
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minReorder(self, n, connections):
        from collections import defaultdict

        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        def dfs(node, prev):
            res = 0
            for (adj, rev) in graph[node]:
                if adj != prev:
                    res += rev
                    res += dfs(adj, node)
            return res
        
        return dfs(0, -1)
    
    # Breadth First Search
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minReorder(self, n, connections):
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        res = 0
        queue = deque()
        queue.append((0, -1))

        while queue:
            node, prev = queue.popleft()
            for (adj, rev) in graph[node]:
                if adj != prev:
                    res += rev
                    queue.append((adj, node))
        
        return res
