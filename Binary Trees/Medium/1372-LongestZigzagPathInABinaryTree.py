"""
LeetCode Problem: Longest ZigZag Path in a Binary Tree
Problem Number: 1372
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Depth First Search
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def longestZigZag(self, root):
        if not root:
            return 0

        def helper(node, left, cur):
            if not node:
                return cur - 1
            if left:
                return max(helper(node.left, False, cur + 1), 
                           helper(node.right, True, 1))
            else:
                return max(helper(node.left, False, 1),
                           helper(node.right, True, cur + 1))
        
        return helper(root, True, 0)
