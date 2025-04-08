"""
LeetCode Problem: Minimum Number of Operations to Make Elements in Array Distinct
Problem Number: 3396
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
"""

class Solution:
    # Reverse Iteration
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minimumOperations(self, nums):
        seen = set()
        n = len(nums)
        for idx in range(n - 1, -1, -1):
            if nums[idx] in seen:
                return (idx // 3) + 1
            seen.add(nums[idx])
        return 0
