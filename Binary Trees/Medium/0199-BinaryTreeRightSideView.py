"""
LeetCode Problem: Binary Tree Right Side View
Problem Number: 199
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/binary-tree-right-side-view/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Breadth First Search
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def rightSideView(self, root):
        if not root:
            return []

        from collections import deque
        queue = deque()
        queue.append(root)

        res = []
        while queue:
            res.append(queue[-1])
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res
