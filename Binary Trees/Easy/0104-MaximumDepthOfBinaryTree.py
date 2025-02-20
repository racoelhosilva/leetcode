"""
LeetCode Problem: Maximum Depth of Binary Tree
Problem Number: 104
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Approach
    # At any node, the maximum depth can be calculated as the maximum
    # between the max depth of left subtree and right subtree + 1
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))