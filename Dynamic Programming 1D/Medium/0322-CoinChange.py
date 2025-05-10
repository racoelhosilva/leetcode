"""
LeetCode Problem: Coin Change
Problem Number: 322
Difficulty: Medium
Topic: Dynamic Programming 1D
Link: https://leetcode.com/problems/coin-change/
"""

class Solution:
    # Recursive Approach
    # Time Complexity: O(n^t) -> Time Limit Exceeded
    # Space Complexity: O(t)
    def coinChange(self, coins, amount):
        def aux(amount):
            if amount == 0:
                return 0
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + aux(amount - coin))
            return res
        res = aux(amount)
        return -1 if res >= 1e9 else res

    # Recursion with Memoization (Top-Down)
    # Time Complexity: O(n * t)
    # Space Complexity: O(t)
    def coinChange(self, coins, amount):
        memo = dict()

        def aux(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + aux(amount - coin))
            
            memo[amount] = res
            return res
        res = aux(amount)
        return -1 if res >= 1e9 else res
    
    # Tabulation (Bottom-Up)
    # Time Complexity: O(n * t)
    # Space Complexity: O(t)
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], 1 + dp[a - coin])
        
        return dp[amount] if dp[amount] != amount + 1 else -1

