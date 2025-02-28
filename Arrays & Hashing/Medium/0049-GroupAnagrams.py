"""
LeetCode Problem: Group Anagrams
Problem Number: 49
Difficulty: Medium
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/group-anagrams/
"""

from collections import defaultdict

class Solution:
    # Sorting Characters
    # Time Complexity: O(n * m log m)
    # Space Complexity: O(m * n)
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for string in strs:
            sortedString = ''.join(sorted(string))
            res[sortedString].append(string)
        return list(res.values())
    
    # Character Frequency
    # Time Complexity: O(n * m)
    # Space Complexity: O(n * m)
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for string in strs:
            chars = [0] * 26
            for char in string:
                chars[ord(char) - ord('a')] += 1    
            res[tuple(chars)].append(string)
        return list(res.values())
