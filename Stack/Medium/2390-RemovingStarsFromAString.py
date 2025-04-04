"""
LeetCode Problem: Removing Stars From a String
Problem Number: 2390
Difficulty: Medium
Topic: Stack
Link: https://leetcode.com/problems/removing-stars-from-a-string/
"""

class Solution:
    # Stack
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def removeStars(self, s):
        from collections import deque
        stack = deque()
        
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
