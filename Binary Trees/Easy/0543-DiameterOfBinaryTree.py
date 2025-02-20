"""
LeetCode Problem: Diameter of Binary Tree
Problem Number: 543
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/diameter-of-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Top-Down Approach
    # At each node, the maximum diameter of the tree is the maximum between:
    # - Left and right subtree depths
    # - Max diameter of left subtree
    # - Max diameter of right subtree
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        
        left = self.depth(root.left)
        right = self.depth(root.right)

        return max(left + right, \
                max(self.diameterOfBinaryTree(root.left), \
                    self.diameterOfBinaryTree(root.right)))
    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    # Bottom-Up Approach
    # Instead of recalculating the depth and diameter of subtrees at each node,
    # Keep track of the largest diameter when bubbling up the recursion
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.diameter = 0
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.diameter