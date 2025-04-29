"""
LeetCode Problem: Count Subarrays Where Max Element Appears at Least K Times
Problem Number: 2962
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
"""

class Solution:
    # Sliding Window
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def countSubarrays(self, nums, k):
        n = len(nums)
        mx = max(nums)
        mx_count = 0
        res = 0
        l = 0
        for r in range(n):
            if nums[r] == mx:
                mx_count += 1

            temp = n - r        
            while mx_count == k:
                res += temp
                if nums[l] == mx:
                    mx_count -= 1
                l += 1
        return res
    
    # Track Max Indexes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def countSubarrays(self, nums, k):
        n = len(nums)
        mx = max(nums)
        idxs = []
        res = 0

        for idx in range(n):
            if nums[idx] == mx:
                idxs.append(idx)
            if len(idxs) >= k:
                res += idxs[-k] + 1
        return res
