"""
LeetCode Problem: Longest Binary Subsequence Less Than or Equal to K
Problem Number: 2311
Difficulty: Medium
Topic: Greedy
Link: https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/
"""

class Solution:
    # Greedy + Reverse Iteration
    # Note: bits = k.bit_length is used as an optimization since if the index of a 1 is
    # larger than the bit_length of k, the number will definitely be larger than k
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def longestSubsequence(self, s, k):
        n = len(s) - 1
        res = 0
        cur = 0
        bits = k.bit_length()
        for i in range(n, -1, -1):
            if s[i] == "1":
                idx = n - i
                if idx < bits and cur + (1 << idx) <= k:
                    cur += 1 << idx
                    res += 1
            else:
                res += 1
        return res
