"""
LeetCode Problem: Kth Smallest Element in a BST
Problem Number: 230
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Inorder Traversal
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def kthSmallest(self, root, k):
        traversal = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            traversal.append(node.val)
            inorder(node.right)
        inorder(root)
        return traversal[k-1]
    
    # Inorder Traversal (Optimal)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def kthSmallest(self, root, k):
        res = 0
        def inorder(node):
            nonlocal k, res
            if not node:
                return
            inorder(node.left)
            k -= 1
            if k == 0:
                res = node.val
                return
            inorder(node.right)
        inorder(root)
        return res

    # Morris Inorder Traversal
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def kthSmallest(self, root, k):
        node = root

        while node:
            if not node.left:
                k -= 1
                if k == 0:
                    return node.val
                node = node.right
            else:
                prev = node.left

                while prev.right and prev.right != node:
                    prev = prev.right
                
                if not prev.right:
                    prev.right = node
                    node = node.left
                else:
                    prev.right = None
                    k -= 1
                    if k == 0:
                        return node.val
                    node = node.right
        return -1
