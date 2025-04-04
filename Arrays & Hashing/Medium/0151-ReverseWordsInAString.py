"""
LeetCode Problem: Reverse Words in a String
Problem Number: 151
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/reverse-words-in-a-string/
"""

class Solution:
    # Reverse Iteration
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverseWords(self, s):
        words = s.split()
        res = []
        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])
        return " ".join(res)
    
    # Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverseWords(self, s):
        words = s.split()
        l, r = 0, len(words) - 1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        return " ".join(words)

    # Python one-liner
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
