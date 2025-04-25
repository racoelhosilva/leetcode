"""
LeetCode Problem: Integer to Roman
Problem Number: 12
Difficulty: Medium
Topic: Math & Geometry
Link: https://leetcode.com/problems/integer-to-roman/
"""

class Solution:
    # Reducing the target value
    # Time Complexity: O(13) -> O(1)
    # Space Complexity: O(1)
    def intToRoman(self, num):
        convert = [
            (1000, 'M'), 
            (900, 'CM'), 
            (500, 'D'), 
            (400, 'CD'), 
            (100, 'C'), 
            (90, 'XC'), 
            (50, 'L'), 
            (40, 'XL'), 
            (10, 'X'), 
            (9, 'IX'), 
            (5, 'V'), 
            (4, 'IV'), 
            (1, 'I')
        ]

        res = []
        for integer, roman in convert.items():
            if num == 0:
                break
            count = num // integer
            res.append(roman * count)
            num -= integer * count
        return "".join(res)

    # Relying on pre-calculations
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def intToRoman(self, num):
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return m[num // 1000] + c[(num % 1000) // 100] + x[(num % 100) // 10] + i[(num % 10) // 1]
