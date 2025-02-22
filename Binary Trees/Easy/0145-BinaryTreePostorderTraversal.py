"""
LeetCode Problem: Binary Tree Postorder Traversal
Problem Number: 145
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative (Stack)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::1]

    # Recursive (Call Stack)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorderTraversal(self, root):
        def traverse(root, res):
            if not root:
                return 
            traverse(root.left, res)
            traverse(root.right, res)
            res.append(root.val)
        res = []
        traverse(root, res)
        return res
