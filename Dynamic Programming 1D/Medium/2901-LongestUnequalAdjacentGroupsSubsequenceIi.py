"""
LeetCode Problem: Longest Unequal Adjacent Groups Subsequence II
Problem Number: 2901
Difficulty: Medium
Topic: Dynamic Programming 1D
Link: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/
"""

class Solution:
    # Dynamic Programming
    # Time Complexity: O(l * n^2)
    # Space Compleixty: O(n)
    def getWordsInLongestSubsequence(self, words, groups):
        n = len(words)
        max_idx = 0
        dp = [1] * n
        prev = [-1] * n

        def check(a, b):
            if len(a) != len(b):
                return False
            res = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    res += 1
                    if res > 1:
                        return False
            return res == 1
        
        for r in range(1, n):
            for l in range(r):
                if check(words[r], words[l]) and groups[r] != groups[l] and dp[l] + 1 > dp[r]:
                    dp[r] = dp[l] + 1
                    prev[r] = l
            if dp[r] > dp[max_idx]:
                max_idx = r
        
        res = []
        while max_idx >= 0:
            res.append(words[max_idx])
            max_idx = prev[max_idx]
        res.reverse()
        return res
