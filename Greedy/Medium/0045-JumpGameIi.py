"""
LeetCode Problem: Jump Game II
Problem Number: 45
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/jump-game-ii/
"""

class Solution:
    # Greedy Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def jump(self, nums):
        n = len(nums)
        l = r = 0
        res = 0

        while r < n - 1:
            mx = -1
            for j in range(l, r + 1):
                mx = max(mx, j + nums[j])
            l = r + 1
            r = mx
            res += 1
        return res
