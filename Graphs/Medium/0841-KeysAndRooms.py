"""
LeetCode Problem: Keys and Rooms
Problem Number: 841
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/keys-and-rooms/
"""

class Solution:
    # Depth First Search (Recursive)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = set([0])

        def dfs(room):
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    dfs(key)

        dfs(0)
        return len(visited) == n

    # Depth First Search (Iterative)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        keys = [0]
        visited = set(keys)

        while keys:
            room = keys.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    keys.append(key)

        return len(visited) == n
