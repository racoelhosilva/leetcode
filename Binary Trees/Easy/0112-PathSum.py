"""
LeetCode Problem: Path Sum
Problem Number: 112
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/path-sum/
"""

class Solution:
    # Depth First Search
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        targetSum = targetSum - root.val        

        if not root.left and not root.right:
            return targetSum == 0 

        return self.hasPathSum(root.left, targetSum) or \
            self.hasPathSum(root.right, targetSum)
