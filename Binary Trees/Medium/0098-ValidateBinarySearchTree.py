"""
LeetCode Problem: Validate Binary Search Tree
Problem Number: 98
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/validate-binary-search-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Inorder Traversal
    # Inorder traversal of a BST should be an ordered sequence
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValidBST(self, root):
        def traverse(root, order):
            if not root:
                return
            traverse(root.left, order)
            order.append(root.val)
            traverse(root.right, order)
        order = []
        traverse(root, order)
        for idx in range(len(order) - 1):
            if order[idx] >= order[idx+1]:
                return False
        return True
    
    # Depth First Search
    # Perform a DFS with lower and upper bounds for each node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isValidBST(self, root):
        def valid(root, lower, upper):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return valid(root.left, lower, root.val) and valid(root.right, root.val, upper)
        return valid(root, float("-inf"), float("+inf"))
