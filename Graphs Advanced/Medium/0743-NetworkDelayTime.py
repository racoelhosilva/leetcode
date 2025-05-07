"""
LeetCode Problem: Network Delay Time
Problem Number: 743
Difficulty: Medium
Topic: Graphs Advanced
Link: https://leetcode.com/problems/network-delay-time/
"""

from collections import defaultdict, deque
from heapq import heappop, heappush

class Solution:
    # Depth First Search
    # Time Complexity: O(V * E)
    # Space Complexity: O(V + E)
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {i: float("inf") for i in range(1, n+1)}

        def dfs(node, time):
            if time >= dist[node]:
                return
            dist[node] = time
            for neighbor, weight in graph[node]:
                dfs(neighbor, time + weight)

        dfs(k, 0)

        mx = max(dist.values())
        return mx if mx < float("inf") else -1

    # Breadth First Search
    # Time Complexity: O(V * E)
    # Space Complexity: O(V + E)
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {i: float("inf") for i in range(1, n+1)}
        queue = deque()
        queue.append((k, 0))

        while queue:
            node, time = queue.popleft()
            if time >= dist[node]:
                continue
            dist[node] = time
            for neighbor, weight in graph[node]:
                queue.append((neighbor, time + weight))

        mx = max(dist.values())
        return mx if mx < float("inf") else -1

    # Floyd-Warshall Algorithm
    # Time Complexity: O(V^3)
    # Space Complexity: O(V^2)
    def networkDelayTime(self, times, n, k):
        dist = [[float("inf")] * n for _ in range(n)]
        for u, v, w in times:
            dist[u-1][v-1] = w
        for i in range(n):
            dist[i][i] = 0
        
        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][mid] + dist[mid][j])

        mx = max(dist[k-1])
        return mx if mx < float("inf") else -1
    
    # Bellman-Ford Algorithm
    # Time Complexity: O(V * E)
    # Space Complexity: O(V)
    def networkDelayTime(self, times, n, k):
        dist = [float("inf")] * n
        dist[k-1] = 0

        for _ in range(n-1):
            for u, v, w in times:
                if dist[u - 1] + w < dist[v-1]:
                    dist[v - 1] = dist[u - 1] + w

        mx = max(dist)
        return mx if mx < float("inf") else -1

    # Shortest Path Faster Algorithm
    # Time Complexity: average -> O(V + E)
    # Space Complexity: O(V + E)
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {i: float("inf") for i in range(1, n+1)}
        dist[k] = 0
        queue = deque()
        queue.append((k, 0))

        while queue:
            node, time = queue.popleft()
            if time > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_time = time + weight
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    queue.append((neighbor, new_time))

        mx = max(dist.values())
        return mx if mx < float("inf") else -1

    # Dijkstra's Algorithm
    # Time Complexity: O(E log V)
    # Space Complexity: O(V + E)
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        heap = [(0, k)]
        dist = {}

        while heap:
            time, node = heappop(heap)
            if node in dist:
                continue
            dist[node] = time
            for neighbor, wt in graph[node]:
                if neighbor not in dist:
                    heappush(heap, (time + wt, neighbor))
        
        return max(dist.values()) if len(dist) == n else -1
