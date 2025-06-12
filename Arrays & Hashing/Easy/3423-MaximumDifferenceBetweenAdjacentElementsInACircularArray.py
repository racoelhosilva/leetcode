"""
LeetCode Problem: Maximum Difference Between Adjacent Elements in a Circular Array
Problem Number: 3423
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
"""

class Solution:
    # Edge Case + Traversal
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxAdjacentDistance(self, nums):
        res = abs(nums[0] - nums[-1])
        for i in range(1, len(nums)):
            res = max(res, abs(nums[i] - nums[i-1]))
        return res
