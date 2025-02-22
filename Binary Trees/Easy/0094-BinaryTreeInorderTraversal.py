"""
LeetCode Problem: Binary Tree Inorder Traversal
Problem Number: 94
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative (Stack)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
        
            node = stack.pop()
            res.append(node.val)
            node = node.right

        return res

    # Recursive (Call Stack)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorderTraversal(self, root):
        res = []
        def traverse(root, res):
            if not root:
                return
            traverse(root.left, res)
            res.append(root.val)
            traverse(root.right, res)
        traverse(root, res)
        return res
    
    # Morris Traversal
    # This algorithm is more complicated, but it traverses the tree without additional space (just output)
    # The idea is that we first want to find the rightmost node from the left subtree and link it back to the current node
    # This is because in an inorder traversal, this node will be just before the current
    # After this, we move on to the node on the left and repeat this process
    # Eventually, there will be no more nodes to the left, in which case, we have reached the leftmost node 
    # At this stage, moving right is the same as  traversing up the tree to an ancestor of the node (we have a loop)
    # We will then find the rightmost node of the left subtree different from the current node
    # Undo the loop by removing the edge, and append the current node to the result
    # We have restored the structure and can then move right again to continue the traversal
    # Repeating this process will complete the inorder traversal and keep the tree structure
    # Time Complexity: O(n)
    # Space Complexity: O(n) -> just for output
    def inorderTraversal(self, root):
        res = []
        node = root

        while node:
            if not node.left:
                res.append(node.val)
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
                    res.append(node.val)
                    node = node.right
        return res