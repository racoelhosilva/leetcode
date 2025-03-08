"""
LeetCode Problem: Count Good Nodes in Binary Tree
Problem Number: 1448
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
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
    # Space Complexity: O(n)
    def goodNodes(self, root):
        def helper(node, highest):
            if not node:
                return 0
            if node.val >= highest:
                return 1 + helper(node.left, node.val) + helper(node.right, node.val)
            else:
                return helper(node.left, highest) + helper(node.right, highest) 
        return helper(root, root.val)
