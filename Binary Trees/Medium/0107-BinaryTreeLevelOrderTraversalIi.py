"""
LeetCode Problem: Binary Tree Level Order Traversal II
Problem Number: 107
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    # Determine depth + Level Order Traversal
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def levelOrderBottom(self, root):
        if not root:
            return []

        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        d = depth(root)
        res = [[] for _ in range(d)]
        queue = deque()
        queue.append(root)

        while queue:
            d -= 1
            for _ in range(len(queue)):
                node = queue.popleft()
                res[d].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


    # Level Order Traversal + Reverse
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def levelOrderBottom(self, root):
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        res.reverse()
        return res
