"""
LeetCode Problem: Maximum Width of Binary Tree
Problem Number: 662
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/maximum-width-of-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Indexed level order traversal
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        from collections import deque
        queue = deque()
        queue.append((root, 0))
        res = 0

        while queue:
            n = len(queue)

            _, left_idx = queue[0]
            _, right_idx = queue[-1]
            res = max(res, right_idx - left_idx + 1)

            for _ in range(n):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))

        return res
