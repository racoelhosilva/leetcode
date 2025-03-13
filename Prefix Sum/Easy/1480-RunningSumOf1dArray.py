"""
LeetCode Problem: Running Sum of 1D Array
Problem Number: 1480
Difficulty: Easy
Topic: Prefix Sum
Link: https://leetcode.com/problems/running-sum-of-1d-array/
"""

class Solution:
    def runningSum(self, nums):
        for idx in range(1, len(nums)):
            nums[idx] = nums[idx] + nums[idx-1]
        return nums
