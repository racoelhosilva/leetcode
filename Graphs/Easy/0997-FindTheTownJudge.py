"""
LeetCode Problem: Find the Town Judge
Problem Number: 997
Difficulty: Easy
Topic: Graphs
Link: https://leetcode.com/problems/find-the-town-judge/
"""

from collections import defaultdict

class Solution:
    # Indegree and Outdegree
    # Storing the indegree and outdegree of each vertex
    # If any vertex has outdegree 0 and indegree n-1, that person is judge
    # Time Complexity: O(V + E)
    # Space Complexity: O(V)
    def findJudge(self, n, trust):
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for src, dest in trust:
            outdegree[src] += 1
            indegree[dest] += 1
        
        for person in range(1, n+1):
            if outdegree[person] == 0 and indegree[person] == n - 1:
                return person
        
        return -1
    
    # Degree Delta
    # Instead of storing the indegree and outdegree of each vertex
    # Store only the delta of that vertex
    # Time Complexity: O(V + E)
    # Space Complexity: O(V)
    def findJudge(self, n, trust):
        delta = defaultdict(int)

        for src, dest in trust:
            delta[src] -= 1
            delta[dest] += 1
        
        for person in range(1, n+1):
            if delta[person] == n - 1:
                return person
        
        return -1