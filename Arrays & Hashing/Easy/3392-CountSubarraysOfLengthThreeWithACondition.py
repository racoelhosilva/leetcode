"""
LeetCode Problem: Count Subarrays of Length Three With a Condition
Problem Number: 3392
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/
"""

class Solution:
    # Single Traversal
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def countSubarrays(self, nums):
        if len(nums) < 3:
            return 0
        res = 0
        for idx in range(2, len(nums)):
            if (nums[idx-2] + nums[idx]) * 2 == nums[idx-1]:
                res += 1
        return res
