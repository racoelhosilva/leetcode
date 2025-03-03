"""
LeetCode Problem: Sum of Two Integers
Problem Number: 371
Difficulty: Medium
Topic: Bit Manipulation
Link: https://leetcode.com/problems/sum-of-two-integers/
"""

class Solution:
    # Bit Manipulation
    # For each of the 32 bits:
    # Isolate the bits of each number
    # Calculate the final bit using XORs
    # Determine the carry (based on a truth table derivation)
    # Add to the result
    # In case the result is negative (> 0x7FFFFFFF) due to 2's complement:
    # Mask it and sign extend it (in some languages the variable always takes 64 bits for example)
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def getSum(self, a, b):
        res = 0
        carry = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur = a_bit ^ b_bit ^ carry
            carry = (b_bit & carry) | (a_bit & ((~b_bit & carry) | (b_bit & ~carry))) 
            res |= (cur << i)
        
        if res > 0x7FFFFFFF:
            res = ~ (res ^ 0xFFFFFFFF)
        
        return res

    # Bit Manipulation
    # At each step:
    # XOR all the digits between A and B (addition)
    # Store the digits with carry in B (carry)
    # Repeat the process
    # If the number is negative, repeat the final step like the last approach
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def getSum(self, a, b):
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & 0xFFFFFFFF
            b = carry & 0xFFFFFFFF
        return a if a <= 0x7FFFFFFF else ~(a ^ 0xFFFFFFFF)
