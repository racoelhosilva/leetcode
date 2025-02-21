"""
LeetCode Problem: Climbing Stairs
Problem Number: 70
Difficulty: Easy
Topic: Dynamic Programming 1D
Link: https://leetcode.com/problems/climbing-stairs/
"""

class Solution:
    # Recursive Approach
    # Time Complexity: O(2^n) -> Time Limit Exceeded
    # Space Complexity: O(n)
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    # Recursion with Memoization (Top-Down)
    # Time Complexity: O(n) 
    # Space Complexity: O(n)
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        memo = {0:1, 1:1}
        def aux(n):
            if n not in memo:
                memo[n] = aux(n-1) + aux(n-2)
            return memo[n]
        return aux(n)
    
    # Tabulation (Bottom-Up)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        table = {0:1, 1:1}
        for num in range(2, n+1):
            table[num] = table[num-1] + table[num-2]
        return table[n]
    
    # Space Optimization
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        prev = cur = 1
        for _ in range(2, n+1):
            prev, cur = cur, cur + prev
        return cur
