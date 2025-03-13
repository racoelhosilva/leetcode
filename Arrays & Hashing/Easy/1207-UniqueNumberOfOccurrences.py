"""
LeetCode Problem: Unique Number of Occurrences
Problem Number: 1207
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/unique-number-of-occurrences/
"""

class Solution:
    # Hash Map + Hash Set
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def uniqueOccurrences(self, arr):
        freq = dict()
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        freqs = set()
        for _num, frequency in freq.items():
            if frequency in freqs:
                return False
            freqs.add(frequency)
        return True
