"""
LeetCode Problem: Palindrome Number
Problem Number: 9
Difficulty: Easy
Topic: Math & Geometry
Link: https://leetcode.com/problems/palindrome-number/
"""

class Solution:
    # Reverse Entire Number
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        temp, rev = x, 0
        while temp > 0:
            rev *= 10
            rev += temp % 10
            temp //= 10
        return rev == x
    
    # Reverse Half Number
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        rev = 0
        while x > rev:
            rev *= 10
            rev += x % 10
            x //= 10
        return x == rev or x == rev // 10
    
    # Python Shorthand
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
