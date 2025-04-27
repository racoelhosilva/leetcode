"""
LeetCode Problem: Number of Provinces
Problem Number: 547
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/number-of-provinces/
"""

class Solution:
    # Depth First Search
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        res = 0

        def dfs(city):
            visited[city] = True
            for newCity in range(n):
                if isConnected[city][newCity] and not visited[newCity]:
                    dfs(newCity)

        for city in range(n):
            if not visited[city]:
                res += 1
                dfs(city)
        
        return res

    # Breadth First Search
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def findCircleNum(self, isConnected):
        from collections import deque

        n = len(isConnected)
        visited = [False] * n
        res = 0

        for city in range(n):
            if not visited[city]:
                res += 1
                queue = deque()
                queue.append(city)
                visited[city] = True

                while queue:
                    newCity = queue.popleft()
                    for nearby in range(n):
                        if isConnected[newCity][nearby] and not visited[nearby]:
                            queue.append(nearby)
                            visited[nearby] = True
        return res
