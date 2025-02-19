"""
LeetCode Problem: Valid Palindrome
Problem Number: 125
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/valid-palindrome/
"""

class Solution:
    # Two Pointer Approach
    # First, clean the input string to contain only alphanumerics
    # Initialize a pointer at the start and end of the string and sequentially 
    # compare the letters, moving close to the center until they meet
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, s):
        s = ''.join(char for char in s.lower() if char.isalnum())
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    # Python Shorthands
    # A slightly faster result is using regular expressions to clean the string
    # And comparing the string with its reverse
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, s):
        import re
        s = re.compile('[^a-z0-9]').sub('', s.lower())
        return s == s[::-1]