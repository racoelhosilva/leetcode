"""
LeetCode Problem: Backspace String Compare
Problem Number: 844
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/backspace-string-compare/
"""

class Solution:
    # Stack
    # Construct the strings using a stack structure
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def backspaceCompare(self, s, t):
        def build(s):
            res = []
            for char in s:
                if char != '#':
                    res.append(char)
                elif res:
                    res.pop()
            return "".join(res)
        return build(s) == build(t)
    
    # Two Pointers
    # Process the strings backwards, skipping erased characters
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def backspaceCompare(self, s, t):
        def nextValidChar(string, index):
            backspace = 0
            while index >= 0:
                if string[index] == '#':
                    backspace += 1
                elif backspace > 0:
                    backspace -= 1
                else:
                    break
                index -= 1
            return index
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = nextValidChar(s, i)
            j = nextValidChar(t, j)
            cs = s[i] if i >= 0 else ""
            ct = t[j] if j >= 0 else ""
            if cs != ct:
                return False
            i -= 1
            j -= 1
        return True
