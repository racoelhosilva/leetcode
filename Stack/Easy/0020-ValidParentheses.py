"""
LeetCode Problem: Valid Parentheses
Problem Number: 20
Difficulty: Easy
Topic: Stack
Link: https://leetcode.com/problems/valid-parentheses/
"""

from collections import deque

class Solution:
    # Stack
    # If it is an open parentheses, consume it and push it to the stack
    # If it is a close parentheses, consume if its match is the top of the stack
    # In the end, the stack should be empty
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValid(self, s):
        matches = {')':'(', '}':'{', ']':'['}
        stack = deque()

        for char in s:
            if char in matches and stack:
                top = stack.pop()
                if top != matches[char]:
                    return False
            else:
                stack.append(char)

        return not stack
