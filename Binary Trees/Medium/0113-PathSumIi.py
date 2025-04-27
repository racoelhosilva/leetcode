"""
LeetCode Problem: Path Sum II
Problem Number: 113
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/path-sum-ii/
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
    # Space Complexity: O(h + k * h)
    def pathSum(self, root, targetSum):
        if not root:
            return []
        
        res = []
        
        def dfs(node, target, cur):
            if not node:
                return
            
            target -= node.val
            cur.append(node.val)
            
            if not node.left and not node.right and target == 0:
                res.append(cur[:])
            else:
                dfs(node.left, target, cur)
                dfs(node.right, target, cur)
            
            cur.pop()
        
        dfs(root, targetSum, [])
        return res
