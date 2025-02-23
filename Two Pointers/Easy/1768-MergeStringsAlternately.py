"""
LeetCode Problem: Merge Strings Alternately
Problem Number: 1768
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/merge-strings-alternately/
"""

class Solution:
    # Two Pointers
    # Time Complexity: O(m + n)
    # Space Complexity: O(m + n)
    def mergeAlternately(self, word1, word2):
        res = ""
        i = j = 0
        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
        res += word1[i:]
        res += word2[j:]
        return res

    # One Pointer
    # Time Complexity: O(m + n)
    # Space Complexity: O(m + n)
    def mergeAlternately(self, word1, word2):
        res = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return res
