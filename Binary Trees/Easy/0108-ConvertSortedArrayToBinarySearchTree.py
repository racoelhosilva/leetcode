"""
LeetCode Problem: Convert Sorted Array to Binary Search Tree
Problem Number: 108
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Depth First Search
    # The root node of a balanced BST is the middle element of the sorted array
    # The same logic can be applied to select its descendants
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        middle = len(nums) // 2
        return TreeNode(nums[middle], \
                self.sortedArrayToBST(nums[:middle]), \
                self.sortedArrayToBST(nums[middle+1:]))

    # Depth First Search (Optimized)
    # By substituting the array slicing with indexes, we reduce both
    # temporal and spatial complexities
    # Time Complexity: O(n)
    # Space Complexity: O(log n)
    def sortedArrayToBST(self, nums):
        def helper(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            return TreeNode(nums[middle], \
                    helper(left, middle-1), \
                    helper(middle+1, right))
        return helper(0, len(nums)-1)
