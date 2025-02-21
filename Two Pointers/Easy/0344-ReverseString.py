"""
LeetCode Problem: Reverse String
Problem Number: 344
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/reverse-string/
"""

class Solution:
    # Two Pointers
    # Initialize pointers on the ends of the string
    # At each step, swap the elements, until pointers meet
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseString(self, s):
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
