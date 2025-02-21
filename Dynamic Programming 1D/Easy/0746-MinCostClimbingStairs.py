"""
LeetCode Problem: Min Cost Climbing Stairs
Problem Number: 746
Difficulty: Easy
Topic: Dynamic Programming 1D
Link: https://leetcode.com/problems/min-cost-climbing-stairs/
"""

class Solution:
    # Recursive Approach
    # Time Complexity: O(2^n) -> Time Limit Exceeded
    # Space Complexity: O(n)
    def minCostClimbingStairs(self, cost):
        def minCost(step):
            if step == 0 or step == 1:
                return 0
            return min(cost[step-1] + minCost(step-1), cost[step-2] + minCost(step-2))
        return minCost(len(cost))

    # Memoization (Top-Down)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minCostClimbingStairs(self, cost):
        memo = {0:0, 1:0}
        def minCost(step):
            if step not in memo:
                memo[step] = min(cost[step-1] + minCost(step-1), cost[step-2] + minCost(step-2))
            return memo[step]
        return minCost(len(cost))

    # Tabulation (Bottom-Up)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minCostClimbingStairs(self, cost):
        table = {0:0, 1:0}
        for step in range(2, len(cost)+1):
            table[step] = min(cost[step-1] + table[step-1], cost[step-2] + table[step-2])
        return table[len(cost)]
    
    # Space Optimization
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minCostClimbingStairs(self, cost):
        prev, cur = cost[0], cost[1]
        for step in range(2, len(cost)):
            next = cost[step] + min(prev, cur)
            prev, cur = cur, next
        return min(prev, cur)
