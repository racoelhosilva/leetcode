"""
LeetCode Problem: Symmetric Tree
Problem Number: 101
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/symmetric-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Approach
    # For each node on the left and the right, check if they have the same value
    # Recursively do this, comparing the left subtree of the left node with the 
    # right subtree of the right node
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def isSymmetric(self, root):
        if not root:
            return True
        
        def symmetric(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and symmetric(a.left, b.right) and symmetric(a.right, b.left)

        return symmetric(root.left, root.right)

