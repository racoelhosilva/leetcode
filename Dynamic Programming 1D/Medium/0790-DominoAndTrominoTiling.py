"""
LeetCode Problem: Domino and Tromino Tiling
Problem Number: 790
Difficulty: Medium
Topic: Dynamic Programming 1D
Link: https://leetcode.com/problems/domino-and-tromino-tiling/
"""

class Solution:
    # Brute Force
    # Time Complexity: O(3^n)
    # Space Complexity: O(3^n)
    def numTilings(self, n):
        MOD = 1000000007
        def aux(i, gap):
            if i > n:
                return 0
            if i == n:
                return not gap
            if gap:
                return aux(i+1, False) + aux(i+1, True)
            return aux(i+1, False) + aux(i+2, False) + 2 * aux(i+2, True)
        return aux(0, False) % MOD

    # Memoization (Top-Down)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def numTilings(self, n):
        MOD = 1000000007
        memo = [[-1] * 2 for _ in range(n)]
        def aux(i, gap):
            if i > n:
                return 0
            if i == n:
                return not gap
            if memo[i][gap] != -1:
                return memo[i][gap]

            if gap:
                memo[i][gap] = aux(i+1, False) + aux(i+1, True)
            else:
                memo[i][gap] = aux(i+1, False) + aux(i+2, False) + 2 * aux(i+2, True)
            return memo[i][gap]
        return aux(0, False) % MOD
    
    # Dynamic Programming (Bottom-Up)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def numTilings(self, n):
        MOD = 1000000007

        dp = [[0] * 2 for _ in range(n+2)]
        dp[1], dp[2] = [1, 1], [2, 2]
        
        for i in range(3, n+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + 2*dp[i-2][1]
            dp[i][1] = dp[i-1][0] + dp[i-1][1]
        
        return dp[n][0] % MOD
    
    # Space Optimized
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def numTilings(self, n):
        if n <= 2:
            return n

        MOD = 1000000007
        fp, gp, fp2, gp2 = 2, 2, 1, 1
        
        for _ in range(3, n+1):
            f = fp + fp2 + 2 * gp2
            g = fp + gp
            fp, gp, fp2, gp2 = f, g, fp, gp
        
        return fp % MOD 

    # Alternative Recurrence Formula
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def numTilings(self, n):
        if n <= 2:
            return n
        MOD = 10**9 + 7
        dp = [1] * (n+1)
        dp[2] = 2
        dp[3] = 5
        for i in range(4, n+1):
            dp[i] = (2 * dp[i-1] + dp[i-3])
        return dp[n] % MOD
