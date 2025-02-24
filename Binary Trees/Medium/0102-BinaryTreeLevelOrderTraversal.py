"""
LeetCode Problem: Binary Tree Level Order Traversal
Problem Number: 102
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    # Breadth First Search
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            nodes = len(queue)
            for _ in range(nodes):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
