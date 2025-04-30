"""
LeetCode Problem: Path Sum III
Problem Number: 437
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/path-sum-iii/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS Brute-Force
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def pathSum(self, root, targetSum):
        if not root:
            return 0
        
        def dfs(node, target, prev):
            if not node:
                return 0
            
            res = 0
            if not prev:
                res += dfs(node.left, target, False)
                res += dfs(node.right, target, False)

            target -= node.val
            if target == 0:
                res += 1
            res += dfs(node.left, target, True)
            res += dfs(node.right, target, True)

            return res
        return dfs(root, targetSum, False)
    
    # DFS with Cache
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def pathSum(self, root, targetSum):
        cache = {0:1}

        def dfs(node, target, cur, cache):
            if not node:
                return 0

            cur += node.val
            res = cache.get(cur - target, 0)
            
            cache[cur] = cache.get(cur, 0) + 1
            res += dfs(node.left, target, cur, cache)
            res += dfs(node.right, target, cur, cache)
            cache[cur] -= 1

            return res
        
        return dfs(root, targetSum, 0, cache)
