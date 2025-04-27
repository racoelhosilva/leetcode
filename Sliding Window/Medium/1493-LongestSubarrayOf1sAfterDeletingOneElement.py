"""
LeetCode Problem: Longest Subarray of 1s After Deleting One Element
Problem Number: 1493
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
"""

class Solution:
    # Sliding Window
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def longestSubarray(self, nums):
        l, r = 0, 0
        zero_count = 0
        res = 0
        while r < len(nums):
            if nums[r] == 0:
                zero_count += 1
            
            if zero_count > 1:                    
                while zero_count > 1:
                    if nums[l] == 0:
                        zero_count -= 1
                    l += 1
            
            res = max(r - l, res)
            r += 1
        return res
