"""
LeetCode Problem: Longest Common Subsequence
Problem Number: 1143
Difficulty: Medium
Topic: Dynamic Programming 2D
Link: https://leetcode.com/problems/longest-common-subsequence/
"""

class Solution:
    # Brute Force
    # Time Complexity: O(2^(m+n))
    # Space Complexity: O(m + n)
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        def aux(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + aux(i+1, j+1)
            return max(aux(i+1, j), aux(i, j+1))
        return aux(0, 0)

    # Memoization (Top-Down)
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        memo = [[-1] * n for _ in range(m)]
        def aux(i, j):
            if i == m or j == n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            
            if text1[i] == text2[j]:
                memo[i][j] = 1 + aux(i+1, j+1)
            else:
                memo[i][j] = max(aux(i+1, j), aux(i, j+1))
            return memo[i][j]
        return aux(0, 0)
    
    # Dynamic Programming (Bottom-Up)
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]
    
    # Space Optimization (Single Row)
    # Time Complexity: O(m * n)
    # Space Complexity: O(min(m, n))
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        if n > m:
            text1, text2 = text2, text1
            m, n = n, m

        dp = [0] * (n+1)
        
        for i in range(m):
            prev = 0
            for j in range(n):
                tmp = dp[j+1]
                if text1[i] == text2[j]:
                    dp[j+1] = prev + 1
                else:
                    dp[j+1] = max(dp[j], tmp)
                prev = tmp
        return dp[-1]
