"""
LeetCode Problem: Longest Unequal Adjacent Groups Subsequence I
Problem Number: 2900
Difficulty: Easy
Topic: Greedy
Link: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/
"""

class Solution:
    # Greedy
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def getLongestSubsequence(self, words, groups):
        res = [words[0]]
        cur = groups[0]

        for idx in range(1, len(groups)):
            if groups[idx] != cur:
                cur = groups[idx]
                res.append(words[idx])

        return res
