"""
LeetCode Problem: Count Complete Subarrays in an Array
Problem Number: 2799
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/count-complete-subarrays-in-an-array/
"""

class Solution:
    # Sliding Window
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def countCompleteSubarrays(self, nums):
        n = len(nums)
        diff = len(set(nums))
        l = 0
        freqs = dict()
        res = 0
        for r in range(n):
            freqs[nums[r]] = freqs.get(nums[r], 0) + 1
            while len(freqs) == diff:
                res += n - r
                freqs[nums[l]] -= 1
                if freqs[nums[l]] <= 0:
                    freqs.pop(nums[l])
                l += 1
        return res
