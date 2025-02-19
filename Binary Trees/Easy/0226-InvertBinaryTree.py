"""
LeetCode Problem: Invert Binary Tree
Problem Number: 226
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/invert-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Approach
    # For the current node, swap the left and right subtrees
    # Propagate the change to each subtree
    # If there is no subtree, stop and return
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
