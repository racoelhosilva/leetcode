"""
LeetCode Problem: Minimum Deletions to Make String K Special
Problem Number: 3085
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/
"""

class Solution:
    # Frequency + Enumeration
    # Time Complexity: O(n + c^2)
    # Space Complexity: O(c)
    def minimumDeletions(self, word, k):
        from collections import defaultdict
        freqs = defaultdict(int)

        for char in word:
            freqs[char] += 1
        
        res = len(word)
        for c1 in freqs.values():
            dels = 0
            for c2 in freqs.values():
                if c2 < c1:
                    dels += c2
                elif c2 > c1 + k:
                    dels += c2 - (c1 + k)
            res = min(dels, res)
        return res
