"""
LeetCode Problem: Unique Paths II
Problem Number: 63
Difficulty: Medium
Topic: Dynamic Programming 2D
Link: https://leetcode.com/problems/unique-paths-ii/
"""

class Solution:
    # Recursive Approach
    # Time Complexity: O(2^(m+n)) -> TLE
    # Space Complexity: O(2^(m+n))
    def uniquePathsWithObstacles(self, grid):
        M, N = len(grid), len(grid[0])

        def aux(r, c):
            if r >= M or c >= N or grid[r][c]:
                return 0
            if r == M-1 and c == N-1:
                return 1
            return aux(r+1, c) + aux(r, c+1)
        return aux(0, 0)
    
    # Recursion with Memoization (Top-Down)
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def uniquePathsWithObstacles(self, grid):
        M, N = len(grid), len(grid[0])
        memo = [[-1] * N for _ in range(M)]
        memo[M-1][N-1] = 1

        def aux(r, c):
            if r >= M or c >= N or grid[r][c]:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
            memo[r][c] = aux(r+1, c) + aux(r, c+1)
            return memo[r][c]
        return aux(0, 0)
    
    # Tabulation (Bottom-Up)
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def uniquePathsWithObstacles(self, grid):
        M, N = len(grid), len(grid[0])
        if grid[0][0] or grid[M-1][N-1]:
            return 0
        
        dp = [[0] * (N+1) for _ in range(M+1)]
        dp[M-1][N-1] = 1

        for r in range(M-1, -1, -1):
            for c in range(N-1, -1, -1):
                if grid[r][c] == 0:
                    dp[r][c] += dp[r+1][c] + dp[r][c+1] 

        return dp[0][0]
    
    # Space Optimized
    # Time Complexity: O(m * n)
    # Space Complexity: O(n)
    def uniquePathsWithObstacles(self, grid):
        M, N = len(grid), len(grid[0])
        if grid[0][0] or grid[M-1][N-1]:
            return 0
        
        dp = [0] * (N + 1)
        dp[N-1] = 1

        for r in range(M-1, -1, -1):
            for c in range(N-1, -1, -1):
                if grid[r][c]:
                    dp[c] = 0
                else:
                    dp[c] += dp[c+1] 

        return dp[0]
