"""
LeetCode Problem: N-th Tribonacci Number
Problem Number: 1137
Difficulty: Easy
Topic: Dynamic Programming 1D
Link: https://leetcode.com/problems/n-th-tribonacci-number/
"""

class Solution:
    # Recursive Approach
    # Time Complexity: O(3^n)
    # Space Complexity: O(n)
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
    
    # Memoization (Top-Down)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        memo = {0:0, 1:1, 2:1}
        def aux(n):
            if n not in memo:
                memo[n] = aux(n-1) + aux(n-2) + aux(n-3)
            return memo[n]
        return aux(n)
    
    # Tabulation (Bottom-Up)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        table = {0:0, 1:1, 2:1}
        for i in range(3, n+1):
            table[i] = table[i-1] + table[i-2] + table[i-3]
        return table[n]

    # Space Optimization
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        twoprev, prev, cur = 0, 1, 1
        for _ in range(3, n+1):
            twoprev, prev, cur = prev, cur, twoprev + prev + cur 
        return cur
