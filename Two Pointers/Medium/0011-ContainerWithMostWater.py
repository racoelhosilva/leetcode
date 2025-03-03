"""
LeetCode Problem: Container With Most Water
Problem Number: 11
Difficulty: Medium
Topic: Two Pointers
Link: https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    # Two Pointer Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
