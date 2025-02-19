"""
LeetCode Problem: Valid Anagram
Problem Number: 242
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/valid-anagram/
"""

class Solution:
    # Hash Table Approach
    # Store the frequencies of each letter of s in a hash table
    # Compare those frequencies to the ones in t
    # This solution works for every possible character
    # Time Complexity: O(n)
    # Space Complexity: O(26) -> O(1)
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        freq = dict()
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1
        return True
    
    # Python Counters
    # Collection library implements Counter for situations like this
    # Time Complexity: O(n)
    # Space Complexity: O(26) -> O(1)
    def isAnagram(self, s, t):
        from collections import Counter
        return Counter(s) == Counter(t)

    # Array Approach
    # Since there are only lowercase letters, store frequencies in array
    # Time Complexity: O(n)
    # Space Complexity: O(26) -> O(1)
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        for char in t:
            if freq[ord(char) - ord('a')] == 0:
                return False
            freq[ord(char) - ord('a')] -= 1
        return True
