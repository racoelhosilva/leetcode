"""
LeetCode Problem: Subtree of Another Tree
Problem Number: 572
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/subtree-of-another-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Approach
    # Search down the tree until the root matches the subroot
    # Compare the two trees recursively
    # Time Complexity: O(m * n)
    # Space Complexity: O(hm + hn)
    def isSubtree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return self.sameTree(root, subRoot) or \
               self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)
    def sameTree(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)
    
    # Serialization
    # By serializing both of the trees, we cna check if one string is contained in the other
    # Time Complexity: O(m + n)
    # Space Complexity: O(m + n)
    def isSubtree(self, root, subroot):
        def preorderSerialziation(root):
            if not root:
                return '$'
            return '@' + str(root.val) + preorderSerialziation(root.left) + preorderSerialziation(root.right)
        r = preorderSerialziation(root)
        sr = preorderSerialziation(subroot)
        return sr in r
