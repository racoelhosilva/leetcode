"""
LeetCode Problem: Add Binary
Problem Number: 67
Difficulty: Easy
Topic: Bit Manipulation
Link: https://leetcode.com/problems/add-binary/
"""

class Solution:
    # Right->Left Addition
    # Process the addition from right to left keeping track of carry
    # Repeat until both strings consumed and no more carry, reverse result
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def addBinary(self, a, b):
        res = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res.append(str(carry % 2))
            carry //= 2
        
        return res[::-1]
    
    # Python Shorthand
    # Use conversions to int, binary and string
    def addBinary(self, a, b):
        return bin(int(a,2) + int(b,2))[2:]