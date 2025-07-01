"""
LeetCode Problem: Find the Original Typed String I
Problem Number: 3330
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/find-the-original-typed-string-i/
"""

class Solution:
    # One Pass
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def possibleStringCount(self, word):
        res = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                res += 1
        return res
