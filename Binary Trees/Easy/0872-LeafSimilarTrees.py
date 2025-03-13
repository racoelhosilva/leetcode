"""
LeetCode Problem: Leaf Similar Trees
Problem Number: 872
Difficulty: Easy
Topic: Binary Trees
Link: https://leetcode.com/problems/leaf-similar-trees/
"""

class Solution:
    # Store Leaves
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def leafSimilar(self, root1, root2):
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val
            yield from dfs(root.left)
            yield from dfs(root.right)
        return list(dfs(root1)) == list(dfs(root2))
