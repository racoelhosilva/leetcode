"""
LeetCode Problem: Jump Game
Problem Number: 55
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/jump-game/
"""

class Solution:
    # Greedy Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def canJump(self, nums):
        n = len(nums)
        pos = n - 1
        for idx in range(n - 2, -1, -1):
            if idx + nums[idx] >= pos:
                pos = idx
        return pos == 0
