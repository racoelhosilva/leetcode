"""
LeetCode Problem: Generate Parentheses
Problem Number: 22
Difficulty: Medium
Topic: Stack
Link: https://leetcode.com/problems/generate-parentheses/
"""

class Solution:
    # Backtracking
    # Time Complexity: O(4^n / sqrt(n))
    # Space Complexity: O(n)
    def generateParenthesis(self, n):
        res = []
        cur = []
        def backtrack(o, c):
            if len(cur) == n * 2:
                res.append(cur[:])
                return
            
            if o < n:
                cur.append('(')
                backtrack(o+1, c)
                cur.pop()
            if c < o:
                cur.append(')')
                backtrack(o, c+1)
                cur.pop()

        backtrack(0, 0)
        return res
    
    # Dynamic Programming
    # Time Complexity: O(4^n / sqrt(n))
    # Space Complexity: O(n)
    def generateParenthesis(self, n):
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]

        for i in range(n+1):
            for j in range(i):
                for l in dp[j]:
                    for r in dp[i - j - 1]:
                        dp[i].append('(' + l + ')' + r)

        return dp[-1]
