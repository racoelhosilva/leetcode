"""
LeetCode Problem: Maximum Average Subarray I
Problem Number: 643
Difficulty: Easy
Topic: Sliding Window
Link: https://leetcode.com/problems/maximum-average-subarray-i/
"""

class Solution:
    # Sliding Window
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Note: it's easier to keep track of max sum since divisions take some time to perform
    def findMaxAverage(self, nums, k):
        cur = 0
        for idx in range(k):
            cur += nums[idx]
        res = cur
        for idx in range(k, len(nums)):
            cur +=  nums[idx] - nums[idx - k]
            res = max(res, cur)
        return res / float(k)
