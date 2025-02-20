"""
LeetCode Problem: Reverse Bits
Problem Number: 190
Difficulty: Easy
Topic: Bit Manipulation
Link: https://leetcode.com/problems/reverse-bits/
"""

class Solution:
    # Masking and Shifting
    # Time Complexity: O(32) -> O(1)
    # Space Complexity: O(1)
    def reverseBits(self, n):
        res = 0
        for idx in range(32):
            bit = (n >> idx) & 1
            res |= bit << (31 - idx)
        return res
    
    # Optimal Bit Manipulation
    # Time Complexity: O(5) -> O(1)
    # Space Complexity: O(1)
    def reverseBits(self, n):
        res = n
        res = ((res & 0xFFFF0000) >> 16 | (res & 0x0000FFFF) << 16)
        res = ((res & 0xFF00FF00) >> 8 | (res & 0x00FF00FF) << 8)
        res = ((res & 0xF0F0F0F0) >> 4 | (res & 0x0F0F0F0F) << 4)
        res = ((res & 0xCCCCCCCC) >> 2 | (res & 0x33333333) << 2)
        res = ((res & 0xAAAAAAAA) >> 1 | (res & 0x55555555) << 1)
        return res & 0xFFFFFFFF
