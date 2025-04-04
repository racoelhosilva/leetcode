"""
LeetCode Problem: Smallest Subtree with all the Deepest Nodes
Problem Number: 865
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Bottom-up LCA and depth
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def subtreeWithAllDeepest(self, root):
        def aux(node):
            if not node:
                return (None, -1)
            
            left_lca, left_depth = aux(node.left)
            right_lca, right_depth = aux(node.right)

            if left_depth > right_depth:
                return (left_lca, left_depth + 1)
            elif left_depth < right_depth:
                return (right_lca, right_depth + 1)
            else:
                return (node, left_depth + 1)

        lca, depth = aux(root)
        return lca
