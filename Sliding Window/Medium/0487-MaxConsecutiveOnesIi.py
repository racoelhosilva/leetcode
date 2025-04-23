"""
LeetCode Problem: Max Consecutive Ones II
Problem Number: 487
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/max-consecutive-ones-ii/
"""

class Solution:
    # Sliding Window
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findMaxConsecutiveOnes(self, nums):
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
            
            res = max(r - l + 1, res)
            r += 1
        return res
