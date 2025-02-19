"""
LeetCode Problem: Ransom Note
Problem Number: 383
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/ransom-note/
"""

class Solution:
    # Hash table Approach
    # Store the frequencies of each letter of s in a hash table
    # Compare those frequencies to the ones in t
    # This solution works for every possible character
    # Time Complexity: O(n)
    # Space Complexity: O(26) -> O(1)
    def canConstruct(self, ransomNote, magazine):
        freq = dict()
        for char in magazine:
            freq[char] = freq.get(char, 0) + 1
        for char in ransomNote:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1
        return True

    # Array Approach
    # Since there are only lowercase letters, store frequencies in array
    # Time Complexity: O(n)
    # Space Complexity: O(26) -> O(1)
    def canConstruct(self, ransomNote, magazine):
        freq = [0] * 26
        for char in magazine:
            freq[ord(char) - ord('a')] += 1
        for char in ransomNote:
            if freq[ord(char) - ord('a')] == 0:
                return False
            freq[ord(char) - ord('a')] -= 1
        return True