"""
LeetCode Problem: Maximum Difference Between Even and Odd Frequency I
Problem Number: 3442
Difficulty: Easy
Topic: Arrays & Hashing
Link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
"""

class Solution:
    # Frequency tracking
    # Time Complexity: O(n)
    # Space Complexity: O(l)
    def maxDifference(self, s):
        freqs = dict()
        max_odd = -1
        min_even = 101

        for char in s:
            freqs[char] = freqs.get(char, 0) + 1
        for _,v in freqs:
            if v % 2 == 1 and v > max_odd:
                max_odd = v
            if v % 2 == 0 and v < min_even:
                min_even = v
        return max_odd - min_even
