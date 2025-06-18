"""
LeetCode Problem: Best Time to Buy and Sell Stock with Transaction Fee
Problem Number: 714
Difficulty: Medium
Topic: Dynamic Programming 2D
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""

class Solution:
    # Brute-Force
    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    def maxProfit(self, prices, fee):
        n = len(prices)

        def aux(idx, own):
            if idx == n:
                return 0
            
            # skip
            res = aux(idx + 1, own) 
            
            if own: # sell
                sell = prices[idx] - fee + aux(idx + 1, False)
                res = max(res, sell)
            else: # buy
                buy = -prices[idx] + aux(idx + 1, True)
                res = max(res, buy)
            return res
        return aux(0, False)
    
    # Memoization (Top-Down)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxProfit(self, prices, fee):
        n = len(prices)
        memo = [[None] * 2 for _ in range(n)]
        
        def aux(idx, own):
            if idx == n:
                return 0
            if memo[idx][own]:
                return memo[idx][own]

            # skip
            res = aux(idx + 1, own) 
            if own: # sell
                sell = prices[idx] - fee + aux(idx + 1, False)
                res = max(res, sell)
            else: # buy
                buy = -prices[idx] + aux(idx + 1, True)
                res = max(res, buy)
            
            memo[idx][own] = res
            return res
        return aux(0, False)

    # Dynamic Programming (Bottom-Up)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxProfit(self, prices, fee):
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        
        for idx in range(n-1, -1, -1):
            for own in range(2):
                best = dp[idx+1][own]
                if own:
                    best = max(best, prices[idx] - fee + dp[idx+1][0])
                else:
                    best = max(best, -prices[idx] + dp[idx+1][1])
                dp[idx][own] = best

        return dp[0][0]
    
    # Space Optimized
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxProfit(self, prices, fee):
        n = len(prices)
        cur = nxt = [0, 0]
        
        for idx in range(n-1, -1, -1):
            for own in range(2):
                best = nxt[own]
                if own:
                    best = max(best, prices[idx] - fee + nxt[0])
                else:
                    best = max(best, -prices[idx] + nxt[1])
                cur[own] = best
            nxt = cur
        return nxt[0]
    
    # Loop Unrolling
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices, fee):
        n = len(prices)
        cur = nxt = [0, 0]
        
        for idx in range(n-1, -1, -1):
            cur[0] = max(nxt[0], -prices[idx] + nxt[1])
            cur[1] = max(nxt[1], prices[idx] - fee + nxt[0])
            nxt = cur
        return nxt[0]

    # Space Optimization
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices, fee):
        n = len(prices)
        n0 = n1 = 0
        
        for idx in range(n-1, -1, -1):
            n0 = max(n0, -prices[idx] + n1)
            n1 = max(n1, prices[idx] - fee + n0)
        return n0

    # Greedy Solution
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices, fee):
        buy, profit = 1e9, 0
        for price in prices:
            buy = min(buy, price - profit)
            profit = max(profit, price - buy - fee)
        return profit
