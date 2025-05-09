"""
LeetCode Problem: Length of Last Word
Problem Number: 58
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/length-of-last-word/
"""

class Solution:
    # Reverse iteration
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lengthOfLastWord(self, s):
        end = len(s) - 1
        while s[end] == " ":
            end -= 1
        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        return end - start
