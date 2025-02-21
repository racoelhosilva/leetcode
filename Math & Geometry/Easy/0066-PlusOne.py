"""
LeetCode Problem: Plus One
Problem Number: 66
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/plus-one/
"""

class Solution:
    # Starting from the last digit, while it is a 9, it will turn into a 0
    # If, the digit is not a 9, we will simply add 1 to the digit in that position
    # Edge case is when all digits are 9, so we reach the first digit
    # Append a 0 at the end and turn it into a 1
    # Time Complexity: O(n)
    # where n is the number of 9s from right->left
    # Space Complexity: O(1)
    def plusOne(self, digits):
        idx = len(digits)-1
        while digits[idx] == 9:
            digits[idx] = 0
            if idx == 0:
                digits.append(0)
            else:
                idx -= 1
        digits[idx] += 1
        return digits