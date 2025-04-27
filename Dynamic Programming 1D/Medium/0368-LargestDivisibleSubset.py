"""
LeetCode Problem: Largest Divisible Subset
Problem Number: 368
Difficulty: Medium
Topic: Dynamic Programming 1D
Link: https://leetcode.com/problems/largest-divisible-subset/
"""

class Solution:
    # Dynamic Programming
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums.sort()
        dp = [1 for _ in range(n)]
        prev = [-1 for _ in range(n)]
        largest_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[largest_idx]:
                largest_idx = i 
        
        res = []
        while largest_idx != -1:
            res.append(nums[largest_idx])
            largest_idx = prev[largest_idx]

        return res
