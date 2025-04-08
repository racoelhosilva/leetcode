"""
LeetCode Problem: Maximum Level Sum of a Binary Tree
Problem Number: 1161
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Breadth First Search (Level Traversal)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxLevelSum(self, root):
        from collections import deque

        queue = deque()
        queue.append(root)
        max_sum = root.val
        res = 1

        level = 1
        while queue:
            cur = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                cur += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if cur > max_sum:
                max_sum = cur
                res = level
            level += 1
        return res
