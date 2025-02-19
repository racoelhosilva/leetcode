"""
LeetCode Problem: Lowest Common Ancestor of a Binary Search Tree
Problem Number: 235
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Recursive Approach
    # If both values are smaller than root, continue search on the left
    # If both values are greater than root, continue search on the right
    # Otherwise, either one element is root or they are on different subtrees
    # In both of these cases, the lowest common ancestor is root
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
    
    # Iterative Approach
    # If both values are smaller than root, continue search on the left
    # If both values are greater than root, continue search on the right
    # Otherwise, either one element is root or they are on different subtrees
    # In both of these cases, the lowest common ancestor is root
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return None