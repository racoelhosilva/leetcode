"""
LeetCode Problem: Valid Palindrome II
Problem Number: 680
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/valid-palindrome-ii/
"""

class Solution:
    # Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def validPalindrome(self, s):
        def palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return palindrome(l+1, r) or palindrome(l, r+1)
            l += 1
            r -= 1
        return True

    # Python Shorthand
    # String slicing takes O(n) space, but comparison is faster
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def validPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skipLeft = s[l+1:r+1]
                skipRight = s[l:r]
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
            l += 1
            r -= 1
        return True
