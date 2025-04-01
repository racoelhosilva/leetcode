"""
LeetCode Problem: Construct Binary Tree from Preorder and Inorder Traversal
Problem Number: 105
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        node = TreeNode(preorder[0])
        middle = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:middle+1], inorder[:middle])
        node.right = self.buildTree(preorder[middle+1:], inorder[middle+1:])
        return node
    
    # Hash Table
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def buildTree(self, preorder, inorder):
        indices = {val: idx for idx, val in enumerate(inorder)}
        preorder_index = 0
        def dfs(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            
            value = preorder[preorder_index]
            preorder_index += 1
            node = TreeNode(value)
            middle = indices[value]
            node.left = dfs(left, middle-1)
            node.right = dfs(middle+1, right)
            return node
        return dfs(0, len(inorder) - 1)
