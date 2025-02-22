"""
LeetCode Problem: Maximum Subarray
Problem Number: 53
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/maximum-subarray/
"""

class Solution:
    # Kadane's Algorithm
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxSubArray(self, nums):
        res, cur = nums[0], 0
        for idx in range(len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[idx]
            res = max(cur, res)
        return res
