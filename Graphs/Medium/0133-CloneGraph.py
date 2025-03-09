"""
LeetCode Problem: Clone Graph
Problem Number: 133
Difficulty: Medium
Topic: Graphs
Link: https://leetcode.com/problems/clone-graph/
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # Breadth First Search
    # Time Complexity: O(V + E)
    # Space Complexity: O(V)
    def cloneGraph(self, node):
        if not node:
            return None
        
        old_to_new = dict()
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            old_to_new[node] = Node(node.val)
            for adjacent in node.neighbors:
                old_to_new[node].neighbors.append(dfs(adjacent))
            return old_to_new[node]

        return dfs(node)

    # Breadth First Search
    # Time Complexity: O(V + E)
    # Space Complexity: O(V)
    def cloneGraph(self, node):
        if not node:
            return None
        
        from collections import deque

        old_to_new = dict()
        queue = deque()
        queue.append(node)
        old_to_new[node] = Node(node.val)

        while queue:
            old_node = queue.popleft()
            new_node = old_to_new[old_node]

            for adjacent in old_node.neighbors:
                if adjacent not in old_to_new:
                    old_to_new[adjacent] = Node(adjacent.val)
                    queue.append(adjacent)
                new_node.neighbors.append(old_to_new[adjacent])
        return old_to_new[node]
