"""
LeetCode Problem: Balanced Binary Tree
Problem Number: 110
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/balanced-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Top-Down Approach
    # For each node, check if it is balanced by comparing heights of both subtrees
    # Recursively check if balanced for the left and right subtrees
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def isBalanced(self, root):
        if not root:
            return True
        return abs(self.maxHeight(root.left) - self.maxHeight(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)
    def maxHeight(self, root):
        if not root: 
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
    
    # Bottom-Up Approach
    # To avoid recalculating heights and checking balances of nodes,
    # We can use a modified height function that returns -1 if any of the 
    # subtrees is not balanced and propagate this value up the tree
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def isBalanced(self, root):
        return self.balancedHeight(root) >= 0
    def balancedHeight(self, root):
        if not root:
            return 0
        
        left = self.balancedHeight(root.left)
        if left < 0: 
            return left
        right = self.balancedHeight(root.right)
        if right < 0: 
            return right

        if abs(left - right) > 1: 
            return -1
        return 1 + max(left, right)