"""
LeetCode Problem: Increasing Triplet Subsequence
Problem Number: 334
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/increasing-triplet-subsequence/
"""

class Solution:
    # Greedy Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def increasingTriplet(self, nums):
        i, j = nums[0], float("inf")

        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False
