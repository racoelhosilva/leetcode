"""
LeetCode Problem: Best Time to Buy and Sell Stock
Problem Number: 121
Difficulty: Easy
Topic: Sliding Window
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    # Naive Approach
    # For each day, assume that we bought stock and check for future days
    # until the maximum profit is found
    # Time Complexity: O(n^2) -> Time Limit Exceeded
    # Space Complexity: O(1)
    def maxProfit(self, prices):
        profit = 0
        for buy in range(len(prices)):
            for sell in range(buy, len(prices)):
                profit = max(profit, prices[sell] - prices[buy])
        return profit

    # Kadane's Algorithm
    # Besides the maximum profit, keep track of the lowest value
    # Go through the days and if the current profit using the lowest value
    # is greater, update the maximum profit
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices):
        profit = 0
        lowest = prices[0]
        for day in range(len(prices)):
            lowest = min(lowest, prices[day])
            profit = max(profit, prices[day] - lowest)
        return profit
