"""
LeetCode Problem: Longest Nice Subarray
Problem Number: 2401
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/longest-nice-subarray/
"""

class Solution:
    # Sliding Window + Bit Manipulation
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def longestNiceSubarray(self, nums):
        l = 0
        acc = 0
        res = 0

        for r in range(len(nums)):
            while acc & nums[r] != 0:
                acc ^= nums[l]
                l += 1
            acc |= nums[r]
            res = max(res, r - l + 1)
        
        return res
