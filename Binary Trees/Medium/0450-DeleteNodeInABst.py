"""
LeetCode Problem: Delete Node in a BST
Problem Number: 450
Difficulty: Medium
Topic: Binary Trees
Link: https://leetcode.com/problems/delete-node-in-a-bst/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Approach
    # Time Complexity: O(h)
    # Space Complexity: O(h)
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                # Swapping with smallest larger node
                # Could also be done the other way around
                if not root.right.left:
                    root.val = root.right.val
                    root.right = root.right.right
                else:
                    sub = root.right
                    while sub.left.left:
                        sub = sub.left
                    root.val = sub.left.val
                    sub.left = sub.left.right
        return root    

    # Iterative Approach
    # Time Complexity: O(h)
    # Space Complexity: O(1)
    def deleteNode(self, root, key):
        parent = None
        node = root
        while node and node.val != key:
            parent = node
            if node.val > key:
                node = node.left
            elif node.val < key:
                node = node.right
        if not node:
            return root
    
        if not node.right:
            if not parent:
                return node.left
            elif parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
        elif not node.left:
            if not parent:
                return node.right
            elif parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
        else:
            # Swapping with smallest larger node
            # Could also be done the other way around
            if not node.right.left:
                node.val = node.right.val
                node.right = node.right.right
            else:
                sub = node.right
                while sub.left.left:
                    sub = sub.left
                node.val = sub.left.val
                sub.left = sub.left.right

        return root
