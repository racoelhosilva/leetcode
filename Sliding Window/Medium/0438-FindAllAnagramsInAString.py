"""
LeetCode Problem: Find All Anagrams in a String
Problem Number: 438
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""

class Solution:
    # Sliding Window + Hash comparison
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        
        orda = ord('a')
        res = []
        p_freq = [0] * 26
        s_freq = [0] * 26

        for char in p:
            p_freq[ord(char) - orda] += 1
        
        for idx in range(len(s)):
            s_freq[ord(s[idx]) - orda] += 1
            if idx >= len(p):
                s_freq[ord(s[idx-len(p)]) - orda] -= 1
            if s_freq == p_freq:
                res.append(idx - len(p) + 1)
        
        return res
