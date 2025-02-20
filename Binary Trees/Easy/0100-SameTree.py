"""
LeetCode Problem: Same Tree
Problem Number: 100
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/same-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Approach
    # If they are both null, then they are same
    # Else if one of them is null (and the other implicitly is not), they are different
    # Else compare their values and check if their subtrees are the same
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
