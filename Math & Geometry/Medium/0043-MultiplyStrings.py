"""
LeetCode Problem: Multiply Strings
Problem Number: 43
Difficulty: Medium
Topic: Math & Geometry
Link: https://leetcode.com/problems/multiply-strings/
"""

class Solution:
    # Multiplication Algorithm
    # Time Complexity: O(m + n)
    # Space Complexity: O(m + n)
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1 = len(num1)
        n2 = len(num2)
        res = [0] * (n1 + n2)

        num1 = num1[::-1]
        num2 = num2[::-1]

        for place2, digit2 in enumerate(num2):
            for place1, digit1 in enumerate(num1):
                place = place1 + place2
                operation = int(digit1) + int(digit2) + res[place]
                res[place] = operation % 10
                res[place + 1] = operation // 10
        
        while res[-1] == 0:
            res.pop()
        
        return "".join(str(digit) for digit in reversed(res))
