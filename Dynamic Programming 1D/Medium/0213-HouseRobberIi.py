"""
LeetCode Problem: House Robber II
Problem Number: 213
Difficulty: Medium
Topic: Dynamic Programming 1D
Link: https://leetcode.com/problems/house-robber-ii/
"""

class Solution:
    # Recursive Approach
    # Time Complexity: O(2^n) -> Time Limit Exceeded
    # Space Complexity: O(n)
    def rob(self, nums):
        def aux(n, flag):
            if (n >= len(nums)) or (flag and n >= len(nums) - 1):
                 return 0
            return max(aux(n+1, flag), nums[n] + aux(n+2, flag or n == 0))
        return aux(0, False)
    
    # Recursion with Memoization (Top-Down)
    # Time Complexity: O(n) 
    # Space Complexity: O(n)
    def rob(self, nums):
        memo = [[-1] * 2 for _ in range(len(nums))]

        def aux(n, flag):
            if (n >= len(nums)) or (flag and n >= len(nums) - 1):
                 return 0
            if memo[n][flag] != -1:
                return memo[n][flag]
            memo[n][flag] = max(aux(n+1, flag), nums[n] + aux(n+2, flag or n == 0))
            return memo[n][flag]
        return aux(0, False)
    
    # Tabulation (Bottom-Up)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        def aux(ns):
            if not ns:
                return 0
            if len(ns) == 1:
                return ns[0]

            dp = [-1] * len(ns)
            dp[0] = ns[0]
            dp[1] = max(ns[0], ns[1])

            for idx in range(2, len(ns)):
                dp[idx] = max(ns[idx] + dp[idx-2], dp[idx-1])
            
            return dp[-1]
        return max(aux(nums[:-1]), aux(nums[1:]))
    
    # Space Optimization
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        def aux(ns):
            r1 = r2 = 0
            for num in ns:
                r1, r2 = max(r1, num + r2), r1
            return r1
        return max(aux(nums[:-1]), aux(nums[1:]))
