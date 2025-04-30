"""
LeetCode Problem: Minimum Flips to Make a OR b Equal to c
Problem Number: 1318
Difficulty: Medium
Topic: Bit Manipulation
Link: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
"""

class Solution:
    # Caching Results
    # Time Complexity: O(32) -> O(1)
    # Space Complexity: O(8) -> O(1)
    def minFlips(self, a, b, c):
        """
        A:01010101
        B:00110011
        C:00001111
        r:01121000
        """
        res = 0
        op = [0,1,1,2,1,0,0,0]
        for i in range(32):
            ba = ((a >> i) & 1)
            bb = ((b >> i) & 1) << 1
            bc = ((c >> i) & 1) << 2
            res += op[bc + bb + ba]
        return res
    
    # Bit Count
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def minFlips(self, a, b, c):
        # Other representations
        # A~B~C + ~AB~C + (AB~C) * 2 + ~A~BC
        # ~C(A|B) + ~(A^B) & (A^C)
        return ((a | b) ^ c).bit_count() + (a & b & ~c).bit_count()
