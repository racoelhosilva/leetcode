"""
LeetCode Problem: Build Array from Permutation
Problem Number: 1920
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/build-array-from-permutation/
"""

class Solution:
    # Create new array
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def buildArray(self, nums):
        return [nums[nums[idx]] for idx in range(len(nums))]

    # In-place (constraint analysis)
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def buildArray(self, nums):
        for idx in range(len(nums)):
            nums[idx] += 1000 * (nums[nums[idx]] % 1000)
        for idx in range(len(nums)):
            nums[idx] //= 1000
        return nums
