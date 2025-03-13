"""
LeetCode Problem: Search in a Binary Search Tree
Problem Number: 700
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Binary Search Tree Search
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchBST(self, root, val):
        while root and root.val != val:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
        return root
