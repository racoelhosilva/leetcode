"""
LeetCode Problem: Solving Questions With Brainpower
Problem Number: 2140
Difficulty: Medium
Topic: Dynamic Programming 1D
Link: https://leetcode.com/problems/solving-questions-with-brainpower/
"""

class Solution:
    # Memoization (Top-Down)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def mostPoints(self, questions):
        memo = [0] * (len(questions) + 1)
        def aux(n):
            if n >= len(questions):
                return 0
            if memo[n]:
                return memo[n]
            memo[n] = max(questions[n][0] + aux(n + questions[n][1] + 1), aux(n + 1))
            return memo[n]
        return aux(0)

    # Dynamic Programming (Bottom-Up)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * (n + 1)
        for idx in range(n - 1, -1, -1):
            dp[idx] = max(questions[idx][0] + dp[min(n, idx + questions[idx][1] + 1)], dp[idx + 1])
        return dp[0]
