"""
LeetCode Problem: Concatenation of Array
Problem Number: 1929
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/concatenation-of-array/
"""

class Solution:
    # One Pass
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def getConcatenation(self, nums):
        res = [0] * 2 * len(nums)
        for idx in range(len(nums)):
            res[idx] = res[idx + len(nums)] = nums[idx]
        return res