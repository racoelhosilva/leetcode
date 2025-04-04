"""
LeetCode Problem: Maximum Number of Vowels in a Substring of Given Length
Problem Number: 1456
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""

class Solution:
    # Sliding Window
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxVowels(self, s, k):
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        res = 0
        for idx in range(k):
            if s[idx] in vowels:
                count += 1
        res = count
        for idx in range(k, len(s)):
            if s[idx - k] in vowels:
                count -= 1
            if s[idx] in vowels:
                count += 1
            res = max(res, count)
        return res
