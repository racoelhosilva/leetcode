"""
LeetCode Problem: Reverse Integer
Problem Number: 7
Difficulty: Medium
Topic: Bit Manipulation
Link: https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    # Iteration
    # To avoid overflows in 32 bit integers, we need to check, at every step that updating the res is safe
    # res will definitely overflow when it is larger than INTMAX//10
    # res will also overflow when it is equal to INTMAX//10 but we will add a number larger than INTMAX%10
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def reverse(self, x):
        MAX = (1 << 31) - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x > 0:
            digit = x % 10
            x = x // 10

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            res = res * 10 + digit

        return sign * res
