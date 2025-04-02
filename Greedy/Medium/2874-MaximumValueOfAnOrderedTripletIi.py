"""
LeetCode Problem: Maximum Value of an Ordered Triplet II
Problem Number: 2874
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/
"""

class Solution:
    # Brute-Force Approach
    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    def maximumTripletValue(self, nums):
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res
    
    # Greedy First Value
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def maximumTripletValue(self, nums):
        res = 0
        for k in range(2, len(nums)):
            best_i = nums[0]
            for j in range(1, k):
                res = max(res, (best_i - nums[j]) * nums[k])
                best_i = max(best_i, nums[j])
        return res

    # Fix j and Prefix Sums
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maximumTripletValue(self, nums):
        n = len(nums)
        res = 0
        left_max = [0] * n
        right_max = [0] * n
        for idx in range(1, n):
            left_max[idx] = max(left_max[idx - 1], nums[idx - 1])
            right_max[n - idx - 1] = max(right_max[n - idx], nums[n - idx])
        for j in range(1, n-1):
            res = max(res, (left_max[j] - nums[j]) * right_max[j])
        return res

    # Greedy First Value and Difference
    # Time Complexity: O(n)
    # Space Complexity: O(1)    
    def maximumTripletValue(self, nums):
        res = 0
        best_i = 0
        best_diff = 0
        for k in range(len(nums)):
            res = max(res, best_diff * nums[k])
            best_diff = max(best_diff, best_i - nums[k])
            best_i = max(best_i, nums[k])
        return res
