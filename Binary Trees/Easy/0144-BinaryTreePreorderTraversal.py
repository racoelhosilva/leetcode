"""
LeetCode Problem: Binary Tree Preorder Traversal
Problem Number: 144
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
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
    def preorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res
    
    # Recursive (Call Stack)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorderTraversal(self, root):
        def traverse(root, res):
            if not root:
                return
            res.append(root.val)
            traverse(root.left, res)
            traverse(root.right, res)
        res = []
        traverse(root, res)
        return res
