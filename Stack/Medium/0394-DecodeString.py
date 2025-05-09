"""
LeetCode Problem: Decode String
Problem Number: 394
Difficulty: Medium
Topic: Stack
Link: https://leetcode.com/problems/decode-string/
"""

class Solution:
    # Stack
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def decodeString(self, s):
        string = []
        num = 0
        stack = []

        for char in s:
            if char == '[':
                stack.append(num)
                num = 0
                stack.append(string)
                string = []
            elif char == ']':
                string = stack.pop() + stack.pop() * string 
            elif char.isdigit():
                num = (num * 10) + int(char)
            else:
                string.append(char)
        return "".join(string)
