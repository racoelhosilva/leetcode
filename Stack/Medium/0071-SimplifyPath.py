"""
LeetCode Problem: Simplify Path
Problem Number: 71
Difficulty: Medium
Topic: Stack
Link: https://leetcode.com/problems/simplify-path/
"""

class Solution:
    # Stack
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def simplifyPath(self, path):
        stack = []
        refs = path.split("/")
        for ref in refs:
            if ref == "" or ref == ".":
                continue
            elif ref == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(ref)
        return "/" + "/".join(stack)
