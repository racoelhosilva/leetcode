"""
LeetCode Problem: Edit Distance
Problem Number: 72
Difficulty: Medium
Topic: Dynamic Programming 2D
Link: https://leetcode.com/problems/edit-distance/
"""

class Solution:
    # Brute Force
    # Time Complexity: O(3^min(m, n))
    # Space Complexity: O(3^min(m, n))
    def minDistance(self, word1, word2):
        def aux(w1, w2):
            if not w1 and not w2:
                return 0
            if not w1:
                return len(w2)
            if not w2:
                return len(w1)
            
            if w1[0] == w2[0]:
                return aux(w1[1:], w2[1:])
            
            insert = aux(w1, w2[1:])
            delete = aux(w1[1:], w2)
            switch = aux(w1[1:], w2[1:])
            return min(insert, delete, switch)
        return aux(word1, word2)

    # Memoization (Top-Down)
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        memo = [[-1] * (n) for _ in range(m)]
        
        def aux(i1, i2):
            if i1 == m:
                return n - i2
            if i2 == n:
                return m - i1
            
            if memo[i1][i2] != -1:
                return memo[i1][i2]
            
            if word1[i1] == word2[i2]:
                memo[i1][i2] = aux(i1+1, i2+1)
            else:
                insert = aux(i1, i2+1)
                delete = aux(i1+1, i2)
                switch = aux(i1+1, i2+1)
                memo[i1][i2] = 1 + min(insert, delete, switch)
            
            return memo[i1][i2]
        
        return aux(0, 0)

    # Dynamic Programming (Bottom-Up)
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i1 in range(m+1):
            dp[i1][0] = i1
        for i2 in range(n+1):
            dp[0][i2] = i2
        
        for i1 in range(1, m+1):
            for i2 in range(1, n+1):
                if word1[i1-1] == word2[i2-1]:
                    dp[i1][i2] = dp[i1-1][i2-1]
                else:
                    insert = dp[i1][i2-1]
                    delete = dp[i1-1][i2]
                    switch = dp[i1-1][i2-1]
                    dp[i1][i2] = 1 + min(insert, delete, switch)
        return dp[-1][-1]
    
    # Space Optimization (Single Row)
    # Time Complexity: O(m * n)
    # Space Complexity: O(min(m, n))
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        if not word1 and not word2:
            return 0
        if not word1:
            return n
        if not word2:
            return m
        
        if n > m:
            m, n = n, m
            word1, word2 = word2, word1

        dp = [0] * (n+1)
        
        for i2 in range(n+1):
            dp[i2] = i2
        
        for i1 in range(1, m+1):
            diagonal = i1-1
            left = i1
            for i2 in range(1, n+1):
                top = dp[i2]                
                if word1[i1-1] == word2[i2-1]:
                    dp[i2] = diagonal
                else:
                    dp[i2] = 1 + min(left, top, diagonal)
                left = dp[i2]
                diagonal = top
        return dp[-1]
