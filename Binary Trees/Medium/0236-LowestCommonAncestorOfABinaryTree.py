"""
LeetCode Problem: Lowest Common Ancestor of a Binary Tree
Problem Number: 236
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Depth First Search
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if not l:
            return r
        elif not r:
            return l
        return root
