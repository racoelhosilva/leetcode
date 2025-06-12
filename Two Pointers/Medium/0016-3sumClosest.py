"""
LeetCode Problem: 3Sum Closest
Problem Number: 16
Difficulty: Medium
Topic: Two Pointers
Link: https://leetcode.com/problems/3sum-closest/
"""

class Solution:
    # Two Pointers
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            l, r = i + 1, n - 1
            
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if abs(cur - target) < abs(res - target):
                    res = cur
                
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    return cur
        
        return res
