"""
LeetCode Problem: Construct Binary Tree from Inorder and Postorder Traversal
Problem Number: 106
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Approach
    # Operations take longer due to Python's index
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        value = postorder[-1]
        node = TreeNode(value)
        middle = inorder.index(value)
        node.left = self.buildTree(inorder[:middle], postorder[:middle])
        node.right = self.buildTree(inorder[middle+1:], postorder[middle:-1])
        return node

    # Hash Table
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def buildTree(self, inorder, postorder):
        indices = {val: idx for idx, val in enumerate(inorder)}
        postorder_index = len(postorder) - 1
        
        def dfs(left, right):
            nonlocal postorder_index
            if left > right:
                return None
            
            value = postorder[postorder_index]
            postorder_index -= 1
            node = TreeNode(value)
            middle = indices[value]
            node.right = dfs(middle + 1, right)
            node.left = dfs(left, middle - 1)
            return node
        return dfs(0, len(inorder) - 1)

