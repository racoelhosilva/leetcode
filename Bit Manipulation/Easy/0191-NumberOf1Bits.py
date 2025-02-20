"""
LeetCode Problem: Number of 1 Bits
Problem Number: 191
Difficulty: Easy
Topic: Bit Manipulation
Link: https://leetcode.com/problems/number-of-1-bits/
"""

class Solution:
    # Mask Comparison
    # Time Complexity: O(32) -> O(1)
    # Space Complexity: O(1)  
    def hammingWeight(self, n):
        res = 0
        for i in range(32):
            if n & (1 << i):
                res += 1
        return res
    
    # Right Shifting
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def hammingWeight(self, n):
        res = 0
        while n != 0:
            if n & 1:
                res += 1
            n >>= 1
        return res

    # Bit Manipulation (Optimal)
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def hammingWeight(self, n):
        res = 0
        while n != 0:
            res += 1
            n &= n-1
        return res
