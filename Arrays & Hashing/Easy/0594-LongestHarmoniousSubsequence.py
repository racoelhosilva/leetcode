"""
LeetCode Problem: Longest Harmonious Subsequence
Problem Number: 594
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/longest-harmonious-subsequence/
"""

class Solution:
    # Hash Map + Two Pointer
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findLHS(self, nums):
        freqs = dict()
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        res = 0
        for x in freqs.keys():
            if x + 1 in freqs:
                res = max(res, freqs[x] + freqs[x+1])
        return res
