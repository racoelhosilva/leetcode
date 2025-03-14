"""
LeetCode Problem: House Robber
Problem Number: 198
Difficulty: Medium
Topic: Dynamic Programming 1D
Link: https://leetcode.com/problems/house-robber/
"""

class Solution:
    # Recursive Approach
    # Time Complexity: O(2^n) -> Time Limit Exceeded
    # Space Complexity: O(n)
    def rob(self, nums):
        def aux(n):
            if n >= len(nums):
                return 0
            return max(aux(n+1), nums[n] + aux(n+2))
        return aux(0)
    
    # Recursion with Memoization (Top-Down)
    # Time Complexity: O(n) 
    # Space Complexity: O(n)
    def rob(self, nums):
        memo = [-1] * len(nums)
        
        def aux(n):
            if n >= len(nums):
                return 0
            if memo[n] != -1:
                return memo[n]
            memo[n] = max(aux(n+1), nums[n] + aux(n+2))
            return memo[n]

        return aux(0)
    
    # Tabulation (Bottom-Up)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])            
        
        return dp[-1]

    # Space Optimization
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def rob(self, nums):
        r1 = r2 = 0
        for num in nums:
            r1, r2 = max(r1, num + r2), r1        
        return r1
