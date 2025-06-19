"""
LeetCode Problem: Partition Array Such That Maximum Difference Is K
Problem Number: 2294
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
"""

class Solution:
    # Sort + Greedy
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def partitionArray(self, nums, k):
        nums.sort()
        res = 0
        l = nums[0]
        for r in nums:
            if r - l > k:
                res += 1
                l = r
        return res
