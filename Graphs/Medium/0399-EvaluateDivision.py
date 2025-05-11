"""
LeetCode Problem: Evaluate Division
Problem Number: 399
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/evaluate-division/
"""

class Solution:
    # Depth First Search
    # Time Complexity: O(n * q)
    # Space Complexity: O(n + q)
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict

        graph = defaultdict(list)

        for idx in range(len(equations)):
            graph[equations[idx][0]].append((equations[idx][1], values[idx]))
            graph[equations[idx][1]].append((equations[idx][0], 1/values[idx]))

        def dfs(src, target, visited):
            if src not in graph or target not in graph:
                return -1
            if src == target:
                return 1
            
            visited.add(src)
            for adj, weight in graph[src]:
                if adj not in visited:
                    res = dfs(adj, target, visited)
                    if res != -1:
                        return weight * res
            return -1
        
        return [dfs(query[0], query[1], set()) for query in queries]

    # Breadth First Search
    # Time Complexity: O(n * q)
    # Space Complexity: O(n + q)
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict, deque

        graph = defaultdict(list)

        for idx in range(len(equations)):
            graph[equations[idx][0]].append((equations[idx][1], values[idx]))
            graph[equations[idx][1]].append((equations[idx][0], 1/values[idx]))

        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1
            visited = set()
            visited.add(src)
            queue = deque()
            queue.append((src, 1))

            while queue:
                node, res = queue.popleft()
                if node == target:
                    return res
                for adj, weight in graph[node]:
                    if adj not in visited:
                        queue.append((adj, weight * res))
                        visited.add(adj)
            return -1
        
        return [bfs(query[0], query[1]) for query in queries]

    # Floyd-Warshall
    # Time Complexity: O(q + n^3)
    # Space Complexity: O(n^2 + q)
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict

        graph = defaultdict(dict)

        for idx in range(len(equations)):
            graph[equations[idx][0]][equations[idx][1]] = values[idx]
            graph[equations[idx][1]][equations[idx][0]] = 1 / values[idx]

        for k in graph:
            for j in graph[k]:
                for i in graph[k]:
                    if j not in graph[i]:
                        graph[i][j] = graph[i][k] * graph[k][j]

        res = []
        for a,b in queries:
            if a in graph and b in graph[a]:
                res.append(graph[a][b])
            else:
                res.append(-1)
        return res
