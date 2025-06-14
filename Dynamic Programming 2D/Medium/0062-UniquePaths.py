"""
LeetCode Problem: Unique Paths
Problem Number: 62
Difficulty: Medium
Topic: Dynamic Programming 2D
Link: https://leetcode.com/problems/unique-paths/
"""

class Solution:
    # Recursive Approach
    # Time Complexity: O(2^(m+n)) -> TLE
    # Space Complexity: O(2^(m+n))
    def uniquePaths(self, m, n):
        def aux(r, c):
            if r == m-1 and c == n-1:
                return 1
            if r >= m or c >= n:
                return 0
            return aux(r, c+1) + aux(r+1, c)
        return aux(0, 0)
    
    # Recursion with Memoization (Top-Down)
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def uniquePaths(self, m, n):
        memo = [[-1] * n for _ in range(m)]
        def aux(r, c):
            if r == m-1 and c == n-1:
                return 1
            if r >= m or c >= n:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
            
            memo[r][c] = aux(r, c+1) + aux(r+1, c)
            return memo[r][c]
        return aux(0, 0)
    
    # Tabulation (Bottom-Up)
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def uniquePaths(self, m, n):
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] += dp[r+1][c] + dp[r][c+1]

        return dp[0][0]

    # Space Optimized
    # Time Complexity: O(m * n)
    # Space Complexity: O(n)
    def uniquePaths(self, m, n):
        dp = [1] * n
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                dp[c] += dp[c + 1]

        return dp[0]

    # Math: Permutations
    # Every path from [0,0] to [m-1,n-1] takes exactly m + n - 2 steps
    # This means that the solution can be found as the number of permutations of those two movements
    # Excluding permutations of equal down and right movements: (m + n - 2)! / ((m-1)! * (n-1)!) 
    # To avoid calculating a factorial function, we can do the math iteratively
    # Time Complexity: O(min(n, m))
    # Space Complexity: O(1)
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        if n > m:
            m, n = n, m
        
        res = 1
        c = 1
        for r in range(m, m + n - 1):
            res *= r
            res //= c
            c += 1
        
        return res
