"""
LeetCode Problem: Is Subsequence
Problem Number: 392
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/is-subsequence/
"""

class Solution:
    # Two Pointer
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isSubsequence(self, s, t):
        ps = pt = 0
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        return ps == len(s)
