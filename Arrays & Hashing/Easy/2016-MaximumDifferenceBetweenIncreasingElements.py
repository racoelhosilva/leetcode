"""
LeetCode Problem: Maximum Difference Between Increasing Elements
Problem Number: 2016
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/maximum-difference-between-increasing-elements/
"""

class Solution:
    # Minimum Tracking
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maximumDifference(self, nums):
        res = -1
        mn = nums[0]
        
        for idx in range(1, len(nums)):
            if nums[idx] > mn:
                res = max(res, nums[idx] - mn)
            else:
                mn = nums[idx]
        return res
